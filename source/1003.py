term = int(input())
nums = []
for i in range(term):
    nums.append(int(input()))
fibonacci = [0,1]
for i in range(2,max(nums)+1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
for i in range(0,term): 
    if nums[i]==0 :
        print("1 0")
    else:
        print(fibonacci[nums[i]-1], fibonacci[nums[i]])