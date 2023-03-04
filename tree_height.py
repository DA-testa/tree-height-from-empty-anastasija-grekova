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
    #check = input()


    path = os.getcwd() + '/test'
    os.chdir(path)
    
    for file in os.listdir():
        file_path = f"{path}/{file}"
    #print(file)
        #if 'a' in file:
        #'''with open(file_path, "r", encoding="utf-8-sig") as f:
        #        lines = f.readlines()
        #        newLines = []
        #        for x in lines:
        #            newLines.append(x.replace("\n", ""))
        #        print(int(newLines[0]))'''
        #    quit()
                
        #else:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
            newLines = []
            for x in lines:
                newLines.append(x.replace("\n", ""))
            n = int(newLines[0])
            parents = newLines[1].split()
            parents = [int(i) for i in parents]
        print(compute_height(n, parents))


    #if check == "I":
    #    n = int(input())
    #    parents = list(map(int, input().split()))
    #    print(compute_height(n, parents))

    '''if check == 'F':
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
            with open(file_path, "r", encoding="utf-8-sig") as f:
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
               
    
        print(compute_height(n, parents))'''
  
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
