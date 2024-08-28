const { redisClientFactory, createQueue } = require('kue');
const redis = require('redis');
const { promisify } = require('util');
const express = require('express');

//VARIABLE DECLARATION
const app = express();
const port = 1245;
const reservationEnabled = true;
const redisClient = redis.createClient();
redisClient.on('error', (err) => {
  console.log(`Error on redis client: ${err}`);
})
redisClient.connect()
  .then(() => {
    console.log('Successfully connected to redis server');
  })
  .catch((err) => {
    console.log(`Error connecting to redis server: ${err}`)
  });

const queue = createQueue();

//UTILITY FUNCTIONS
const reserveSeat = async (number) => {
  await redisClient.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  try {
    const availableSeats = await redisClient.get('available_seats');
    return availableSeats ? parseInt(availableSeats, 10): 0;
  } catch (error) {
    console.log(`Error retrieving seats: ${error}`);
    throw error;
  }
}

// API ENDPOINTS
app.get('/available_seats', (req, res) => {
  getCurrentAvailableSeats()
    .then((availableSeats) => {
      res.send(JSON.stringify({numberofAvailableSeats: availableSeats}));
    })
    .catch((err) => {
      res.send(JSON.stringify({error: err}));
    })
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.send(JSON.stringify({status: 'Reservation are blocked'}));
  } else {
    const reserve_seat = queue.create('reservation').save((err) => {
      if (!err) {
        res.send({status: 'Reservation in process'});
      } else {
        res.send({status: 'Reservation failed'});
      }
    });
    reserve_seat.on('complete', () => {
      console.log(`Seat reservation job ${reserve_seat.id} completed`);
    }).on('failed', (err) => {
      console.log(`Seat reservation job ${reserve_seat.id} failed: ${err}`);
    });
  }
});

app.get('/process', (req, res) => {
  queue.process('reservation', async (job, done) => {
    const avaialableSeats = await getCurrentAvailableSeats();
    const newAvailableSeats = avaialableSeats - 1;
    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    } 
    reserveSeat(newAvailableSeats)
      .then(() => {
        done()
      })
      .catch((error) => {
        done(new Error('Not enough seats available'));
      });
  });
  res.send(JSON.stringify({status: 'Queue processing'}));
});

app.listen(port, () => {
  reserveSeat(50);
  console.log(`Your application is running on port ${port}`);
})
