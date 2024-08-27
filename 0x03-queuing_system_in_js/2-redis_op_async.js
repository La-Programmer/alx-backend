const redis = require('redis');
const util = require('util');

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

const promisifiedDisplaySchoolValue = util.promisify(displaySchoolValue);

const client = redis.createClient();

client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
    promisifiedDisplaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    promisifiedDisplaySchoolValue('HolbertonSanFrancisco');
  })
  .catch((error) => {
    console.log('Redis client not connected to the server: ', error.message)
  })
