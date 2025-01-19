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
