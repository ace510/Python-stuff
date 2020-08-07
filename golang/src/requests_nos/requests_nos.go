package main

import (
	"fmt"
	//"runtime"
	//"net/http"
	"github.com/pkg/profile"
	"github.com/valyala/fasthttp"
)

func GenerateCombinations(alphabet string, length int) <-chan string {
	c := make(chan string)

	// Starting a separate goroutine that will create all the combinations,
	// feeding them to the channel c
	go func(c chan string) {
		defer close(c) // Once the iteration function is finished, we close the channel

		AddLetter(c, "", alphabet, length) // We start by feeding it an empty string
	}(c)

	return c // Return the channel to the calling function
}

// AddLetter adds a letter to the combination to create a new combination.
// This new combination is passed on to the channel before we call AddLetter once again
// to add yet another letter to the new combination in case length allows it
func AddLetter(c chan string, combo string, alphabet string, length int) {
	// Check if we reached the length limit
	// If so, we just return without adding anything
	if length <= 0 {
		return
	}

	var newCombo string
	for _, ch := range alphabet {
		newCombo = combo + string(ch)
		c <- newCombo
		AddLetter(c, newCombo, alphabet, length-1)
	}
}

// func PrintMemUsage() {
// 	var m runtime.MemStats
// 	runtime.ReadMemStats(&m)
// 	// For info on each, see: https://golang.org/pkg/runtime/#MemStats
// 	fmt.Printf("Alloc = %v MiB", bToMb(m.Alloc))
// 	fmt.Printf("\tTotalAlloc = %v MiB", bToMb(m.TotalAlloc))
// 	fmt.Printf("\tSys = %v MiB", bToMb(m.Sys))
// 	fmt.Printf("\tNumGC = %v\n", m.NumGC)
// }

// func MakeRequest(url string, guard chan struct{}) {
// 	resp, err := http.Get(url)
// 	fmt.Println(url)
// 	if err != nil {
// 		return
// 	}
// 	defer resp.Body.Close()
// 	defer func() {
// 		<-guard
// 	}()

// 	StatusCode := resp.StatusCode

// 	if StatusCode != 403 {
// 		fmt.Println(StatusCode)
// 	}
// }

func main() {
	var url_preamble string = "http://cdn-dlm.esd.sage.com/Sage300ConstructionandRealEstate/"

	guard := make(chan struct{}, 500)
	defer profile.Start().Stop()

	for url_payload := range GenerateCombinations("abcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=", 64) {
		var url string = (url_preamble + url_payload)
		//fmt.Println(url)
		guard <- struct{}{}

		go func(url string) {
			StatusCode, _, err := fasthttp.Get([]byte("hungus chungus"), url)
			defer func() {
				<-guard
			}()
			if err != nil {
				fmt.Println(err)
				fmt.Println(len(guard))
				return
			}

			if StatusCode != 403 {
				fmt.Println(StatusCode)
			}
		}(url)
		// fmt.Println("another critter running")
	}
	fmt.Println("done!")

}
