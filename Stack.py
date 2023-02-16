class Stack:
    def __init__(self, stack: str):
        self.stack = stack

    def is_empty(self):
        return True if self.stack == '' else False

    def push(self, new_elem):
        stack_ = []
        for elem_stack in self.stack:
            stack_.append(elem_stack)
        stack_.append(new_elem)
        self.stack = ''.join(stack_)

    def pop(self):
        stack_ = list(self.stack)

        stack_popElem = stack_.pop()
        self.stack = ''.join(stack_)
        return stack_popElem

    def peek(self):
        step_ = list(self.stack)
        return step_[len(step_)-1]

    def size(self):
        return len(self.stack)

    def __repr__(self):
        return self.stack