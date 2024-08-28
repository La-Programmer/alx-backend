const kue = require('kue');

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

const process_queue = kue.createQueue();

process_queue.process('notification', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
