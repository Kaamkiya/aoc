#include <stdio.h>
#include <string.h>

unsigned int smallest_area(unsigned int a, unsigned int b, unsigned int c) {
  if (a < b && a < c) return a;
  if (b < c) return b;
  return c;
}

unsigned int smallest_perimeter(unsigned int l, unsigned int w, unsigned int h) {
  unsigned int sides[2];
  sides[0] = l;
	
  if (w < sides[0]) {
    sides[1] = l;
    sides[0] = w;
  } else {
    sides[1] = w;
  }
	
  if (h < sides[0]) {
    sides[1] = sides[0];
    sides[0] = h;
	} else if (h < sides[1]) {
    sides[1] = h;
  }

  return 2*sides[0] + 2*sides[1];
}

int main() {
  char buf[128];
  unsigned int part1 = 0;
  unsigned int part2 = 0;

  unsigned int l, w, h;

  FILE *infile = fopen("2015/_inputs/day2.txt", "r");
  if (infile == NULL) {
    perror("Failed to open file");
    return 1;
  }

  while ((fgets(buf, sizeof(buf), infile)) != NULL) {
    if (buf[strlen(buf)-1] == '\n') buf[strlen(buf)-1] == '\0';
    
    sscanf(buf, "%ux%ux%ux", &l, &w, &h);

    part1 += 2*l*w + 2*w*h + 2*l*h + smallest_area(l*w, w*h, l*h);
    part2 += l*w*h + smallest_perimeter(l, w, h);
  }

  printf("Part 1: %d\n", part1);
  printf("Part 2: %d\n", part2);
}
