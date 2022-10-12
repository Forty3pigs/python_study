class OneList(list):
    def __getitem__(self, item):
        if item > 0:
            return super().__getitem__(item-1)
        elif item < 0:
            return super().__getitem__(item)
        else:
            raise IndexError("Index out of range")


s = OneList([1,2,3,4,5,6])

print(s[1])
print(s[2])
print(s[3])
print(s[-1])