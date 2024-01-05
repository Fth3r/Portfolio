package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"slices"
)

func main() {
	/*
		A quick little project to put some newly learned things
		into practice with a new language. It's a small program,
		but it's useful and I learned some things in the process.

		This implimentation gets the words in alphabetical order
		as an artifact of minimizing the loops needed. I think
		if I wanted to randomize them I would need one loop for that
		and another to print them all out after it's done.
	*/

	file, err := os.Open("dictionary.txt")
	if err != nil {
		fmt.Print(err)
	}

	ints := make([]int, 4)
	for range ints {
		r := rand.Intn(370105) // length of this dictionary file
		ints = append(ints, r)
	}
	slices.Sort(ints)

	scanner := bufio.NewScanner(file)
	i := 1
	for scanner.Scan() {
		for _, val := range ints {
			if i == val {
				fmt.Print(scanner.Text(), ".")
			}
		}
		i++
	}

}
