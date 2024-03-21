#!/usr/bin/node
const count = process.argv.length;
console.log(
  count === 2
    ? "No argument"
    : count === 3
    ? "Argument found"
    : "Arguments found"
);

// OR

if (count === 2) {
  console.log("No Argument.");
} else if (count === 3) {
  console.log("Argument Found.");
} else {
  console.log("Arguments Found.");
}
