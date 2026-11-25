def matchingStrings(strings, queries):
    frequency = {}

    for s in strings:
        frequency[s] = frequency.get(s, 0) + 1

    return [frequency.get(q, 0) for q in queries]

if __name__ == "__main__":
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    print(*matchingStrings(strings, queries), sep="\n")
