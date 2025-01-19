var part1 = (num 0)
var part2 = (num -1)

var data = (cat 2015/_inputs/day1.txt)

for i [(range (count $data))] {
  var c = $data[$i]

  if (eq $c '(') {
    set part1 = (+ $part1 1)
  } else {
    set part1 = (- $part1 1)
  }

  if (and (== $part2 -1) (> 0 $part1)) {
    set part2 = (+ $i 1) # Add 1 because the steps are not 0-indexed
  }
}

echo 'Part 1: '$part1
echo 'Part 2: '$part2
