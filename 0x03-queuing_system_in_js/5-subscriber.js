const redis = require('redis');

const client = redis.createClient();

const susbcribeToChannel = (channel) => {
  client.subscribe(channel, (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel');
      process.exit(0);
    }
  })
}

client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
    susbcribeToChannel('holberton school channel');
  })
  .catch((err) => console.log(`Redis client not connected to the server: ${err.message}`));


