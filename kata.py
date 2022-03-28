def add(str):
    if str == "":
        return 0
    split = str.split(",")
    sum = 0
    for i in split:
        sum += int(i)
    return sum
    

   
        

