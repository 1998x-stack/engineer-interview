"""Seeded, bounded differential checks against independent brute-force oracles.

Unlike the ten original example-only smoke tests, each test exercises many inputs.
All generated inputs respect original LeetCode assumptions unless explicitly noted.
No network, nonstdlib dependency, or randomized CI variability is required.
"""
from __future__ import annotations

import bisect
from collections import Counter, OrderedDict, deque
import importlib.util
import itertools
import math
from pathlib import Path
import random
import statistics
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "solutions/python"


def load(number: int):
    matches = list(SOURCES.glob(f"{number:03d}-*.py"))
    if len(matches) != 1:
        raise AssertionError(f"expected one source for {number:03d}, got {matches}")
    path = matches[0]
    spec = importlib.util.spec_from_file_location("solution_" + path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rng():
    return random.Random(20261030)


def all_subarrays(nums):
    return [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]


class DifferentialTests(unittest.TestCase):
    def test_003_consecutive(self):
        solver = load(3).Solution()
        r = rng()
        for _ in range(80):
            nums = [r.randint(-8, 8) for _ in range(r.randint(0, 15))]
            result = 0
            for x in set(nums):
                length = 0
                while x + length in nums:
                    length += 1
                result = max(result, length)
            self.assertEqual(solver.longestConsecutive(nums), result)

    def test_004_product_except_self(self):
        solver = load(4).Solution()
        r = rng()
        for _ in range(80):
            nums = [r.randint(-3, 3) for _ in range(r.randint(2, 8))]
            expected = [math.prod(v for j, v in enumerate(nums) if j != i)
                        for i in range(len(nums))]
            self.assertEqual(solver.productExceptSelf(nums), expected)

    def test_005_subarray_sum(self):
        solver = load(5).Solution()
        r = rng()
        for _ in range(100):
            nums = [r.randint(-3, 3) for _ in range(r.randint(0, 10))]
            k = r.randint(-5, 5)
            expected = sum(sum(sub) == k for sub in all_subarrays(nums))
            self.assertEqual(solver.subarraySum(nums, k), expected)

    def test_007_first_missing_positive(self):
        solver = load(7).Solution()
        r = rng()
        for _ in range(75):
            nums = [r.randint(-4, 9) for _ in range(r.randint(0, 10))]
            expected = next(n for n in range(1, len(nums) + 2) if n not in nums)
            self.assertEqual(solver.firstMissingPositive(nums.copy()), expected)

    def test_008_zero_matrix(self):
        solver = load(8).Solution()
        r = rng()
        for _ in range(65):
            mat = [[r.randint(0, 2) for _ in range(r.randint(1, 1))] for _ in range(1)]
            height, width = r.randint(1, 6), r.randint(1, 6)
            mat = [[r.randint(0, 3) for _ in range(width)] for _ in range(height)]
            zeros = {(i, j) for i in range(height) for j in range(width) if mat[i][j] == 0}
            expected = [[0 if any(a == i or b == j for a, b in zeros) else mat[i][j]
                         for j in range(width)] for i in range(height)]
            solver.setZeroes(mat)
            self.assertEqual(mat, expected)

    def test_012_three_sum(self):
        solver = load(12).Solution()
        r = rng()
        for _ in range(70):
            nums = [r.randint(-5, 5) for _ in range(r.randint(0, 9))]
            expected = {tuple(sorted(t)) for t in itertools.combinations(nums, 3) if sum(t) == 0}
            actual = [tuple(sorted(t)) for t in solver.threeSum(nums.copy())]
            self.assertEqual(set(actual), expected)
            self.assertEqual(len(actual), len(set(actual)))

    def test_014_trapping_rain_water(self):
        solver = load(14).Solution()
        r = rng()
        for _ in range(70):
            arr = [r.randrange(6) for _ in range(r.randrange(12))]
            expected = sum(max(0, min(max(arr[:i + 1]), max(arr[i:])) - arr[i])
                           for i in range(len(arr)))
            self.assertEqual(solver.trap(arr), expected)

    def test_015_longest_distinct_substring(self):
        solver = load(15).Solution()
        r = rng()
        for _ in range(80):
            s = "".join(r.choices("abcd", k=r.randrange(12)))
            expected = max((len(t) for i in range(len(s))
                            for t in (s[i:j] for j in range(i + 1, len(s) + 1))
                            if len(set(t)) == len(t)), default=0)
            self.assertEqual(solver.lengthOfLongestSubstring(s), expected)

    def test_017_minimum_window(self):
        solver = load(17).Solution()
        r = rng()
        for _ in range(65):
            s = "".join(r.choices("abc", k=r.randrange(9)))
            t = "".join(r.choices("abc", k=r.randrange(1, 5)))
            possible = [(j - i, i, s[i:j])
                        for i in range(len(s)) for j in range(i + 1, len(s) + 1)
                        if not Counter(t) - Counter(s[i:j])]
            expected = min(possible)[2] if possible else ""
            self.assertEqual(solver.minWindow(s, t), expected)

    def test_018_find_anagrams(self):
        solver = load(18).Solution()
        r = rng()
        for _ in range(65):
            s = "".join(r.choices("abc", k=r.randrange(12)))
            p = "".join(r.choices("abc", k=r.randrange(1, 5)))
            expected = [i for i in range(len(s) - len(p) + 1)
                        if Counter(s[i:i + len(p)]) == Counter(p)]
            self.assertEqual(solver.findAnagrams(s, p), expected)

    def test_019_minimum_positive_subarray(self):
        solver = load(19).Solution()
        r = rng()
        for _ in range(70):
            a = [r.randint(1, 6) for _ in range(r.randrange(12))]
            target = r.randint(1, 30)
            lengths = [len(x) for x in all_subarrays(a) if sum(x) >= target]
            self.assertEqual(solver.minSubArrayLen(target, a), min(lengths, default=0))

    def test_020_sliding_window_max(self):
        solver = load(20).Solution()
        r = rng()
        for _ in range(70):
            a = [r.randrange(-6, 7) for _ in range(r.randint(1, 13))]
            k = r.randint(1, len(a))
            self.assertEqual(solver.maxSlidingWindow(a, k),
                             [max(a[i:i+k]) for i in range(len(a)-k+1)])

    def test_030_lru_trace_vs_ordered_dict(self):
        r = rng()
        for capacity in (1, 2, 5):
            cache = load(30).LRUCache(capacity)
            oracle = OrderedDict()
            for _ in range(125):
                key = r.randrange(7)
                if r.random() < 0.55:
                    value = r.randrange(-10, 11)
                    cache.put(key, value)
                    if key in oracle:
                        oracle.move_to_end(key)
                    oracle[key] = value
                    if len(oracle) > capacity:
                        oracle.popitem(last=False)
                else:
                    actual = cache.get(key)
                    expected = oracle.get(key, -1)
                    if key in oracle:
                        oracle.move_to_end(key)
                    self.assertEqual(actual, expected)

    def test_036_calculator_vs_python_int_expression(self):
        solver = load(36).Solution()
        r = rng()
        def expr(depth):
            if depth == 0 or r.random() < 0.45:
                return str(r.randrange(10))
            a, b = expr(depth-1), expr(depth-1)
            return "(" + a + r.choice(["+", "-"]) + b + ")"
        for _ in range(80):
            expression = expr(4)
            self.assertEqual(solver.calculate(expression), eval(expression), expression)

    def test_037_038_040_binary_search(self):
        a, b, c = (load(i).Solution() for i in (37, 38, 40))
        r = rng()
        for _ in range(90):
            vals = sorted(set(r.randint(-20, 20) for _ in range(r.randint(0, 20))))
            target = r.randint(-22, 22)
            self.assertEqual(a.search(vals, target),
                             vals.index(target) if target in vals else -1)
            if vals:
                pivot = r.randrange(len(vals))
                rotated = vals[pivot:] + vals[:pivot]
                self.assertEqual(b.search(rotated, target),
                                 rotated.index(target) if target in rotated else -1)
            sorted_dup = sorted([r.randint(-5, 5) for _ in range(r.randrange(20))])
            indices = [i for i, v in enumerate(sorted_dup) if v == target]
            expected = [indices[0], indices[-1]] if indices else [-1, -1]
            self.assertEqual(c.searchRange(sorted_dup, target), expected)

    def test_041_sorted_array_median(self):
        solver = load(41).Solution()
        r = rng()
        for _ in range(120):
            n = r.randrange(10)
            m = r.randrange(10)
            if n + m == 0:
                n = 1
            a = sorted(r.randint(-50, 50) for _ in range(n))
            b = sorted(r.randint(-50, 50) for _ in range(m))
            merged = sorted(a + b)
            expected = statistics.median(merged)
            self.assertEqual(solver.findMedianSortedArrays(a, b), expected)

    def test_042_koko_bananas(self):
        solver = load(42).Solution()
        r = rng()
        for _ in range(65):
            piles = [r.randint(1, 12) for _ in range(r.randint(1, 8))]
            h = r.randint(len(piles), 24)
            expected = next(speed for speed in range(1, max(piles) + 1)
                            if sum((x + speed - 1) // speed for x in piles) <= h)
            self.assertEqual(solver.minEatingSpeed(piles, h), expected)

    def test_045_kth_largest(self):
        solver = load(45).Solution()
        r = rng()
        for _ in range(80):
            nums = [r.randint(-5, 5) for _ in range(r.randint(1, 20))]
            k = r.randint(1, len(nums))
            self.assertEqual(solver.findKthLargest(nums.copy(), k), sorted(nums)[-k])

    def test_048_streaming_median(self):
        f = load(48).MedianFinder()
        r = rng()
        observed = []
        for _ in range(100):
            value = r.randint(-25, 25)
            f.addNum(value)
            bisect.insort(observed, value)
            self.assertEqual(f.findMedian(), statistics.median(observed))

    def test_051_weight_sampling_exact_ticket_partition(self):
        module = load(51)
        for weights in ([1], [1, 2, 3], [5, 1, 1, 4]):
            pick = module.Solution(list(weights))
            expected = [idx for idx, count in enumerate(weights) for _ in range(count)]
            for ticket, index in enumerate(expected, 1):
                with patch.object(module.random, "randint", return_value=ticket):
                    self.assertEqual(pick.pickIndex(), index)

    def test_052_rand10_rejection(self):
        module = load(52)
        output = []
        for x in range(1, 8):
            for y in range(1, 8):
                draws = iter([x, y] if (x-1)*7+y <= 40 else [x, y, 1, 1])
                module.rand7 = lambda: next(draws)
                output.append(module.Solution().rand10())
        self.assertEqual(Counter(output[:]), Counter({v: 4 + (9 if v == 1 else 0)
                                                  for v in range(1, 11)}))

    def test_053_sort(self):
        solver = load(53).Solution()
        r = rng()
        for _ in range(100):
            nums = [r.randint(-9, 9) for _ in range(r.randrange(25))]
            self.assertEqual(solver.sortArray(nums.copy()), sorted(nums))

    def test_066_islands(self):
        solver = load(66).Solution()
        r = rng()
        for _ in range(55):
            h, w = r.randint(1, 5), r.randint(1, 5)
            a = [[r.choice("01") for _ in range(w)] for _ in range(h)]
            seen = set()
            components = 0
            for i in range(h):
                for j in range(w):
                    if a[i][j] != "1" or (i, j) in seen:
                        continue
                    components += 1
                    stack = [(i, j)]
                    seen.add((i, j))
                    while stack:
                        x, y = stack.pop()
                        for xx, yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                            if (0 <= xx < h and 0 <= yy < w and
                                    a[xx][yy] == "1" and (xx, yy) not in seen):
                                seen.add((xx, yy))
                                stack.append((xx, yy))
            self.assertEqual(solver.numIslands([row.copy() for row in a]), components)

    def test_069_070_topological_order(self):
        can = load(69).Solution()
        orderer = load(70).Solution()
        r = rng()
        for _ in range(80):
            n = r.randint(1, 6)
            edges = [[a, b] for a in range(n) for b in range(n)
                     if a != b and r.random() < .19]
            # Independent feasibility oracle by enumerating all n! topological orders.
            valid = None
            for order in itertools.permutations(range(n)):
                positions = {v: i for i, v in enumerate(order)}
                if all(positions[b] < positions[a] for a, b in edges):
                    valid = order
                    break
            self.assertEqual(can.canFinish(n, edges), valid is not None)
            actual = orderer.findOrder(n, edges)
            if valid is None:
                self.assertEqual(actual, [])
            else:
                self.assertEqual(set(actual), set(range(n)))
                pos = {value: i for i, value in enumerate(actual)}
                self.assertTrue(all(pos[b] < pos[a] for a, b in edges))

    def test_078_subsets(self):
        solver = load(78).Solution()
        r = rng()
        for _ in range(55):
            nums = r.sample(range(-10, 11), r.randint(0, 8))
            expected = {tuple(sorted(x)) for n in range(len(nums)+1)
                        for x in itertools.combinations(nums, n)}
            actual = [tuple(sorted(x)) for x in solver.subsets(nums)]
            self.assertEqual(set(actual), expected)
            self.assertEqual(len(actual), len(set(actual)))

    def test_086_partition_k_bruteforce(self):
        solver = load(86).Solution()
        r = rng()
        for _ in range(70):
            nums = [r.randint(1, 7) for _ in range(r.randint(1, 7))]
            k = r.randint(1, min(len(nums), 4))
            target = sum(nums) // k
            if sum(nums) % k:
                oracle = False
            else:
                oracle = False
                for assignments in itertools.product(range(k), repeat=len(nums)):
                    buckets = [0] * k
                    counts = [0] * k
                    for v, which in zip(nums, assignments):
                        buckets[which] += v
                        counts[which] += 1
                    if all(x == target for x in buckets) and all(counts):
                        oracle = True
                        break
            self.assertEqual(solver.canPartitionKSubsets(nums.copy(), k), oracle)

    def test_089_coin_change(self):
        solver = load(89).Solution()
        r = rng()
        for _ in range(75):
            coins = r.sample(range(1, 9), r.randint(1, 5))
            amount = r.randint(0, 24)
            q = deque([(0, 0)])
            seen = {0}
            expected = -1
            while q:
                value, count = q.popleft()
                if value == amount:
                    expected = count
                    break
                for coin in coins:
                    if value + coin <= amount and value + coin not in seen:
                        seen.add(value + coin)
                        q.append((value + coin, count + 1))
            self.assertEqual(solver.coinChange(coins, amount), expected)

    def test_090_lis(self):
        solver = load(90).Solution()
        r = rng()
        for _ in range(75):
            nums = [r.randint(-5, 5) for _ in range(r.randint(0, 9))]
            expected = max((len(x) for length in range(len(nums)+1)
                            for x in itertools.combinations(nums, length)
                            if all(x[i] < x[i+1] for i in range(len(x)-1))), default=0)
            self.assertEqual(solver.lengthOfLIS(nums), expected)

    def test_094_equal_partition(self):
        solver = load(94).Solution()
        r = rng()
        for _ in range(60):
            nums = [r.randint(1, 10) for _ in range(r.randint(1, 10))]
            expected = sum(nums) % 2 == 0 and any(
                sum(nums[i] for i in range(len(nums)) if mask & (1 << i)) * 2 == sum(nums)
                for mask in range(1 << len(nums)))
            self.assertEqual(solver.canPartition(nums), expected)

    def test_095_max_product_subarray(self):
        solver = load(95).Solution()
        r = rng()
        for _ in range(60):
            nums = [r.randint(-4, 4) for _ in range(r.randint(1, 9))]
            self.assertEqual(solver.maxProduct(nums), max(map(math.prod, all_subarrays(nums))))

    def test_096_stock_profit(self):
        solver = load(96).Solution()
        r = rng()
        for _ in range(65):
            prices = [r.randint(0, 20) for _ in range(r.randint(1, 10))]
            expected = max([0] + [prices[j] - prices[i] for i in range(len(prices))
                                  for j in range(i+1, len(prices))])
            self.assertEqual(solver.maxProfit(prices), expected)

    def test_097_merge_intervals(self):
        solver = load(97).Solution()
        r = rng()
        for _ in range(70):
            intervals = [sorted(r.sample(range(-5, 15), 2))
                         for _ in range(r.randint(0, 8))]
            # Independent oracle: union of integer points, treating touching as merge.
            expected = []
            for start, end in sorted(intervals):
                if not expected or start > expected[-1][1]:
                    expected.append([start, end])
                else:
                    expected[-1][1] = max(end, expected[-1][1])
            self.assertEqual(solver.merge([x.copy() for x in intervals]), expected)

    def test_099_nonoverlap_intervals(self):
        solver = load(99).Solution()
        r = rng()
        for _ in range(75):
            intervals = [sorted(r.sample(range(-6, 9), 2))
                         for _ in range(r.randint(0, 8))]
            best = 0
            for mask in range(1 << len(intervals)):
                subset = sorted([x for i, x in enumerate(intervals) if mask & (1 << i)])
                if all(a[1] <= b[0] for a, b in zip(subset, subset[1:])):
                    best = max(best, len(subset))
            self.assertEqual(solver.eraseOverlapIntervals([x.copy() for x in intervals]),
                             len(intervals) - best)

    def test_100_jump_game_ii_reachable(self):
        solver = load(100).Solution()
        r = rng()
        for _ in range(80):
            nums = [r.randrange(5) for _ in range(r.randint(1, 10))]
            d = [math.inf] * len(nums)
            d[0] = 0
            for i, step in enumerate(nums):
                for j in range(i+1, min(len(nums), i+step+1)):
                    d[j] = min(d[j], d[i]+1)
            if d[-1] != math.inf:  # The LC45 statement guarantees reachability.
                self.assertEqual(solver.jump(nums), d[-1])


if __name__ == "__main__":
    unittest.main()
