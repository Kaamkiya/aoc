#include <stdio.h>
#include <string.h>

int main() {
	char input[65536];
	FILE *infile = fopen("2015/_inputs/day1.txt", "r");
	if (infile == NULL) {
		perror("Failed to open input file.");
		return 1;
	}

	fscanf(infile, "%s", &input);
	fclose(infile);

	int part1 = 1;
	int part2 = -1;

	for (int i = 0; i < strlen(input); i++) {
		if (input[i] == '(') part1++;
		else part1--;

		if (part2 == -1 && part1 < 0) part2 = i;
	}

	printf("Part 1: %d\n", part1);
	printf("Part 2: %d\n", part2);
}
