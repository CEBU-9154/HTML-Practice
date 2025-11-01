def display(maze,i,j,path):
    n=len(maze)
    m=len(maze[0])

    if i >= n or j >= n or maze[i][j] == 1:
        return
    
    if i == n - 1 and j == m - 1:
        print(path)
        return
    
    display(maze, i+1, j, path+"D")
    display(maze, i, j+1, path+"R")

maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print("All possible paths for the rat to escape: ")
display(maze,0,0,"")