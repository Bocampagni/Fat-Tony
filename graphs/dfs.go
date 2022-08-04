package main

func Dfs(graph *Graph, head *node) {

	for i := 0; i < len(graph.V); i++ {
		graph.V[i].color = 0
		graph.V[i].parent = -1
		graph.V[i].id = i
	}

	head.color = 1
	for _, element := range graph.E[head.id] {
		if element.color == 0 {
			element.color = 1
			element.parent = head.id
			DfsVisit(graph, element)
		}
	}
}

func DfsVisit(graph *Graph, node *node) {
	for _, element := range graph.E[node.id] {
		if element.color == 0 {
			element.color = 1
			element.parent = node.id
		}
	}
}
