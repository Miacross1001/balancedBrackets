from Stack import Stack

class is_Balanced:
    def checkBalance(self, string: str):
        self.string = string
        stack = Stack('')
        check = 0
        log = True

        for i in range(len(self.string)):
            check = i
            if self.string[i] == '(' and self.string[len(self.string)-i-1] == ')':
                stack.push('(')
                stack.push(')')
            elif self.string[i] == '[' and self.string[len(self.string)-i-1] == ']':
                stack.push('[')
                stack.push(']')
            elif self.string[i] == '{' and self.string[len(self.string)-i-1] == '}':
                stack.push('{')
                stack.push('}')

        if stack.size() == len(self.string):
            return 'Yes'
        else:
            return 'No'

if "__main__" == __name__:
    balance = is_Balanced()
    print(balance.checkBalance('(((([{}]))))'))
    print(balance.checkBalance('[([])((([[[]]])))]{()}'))
    print(balance.checkBalance('{{[()]}}'))
    print(balance.checkBalance('}{}'))
    print(balance.checkBalance('{{[(])]}}'))
    print(balance.checkBalance('[[{())}]'))
