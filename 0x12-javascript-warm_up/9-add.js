#!/usr/bin/node

function add(a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  const sum = num1 + num2;
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
