import copy

def my_copy(obj, copy_mode):
    if copy_mode == "shallow copy":
        return copy.copy(obj)
    else:
        return copy.deepcopy(obj)
