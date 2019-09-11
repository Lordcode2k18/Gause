import gauss
import numpy

a = numpy.array([[1., 2, 1, 1],
                 [1, 3 , 1, 1],
                 [0, 1, 1, 2]])
print(a)
print("\n")

b = gauss.gaussFunc(a)
print("Ответ:")
print(b)
