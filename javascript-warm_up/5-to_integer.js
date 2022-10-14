#!/usr/bin/node
const args = process.argv;
const rnd = Number(args[2]);
if (rnd) {
  console.log(`My number: ${args[2]}`);
} else {
  console.log('Not a number');
}
