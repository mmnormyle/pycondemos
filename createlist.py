basename = "user"

with open("/home/revoscaler/Source/pycondemos/userlist.txt", "w") as f:
    for i in range(100):
        name = basename + str(i)
        f.write(name + "\n")


        
    

