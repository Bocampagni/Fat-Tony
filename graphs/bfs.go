package main

import "fmt"

func main() {
	var a = [][]int{
		{0, 1, 2, 3},   /*  initializers for row indexed by 0 */
		{4, 5, 6, 7},   /*  initializers for row indexed by 1 */
		{8, 9, 10, 11}, /*  initializers for row indexed by 2 */
	}
	multiplyMatrix(a, 5)
	makeDiagonalZero(a)
	printMatrix(a, 3, 4)
}

func printMatrix(matrix [][]int, row int, col int) {
	var i, j int
	for i = 0; i < row; i++ {
		for j = 0; j < col; j++ {
			fmt.Printf("a[%d][%d] = %d\n", i, j, matrix[i][j])
		}
	}
}

func multiplyMatrix(matrix [][]int, scale int) [][]int {
	var i, j int

	for i = 0; i < 3; i++ {
		for j = 0; j < 4; j++ {
			matrix[i][j] = matrix[i][j] * scale
		}
	}

	return matrix
}

func makeDiagonalZero(matrix [][]int) [][]int {
	var i, j int

	for i = 0; i < 3; i++ {
		for j = 0; j < 4; j++ {
			if i == j {
				matrix[i][j] = 0
			}
		}
	}

	return matrix
}