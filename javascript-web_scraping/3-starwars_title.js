#!/usr/bin/node
const request = require('request');

const filmId = 1;
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }
  const statusCode = response.statusCode;
  
  if (statusCode === 200) {
    const film = JSON.parse(body);
    console.log('${film.title}');
  } else {
    console.error('Request failed with status code:', statusCode);
  }
});
