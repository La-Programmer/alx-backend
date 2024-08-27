const redis = require('redis');

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print)
    .then((reply) => console.log(`Reply: ${reply}`))
    .catch((err) => console.log('Could not add key: ', err.message));
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName)
    .then((result) => console.log(result))
    .catch((err) => console.log('Could not retrieve key: ', err));
};

const client = redis.createClient();

client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
  })
  .catch((error) => {
    console.log('Redis client not connected to the server: ', error.message)
  })
