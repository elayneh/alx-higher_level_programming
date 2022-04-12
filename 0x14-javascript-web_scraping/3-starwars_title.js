#!/usr/bin/node

request = require('request');

request('https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]), function (_err, _response, content) {

	content =JSON.parse(content);
	console.log(content.title);
});
