def bin_to_dec(n):

    count = 0
    dec = 0

    for i in n[::-1]:
        dec += (2**count) * int(i)
        count += 1
    return dec 

print(bin_to_dec('1010'))

def bin_to_dec_recurse(n):
    pass
