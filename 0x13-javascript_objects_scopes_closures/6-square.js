#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// se hizo el mismo ciclo del punto 5
const Squre = require('./5-square');
class Square extends Squre {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let sq = '';
        for (let j = 0; j < this.width; j++) {
          sq += c;
        }
        console.log(sq);
      }
    }
  }
}
module.exports = Square;
