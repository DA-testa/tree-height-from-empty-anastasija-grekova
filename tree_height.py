# python3

import sys
import threading
#import csv
#import numpy
import os


def compute_height(n, parents):
    max_height = [1] * n
    for i, j in enumerate(parents):
        while j != -1:
            max_height[i] += 1
            j = parents[j]
    return max(max_height)

def main():
    check = input()
    if check == "I":
        n = int(input())
        parents = list(map(int, input().split()))

    if check == 'F':
        path = os.getcwd() + '/test'
        os.chdir(path)
        file_name = input()
        file_path = f"{path}/{file_name}"
        if 'a' in file_name:
            with open(file_path, "r", encoding="utf-8-sig") as f:
                lines = f.readlines()
                newLines = []
                for x in lines:
                    newLines.append(x.replace("\n", ""))
                print(int(newLines[0]))
                quit()
                
        else:
            #file_path = f"{path}/{file_name}"
            #print(file_path)
            with open(file_path, "r", encoding="utf-8-sig") as f:
                #    data = f.read()
                #for line in lines:
                lines = f.readlines()
                newLines = []
                for x in lines:
                    newLines.append(x.replace("\n", ""))
                #for i in range(0, len(newLines)):
                #    newLines[i] = int(newLines[i])
                #    newLines.append(int(x))
                n = int(newLines[0])
                parents = newLines[1].split()
                parents = [int(i) for i in parents]
                #for i in enumerate(parents):
                #    parents[i] = int(parents[i])
                #print(parents)
                    #for line in lines:
                    #    count += 1
                    #    n = lines.format(1, line.strip())
                    #    parents = lines.format
                    #if countLines == 1 :
                #        print(f.readline())
                        
                    #    n = f.readline;
                    #    print(n)
                #    else:
                        #print(f.readline())
                #        parents = f.readline()
                #    countLines += 1
        #else:
        #    print("sorry!")
    
    print(compute_height(n, parents))
    
        #print(text)







    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
