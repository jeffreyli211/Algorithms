import sys

def make_adj_list(e,n):
    ret = [[None,None]] * n
    for edge in e:
        (u,v,w) = (edge[0],edge[1],edge[2])
        if ret[u] == [None,None]:
            ret[u] = [(v,w)]
        else:
            ret[u].append((v,w))
        '''
        if ret[v] == ['-']:
            ret[v] = [(u,w)]
        else:
            ret[v].append((u,w))
        '''
    return ret

def make_res_G(e,n):
    ret = [{} for x in range(n)]
    for u,v,cap in e:
	    ret[u][v] = cap
	    ret[v][u] = 0
    return ret

def is_stPath(Gr,n,s,t,parent):
    visited = [False] * n 
    q = [] 
    q.append(s) 
    visited[s] = True

    while q: 
        u = q.pop(0)
        if u == t:
            return True
        else:
            for v in Gr[u]:
                if visited[v] == False and Gr[u][v] > 0 : 
                    q.append(v)
                    visited[v] = True
                    parent[v] = u
    return False

'''       
def find_s(row,s):
    for i in range(len(row)):
        if row[i][0] == s:
            return i
'''

def ford_fulk(input):
    graph_file = open(input,"r")
    info = graph_file.readlines()
    graph_info = [[int(n) for n in line.split(',')] for line in info]

    n = graph_info[0][0]
    src = graph_info[2][0]
    sink = graph_info[3][0]
    edges = graph_info[4:]
    parents = [-1] * n
    
    residual = make_res_G(edges,n)
    max_flow = 0

    while is_stPath(residual,n,src,sink,parents) == True:
        P_flow = sys.maxsize
        s = sink
        while s != src:
            P_flow = min(P_flow,residual[parents[s]][s])
            s = parents[s]
        max_flow += P_flow

        v = sink
        while v != src:
            u = parents[v]
            residual[u][v] -= P_flow
            residual[v][u] += P_flow 
            v = parents[v]
    
    output = []
    for u,v,_ in edges:
        output.append([u,v,residual[v][u]])
    output_file = open('output','a')
    for u,v,flow in output:
        output_file.write(str(u) + ',' + str(v) + ',' + str(flow) + '\n')
    graph_file.close()
    output_file.close()

ford_fulk("input")