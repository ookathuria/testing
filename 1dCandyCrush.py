

class my_stack_impl:

    def __init__(self):
        #stack is implemented as a list here
          self.s_stack = []

    def s_push(self, s_char ):
        #function to push elements into a stack

        self.s_stack.append(s_char)
        #return(self.s_stack)

    def s_pop(self):
        #stack is a LIFO data structure, wherein pop removes the last element added to the stack of items, and returns the new stack

        self.s_stack.pop()
        return self.s_stack

    def s_peek(self):
        #stack is a LIFO data structure, wherein peek returns the last element added to the stack of items

        peek_item = self.s_stack[-1]
        return peek_item

    def s_size(self):
        return (self.s_stack.count())

    def s_print(self):
        print(self.s_stack)

class one_dim_cc(my_stack_impl):

    def __init__(self):
        #instantiate the super class, my_stack_impl
        super().__init__()

        self.user_input = None
        self._run()

    def _run(self):
        while True:

            print("*********LET'S PLAY CANDY CRUSH*********")
            self.cleanse()
            self.user_input = input("ENTER THE ELEMENTS TO PLAY CANDY CRUSH WITH : ")
            self.crush_repeating_elements()

    def cleanse(self):
        self.user_input = None
        self.s_stack = []

    def crush_repeating_elements(self):

        #to play candycrush with one dimensional array of chars, we first create a stack data structure
        for i in self.user_input:
            count = 1
            if self.s_stack!=[] and self.s_peek()[0] == i:
                #new char being added to stack is same as the last element in the stack, add 1 to the count
                count = self.s_peek()[1] +1
                self.s_pop()
                self.s_push([i,count])
                if self.s_peek()[1] ==3:
                    #we pop here, and remove the pattern
                    self.s_pop()
            else:
                #push new char to the stack
                self.s_push([i,count])


        self.ss_print()

    def ss_print(self):

        self.s_print()

        for item in self.s_stack:
            i = 0
            while i < item[1]:
                print(item[0])
                i+=1


def main():
    onedcc = one_dim_cc()

if __name__ == '__main__':
    main()