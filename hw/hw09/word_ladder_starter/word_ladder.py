from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist

    def make_ladder(self):

        queue = Queue()
        initial_stack = Stack()
        initial_stack.push(self.w1)
        queue.enqueue(initial_stack)
        seen = set()
        seen.add(self.w1)
        while not queue.isEmpty():
            current_stack = queue.dequeue()
            current_word = current_stack.peek()
            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    word = current_word[:i] + c + current_word[i+1:]
                    if word in self.wordlist and word not in seen:
                        new_stack = current_stack.copy()
                        new_stack.push(word)
                        if word == self.w2:
                            return new_stack
                        else:
                            seen.add(word)
                            queue.enqueue(new_stack)
        return None
