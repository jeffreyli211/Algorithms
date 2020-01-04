import sys
import heapq

def make_adj_list(e,n):
    ret = [['-']] * n
    for edge in e:
        (u,v,w) = (edge[0],edge[1],edge[2])
        if ret[u] == ['-']:
            ret[u] = [(v,w)]
        else:
            ret[u].append((v,w))
        if ret[v] == ['-']:
            ret[v] = [(u,w)]
        else:
            ret[v].append((u,w))
    return ret

def MST(input):
    graph_file = open(input, "r")
    info = graph_file.readlines()
    graph_info = [[int(n) for n in line.split(',')] for line in info]

    n = graph_info[0][0]
    #m = graph_info[1][0]
    edges = graph_info[2:]
    adj_list = make_adj_list(edges,n)
    visited = [False] * n
    keys = [sys.maxsize] * n
    connected_to = [0] * n
    output_list = [[None]] * n

    s = 0
    keys[s] = 0
    q = []
    q.append((keys[s],s))
    heapq.heapify(q)
    while q != []:
        (_,u) = heapq.heappop(q)

        if visited[u] == True:
            continue
        else:
            if u != 0:
                if output_list[u] == [None]:
                    output_list[u] = [connected_to[u]]
                    if output_list[connected_to[u]] == [None]:
                        output_list[connected_to[u]] = [u]
                    else:
                        output_list[connected_to[u]].append(u)
                else:
                    output_list[u].append(connected_to[u])
                    if output_list[connected_to[u]] == [None]:
                        output_list[connected_to[u]] = [u]
                    else:
                        output_list[connected_to[u]].append(u)
            visited[u] = True
            for neighbor in adj_list[u]:
                (v,w) = neighbor
                if w < keys[v] and visited[v] == False:
                    keys[v] = w
                    connected_to[v] = u
                    heapq.heappush(q, (w,v))
                
    output_file = open("output", "a")
    for line in output_list:
        output_file.write(','.join(str(x) for x in line)+'\n')
    graph_file.close()
    output_file.close()

MST("input")