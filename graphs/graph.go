package main

type node struct {
	id     int
	parent int
	color  int
	time   int
}

type edge struct {
	source  *node
	destiny *node
	weight  int
}

type Graph struct {
	V []node          `json:"node"`
	E map[int][]*node `json:"edge"`
}

type WGraph struct {
	V []node
	E [][]edge
}

type Network struct {
}

type OSMGraph struct {
}

func CreateGraph(size int) *Graph {
	graph := new(Graph)
	graph.V = make([]node, size)
	graph.E = make(map[int][]*node)

	return graph
}
