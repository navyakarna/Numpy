import numpy as np

# # a = np.arange(12).reshape(3,4)
# # print(a)
# # print(a[2])

# a = np.array([ 0,  1,  2,  3, 5 , 3 ,4 , 5, 6, 7, 8, 9])
      
# a[:6:2] = 100
# print(a)



# data = np.array([[0,1,2],[3,4,5],[6,7,8]])

# data[1]

# data[0:2]

# data[-2]

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[1,2])

# c =a[(a > 2) & (a < 8)]
# print(c)


# divisble_by_2 = a[a%2==0]
# print(divisble_by_2)

# b = np.nonzero(a < 5)
# print(b)


# a = np.array([1,2,3,4,5,6,7,8,9,10])

# x = np.arange(1,25).reshape(4,6)
# print(x)


# b1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# print(b1)

# a = np.array([1,2,3,4])
# a.sum
# print(a)



# a[0:2] = 100
# print(a)


# def f(x,y):
#      return 10*x+y

# b = np.fromfunction(f, (5,4), dtype=int)
# print(b)

# print(b[2,3])


b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(b)

for row in b.flat:
    print(row)

