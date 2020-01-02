import sys
import heapq

def make_adj_list(e,n):
    ret = [['-']] * n
    for u_v in e:
        u = u_v[0]
        v = u_v[1]
        w = u_v[2]
        if ret[u] == ['-']:
            v_w = (v,w)
            ret[u] = [v_w]
        else:
            v_w = (v,w)
            ret[u].append(v_w)
    return ret

def shortest_path(input):
    graph_file = open(input,"r")
    info = graph_file.readlines()
    graph_info = [[int(n) for n in line.split(',')] for line in info]

    n = graph_info[0][0]
    edges = graph_info[3:]
    adj_list = make_adj_list(edges,n)
    visited = [False] * n # Explored nodes
    distances = [sys.maxsize for node in range(n)]
    parents = ['-']*n

    s = graph_info[2][0]
    distances[s] = 0
    q = []
    q.append((distances[s],s))
    while q != []:
        heapq.heapify(q)
        (pi,s) = heapq.heappop(q)
        if visited[s] == True:
            continue
        else:
            visited[s] = True
            for neighbor in adj_list[s]:
                if neighbor != '-':
                    (v,w) = neighbor
                    temp_dist = pi + w
                    if temp_dist < distances[v] and visited[v] == False:
                        distances[v] = temp_dist
                        parents[v] = s
                        heapq.heappush(q, (distances[v],v))
                else:
                    break

    output_file = open("output", "a")
    for path_line in range(n):
        output_file.write(str(distances[path_line]) + ',' + str(parents[path_line]) + '\n')
    graph_file.close()
    output_file.close()


shortest_path("input")
