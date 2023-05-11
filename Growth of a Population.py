def nb_year(p0, percent, aug, p):
    # your code
    percent /= 100
    anos = 0

    while p0 < p:
        p0 += int(p0 * percent + aug)
        anos += 1

    return anos


if __name__ == '__main__':
    result = nb_year(1500, 5, 100, 5000)
    print(result)
