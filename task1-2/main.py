class Stack:
    def __init__(self, str_of_values = ''):
        self.list = list(str_of_values)

    def is_empty(self):
        if self.list:
            return False
        else:
            return True
        
    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop(len(self.list)-1)
    
    def peek(self):
        return self.list[len(self.list)-1]
    
    def size(self):
        return len(self.list)

    def __str__(self):
        new_list = [str(val) for val in self.list]
        return ','.join(new_list)

def check_stack(stack):
    if stack.size() % 2 == 0:
        newstack = Stack()
        for val in stack.list:
            newstack.push(val)
            while (newstack.size() >= 2) and\
                (newstack.list[newstack.size()-2] == '(' and newstack.peek() == ')') or\
                (newstack.list[newstack.size()-2] == '[' and newstack.peek() == ']') or\
                (newstack.list[newstack.size()-2] == '{' and newstack.peek() == '}'):
                newstack.pop()
                newstack.pop()
                if newstack.size() == 0:
                    break
        if newstack.is_empty():
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == '__main__':
    stack = Stack('[([])((([[[]]])))]{()}')
    print(check_stack(stack))