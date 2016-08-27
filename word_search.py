# https://leetcode.com/problems/word-search-ii/
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

import unittest
import json
from sets import Set


class Solution(object):
    def findWords(self, board, found_words):
        """
        :type board: List[List[str]]
        :type found_words: List[str]
        :rtype: List[str]
        """
        trie = build_trie(found_words)

        found_words = Set()
        visited = [[False for col in xrange(0, len(board[0]))] for row in xrange(0, len(board))]

        for row in xrange(0, len(board)):
            for col in xrange(0, len(board[row])):
                self.__dfs__(visited, row, col, board, trie, found_words)

        return sorted(found_words)

    def __dfs__(self, visited, curr_row, curr_col, board, trie_node, found_words):
        visited[curr_row][curr_col] = True

        letter = board[curr_row][curr_col]

        if letter in trie_node:
            if "word" in trie_node[letter]: # include key if this is a word
                found_words.add(trie_node[letter]["word"])

            # try down
            if is_position_valid(curr_row + 1, curr_col, board, visited):
                self.__dfs__(visited, curr_row + 1, curr_col, board, trie_node[letter], found_words)

            # try up
            if is_position_valid(curr_row - 1, curr_col, board, visited):
                self.__dfs__(visited, curr_row - 1, curr_col, board, trie_node[letter], found_words)

            # try right
            if is_position_valid(curr_row, curr_col + 1, board, visited):
                self.__dfs__(visited, curr_row, curr_col + 1, board, trie_node[letter], found_words)

            # try left
            if is_position_valid(curr_row, curr_col - 1, board, visited):
                self.__dfs__(visited, curr_row, curr_col - 1, board, trie_node[letter], found_words)

        visited[curr_row][curr_col] = False

        return found_words


def is_position_valid(row, col, board, visited):
    return 0 <= row <= len(board) - 1 and \
           0 <= col <= len(board[row]) - 1 and \
           not visited[row][col]


def build_trie(words):
    trie = {}
    for word in words:
        add_word(0, trie)

    return trie


def add_word(index, word, parent_node):
    if index == len(word):
        return

    letter = word[index]

    if letter not in parent_node:
        parent_node[letter] = {}

    if index == len(word) - 1:
        parent_node[letter]["word"] = word
    else:
        add_word(index + 1, word, parent_node[letter])


def pretty_print_trie(trie):
    print json.dumps(trie, sort_keys=True, indent=4)


class WordSearchMatrixTest(unittest.TestCase):

    def test_solution(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        words = ["oath", "pea", "eat", "rain"]

        found = Solution().findWords(board, words)

        self.assertEquals(found, ["eat", "oath"])

    def test_solution2(self):
        board = ["aa"]
        words = ["a"]

        found = Solution().findWords(board, words)

        self.assertEquals(found, ["a"])

    def test_solution3(self):
        board = ["ab", "cd"]
        words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]

        found = Solution().findWords(board, words)

        self.assertEquals(found, ['ab', 'ac', 'bd', 'ca', 'db'])

    def test_prefix_tree1(self):
        tree = build_trie(["abc", "abcd"])

        self.assertEquals(tree, {'a': {'b': {'c': {'word': 'abc', 'd': {'word': 'abcd'}}}}})

    def test_prefix_tree2(self):
        tree = build_trie(["abcd", "abefg"])

        self.assertEquals(tree, {'a': {'b': {'c': {'d': {'word': 'abcd'}}, 'e': {'f': {'g': {'word': 'abefg'}}}}}})

    def test_prefix_tree3(self):
        tree = build_trie(["abcd", "abcde"])

        self.assertEquals(tree, {'a': {'b': {'c': {'d': {'e': {'word': 'abcde'}, 'word': 'abcd'}}}}})

if __name__ == '__main__':
    unittest.main()