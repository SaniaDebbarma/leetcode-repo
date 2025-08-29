class solution(object):
    def twoSum(self, nums, target):
        hash_map = {}  #this will store numbers and their indices
        for i, num in enumerate(nums):
            comple = target - num
            if comple in hash_map:
                return[hash_map[comple], i ]
            hash_map[num]= i