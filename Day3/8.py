import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a.shape)
print(a[0])
print(a[1])
print(a[1][2])
a[1][2]=25
print(np.count_nonzero(a))

print("---indexing---")
sub_array=a[1:3, 0:2]
print(sub_array)