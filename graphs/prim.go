package main

import "fmt"

func Prim() {

	var INF = 9999
	graph := [5][5]int{
		{0, 19, 5, 0, 0},
		{19, 0, 5, 9, 2},
		{5, 5, 0, 1, 6},
		{0, 9, 1, 0, 1},
		{0, 2, 6, 1, 0},
	}

	selected_node := [5]bool{false, false, false, false, false}
	no_edge := 0
	selected_node[0] = true
	for {
		minimum := INF
		origin := 0
		destiny := 0
		if no_edge >= len(graph[0])-1 {
			break
		}

		for index := range graph[0] {
			if selected_node[index] {
				for i := 0; i < len(graph[0]); i++ {
					if (!selected_node[i]) && graph[index][i] > 0 {
						if minimum > graph[index][i] {
							minimum = graph[index][i]
							origin = index
							destiny = i
						}
					}
				}
			}
		}
		selected_node[destiny] = true
		no_edge++
		fmt.Println(origin, "-", destiny, ":", graph[origin][destiny])
	}
}
