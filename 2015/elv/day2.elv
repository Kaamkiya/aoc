use str
use math

var part1 = 0
var part2 = 0

var lines = [(cat 2015/_inputs/day2.txt)]
var data = []

fn smallest_area {|a b c|
  echo (math:min $a $b $c)
}

fn smallest_perimeter {|l w h|
  echo (math:min (* 2 (+ $l $w)) (* 2 (+ $w $h) (* 2 (+ $l $h))))
}

for i $lines {
  set data = [$@data [(str:split x $i)]]
}

for v $data {
  var l = $v[0]
  var w = $v[1]
  var h = $v[2]

  var s1 = (* $l $w)
  var s2 = (* $l $h)
  var s3 = (* $w $h)

  set part1 = (+ $part1 (* 2 $s1) (* 2 $s2) (* 2 $s3) (smallest_area $s1 $s2 $s3))
  set part2 = (+ $part2 (smallest_perimeter $l $w $h) (* $l $w $h))
}

echo 'Part 1: '$part1
echo 'Part 2: '$part2
