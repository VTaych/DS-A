# Uses python3
def edit_distance(y, z):
    if y == z:
        return 0
    elif len(y) == 0:
        return len(z)
    elif len(z) == 0:
        return len(y)

    check = {}
    for i in range(len(y) + 1):
        check[i, 0] = i
    for j in range(len(z) + 1):
        check[0, j] = j

    for i in range(1, len(y) + 1):
        dist = y[i-1]
        for j in range(1, len(z) + 1):
            dist2 = z[j-1]

            insertion = check[i, j - 1] + 1
            deletion = check[i - 1, j] + 1
            match = check[i - 1, j - 1]
            mismatch = check[i - 1, j - 1] + 1

            if dist == dist2:
                check[i, j] = min(insertion, deletion, match)
            else:
                check[i, j] = min(insertion, deletion, mismatch)

    return check[len(y), len(z)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("short", "ports"))
    # print(edit_distance("editing", "distance"))
    # print(edit_distance("ab", "ab"))
    # print(edit_distance("", "ab"))
    # print(edit_distance("feet", ""))
    # print(edit_distance("aabcc", "bccdd"))
