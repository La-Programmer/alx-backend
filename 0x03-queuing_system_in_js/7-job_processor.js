const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Send notification to ${phoneNumber} with message: ${message}`);
    done();
  }
};

const push_notification_code_2 = kue.createQueue()
push_notification_code_2.process('notification', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
