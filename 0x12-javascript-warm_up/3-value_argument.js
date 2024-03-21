#!/usr/bin/node
console.log(
  typeof process.argv[2] === "undefined" ? "No argument" : process.argv[2]
);

// OR
if (typeof process.argv[2] === "undefined") {
  console.log("No argument");
} else {
  console.log(process.argv[2]);
}
