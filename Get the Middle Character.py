def get_middle(s):
    size = len(s)
    return s[int(size/2)] if size%2 == 1 else s[int(size/2) - 1] + s[int(size/2)]

if __name__ == '__main__':
    result = get_middle("impar")
    print(result)