import copy


def detect_copy():
    a = [[]]
    obj = copying_machine(a)
    if id(obj[0]) == id(a[0]):
        return "shallow copy"
    else:
        return "deep copy"
