import numpy as np
#numpy for dealing with numerical data

#not from numpy but important:
#zip(x,y)--> this function returns pairs, x and y are 2 arrays/vectors and it will return x[0],y[0] first and then x[1],y[1] and so on.
 
#element wise multiplication is the dot product of 2 vectors:
#to perform dor product using numpy, we first need to convert numpy data into a special data structure "numpy array"
np_array1=np.array([10,20,30])
print("numpy arrays:")
print(np_array1)
np_array2=np.array([40,50,60])
print(np_array2)
#numpy arrays work like a list in many ways
print(np_array2[1])

#dot product, multiplies the array and even adds the products of elemnt wise multiplication
print("numpy dot product result")
product_arrays=np.dot(np_array1,np_array2)
print(product_arrays)
product_element=np.dot(np_array1[2],np_array2[2])
print(product_element)

#for performing element wise multiplication only
print("element wise product and then their sum without using numpy")
ele_product=np_array1*np_array2
print(ele_product)
#and summing up the array
print(ele_product.sum())

#multidimensional numpy array
print("multidimensional numpy array")
multi_array=np.array([[10,20],[30,40],[50,60]])
print(multi_array)
#it is actually a list inside a list
#we can make any dimensional array using numpy by nesting lists inside lists
#to inspect shape along each dimension, we can use this:
print(multi_array.shape)
#all values in a numpy array are the same type and numpy array has its own sligtly different datatypes
#if array has even one floating point number then all the other elements are also converted to floating datatype

#matrix multiplication
print("matrix multiplication")
#the first elemnt is the dot product of the first row of first matrix and the first column of the second matrix
#in the result we will also get annother vector/matrix
np_array3=np.array([[10,20],[30,40]])
np_array4=np.array([[50,60],[70,80]])
print("matrix 1",np_array3)
print("matrix2",np_array4)
matrix_mul=np.matmul(np_array3,np_array4)
print(matrix_mul)
#we can also do matrix multiplication without using the function by using @ character, means the same thing
matrix_mul_nofunc=np_array3 @ np_array4
print(matrix_mul_nofunc)

#using CSV files and doing computations from it
#delimiter is the one by which the data is divided
#skip header rows means the number of rows which contain the column heading and need to be skipped as they are not data 
print("data from the CSV") 
sample_data=np.genfromtxt('sample_demo_csv.txt', delimiter=',', skip_header=1)
print(sample_data)
mul=[10,20,30]
mul_sam_data= sample_data@mul
print(mul_sam_data)
print(mul_sam_data.shape)

#adding the result to the original file
print("joining the result with the original matrix")
print("rowise")
result_row=np.concatenate((sample_data,mul_sam_data[0:3].reshape(1,3)),axis=0)
print(result_row)
#using the concatenate function, it will concatenate the giver array/vector with another array/vector
#arguments of concatenate: the name of the array to concatenate with, 
# reshaping the vector to make it from row vector to column vector and also converting it from 1D to 2D
# as the arrays to be concatenaed should have same dimensions, 
# axis=1 because we are adding it to column, axis 0 is for concatenation along x axis
result_col=np.concatenate((sample_data,mul_sam_data.reshape(9,1)),axis=1)
print("column wise")
print(result_col)

#writing the new concatenated result matrix to the original file
np.savetxt('sample_demo_csv2.txt',result_col,fmt='%.2f',header='col1,col2,col3,result_col',comments='"""demo file"""')
#function to write to a txtx file
#fmt is formatting string, the number of decimal places till which we want to write out results, by default python writes till 10 decimal places, we dont want that
#header is the column heading like it was given in the original csv
#comment adds a comment or line before writing the header.

#numpy can also do element wise arithematic operations on its array/matrix using +,-,*
#numpy can also perform broadcasting, arithematic operations on 2 matrix having different dimensions
#but for bradcasting, the shape of the arrays must be comatible
np_array5=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
np_array6=np.array([100,100,100,100])
broad_array=np_array5+np_array6
print(broad_array)
#array6 got convetted froma  row vector to a 2D array with identical 3 rows
#broadcasting only works if one the arrays can be replicated to match the size of the other array
#no actual copy is made in the array, it is done only conceptually

#numpy also supports comparison operators