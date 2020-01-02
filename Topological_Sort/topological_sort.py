# Helper function that recursively sorts the nodes in a graph
def top_sort(node,edge_list,visit_list,output):
    visit_list[node] = True
    if edge_list[node] != ["-"]:
        for v in edge_list[node]:
            if visit_list[v] == False:
                top_sort(v,edge_list,visit_list,output)
    output.append(node)

def topological(input):
    graph_file = open(input, "r")
    info = graph_file.readlines()
    graph_info = []
    for line in info:
        if line == '-' or line == '-\n':
            graph_info.append(["-"])
        else:
            insert_line = [int(n) for n in line.split(',')]
            graph_info.append(insert_line)
    edges_to = graph_info[1:]

    visited = [False] * graph_info[0][0]
    output_order = []

    for node in range(graph_info[0][0]):
        if visited[node] == False:
            top_sort(node,edges_to,visited,output_order)

    output_order.reverse()

    output_file = open("output","a")
    for n in output_order:
        output_file.write(str(n)+'\n')
    graph_file.close()
    output_file.close()

topological("input")