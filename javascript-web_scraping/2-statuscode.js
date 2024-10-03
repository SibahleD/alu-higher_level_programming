#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const content = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }
  const statusCode = response.statusCode;
  console.log('code:', statusCode);
});
