#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  let max = -Infinity;
  let secondMax = -Infinity;

  for (const num of args) {
    const val = Number(num);
    if (val > max) {
      [secondMax, max] = [max, val];
    } else if (val > secondMax && val < max) {
      secondMax = val;
    }
  }

  return secondMax;
}

const numbers = process.argv.slice(2);
console.log(findSecondBiggest(numbers));
