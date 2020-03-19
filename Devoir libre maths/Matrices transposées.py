import numpy
M =(1/(2**0.5))* numpy.array(([1, 1, 0], [0, 0, 2**0.5], [-1, 1, 0]))
N = numpy.transpose(M)

print("M = \n", M)
print("Transpose = \n", N)
print("produit = \n", numpy.dot(M, N))

