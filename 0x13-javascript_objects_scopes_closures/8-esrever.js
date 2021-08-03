#!/usr/bin/node
// Write a function that returns the reversed version of a list
// en el for se le resta -1 porque cuenta hasta 6 posiciones
// osea pos 0 = 1 y asi...

exports.esrever = function (list) {
  const li = [];

  for (let i = list.length - 1; i >= 0; i--) {
    li.push(list[i]);
  }
  return li;
};
