#!/usr/bin/node
// Write a script that prints x times “C is fun”

const args = process.argv.slice(2);
let i, j;
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < args; ++i) {
    let myVar = '';
    for (j = 0; j < args; ++j) {
      myVar += 'X';
    }
    console.log(myVar);
  }
}
