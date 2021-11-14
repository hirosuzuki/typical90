package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc *bufio.Scanner

func init() {
	sc = bufio.NewScanner(os.Stdin)
	buffsize := 1000000
	buff := make([]byte, buffsize)
	sc.Buffer(buff, buffsize)
	sc.Split(bufio.ScanWords)
}

func loadint64() (result int64) {
	sc.Scan()
	result, _ = strconv.ParseInt(sc.Text(), 10, 64)
	return
}

func main() {
	n := loadint64()
	l := loadint64()
	k := loadint64()

	a := make([]int64, n)
	var i int64
	for i = 0; i < n; i++ {
		a[i] = loadint64()
	}

	d := make([]int64, n+1)
	d[0] = a[0]
	d[n] = l - a[n-1]
	for i = 0; i < n-1; i++ {
		d[i+1] = a[i+1] - a[i]
	}

	check := func(v int64) bool {
		var x int64 = 0
		var c int64 = 0
		var i int64
		for i = 0; i < n+1; i++ {
			x += d[i]
			if x >= v {
				x = 0
				c += 1
			}
		}
		return c >= k+1
	}

	hi := l
	var lo int64 = 0
	for lo+1 < hi {
		m := (hi + lo) / 2
		if check(m) {
			lo = m
		} else {
			hi = m
		}
	}

	fmt.Println(lo)
}
