class Solution(object):
    def maxArea(self, height):
        left_pointer = 0
        right_pointer = len(height) - 1
        max_water = 0

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            h = min(height[left_pointer], height[right_pointer])
            area = width * h
            max_water = max(max_water, area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water

# Taking user input
height = list(map(int, input("Enter heights separated by space: ").split()))

# Calling the function
sol = Solution()
print("Maximum area:", sol.maxArea(height))