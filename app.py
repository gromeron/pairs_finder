#!/bin/python3

def pairs_finder(arr, sum):

    s1 = arr
    s2 = {}

    for i, v in enumerate(s1):
        diff = sum - v
        if diff in s1:
            s2[v] = diff
    return s2

def show_results(s2):
    for key, values in s2.items():
        print("+ ",key,",",values)


if __name__ == '__main__':

    arr = list(map(int, input('> Enter comma separated integers: ').rstrip().split(',')))
    
    sum = int(input('> Please enter the sum value: ').strip())

    result = pairs_finder(arr, sum)

    print(f'the solution is: {result}')
    show_results(result)