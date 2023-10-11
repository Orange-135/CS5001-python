from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.stack = Stack()

    def process_string(self, input_str):
        output_str = ""
        for char in input_str:
            if char == "*":
                output_str += self.stack.pop()
            elif char == "^":
                second_char = self.stack.pop()
                first_char = self.stack.pop()
                output_str += first_char + second_char
            else:
                self.stack.push(char)
        return output_str
