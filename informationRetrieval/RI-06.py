import numpy as np

def pagerank(matrix, damping_factor=0.85, max_iterations=100, tol=1e-6):
    matrix = matrix / matrix.sum(axis=0, keepdims=True)
    
    n = matrix.shape[0]
    initial_rank = np.ones(n) / n

    for _ in range(max_iterations):
        new_rank = (1 - damping_factor) / n + damping_factor * np.dot(matrix, initial_rank)
        
        if np.linalg.norm(new_rank - initial_rank) < tol:
            return new_rank

        initial_rank = new_rank

    return initial_rank

if __name__ == "__main__":
    transition_matrix = np.array([
        [0, 1, 1, 1 ],
        [0,0,1,1],
        [1,0,0,0],
        [1,0,1,0]
    ])
    
    ranks = pagerank(transition_matrix)
    print("Page Ranks:")
    print(ranks)