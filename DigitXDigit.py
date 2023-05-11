def square_digits(num):
# Your code here
    numbers = [str(int(n)**2) for n in str(num)]
    return int("".join(numbers))

if __name__ == '__main__':
    result = square_digits(9119)
    print(result)