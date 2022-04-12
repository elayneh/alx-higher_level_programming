#!/usr/bin/node

const request = require('request');

request( 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]), function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
