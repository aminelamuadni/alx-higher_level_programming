#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const mappedList = list.map((item, index) => item * index);

console.log(mappedList);
