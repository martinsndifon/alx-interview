#!/usr/bin/node
const request = require('request');

if (process.argv.length != 3) {
  console.log("Usage: ./0-starwars_characters.js <n>");
  process.exit(1);
}

const id = process.argv[2];
if (isNaN(id)) {
  console.log("<n> must be an integer");
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error', error);
  } else {
    try {
      const parsedBody = JSON.parse(body);
      const characters = parsedBody.characters;
      for (const character of characters) {
        request.get(character, (error, response, body) => {
          if (error) {
            console.error('Error', error);
          } else {
            try {
              const pBody = JSON.parse(body);
              const name = pBody.name;
              console.log(name);
            } catch (parseError) {
              console.error(parseError);
            }
          }
        });
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
