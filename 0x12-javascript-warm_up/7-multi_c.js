#!/usr/bin/node
// Write a script that prints x times “C is fun”

const args = process.argv.slice(2);
const myVar = 'C is fun';
let i;
if (isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < args; i++) {
    console.log(myVar);
  }
}
