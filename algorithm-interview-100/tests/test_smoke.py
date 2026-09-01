from __future__ import annotations
import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
    path=ROOT/'solutions/python'/name
    spec=importlib.util.spec_from_file_location(name.replace('-','_'),path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
class SmokeTests(unittest.TestCase):
    def test_two_sum(self): self.assertEqual(load('001-two-sum.py').Solution().twoSum([2,7,11,15],9),[0,1])
    def test_longest_consecutive(self): self.assertEqual(load('003-longest-consecutive-sequence.py').Solution().longestConsecutive([100,4,200,1,3,2]),4)
    def test_subarray_sum(self): self.assertEqual(load('005-subarray-sum-equals-k.py').Solution().subarraySum([1,1,1],2),2)
    def test_three_sum(self): self.assertEqual(sorted(load('012-3sum.py').Solution().threeSum([-1,0,1,2,-1,-4])),[[-1,-1,2],[-1,0,1]])
    def test_window(self): self.assertEqual(load('015-longest-substring-without-repeating-characters.py').Solution().lengthOfLongestSubstring('abcabcbb'),3)
    def test_binary(self): self.assertEqual(load('037-binary-search.py').Solution().search([-1,0,3,5,9,12],9),4)
    def test_kth(self): self.assertEqual(load('045-kth-largest-element-in-an-array.py').Solution().findKthLargest([3,2,1,5,6,4],2),5)
    def test_islands(self): self.assertEqual(load('066-number-of-islands.py').Solution().numIslands([list('110'),list('010'),list('001')]),2)
    def test_subsets(self): self.assertEqual(len(load('078-subsets.py').Solution().subsets([1,2,3])),8)
    def test_jump(self): self.assertEqual(load('100-jump-game-ii.py').Solution().jump([2,3,1,1,4]),2)
if __name__=='__main__': unittest.main()
