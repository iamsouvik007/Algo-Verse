# 961. N-Repeated Element in Size 2N Array
'''
You are given an integer array nums with the following properties:
    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.
    Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 

Constraints:

    2 <= n <= 5000
    nums.length == 2 * n
    0 <= nums[i] <= 104
    nums contains n + 1 unique elements and one of them is repeated exactly n times.
'''


from typing import List
from collections import Counter

class Solution:

    # Approach 1: HashSet (Most straightforward)
    # Time: O(n), Space: O(n)
    def repeatedNTimes_set(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)

    # Approach 2: Counter / Frequency Map
    # Time: O(n), Space: O(n)
    def repeatedNTimes_counter(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for num, count in freq.items():
            if count > 1:
                return num

    # Approach 3: Sorting
    # Time: O(n log n), Space: O(1) or O(n) depending on implementation
    def repeatedNTimes_sort(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    # Approach 4: Distance-based trick (Optimal, uses problem guarantee)
    # Time: O(n), Space: O(1)
    class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(2,len(nums)):
            if nums[i]==nums[i-1] or nums[i]==nums[i-2]:
                return nums[i]
        return nums[0] 
# If the loop does not return, the repeated element must be in the first two positions.
# Example: [5, 5, 1, 2] or [5, 1, 2, 5].
# Since the loop starts from index 2, we return nums[0] to handle this case.

# Fallback: if not found from index 2 onward, the repeated element is in nums[0] or nums[1].


class Solution:
    def repeatedNTimes(self, A: list[int]) -> int:
        for i in range(len(A) - 2):
            if A[i] == A[i + 1] or A[i] == A[i + 2]:
                return A[i]
        return A[-1]

        






