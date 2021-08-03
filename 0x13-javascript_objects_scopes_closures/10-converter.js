#!/usr/bin/node
//

exports.converter = function (base) {
  return function (numY) {
    return numY.toString(base);
  };
};
