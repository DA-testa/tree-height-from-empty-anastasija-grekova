# python3

import sys
import threading, queue
import os


def compute_height(n, parents):
    out_queue=queue.Queue()
    for i, j in enumerate(parents):
        result = depth(j, parents, out_queue)
        if result == n:
            return result
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
    return element_depth

def main():
    check = input()
    check = check.replace("\r","")
    check = check.replace("\n","")
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
                n = int(newLines[0].replace("\n", ""))
                parents = newLines[1].replace("\n", "").split()
                parents = [int(i) for i in parents] 
            print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**30)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
