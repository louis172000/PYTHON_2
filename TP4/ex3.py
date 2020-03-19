from pile import *
chaine = "(5*5)"


def inspection(chaine):
    s=newstack()
    left = "([{"
    right = ")]}"
    for c in chaine:
        if c in left:
            push(s, c)
        elif isEmpty(s):
            return False
        elif c in right:
            if right.index(c) != left.index(s.pop()):
                return False
    return isEmpty(s)

print(inspection(chaine))
