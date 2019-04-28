import sys
current_ID = None
f_ID = None
count = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    #print len(line)
    ID = line[0]
    f = line[1]
    if current_ID == ID and f_ID == f:
        count = count+1
    else:
        if current_ID is not None:
            print current_ID + "\t" + str(count) + "\t" + f_ID
        current_ID = ID
        f_ID= f
        count = 1
        
      

