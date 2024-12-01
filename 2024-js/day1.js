/* NOTE: These scripts are meant to be run from the browser console.
 * Navigate to https://adventofcode.com/2024/day/1/input, open the browser
 * console, and then run this code.
 */

let input = document.body.innerText.split('\n').map(line => line.split('   '));
let left = [], right = [], diff = 0, similarity = 0;

input.forEach(n => left.push(n[0]) && right.push(n[1]));

left.pop();
right.pop();

left.sort().map(n => parseInt(n));
right.sort().map(n => parseInt(n));

for (let i in left) {
  let a = left[i], b = right[i];
  diff += Math.abs(a - b);
  similarity += a * right.filter(k => k === a).length;
}

console.log("Diff:", diff);
console.log("Similarity:", similarity);
