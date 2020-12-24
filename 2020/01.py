input = [int(line.rstrip('\n')) for line in open("input/01.txt")]

def twoSum(nums, target):
    seen = set()
    for n in nums:
        comp = target - n
        if comp in seen:
            return n * comp
        seen.add(n)
    return -1

def threeSum(nums, target):
    for i in range(len(nums)):
        n = nums[i]
        new_target = target - n
        val = twoSum(nums[i+1:], new_target)
        if val >0:
            return n*val

def print_solution():
    print("Day 1 : " + str(twoSum(input, 2020)))
    print("Day 2 : " + str(threeSum(input, 2020)))
    

print_solution()