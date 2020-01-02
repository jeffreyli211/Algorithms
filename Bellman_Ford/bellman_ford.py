import sys
import heapq

def BF(G,v,e,src):
    M = [sys.maxsize] * v
    M[src] = 0

    for _ in range(v-1):
        for j in range(e):
            calc_dist = M[G[j][0]] + G[j][2]
            curr_dist = M[G[j][1]]
            if calc_dist < curr_dist:
                M[G[j][1]] = calc_dist
    return M

def read_and_call_BF(input):
    graph_file = open(input,'r')
    info = graph_file.readlines()
    graph_info = [[int(n) for n in line.split(',')] for line in info]

    n = graph_info[0][0]
    m = graph_info[1][0]
    source = graph_info[2][0]
    edges = graph_info[3:]
    M = BF(edges,n,m,source)

    output_file = open('output','a')
    for distance in M:
        output_file.write(str(distance)+'\n')
    graph_file.close()
    output_file.close()

read_and_call_BF('03_input')