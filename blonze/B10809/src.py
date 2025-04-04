import sys

def slv():
    arr = sys.stdin.readline().strip()
    alpha_arr = [-1] * 26

    for x in range(len(arr)):
        index = ord(arr[x]) - 97
        if alpha_arr[index] == -1:
            alpha_arr[index] = x
    
    for x in alpha_arr:
        print(x , end=' ')

if __name__ == "__main__":
    slv()