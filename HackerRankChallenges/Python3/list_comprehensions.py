#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/17/2021
#
#Task
#Let's learn about list comprehensions! You are given three integers x,y and z representing 
# the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by i,j,k on a 3D grid
# 
# Constraints
# 
#  1.where the sum of (i + j + k ) != n
#  2. 0 <= i <= x;  0 <= j <= y;  0 <= k <= z;
#  3. Please use list comprehensions rather thant multiple loops as a learning. 


def list_x(x):
    x = list(range(x+1))
    return x


def list_y(y):
     y = list(range(y+1))
     return y

def list_z(z):
    z = list(range(z+1))
    return z


def create_list_ijk(xlist, ylist, zlist, n):
 zip_list = [[i, j, k] for i in xlist for j in ylist for k in zlist if i+j+k != n ]
 print(zip_list)

if __name__ == '__main__':
 x = int(input())
 y = int(input())
 z = int(input())
 n = int(input())

 xlist = list_x(x)
 ylist = list_y(y)
 zlist = list_z(z)

 #print(xlist)
 #print(ylist)
 #print(zlist)
 create_list_ijk(xlist,ylist, zlist,n)

 quit()




