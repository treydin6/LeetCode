import unittest


# 217.
def contains_duplicate(nums: list[int]) -> bool:
    hash: dict[int, int] = {} # {nums[i]: count}
    for num in nums:
        if hash.get(num):
            return True
        hash[num] = 1
    return False


# 242.
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in t:
        char_count[char] = char_count.get(char, 0) - 1
        if char_count[char] < 0:
            return False

    for val in char_count.values():
        if val != 0:
            return False
    return True


# 1.
def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map: {int: int} = {}
    for idx, num in enumerate(nums):
        compliment = hash_map.get(num)
        if compliment is not None:
            return [idx, compliment]
        
        hash_map[target - num] = idx

    return []




class TestFuncs(unittest.TestCase):

    def test_contains_duplicate_true_one(self):
        nums = [1,2,3,1]
        self.assertTrue(contains_duplicate(nums))

    def test_test_contains_duplicate_true_two(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(contains_duplicate(nums))

    def test_test_contains_duplicate_false_two(self):
        nums = [1,2,3,4]
        self.assertFalse(contains_duplicate(nums))


    def test_anagram_correct_true(self):
        anagram: str = "anagram"
        anagramCorrect: str = "nagaram"
        self.assertTrue(is_anagram(anagram, anagramCorrect))

    def test_anagram_correct_false(self):
        anagram: str = "anagram"
        anagramInvalid: str = "grammag"
        self.assertFalse(is_anagram(anagram, anagramInvalid))

    def test_two_sum_one(self):
        two_sum_arr = [2,7,11,15]
        target = 9
        expexted = [0,1]
        res = two_sum(two_sum_arr, target)
        self.assertCountEqual(expexted, res)

    def test_two_sum_two(self):
        two_sum_arr = [3,2,4]
        target = 6
        expexted = [1,2]

        res = two_sum(two_sum_arr, target)
        self.assertCountEqual(expexted, res)

    def test_two_sum_three(self):
        two_sum_arr = [3,3]
        target = 6
        expexted = [0,1]

        res = two_sum(two_sum_arr, target)
        self.assertCountEqual(expexted, res)

if __name__ == '__main__':
    unittest.main()