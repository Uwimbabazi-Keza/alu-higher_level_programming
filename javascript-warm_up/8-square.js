#!/usr/bin/node
let output;
const args = process.argv;
const conV = Number(args[2]);
if (conV) {
  for (let a = 0; a < conV; a++) {
    output = '';
    for (let b = 0; b < conV; b++) {
      output += 'X';
    }
    console.log(output);
  }
} else {
  console.log('Missing size');
}
