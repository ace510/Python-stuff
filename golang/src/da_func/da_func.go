package main

import (
	"fmt"
	"math/rand"
	"math/big"
	crypto_rand "crypto/rand"
)

func seed() {
	seed_val, error_margin := crypto_rand.Int(crypto_rand.Reader, big.NewInt(32767))

	rand.Seed(seed_val.Int64())

	if error_margin != nil {
		fmt.Println(error_margin) }
}

func add(x, y int) int {
	return x + y
}

func rand_int() (massive_nuts int) {
	massive_nuts = rand.Intn(10)
	return
}

func reverse_gear(x, y string) (string, string) {
	return y, x
}


func main() {

	seed()

	fmt.Println(add(60, 5))

	fmt.Println(add(rand_int(),rand_int()))

	fmt.Println(add(rand.Intn(10),rand.Intn(10)))

	a, b := reverse_gear("Cool J", "LL")
	fmt.Println(a,b)
}
