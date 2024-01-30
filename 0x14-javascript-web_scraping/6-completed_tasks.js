#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasks[todo.userId] === undefined) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId]++;
      }
    }
  });

  console.log(completedTasks);
});
