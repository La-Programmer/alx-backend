const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const jobQueues = kue.createQueue();

for (const notification of jobs) {
  const notification_job = jobQueues.create('notification', notification).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notification_job.id}`);
    } else {
      console.log(`Failed to create job: ${err.message}`);
    }
  })

  notification_job.on('failed', (err) => {
    console.log(`Notification job #${notification_job.id} failed: ${err}`);
  })

  notification_job.on('complete', () => {
    console.log(`Notification job #${notification_job.id} completed`);
  })

  notification_job.on('progress', (progress) => {
    console.log(`Notification job #${notification_job.id} ${progress}% complete`);
  });
}
