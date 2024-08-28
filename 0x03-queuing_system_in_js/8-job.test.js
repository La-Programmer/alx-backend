const { expect } = require("chai");
const createPushNotificationsJobs = require("./8-job");
const kue = require('kue');
const { describe } = require("mocha");

const queue = kue.createQueue();

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('Test createPushNotificationsJobs', () => {
  it('display an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('ff243gec', queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(1234567, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs({fast: 'api', htm: 'x'}, queue)).to.throw('Jobs is not an array');
  })
  it('Tests task creation', () => {
    const jobList = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4145232444452',
        message: 'This is the code 1284 to verify your account'
      }
    ]
    createPushNotificationsJobs(jobList, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('notification');
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
    expect(queue.testMode.jobs[1].type).to.equal('notification');
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: '4145232444452',
      message: 'This is the code 1284 to verify your account'
    });
  });
});
