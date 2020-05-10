def pow(nb, puiss):
    if puiss == 1: return nb
    elif puiss == 0: return 1
    return nb*(pow(nb, puiss-1))


print(pow(42, 0))  # 1
print(pow(1, 10))  # 1
print(pow(2, 5))  # 32
print(pow(7, 2))  # 49
