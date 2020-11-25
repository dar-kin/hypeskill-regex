import copy


def solve(obj):
    if id(obj) == id(copy.deepcopy(obj)):
        return False
    else:
        return True
