class AnBnCn:
    def __init__(self):
        self.stack = []
        self.stack1 = []

    def accept(self, in_string):
        expect_a = True
        expect_b = True

        for ch in in_string:
            if ch == 'a':
                if expect_a:
                    self.stack.append(ch)
                else:
                    return False

            elif ch == 'b':
                if not self.stack:
                    return False
                else:
                    if expect_a:
                        expect_a = False
                        self.stack.pop()
                    else:
                        self.stack.pop()
                
                if expect_b:
                    self.stack1.append(ch)
                else:
                    return False
   
            elif ch == 'c':
                if not self.stack1:
                    return False
                else:
                    if expect_b:
                        expect_b = False
                        self.stack1.pop()
                    else:
                        self.stack1.pop()

        if not self.stack and not self.stack1:
            return True

        return False

    def clear(self):
        self.stack = []
        self.stack1 = []
