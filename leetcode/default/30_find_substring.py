'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same
length. Find all strating indices of substring(s) in s that is a concatenation
of each word in words exactly once and without any intervening characters.

Example 1:

    Input:
        s = 'barfootheforbarman'
        words = ['foo', 'bar']
    Output: [0, 9]
    Explanation: Substrings starting at index 0 and 9 are 'barfoo' and 'foobar'
    respectively.
    The output order does not matter, returning [9, 0] is fine too.

Example 2:

    Input:
        s = 'wordgoodgoodgoodbestword'
        words = ['word', 'good', 'best', 'word']
    Output: []
'''

EXAMPLES = [
    (
        ('barfootheforbarman', ['foo', 'bar']), [0, 9],
    ),
    (
        ('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']), [],
    ),
]


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        r = []

        if not s or not words:
            return r

        word_length = len(words[0])
        words_count = len(words)

        i = 0
        while i + words_count * word_length <= len(s):
            arrays = [
                s[i+n*word_length:i+(n+1)*word_length]
                for n in range(0, words_count)
            ]

            for word in words:
                if word in arrays:
                    arrays.remove(word)

            if len(arrays) == 0:
                r.append(i)

            i += 1

        return r
