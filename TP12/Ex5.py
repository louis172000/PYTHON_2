def product(nb, puiss):
    if puiss == 1: return nb
    elif puiss == 0: return 1
    return nb + (product(nb, puiss-1))


print(product(5,2)) # 10
print(product(9,3)) # 27
