const createPushNotificationsJobs = (jobs, queue) => {
  if (!jobs instanceof Array) {
    throw new Error('Jobs is not an array');
  }
  for (const job of jobs) {
    const push_notification_code_3 = queue.create('notification', job).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${push_notification_code_3.id}`);
      } else {
        console.log(`Failed to create job: ${err.message}`);
      }
    });

    push_notification_code_3.on('complete', () => {
      console.log(`Notification job ${push_notification_code_3.id}`);
    });

    push_notification_code_3.on('failed', (err) => {
      console.log(`Notification job ${push_notification_code_3.id} failed: ${err}`);
    });

    push_notification_code_3.on('progress', (progress) => {
      console.log(`Notification job ${push_notification_code_3.id} ${progress}% complete`);
    });
  }
};

module.exports = createPushNotificationsJobs;
