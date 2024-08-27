const redis = require('redis');
const util = require('util');

const client = redis.createClient();

const setNewSet = (setName, setKey, value) => {
  client.hSet(setName, setKey, value, redis.print)
    .then((reply) => console.log(`Reply: ${reply}`))
    .catch((err) => console.log('Could not add key: ', err.message));
};

const displaySetValue = (setName) => {
  client.hGetAll(setName)
    .then((result) => console.log(JSON.stringify(result, null, 2)))
    .catch((err) => console.log('Could not retrieve key: ', err));
};


client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
    setNewSet('HolbertonSchools', 'Portland', 50);
    setNewSet('HolbertonSchools', 'Seattle', 80);
    setNewSet('HolbertonSchools', 'New York', 20);
    setNewSet('HolbertonSchools', 'Bogota', 20);
    setNewSet('HolbertonSchools', 'Cali', 40);
    setNewSet('HolbertonSchools', 'Paris', 2);
    displaySetValue('HolbertonSchools');
  })
  .catch((error) => {
    console.log('Redis client not connected to the server: ', error.message)
  })
