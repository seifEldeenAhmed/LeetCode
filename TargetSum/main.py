

def target(nums,target):
    d={}
    for i,n in enumerate(nums):
       d[n]=i
    for i,n in enumerate(nums):
        diff=target-n
        if diff in d and d[diff]!=i:
            return [d[diff],i]
    return -1

print(target([3,4,5,6], 19))