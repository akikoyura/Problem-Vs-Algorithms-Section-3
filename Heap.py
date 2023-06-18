class Heap:

    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes the next index where a new element should go

    def _up_heapify(self):
        child_idx = self.next_index

        while child_idx >= 1:
            parent_idx = (child_idx - 1) // 2
            parent_element = self.cbt[parent_idx]
            child_element = self.cbt[child_idx]

            if parent_element > child_element:
                self.cbt[parent_idx] = child_element
                self.cbt[child_idx] = parent_element
                child_idx = parent_idx
            else:
                break

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        # insert element at the end next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase the index by 1
        self.next_index += 1

        # handle index out of range
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(len(self.cbt) * 2)]
            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def size(self):
        return self.next_index

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """

        if self.size() == 0:
            return None

        self.next_index = -1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place the last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the element, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def _down_heapify(self):
        pass

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None

        return self.cbt[0]


if __name__ == '__main__':
    print("Heap")
