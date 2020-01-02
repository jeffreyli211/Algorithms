def is_parent_level(parent,current):
    if parent == (current-1):
        return True
    else:
        return False

def BFS(input):
    graph_file = open(input, "r")
    info = graph_file.readlines()
    graph_info = []
    for line in info:
        if line == '-' or line == '-\n':
            graph_info.append(["-"])
        else:
            insert_line = [int(n) for n in line.split(',')]
            graph_info.append(insert_line)
    adj_list = graph_info[2:]
    output_list = ['-'] * graph_info[0][0]

    in_q = [False] * graph_info[0][0]
    level = [0] * graph_info[0][0]
    visited = [False] * graph_info[0][0]
    q = []

    s = graph_info[1][0]
    level[s] = 0
    if adj_list[s] != ["-"]:
        q.append(s)

    while q != []:
        s = q.pop(0)
        in_q[s] = False
        visited[s] = True
        for neighbor in adj_list[s]:
            if visited[neighbor] == False and in_q[neighbor] == False:
                level[neighbor] = level[s]+1
                q.append(neighbor)
                in_q[neighbor] = True

    s = graph_info[1][0]
    if adj_list[s] != ["-"]:
        q.append(s)
        in_q[s] = True
        visited = [False] * graph_info[0][0]

    while q != []:
        s = q.pop(0)
        s_set = set()
        in_q[s] = False
        visited[s] = True
        for neighbor in adj_list[s]:
            if visited[neighbor] == False and in_q[neighbor] == False:
                s_set.add(neighbor)
                q.append(neighbor)
                in_q[neighbor] = True
            elif visited[neighbor] == True and is_parent_level(level[neighbor],level[s]) == True:
                if s in output_list[neighbor]:
                    s_set.add(neighbor)
            else:
                continue
        output_list[s] = s_set


    output_file = open("output", 'a')
    for BFS_line in output_list:
        output_file.write(','.join(str(x) for x in BFS_line)+'\n')
    graph_file.close()
    output_file.close()

BFS("input")
