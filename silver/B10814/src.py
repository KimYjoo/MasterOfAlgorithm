import sys

def slv():
    T = int(sys.stdin.readline().strip())
    arr = []
    for i in range(T):
        age, name = sys.stdin.readline().split()
        arr.append({'age':int(age), 'name':name, 'id': i})
    arr.sort(key= lambda x:(x['age'], x['id']))

    for user in arr:
        print(f"{user['age']} {user['name']}")

if __name__ == "__main__":
    slv()