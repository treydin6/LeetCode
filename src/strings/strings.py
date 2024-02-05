import unittest

def fizz_buzz(n: int) -> list[str]:
        answers: str = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                answers.append("FizzBuzz")
            elif num % 3 == 0:
                answers.append("Fizz")
            elif num % 5 == 0:
                answers.append("Buzz")
            else:
                answers.append(f"{num}")
        return answers
        
class TestFuncs(unittest.TestCase):
     def test_fiz_buzz(self):
        n_one = 3
        expected_one = ["1","2","Fizz"]
        res_one = fizz_buzz(n_one)
        self.assertEqual(expected_one, res_one)

        n_two = 5
        expected_two = ["1","2","Fizz","4","Buzz"]
        res_two = fizz_buzz(n_two)
        self.assertEqual(expected_two, res_two)

        n_three = 15
        expected_three = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        res_three = fizz_buzz(n_three)
        self.assertEqual(expected_three, res_three)

if __name__ == '__main__':
    unittest.main()
