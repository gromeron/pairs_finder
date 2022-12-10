# Pairs finder

## Task
​
The task is to write a function that finds pairs of integers from a list that sum to a given value. The function will take as input the list of numbers as well as the target sum.
​
Sample output is shown below.
```
> app 1,9,5,0,20,-4,12,16,7 12
​
+ 12,0
+ 5,7
+ 16,-4
​
```
​
In the example, there is an executable named `app`. It takes as command line arguments a comma separated list of integers, and the target integer. Your app doesn't need to have identical input/output mechanisms. For example, you could read from a file instead of the command line.
​
You can assume that all input values are integers. You can assume that there aren't any repeat values in the list.
​
The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately. This is _not_ a closed book test. You are
encouraged to reach out with any questions that you come across.

## Installation - linux and mac
1. Ensure you have python installed on your system

2. Download the code

```bash
git clone https://github.com/gromeron/pairs_finder.git
```

2. Get into de directory

```bash
cd pairs_finder
```

3. Excecute de code

```bash
python app.py
```

## Istallation - windows
1. Ensure you have python installed on your system

2. Download the code from the zip file

```bash
https://github.com/gromeron/pairs_finder/archive/refs/heads/main.zip
```

3. Extract the code into de folder

4. Get into de folder

```bash
cd pairs_finder
```

3. Excecute de code

```bash
python app.py
```

## Using the code
After the code excecution, you will prompt an input intructions, please follow them to test the algorithm

1. Enter the items of the array separate by commas
2. Enter the value of the two integers from the array to be added
3. Finally you could see all the possible combinations that fulfill the sum condition in the array


## Explanation
1. Initially we want to find all the pairs into the array where its sum is equal to the given number, this value is taken as the second argument.

![pair_finder](https://user-images.githubusercontent.com/98790008/206528014-135bd961-d09c-4125-925d-396750de1328.png)

2. The algorithm uses just one iteration with one `for` expression that will look into the array for the value into the key, value in a dictionary data structure, using as a key the index of the array; in this way we could map the solution in a proper way without using a second `for`
3. At the very begining the simple working solution just with arrays was

```py
def pairs_finder_1(arr, sum):
    
    s1 = arr
    s2 = []

    for i in range(0,len(s1)):
        for j in range(1,len(s1)-1):
            if(s1[i] + s1[j]) == sum:
                s2.append(s1[i])
                s2.append(s1[j])

    return s2
```

but in this case the behavior of the algorithm was of O(n^2) due the double `for` expresions into the code.
4. This algorithm fullfil a Big O Complexity of O(n) according with the information found in this [link](https://www.bigocheatsheet.com/).

## Addendum
There is another way to inprove the algorithm and is this version

```py
def pairs_finder(arr, sum):

    s1 = {}
    s2 = {}

    for i, v in enumerate(arr):
        diff = sum - v
        s1[v] = diff
        if diff in s1:
            s2[v] = diff

    return s2
```

With this one we could get and speed improve, following the results comparing the three functions

Function | CPU times [μs] | per loop (mean[μs] ± std. dev.[ns] of 7 runs, 100000 loops each)
---|---|---
1 | 26 | 12.5 ± 3.87
2 | 9 | 2.35 ± 74.8
3 | 8 | 2.09 ± 109

### Results

Al the three functions were tested using `%time` and `timeit` methods into a colab python workbook.

### Function 1
```py
def pairs_finder_1(arr, sum):
    
    s1 = arr
    s2 = []

    for i in range(0,len(s1)):
        for j in range(1,len(s1)-1):
            if(s1[i] + s1[j]) == sum:
                s2.append(s1[i])
                s2.append(s1[j])

    return s2
```

### Function 2

```py
def pairs_finder_2(arr, sum):

    s1 = {}

    for i, v in enumerate(arr):
        diff = sum - v
        if diff in arr:
            s1[v] = diff
    return s1
```

### Function 3

def pairs_finder(arr, sum):

    s1 = {}
    s2 = {}

    for i, v in enumerate(arr):
        diff = sum - v
        s1[v] = diff
        if diff in s1:
            s2[v] = diff

    return s2

## Conclusion
The best result was obtained with the third function, using only one 'for' statement and one `if` also, to search in a hash mapped structure.