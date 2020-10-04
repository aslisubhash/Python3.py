#bubble sort
import time
def bubble(l):
    for i in range(len(l)-1):
        print("this is the",i,"pass")
        time.sleep(2)
        for j in range(len(l)-1-i):
            time.sleep(2)
            print("j is",l[j],"j+1 is",l[j+1])
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                
    print(l)

l=[12,34,11,10,45,100]
bubble(l)
