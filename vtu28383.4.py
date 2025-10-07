def minimax(depth, node_index, is_max, scores, alpha, beta, height):
]

    if depth == height:
        return scores[node_index]

    if is_max:
        best = float('-inf')

        # Left child
        val = minimax(depth + 1, node_index * 2, False, scores, alpha, beta, height)
        best = max(best, val)
        alpha = max(alpha, best)

        # Alpha-Beta Pruning
        if beta <= alpha:
            return best

        # Right child
        val = minimax(depth + 1, node_index * 2 + 1, False, scores, alpha, beta, height)
        best = max(best, val)
        alpha = max(alpha, best)
        return best

    else:







        best = float('inf')

        # Left child
        val = minimax(depth + 1, node_index * 2, True, scores, alpha, beta, height)
        best = min(best, val)
        beta = min(beta, best)

        #Pruning
        if beta <= alpha:
            return best

        # Right child
        val = minimax(depth + 1, node_index * 2 + 1, True, scores, alpha, beta, height)
        best = min(best, val)
        beta = min(beta, best)
        return best


if __name__ == "__main__":
    import math

    # Example scores of leaf nodes (8 leaf nodes for a tree of height 3)
    scores = [3, 5, 6, 9, 12, 0, -1, -2]
    height = int(math.log2(len(scores)))
    print("optimal value for player:",minimax(0,0,True,scores,float('-inf'),float('inf'),height))

