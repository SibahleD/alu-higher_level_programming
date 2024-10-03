#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/:id';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }
  const statusCode = response.statusCode;
  
  if (statusCode === 200) {
    const posts = JSON.parse(body);
    posts.forEach(post => {
      console.log('${post.title}');
    });
  } else {
    console.error('Request failed with status code:', statusCode);
  }
});
