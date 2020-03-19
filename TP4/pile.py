def newstack():
    pile = []
    return pile


def push(s, e):
    s.append(e)


def top(s):
    return s[len(s)-1]


def pop(s):
    if s != []:
        dernierElement = s[-1]
        del(s[len(s)-1])
        return dernierElement


def isEmpty(s):
    if s == []:
        return True
    else:
        return False


def size(s):
    return len(s)
