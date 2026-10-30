"""Boundary input contracts for interview reference algorithms."""
import unittest
from test_differential import load

class BoundaryTests(unittest.TestCase):
    def test_empty_median_input(self):
        with self.assertRaises(ValueError):
            load(41).Solution().findMedianSortedArrays([], [])

    def test_median_stream_before_first_update(self):
        with self.assertRaises(ValueError):
            load(48).MedianFinder().findMedian()

    def test_invalid_sampling_weights(self):
        ctor = load(51).Solution
        for weights in ([], [0], [-1, 3], [2, 0, 1], [2, 1.5], [True, 2]):
            with self.subTest(weights=weights), self.assertRaises(ValueError):
                ctor(weights)

    def test_invalid_k_or_values(self):
        solver = load(86).Solution()
        for nums, k in (([], 1), ([1], 0), ([1, 2], 3), ([0, 1], 2), ([-1, 2], 1)):
            with self.subTest(nums=nums, k=k), self.assertRaises(ValueError):
                solver.canPartitionKSubsets(nums, k)

    def test_partition_does_not_mutate_input(self):
        nums = [4, 1, 2, 3, 3, 2, 1]
        expected = nums.copy()
        self.assertTrue(load(86).Solution().canPartitionKSubsets(nums, 4))
        self.assertEqual(nums, expected)

if __name__ == "__main__":
    unittest.main()
