from __future__ import annotations
class Solution:
    def rand10(self) -> int:
        while True:
            x = (rand7()-1)*7 + rand7()  # uniform 1..49
            if x <= 40:
                return 1 + (x-1)%10
