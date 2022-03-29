import re

def add(str):
    if str == "":
        return 0
    delimeter = ',|\n'
    if len(str) > 1 and str[:2] == '//':
        end = str.find('\n')
        delimeter += f'|{str[2:end]}'
        str = str[end+1:]
    split = re.split(delimeter,str)
    sum = 0
    neg_lis = []
    print(split)
    for i in split:
        if int(i) < 0:
            neg_lis.append(i)
        if int(i) < 1001:
            sum += int(i)
    if len(neg_lis) > 0:
        neg_formated =  ' '.join(neg_lis)
        raise ValueError(f'Negative numbers not allowed: {neg_formated}')
    return sum