package main

import "fmt"

func check(x int, nbit int) bool {
	t := 0
	for i := 0; i < nbit; i++ {
		b := (x >> (nbit - i - 1)) & 1
		t += 1 - b*2
		if t < 0 {
			return false
		}
	}
	return t == 0
}

func ntob(x int, nbit int) string {
	result := ""
	for i := 0; i < nbit; i++ {
		b := (x >> (nbit - i - 1)) & 1
		if b == 0 {
			result += "("
		} else {
			result += ")"
		}
	}
	return result
}

func solve(n int) {
	for i := 0; i < (1 << n); i++ {
		if check(i, n) {
			fmt.Println(ntob(i, n))
		}
	}
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	solve(n)
}
