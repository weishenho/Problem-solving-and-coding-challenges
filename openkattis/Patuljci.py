import sys

nums = []
for line in sys.stdin:
    nums.append( int(line.strip()) )

diff = sum(nums) - 100
nums1 = [x for x in nums if x < diff]
a,b = 0,0

while nums1:
    i = nums1.pop(0)
    aim = diff - i
    for x in nums1:
        if x == aim:
            a=i
            b=x
            break
    
    if a > 0 and b > 0:
        break

nums.remove(a)
nums.remove(b)

for n in nums:
    print(n)