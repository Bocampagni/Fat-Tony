package main

func main() {

	//graph := CreateGraph(7)
	//graph.E[0] = []*node{&graph.V[1]}
	//graph.E[1] = []*node{&graph.V[0], &graph.V[2], &graph.V[3]}
	//graph.E[2] = []*node{&graph.V[1]}
	//graph.E[3] = []*node{&graph.V[0]}
	//graph.E[0] = []*node{&graph.V[2], &graph.V[3], &graph.V[4]}
	//graph.E[1] = []*node{&graph.V[2], &graph.V[4], &graph.V[6]}
	//graph.E[2] = []*node{&graph.V[4]}
	//graph.E[3] = []*node{&graph.V[4], &graph.V[5]}
	//graph.E[4] = []*node{&graph.V[5]}
	//graph.E[5] = []*node{&graph.V[1]}
	//graph.E[6] = []*node{}

	//Bfs(graph)
	//graph := CreateGraph(4)
	//graph.E[0] = []*node{&graph.V[1], &graph.V[2]}
	//graph.E[1] = []*node{&graph.V[2]}
	//graph.E[2] = []*node{&graph.V[0], &graph.V[3]}
	//graph.E[3] = []*node{&graph.V[3]}

	wgraph := new(WGraph)
	wgraph.V = make([]node, 4)
	wgraph.E = make([][]edge, 4)

	wgraph.E[0] = []edge{{weight: 1, destiny: &wgraph.V[0], source: &wgraph.V[1]}, {weight: 3, destiny: &wgraph.V[0], source: &wgraph.V[2]}}
	wgraph.E[1] = []edge{{weight: 2, destiny: &wgraph.V[1], source: &wgraph.V[3]}, {weight: 5, destiny: &wgraph.V[1], source: &wgraph.V[3]}}
	wgraph.E[2] = []edge{{weight: 7, destiny: &wgraph.V[2], source: &wgraph.V[0]}, {weight: 10, destiny: &wgraph.V[2], source: &wgraph.V[3]}}
	wgraph.E[3] = []edge{{weight: 12, destiny: &wgraph.V[3], source: &wgraph.V[1]}}

	Prim()

	//Dfs(graph, &graph.V[1])
	//grafo1, _ := json.Marshal(&graph)

	//fmt.Println(string(grafo1))
}
