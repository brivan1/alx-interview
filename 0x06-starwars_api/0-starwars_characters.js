#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getCharacters = (charactersList, index) => {
  if (charactersList.length === index) {
    return;
  }
  request(charactersList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      getCharacters(charactersList, index + 1);
    }
  });
};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charactersList = JSON.parse(body).characters;
    getCharacters(charactersList, 0);
  }
});
