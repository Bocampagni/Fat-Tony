package main

import (
	"container/list"
)

func Bfs(graph *Graph) {

	for i := 0; i < len(graph.V); i++ {
		graph.V[i].color = 0
		graph.V[i].parent = -1
		graph.V[i].id = i
	}

	graph.V[0].color = 1
	time := 0
	queue := list.New()
	queue.PushFront(graph.V[0].id)

	for {
		head := queue.Front()
		vertex := graph.V[head.Value.(int)]
		if vertex.color == 1 {
			BfsVisit(graph, &vertex, &time, queue)
			queue.Remove(head)
			time += 1
		}
		if queue.Len() == 0 {
			break
		}
	}
}

func BfsVisit(graph *Graph, node *node, time *int, queue *list.List) {
	for _, element := range graph.E[node.id] {
		if element.color == 0 {
			element.color = 1
			element.parent = node.id
			element.time = *time
			queue.PushFront(element.id)
		}
	}
	graph.V[node.id].color = 2
}
