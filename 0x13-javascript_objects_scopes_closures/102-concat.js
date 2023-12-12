#!/usr/bin/node

const fs = require('fs');

const [,, fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, contentA + contentB);
