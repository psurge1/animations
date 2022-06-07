def set_digits(num, ndigits):
    for i in range(len(num)-1, -1, -1):
        if num[i]==".":
            for k in range(ndigits-(len(num)-i-1)):
                num+="0"
            return num
    return num

def array_to_string(arr, nl=False):
    s = ""
    for i in arr:
        s+=i
        if nl:
            s+='\n'
    return s

def matrix_to_string(matrix, midnl=False, endnl = False):
    s = ""
    for arr in matrix:
        for i in arr:
            s+=i
            if midnl:
                s+='\n'
        if endnl:
            s+='\n'