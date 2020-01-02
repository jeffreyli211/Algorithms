def opt_sched(input):
    sched_file = open(input, "r")
    info = sched_file.readlines()
    sched_info = [[int(n) for n in line.split(',')] for line in info]
    requests = sched_info[1:]

    R = [(requests[i][1],i) for i in range(sched_info[0][0])]
    R.sort()
    A = []
    while R != []:
        job_i = R.pop(0)
        A.append(job_i[1])
        rest_R = R[0:]
        for j in rest_R:
            S_j = requests[j[1]][0]
            if S_j <= job_i[0]:
                R.remove(j)
    
    output_file = open("output", 'a')
    for job in A:
        output_file.write(str(job)+'\n')
    sched_file.close()
    output_file.close()

opt_sched("input")