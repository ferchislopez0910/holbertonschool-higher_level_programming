#!/usr/bin/node
// Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }

  rotate () {
    const saveVale = this.height;
    this.height = this.width;
    this.width = saveVale;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
