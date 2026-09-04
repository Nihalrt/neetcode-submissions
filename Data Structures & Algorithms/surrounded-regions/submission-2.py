class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        total_nodes = rows * cols + 1
        dummy_node = rows*cols
        parent = [i for i in range(total_nodes)]
        
        def find(node):
            if parent[node]==node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(parent[node1])
            root2 = find(parent[node2])
            if root1!=root2:
                parent[root1] = root2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    index = r*cols + c
                    if r==0 or c==0 or r==rows-1 or c==cols-1:
                        union(index, dummy_node)
                    else:
                        if board[r-1][c]=="O":
                            union(index, (r-1)*cols+c)
                        if board[r+1][c]=="O":
                            union(index,(r+1)*cols+c)
                        if board[r][c+1]=="O":
                            union(index, r*cols+(c+1))
                        if board[r][c-1]=="O":
                            union(index, r*cols+(c-1))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    index = r*cols+c
                    if find(index)!= find(dummy_node):
                        board[r][c]="X"