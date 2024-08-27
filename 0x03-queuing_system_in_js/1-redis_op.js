const redis = require('redis');

const setNewSchool = async (schoolName, value) => {
  const reply = await client.set(schoolName, value, redis.print);
  console.log(`Reply: ${reply}`);
};

const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName, (data) => data);
  console.log(value);
};

const client = redis.createClient();

client.connect()
  .then(async () => {
    console.log('Redis client connected to the server');
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  })
  .catch((error) => {
    console.log('Redis client not connected to the server: ', error.message)
  })
