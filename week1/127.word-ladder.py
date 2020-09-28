#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

# solution 1
# import collections
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
        
#         def construct_dict(word_list):
#             d = {}
#             for word in word_list:
#                 for i in range(len(word)):
#                     s = word[:i] + "_" + word[i+1:]
#                     d[s] = d.get(s, []) + [word]
#             return d
            
#         def bfs_words(begin, end, dict_words):
#             queue, visited = collections.deque([(begin, 1)]), set()
#             while queue:
#                 print(queue)
#                 word, steps = queue.popleft()
#                 if word not in visited:
#                     visited.add(word)
#                     if word == end:
#                         return steps
#                     for i in range(len(word)):
#                         s = word[:i] + "_" + word[i+1:]
#                         neigh_words = dict_words.get(s, [])
#                         for neigh in neigh_words:
#                             if neigh not in visited:
#                                 queue.append((neigh, steps + 1))
#             return 0
        
#         d = construct_dict(set(wordList))
#         print(d)
#         return bfs_words(beginWord, endWord, d)


# solution 2
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        q = collections.deque([(beginWord, 1)])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in "qwertyuiopasdfghijklzxcvbnm":
                    new_word = word[:i] + j + word[i+1:]
                    if new_word in wordSet:
                        q.append((new_word, step + 1))
                        wordSet.remove(new_word)

        return 0

    


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# # beginWord = "a"
# # endWord = "c"
# # wordList = ["a", "b", "c"]
# solution = Solution()
# a = solution.ladderLength(beginWord, endWord, wordList)
# print(a)





# def construct_dict(word_list):
#     d = {}
#     for word in word_list:
#         for i in range(len(word)):
#             s = word[:i] + "_" + word[i+1:]
#             print(s)
#             print(d)
#             d[s] = d.get(s, []) + [word]
#     return d
# wordList = ["hot","dot","dog","lot","log","cog"]
# a = construct_dict(set(wordList))
# print(a)

# @lc code=end

