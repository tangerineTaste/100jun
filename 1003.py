def fibonacci(n):
    
    if n==0:
        global zero_counter
        zero_counter += 1
    elif n==1:
        global one_counter
        one_counter += 1
    else:
        fibonacci(n-1)
        fibonacci(n-2)
    return zero_counter, one_counter
term = int(input())
nums = []
for i in range(term):
    nums.append(int(input('')))
print('========')
for i in nums:
    zero_counter = 0
    one_counter = 0
    print(fibonacci(i)[0], fibonacci(i)[1])