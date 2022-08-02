package main

import (
	"encoding/json"
	"fmt"
)

func main() {

	type graph struct {
		V []int
		E map[int][]int
	}

	grafo := new(graph)
	grafo.E = make(map[int][]int)
	grafo.V = []int{0, 1, 2, 3, 4}
	grafo.E[0] = []int{1, 2, 4}
	grafo.E[1] = []int{2, 4}
	grafo.E[2] = []int{0, 4}
	grafo.E[3] = []int{1, 2, 4}
	grafo.E[4] = []int{1}

	grafo1, _ := json.Marshal(grafo)
	fmt.Println(string(grafo1))

}
