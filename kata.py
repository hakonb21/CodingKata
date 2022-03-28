#
import re
def add(str):
    if str == "":
        return 0
    split = re.split(',|\n',str)
    sum = 0
    neg_lis = []
    for i in split:
        if int(i) < 0:
            neg_lis.append(i)
        if int(i) < 1001:
            sum += int(i)    
    if len(neg_lis) > 0:
        neg_formated =  ' '.join(neg_lis)
        raise ValueError(f'Negative numbers not allowed: {neg_formated}')
    return sum
    

