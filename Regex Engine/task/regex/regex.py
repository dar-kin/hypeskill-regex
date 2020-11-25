metacharacters = {"?", "+", "*"}


def check_slash(reg):
    if len(reg) == 1:
        return reg
    li = list(reg)
    i = 0
    while i < len(li):
        if i == 0:
            if li[i] == "\\" and li[i + 1] != "\\":
                li.insert(i, "\\")
                i += 1
        elif i == len(li) - 1:
            if li[i] == "\\" and li[i - 1] != "\\":
                li.insert(i, "\\")
                i += 1
        else:
            if li[i] == "\\" and (li[i - 1] != "\\" or li[i + 1] != "\\"):
                li.insert(i, "\\")
                i += 1
        i += 1
    return "".join(li)


def turn_regex(reg):
    res = list(reg)
    for i in range(1, len(res)):
        if res[i] in metacharacters:
            res[i], res[i - 1] = res[i - 1], res[i]
    return "".join(res[::-1])


def regex(reg, n):
    if not reg and not n or reg == ".":
        return True
    else:
        return reg == n


def string_regex(reg, n):
    i = 0
    j = 0
    while j < len(reg):
        # print(reg[j], n[i], i, j)
        if i == len(n):
            return False
        if j != len(reg) - 1:
            if reg[j] == "\\" and reg[j + 1] == "\\":
                j += 2
                if not j < len(reg):
                    continue
                elif regex(reg[j], n[i]):
                    continue
                else:
                    return False
            if reg[j + 1] == "?":
                if regex(reg[j], n[i]):
                    j += 2
                    i += 1
                    continue
                else:
                    j += 2
                    continue
            elif reg[j + 1] == "*":
                if not regex(reg[j], n[i]):
                    j += 2
                else:
                    char = n[i]
                    j += 2
                    i += 1
                    while regex(char, n[i]):
                        if i == len(n) - 1:
                            break
                        i += 1
                    continue
            elif reg[j + 1] == "+":
                if not regex(reg[j], n[i]):
                    return False
                else:
                    char = n[i]
                    j += 2
                    i += 1
                    while regex(char, n[i]):
                        if i == len(n) - 1:
                            break
                        i += 1
                    continue
        if not regex(reg[j], n[i]):
            return False
        i += 1
        j += 1
    return True


def find_in_string(reg, n):
    k = 0
    if reg.startswith("\\\\"):
        k = 2
    if k >= len(reg):
        return True
    for i in range(len(n)):
        if regex(reg[k], n[i]):
            if string_regex(reg, n[i:]):
                return True
    return False


def session(reg, n):
    begin = False
    end = False
    if reg.startswith("^"):
        begin = True
        reg = reg[1:]
    if reg.endswith("$"):
        end = True
        reg = reg[:len(reg) - 1]
    elif not reg:
        return True
    if begin and end:
        return string_regex(reg, n) and string_regex(turn_regex(reg), n[::-1])
    elif begin:
        return string_regex(reg, n)
    elif end:
        return string_regex(turn_regex(reg), n[::-1])
    else:
        return find_in_string(reg, n)


match = input().split("|")
print(session(check_slash(match[0]), match[1]))
