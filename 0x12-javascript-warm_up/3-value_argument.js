#!/usr/bin/node
// Write a script that prints the first argument passed to it//

const args = process.argv;

if (args === 2) {
  console.log('No argument');
} else {
  console.log(args);
}
