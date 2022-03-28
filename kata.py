def add(str):
    if str == "":
        return 0
    split = str.split(",")
    if len(split) == 1:
        return int(str)
    if len(split) == 2:
        return int(split[0]) + int(split[1])

   
        

