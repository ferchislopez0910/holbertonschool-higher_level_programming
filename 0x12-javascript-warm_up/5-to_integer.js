#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer> if the //
// first argument can be converted to an integer //

const args = process.argv.slice(2);
// Desplaza el arg el numero de posiciones

if (isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args);
}
