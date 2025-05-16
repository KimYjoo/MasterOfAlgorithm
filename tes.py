def slv():
    T = int(input().strip())

    for _ in range(T):
        commands = list(input().strip())
        question_R = 0
        question_L = 0
        pos_R = []
        pos_L = []
        for command in commands:
            if command == "?":
                question_R += 1
                question_L -= 1
            else:
                question_R += 1 if command == 'R' else -1
                question_L += 1 if command == 'R' else -1
            pos_R.append(question_R)
            pos_L.append(question_L)
        result = max(max([abs(i) for i in pos_R]), max([abs(i) for i in pos_L]))
        print(result)


if __name__ == "__main__":
    slv()