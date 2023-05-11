def create_phone_number(n):
    #your code here
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

if __name__ == '__main__':
    string = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(string)