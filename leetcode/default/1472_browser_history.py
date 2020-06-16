import unittest


'''
1472. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit
another url, get back in the history number of steps or move forward in the history
number of steps.

Implement the BrowserHistory class:

    * BrowserHistory(string homepage) initializes the object with the homepage of
      the browser.
    * void visit(string url) visits url from the current page. It clears up all the
      forward history.
    * string back(int steps) Move steps back in history. If you can only return x
      steps in the history and steps > x, you will return only x steps. Return the
      current url after moving back in history at most steps.
    * string forward(int steps) Move steps forward in history. If you can only forward
      x steps in the history and steps > x, you will forward only x steps. Return the
      current url after forward in history at most steps.

Example:

    Input:
    [
        'BrowserHistory',

        'visit', 'visit', 'visit',

        'back', 'back', 'forward',

        'visit',

        'forward', 'back', 'back',
    ]
    [
        ['leetcode.com'],

        ['google.com'], ['facebook.com'], ['youtube.com'],

        [1], [1], [1],

        ['linkedin.com'],

        [2], [2], [7],
    ]

    Output:
    [
        null,

        null, null, null,

        'facebook.com', 'google.com', 'facebook.coom',

        null,

        'linkedin.com', 'google.com', 'leetcode.com',
    ]

    Explanation:

    BrowserHistory browserHistory = new BrowserHistory('leetcode.com')

'''


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.current_index = None
        self.records = []

    def visit(self, url: str) -> None:
        if self.current_index and self.current_index >= 0:
            self.records = self.records[:self.current_index+1]

        self.records.append(url)
        self.current_index = None

    def update_current_index(self, steps: int) -> int:
        record_length = len(self.records)

        current_index = self.current_index
        if current_index is None:
            current_index = record_length - 1

        new_index = current_index + steps
        if new_index >= record_length:
            new_index = record_length - 1

        return new_index

    def back(self, steps: int) -> str:
        self.current_index = self.update_current_index(-steps)
        r = self.homepage if self.current_index < 0 else self.records[self.current_index]
        return r

    def forward(self, steps: int) -> str:
        self.current_index = self.update_current_index(steps)
        r = self.records[self.current_index]
        return r


class TestCase(unittest.TestCase):

    def test_default(self):
        browser_history = BrowserHistory('leetcode.com')

        browser_history.visit('google.com')
        browser_history.visit('facebook.com')
        browser_history.visit('youtube.com')

        browser_history.back(1)
        browser_history.back(1)
        browser_history.forward(1)

        browser_history.visit('linkedin.com')

        browser_history.forward(2)
        browser_history.back(2)
        browser_history.back(7)
