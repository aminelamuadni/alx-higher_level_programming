#!/usr/bin/node

exports.esrever = function (list) {
  let list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    list.push(list[i]);
  }
  return list;
};
