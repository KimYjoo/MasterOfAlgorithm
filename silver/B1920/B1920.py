import sys



def bin_search (key, arr):
    left = 0
    right = len(arr)-1
    while (left <= right) :
        mid = (left + right) // 2
        if(arr[mid] < key) :
            left = mid + 1
        elif(arr[mid] > key) :
            right = mid - 1
        else :
            return 1
    return 0

def slv(std_arr, search_arr) :
    for i in search_arr :
        print(bin_search(i,std_arr))

if __name__ == "__main__" :
    N = sys.stdin.readline().strip()

    std_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    list.sort(std_arr)

    M = sys.stdin.readline().strip()

    search_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    slv(std_arr,search_arr)
