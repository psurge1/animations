def set_digits(num: str, ndigits: int) -> str:
    for i in range(len(num)-1, -1, -1):
        if num[i]==".":
            for k in range(ndigits-(len(num)-i-1)):
                num+="0"
            return num
    return num

def array_to_string(arr: list, nl=False) -> str:
    s = ""
    for i in arr:
        s+=i
        if nl:
            s+='\n'
    return s

def matrix_to_string(matrix: list, midnl=False, endnl = False) -> str:
    s = ""
    for arr in matrix:
        for i in arr:
            s+=i
            if midnl:
                s+='\n'
        if endnl:
            s+='\n'