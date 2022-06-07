def set_digits(num, ndigits):
    for i in range(len(num)-1, -1, -1):
        if num[i]==".":
            for k in range(ndigits-(len(num)-i-1)):
                num+="0"
            return num
    return num