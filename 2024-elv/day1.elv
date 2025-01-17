use str
use math

var raw_lines = [(cat 2024-inputs/day1.txt)]
var left = []
var right = []

for i $raw_lines {
  var cur = [(str:split '   ' $i)]

  set left = [$@left (num $cur[0])]
  set right = [$@right (num $cur[1])]
}

set left = [(order $left)]
set right = [(order $right)]

var part1 = 0
var part2 = 0

var counts = [&]
for a $right {
  if (not (has-key $counts $a)) {
    set counts[$a] = 0
  }

  set counts[$a] = (+ 1 $counts[$a])
}

for i [(range (count $left))] {
  var a = $left[$i]
  var b = $right[$i]

  set part1 = (+ $part1 (math:abs (- $a $b)))
  if (has-key $counts $a) {
    set part2 = (+ $part2 (* $a $counts[$a]))
  }
}

echo "Part 1: Total diff: "$part1
echo "Part 2: Similarity: "$part2
