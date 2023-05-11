def find_even_index(arr): #your code here
    sumRight = 0
    sumLeft = 0
    nLeft = []
    nRight = []

    for iLeft in range(len(arr)):
        nLeft.append(arr[iLeft])
        sumLeft = sum(nLeft)
        for iRight in range(len(arr) - 1, iLeft - 1, -1):
            nRight.append(arr[iRight])
            sumRight = sum(nRight)

        if sumLeft == sumRight:
            return iLeft
        else:
            nRight.clear()

    return -1

if __name__ == '__main__':
    result = find_even_index([1,2,3,4,3,2,1])
    print(result)

