const kue = require('kue');

const push_notification_code = kue.createQueue();
const jobData = {
  phoneNumber: '34567890987654',
  message: 'This is your invitation to the event',
};

const notification_job = push_notification_code.create('notification', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${notification_job.id}`);
  } else {
    console.log(`Failed to create job: ${err.message}`);
  }
});

notification_job.on('failed', () => {
  console.log('Notification job failed');
});

notification_job.on('complete', () => {
  console.log('Notification job completed');
});
