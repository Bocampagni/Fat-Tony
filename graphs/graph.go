package main

type node struct {
	id     int
	parent int
	color  int
	time   int
}

type Graph struct {
	V []node          `json:"node"`
	E map[int][]*node `json:"edge"`
}

func CreateGraph(size int) *Graph {
	graph := new(Graph)
	graph.V = make([]node, size)
	graph.E = make(map[int][]*node)

	return graph
}

type DGraph struct {
}

type Network struct {
}

type OSMGraph struct {
}
