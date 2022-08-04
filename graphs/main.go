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
	graph := CreateGraph(4)
	graph.E[0] = []*node{&graph.V[1], &graph.V[2]}
	graph.E[1] = []*node{&graph.V[2]}
	graph.E[2] = []*node{&graph.V[0], &graph.V[3]}
	graph.E[3] = []*node{&graph.V[3]}

	Dfs(graph, &graph.V[1])
	//grafo1, _ := json.Marshal(&graph)

	//fmt.Println(string(grafo1))
}
