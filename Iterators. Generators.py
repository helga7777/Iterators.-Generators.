# Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Например

#
nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]


class FlatIterator:
    def __init__(self,list_new):
        self.list = list_new

    def __iter__(self):
        self.cursor_start = 0
        self.cursor_start_2 = 0
        self.cursor_end = len(self.list)
        return self

    def __next__(self):
        while self.cursor_start < len(self.list):
            if self.cursor_start_2 < len(self.list[self.cursor_start]):
                v = self.list[self.cursor_start][self.cursor_start_2]
                self.cursor_start_2 += 1
                return v
            self.cursor_start += 1
            self.cursor_start_2 = 0
        raise StopIteration

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('*'*40)
# Написать генератор, который принимает список списков, и возвращает их плоское представление.

nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]


def flat_generator(nested_list):
    cursor_start = 0
    cursor_start_2 = 0
    while cursor_start < len(nested_list):
        while cursor_start_2 < len(nested_list[cursor_start]):
            v = nested_list[cursor_start][cursor_start_2]
            cursor_start_2 += 1
            yield v
        cursor_start += 1
        cursor_start_2 = 0

for item in  flat_generator(nested_list):
    print(item)
