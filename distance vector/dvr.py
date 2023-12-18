number_of_nodes=int(input("Enter the number of nodes:"))
nodes=[]
for i in range(number_of_nodes):
    nodes.append(input("enter the name of the node:"))
distance_matrix=[]
for i in range(number_of_nodes):
    l=[]
    for j in range(number_of_nodes):
        if i==j:
            l.append(0)
        else:
            k=int(input(f"Enter the distance from node {nodes[i]} to {nodes[j]} enter -1 if no connection: "))
            l.append(k)
    distance_matrix.append(l)

print("current distance matrix")

for i in distance_matrix:
    print(i)

for start_node in range(len(nodes)):
    for neighbor_node in range(len(nodes)):
        for end_node in range(len(nodes)):
            if distance_matrix[start_node][neighbor_node]!=-1 and distance_matrix[neighbor_node][end_node]!=-1:
                if (distance_matrix[start_node][end_node]==-1) or (distance_matrix[start_node][neighbor_node]+distance_matrix[neighbor_node][end_node]<distance_matrix[start_node][end_node]):
                    distance_matrix[start_node][end_node]=distance_matrix[start_node][neighbor_node]+distance_matrix[neighbor_node][end_node]
                    print("updating nodes ",nodes[start_node],"->",nodes[end_node])
                    print("new distance: ",distance_matrix[start_node][end_node])

print("Distance matrix:")

for i in distance_matrix:
    print(i)

