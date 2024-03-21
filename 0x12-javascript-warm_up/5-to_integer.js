#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? "Not a number" : `My number: ${num}`);

// OR

if (isNaN(num)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${num}`);
}
