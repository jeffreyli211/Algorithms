import math

def karatsuba(x,y,n):
    if n == 1:
        return x * y
    else:
        m = n//2
        a = x//(2**m)
        b = x % (2**m)
        c = y//(2**m)
        d = y % (2**m)
        e = karatsuba(a,c,m)
        f = karatsuba(b,d,m)
        g = karatsuba(a-b,c-d,m)
        return ((2**(2*m))*e) + ((2**m)*(e+f-g)) + f

def read_and_compute(input):
    bin_int_file = open(input,"r")
    file_info = bin_int_file.readlines()
    bit_len = int(file_info[0])
    input1 = int(file_info[1],2)
    input2 = int(file_info[2],2)
    bin_value = bin(karatsuba(input1,input2,bit_len))
    ret = bin_value[2:]
    output_file = open("output","a")
    output_file.write(str(ret))
    bin_int_file.close()
    output_file.close()

read_and_compute("input")