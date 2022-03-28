import re
def add(str):
    if str == "":
        return 0
    split = re.split(',|\n',str)
    sum = 0
    for i in split:
        sum += int(i)
    return sum
    


   
        

