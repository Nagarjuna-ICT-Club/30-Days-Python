# Custom Iterator

class Numbers:
    def __init__(self, start, end):
        self.current = start
        self.final = end

    # returns the object itself
    def __iter__(self):
        return self

    # returns the next item
    def __next__(self):
        
        # if current value exceeds final value,
        # stop the iteration
        if self.current >= self.final:
            raise StopIteration

        ret_num = self.current
        self.current += 1

        return ret_num


# iterate over the custom Iterator `Numbers`
for i in Numbers(1, 10):
    print(i)
