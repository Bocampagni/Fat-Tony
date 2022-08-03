package main

import (
	"encoding/json"
	"fmt"
)

func main() {

	graph := new(Graph)
	graph.E = make(map[int][]int)
	graph.V = []int{0, 1, 2, 3, 4}
	graph.E[0] = []int{1, 2, 4}
	graph.E[1] = []int{2, 4}
	graph.E[2] = []int{0, 4}
	graph.E[3] = []int{1, 2, 4}
	graph.E[4] = []int{1}

	grafo1, _ := json.Marshal(graph)
	fmt.Println(string(grafo1))
}
