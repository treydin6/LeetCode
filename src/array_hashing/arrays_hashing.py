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

    def test_contains_duplicate_true(self):
        nums = [1,2,3,1]
        self.assertTrue(contains_duplicate(nums))

        nums2 = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(contains_duplicate(nums2))

    def test_test_contains_duplicate_false(self):
        nums = [1,2,3,4]
        self.assertFalse(contains_duplicate(nums))


    def test_is_anagram_true(self):
        anagram: str = "anagram"
        anagramCorrect: str = "nagaram"
        self.assertTrue(is_anagram(anagram, anagramCorrect))

    def test_is_anagram_false(self):
        anagram: str = "anagram"
        anagramInvalid: str = "grammag"
        self.assertFalse(is_anagram(anagram, anagramInvalid))


    def test_two_sum(self):
        two_sum_arr_one = [2,7,11,15]
        target_one = 9
        expexted_one = [0,1]
        res_one = two_sum(two_sum_arr_one, target_one)
        self.assertCountEqual(expexted_one, res_one)

        two_sum_arr_two = [3,2,4]
        target_two = 6
        expexted_two = [1,2]
        res_two = two_sum(two_sum_arr_two, target_two)
        self.assertCountEqual(expexted_two, res_two)

        two_sum_arr_three = [3,3]
        target_three = 6
        expexted_three = [0,1]
        res_three = two_sum(two_sum_arr_three, target_three)
        self.assertCountEqual(expexted_three, res_three)



if __name__ == '__main__':
    unittest.main()