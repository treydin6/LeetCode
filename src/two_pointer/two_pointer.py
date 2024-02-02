import unittest

# 11.
def container_with_most_water(container: list[int]) -> int:
    lp = 0
    rp = len(container) - 1
    max = 0
    while lp < rp:
        curWater = min(container[lp], container[rp]) * (rp - lp)
        if curWater > max: max = curWater
        if container[lp] > container[rp]:
            rp -= 1
        else:
            lp += 1
    return max

def two_sum_sorted_array(array: list[int], target: int) -> list[int]:
    lp = 0
    rp = len(array) - 1
    while lp < rp:
        if array[lp] + array[rp] == target:
            return [(lp + 1), (rp + 1)]
        if array[lp] + array[rp] > target:
            rp -= 1
        else:
            lp += 1
    return []

def remove_element(nums: list[int], val: int)-> list[int]:
    lp = 0
    rp = len(nums) - 1
    count = 0
    while lp < rp:
        if nums[lp] == val:
            nums[lp], nums[rp] = nums[rp], 0
            rp -= 1
            count += 1
        else:
            lp += 1
    return count


class TestTwoPointerFuncs(unittest.TestCase):

    def test_containers_with_most_water(self):
        container_one: list[int] = [1,8,6,2,5,4,8,3,7]
        expected_one: int = 49
        res_one: int = container_with_most_water(container_one)
        self.assertEqual(res_one, expected_one)

        container_two: list[int] = [1,1]
        expected_two: int = 1
        res_two: int = container_with_most_water(container_two)
        self.assertEqual(res_two, expected_two)


    def test_two_sum_sorted_array(self):
        sorted_one: list[int] = [2,7,11,15]
        target_one: int = 9
        expected_one: list[int] = [1,2]
        res_one = two_sum_sorted_array(sorted_one, target_one)
        self.assertCountEqual(expected_one, res_one)

        sorted_two: list[int] = [2,3,4]
        target_two: int = 6
        expected_two: list[int] = [1,3]
        res_two = two_sum_sorted_array(sorted_two, target_two)
        self.assertCountEqual(expected_two, res_two)

        sorted_three: list[int] = [-1, 0]
        target_three: int = -1
        expected_three: list[int] = [1,2]
        res_three = two_sum_sorted_array(sorted_three, target_three)
        self.assertCountEqual(expected_three, res_three)

    def test_remove_element(self):
        array_one: list[int] = [3,2,2,3]
        val_one: int = 3
        expected_one: int = 2
        res_one: int = remove_element(array_one, val_one)
        self.assertEqual(expected_one, res_one)

        array_two: list[int] = [3,2,2,3]
        val_two: int = 3
        expected_two: int = 2
        res_two: int = remove_element(array_two, val_two)
        self.assertEqual(expected_two, res_two)


if __name__ == '__main__':
    unittest.main()