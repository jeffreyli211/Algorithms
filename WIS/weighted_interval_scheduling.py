def takeFin(elem):
    return elem[2]

sched_file = open('input','r')
info = sched_file.readlines()
sched_info = [[int(n) for n in line.split(',')] for line in info]
sched_n = sched_info[0][0]
requests = sched_info[1:]
fin_Times = sorted(requests,key=takeFin)

p_arr = [0] * (sched_n+1)
if sched_n >= 2:
    j = sched_n
    i = j - 1
    while j != 0:
        if fin_Times[i-1][2] <= fin_Times[j-1][1]:
            p_arr[j] = fin_Times[i-1][0]+1
            j -= 1
            i = j - 1
        elif i == 0:
            j -= 1
            i = j - 1
        else:
            i -= 1

M = [None] * (sched_n+1)
M[0] = 0

final_indices = [[] for n in range(sched_n+1)]

def M_compute_opt(j):
    if M[j] == None:
        choice1 = requests[j-1][3] + M_compute_opt(p_arr[j])
        choice2 = M_compute_opt(j-1)
        M[j] = max(choice1,choice2)
        if M[j] == choice1:
            final_indices[j] += final_indices[p_arr[j]]
            final_indices[j].append(j)
        else:
            final_indices[j] += final_indices[j-1]
    return M[j]

M_compute_opt(sched_n)

output_file = open('output','a')
for i in final_indices[-1]:
    output_file.write(str(i-1)+'\n')
sched_file.close()
output_file.close()
