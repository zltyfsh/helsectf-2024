code = "gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~"
filter = [ 1, 0, -1 ]

flag = ""
i = 0
for j in range(len(code)):
    c = ord(code[j]) + filter[i]
    flag += chr(c)
    i += 1
    if i >= len(filter):
        i = 0

print(flag)

# helsectf{l3nGe_s1D3n_f01k_progaMMeR7e_i_Fortran_90}
