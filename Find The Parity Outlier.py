def find_outlier(integers):

    par = 0

    for i in range(3):
        if integers[i]%2 == 0:
            par += 1

    if par >= 2:
        for integer in integers:
            if integer%2 == 1:
                return integer
                break

    return

if __name__ == '__main__':
    result = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
    print(result)