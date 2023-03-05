# python3

import sys
import threading, queue
#import csv
#import numpy
import os


def compute_height(n, parents):
    out_queue=queue.Queue()

    #max_height = [1] * n
    t1=[1] * n
    for i, j in enumerate(parents):
        t1[i]=threading.Thread(target=depth, args=(j, parents, out_queue))
        t1[i].start()
       # t1[i].join()
       # depth(j, parents, out_queue)
        #while j != -1:
        #    max_height[i] += 1
        #    j = parents[j]
    #out_queue.put(max)
    max_value = 0
    for i in out_queue.queue:
        if max_value < i:
            max_value = i
        
    return max_value

def depth(j, parents, out_queue):
    element_depth = 1
    while j != -1:
        element_depth += 1
        j = parents[j]
    out_queue.put(element_depth)

def main():
    check = input()
    check = check.replace("\r","")
    check = check.replace("\n","")
    #print("-"+check+"-")
    if check == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
        
        print(compute_height(n, parents))

    if check == 'F':
        path = os.getcwd() + '/test'
        os.chdir(path)
        file_name = input()
        if 'a' in file_name:
            print("error")
            quit()        
        else:
            file_path = f"{path}/{file_name}"
            with open(file_path, "r", encoding="utf-8-sig") as f:
                newLines = f.readlines()
            #    newLines = []
            #    for x in lines:
           #         newLines.append(x.replace("\n", ""))
                n = int(newLines[0].replace("\n", ""))
                parents = newLines[1].replace("\n", "").split()
                parents = [int(i) for i in parents] 
              #  out_queue=queue.Queue()
                #t1=threading.Thread(target=compute_height, args=(n, parents, out_queue))
                #t1.start()
                #t1.join()
            #out_queue=queue.Queue()    
            print(compute_height(n, parents))  
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
