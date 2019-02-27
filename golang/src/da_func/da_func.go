package main

import (
	"fmt"
	"math/rand"
	"math/big"
	crypto_rand "crypto/rand"
)

func seed() {
	seedVal, errorMargin := crypto_rand.Int(crypto_rand.Reader, big.NewInt(32767))

	rand.Seed(seedVal.Int64())

	if errorMargin != nil {
		fmt.Println(errorMargin) }
}

func add(x, y int) int {
	return x + y
}

func randInt() (massiveNuts int) {
	massiveNuts = rand.Intn(10)
	return
}

func reverseGear(x, y string) (string, string) {
	return y, x
}


func main() {

	seed()

	fmt.Println(add(60, 5))

	fmt.Println(add(randInt(),randInt()))

	fmt.Println(add(rand.Intn(10),rand.Intn(10)))

	a, b := reverseGear("Cool J", "LL")
	fmt.Println(a,b)
}
