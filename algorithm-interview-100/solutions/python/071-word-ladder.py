from __future__ import annotations
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words=set(wordList)
        if endWord not in words: return 0
        q={beginWord}; steps=1; alphabet='abcdefghijklmnopqrstuvwxyz'
        while q:
            nxt=set()
            for word in q:
                for i,old in enumerate(word):
                    for ch in alphabet:
                        if ch==old: continue
                        cand=word[:i]+ch+word[i+1:]
                        if cand==endWord: return steps+1
                        if cand in words:
                            words.remove(cand); nxt.add(cand)
            q=nxt; steps+=1
        return 0
