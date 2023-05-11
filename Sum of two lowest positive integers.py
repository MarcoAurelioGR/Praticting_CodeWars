def sum_two_smallest_numbers(numbers):
    #your code here
    numb1 = numbers[0]
    numb2 = numbers[1]
    for n in range(2, len(numbers)):
        if numb1 - numb2 > 0:
            if numb1 > numbers[n]:
                numb1 = numbers[n]
        elif numb2 > numbers[n]:
                numb2 = numbers[n]

    return numb1 + numb2

if __name__ == '__main__':
    result = sum_two_smallest_numbers([3122,23122,1123,41233])
    print(result)