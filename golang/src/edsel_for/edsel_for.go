package main

import (
	"fmt"
	"time"
	// "github.com/davecgh/go-spew/spew"
)

const absolute_uint uint64 = 1<<32 -1

func prime_printer(prime_channel chan uint64) {
	for {
	prime_pl := <- prime_channel
	fmt.Println(prime_pl)
}
}

func is_prime( x uint64, prime_channel chan uint64) {
	prim_e := true
	var start uint64 = 3
	for i := start  ; i < x; i++ {
		if x % i == 0 { prim_e = false}
		}
	if prim_e == true {

		//spew.Dump(x)
		prime_channel <- x }
}

func main() {
	var start uint64 = 10
	var prime_channel chan uint64 = make(chan uint64)
	for i := start; i < absolute_uint; i += 3{

		go is_prime(i, prime_channel)
		//go is_prime(i+1, prime_channel)
		var input string
  		fmt.Scanln(&input)
		time.Sleep(time.Second * 1)
		//go is_prime(i+2, prime_channel)
	}
}
