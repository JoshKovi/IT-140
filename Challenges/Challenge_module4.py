
def challenge34(N = 14, numbers = [1,7,14,23,55,3,14]):

    if len(numbers) == 0:
        print('-1')
    else:
        for i in range(len(numbers)):
            if numbers[i] == N:
                print(numbers.index(N))
                break
            elif i == len(numbers)-1:
                print('-1')
            else:
                pass
def challenge35(numbers = [3,6,2,8,14,2,37,55,12,5,11,88]):
    placeHolder = []
    for i in numbers:
        placeHolder.append(i)
    placeHolder.sort(reverse=True)
    print(numbers.index(placeHolder[0]))

def challenge36(N=3, M = 6, numbers = [12,10,55,44,77,22,33,44,55,66,77,88]):
    if len(numbers) > N:
        for i in range(N-1,len(numbers),N):
            numbers[i] = numbers[i] * M
    print(numbers)

def challenge37(numbers= [12,22,33,44,55,66,77,88,99,67,45,34,18]):
    def isEven(n):
        return ((n % 2) == 0)

    oddNums, evenNums = [], []
    
    for i in numbers:
        if isEven(i):
            evenNums.append(i)
        else:
            oddNums.append(i)
    print(oddNums,'\n',evenNums,sep= "",flush=True)
