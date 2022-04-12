#!/usr/bin/node
const request = require('request');
let count = 0;

request(process.argv[2], function (err, response, body) {
	body = JSON.parse(body).results;

	for (let idx = 0; idx < body.length; ++idx) {
		const characters = body[idx].characters;

		 for (let j = 0; j < characters.length; ++j) {
			 const character = characters[j];
			 const characterId = character.split('/')[5];

			  if (characterId === '18') {
        			count += 1;
			  }
		 }
	}
	console.log(count);
});
