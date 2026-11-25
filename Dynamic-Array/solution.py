def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        queryType, x, y = query
        idx = (x ^ lastAnswer) % n

        if queryType == 1:
            seqList[idx].append(y)
        elif queryType == 2:
            value = seqList[idx][y % len(seqList[idx])]
            lastAnswer = value
            answers.append(lastAnswer)

    return answers

if __name__ == "__main__":
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(q)]
    for answer in dynamicArray(n, queries):
        print(answer)
