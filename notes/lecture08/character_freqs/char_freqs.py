import re


class CharFreqs:
    """Handle counts and frequency
    calculations of characters"""
    def __init__(self):
        self.char_counts = {}
        self.total_count = 0

    def count_line(self, line):
        """Add a character to count"""
        chars = re.findall(r"[a-z]", line.lower())
        for char in chars:
            self.add_char(char)

    def add_char(self, char):
         """Add a character to the counts"""
         self.total_count += 1
         if char in self.char_counts.keys():
              self.char_counts[char] += 1
         else:
               self.char_counts[char] = 1

    @property
    def sorted_counts(self):
         """Return a list of sorted counts as a property"""
         return sorted(
              self.char_counts.items(),
              key=lambda x: x[1],
              reverse=True
         )
    
    @property
    def char_freqs(self):
         """Return a dictionary pf frequency of frequencies as a property"""
         ROUND_PLACES = 2
         return {k: round(self.char_counts[k]/self.total_count, ROUND_PLACES)
                 for k in self.char_counts.keys()}
    

    @property
    def sorted_freqs(self):
         """Return a list of sorted counts as a property"""
         return sorted(
              self.char_freqs.items(),
              key=lambda x: x[1],
              reverse=True
         )
