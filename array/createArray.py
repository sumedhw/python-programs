
from array import *

arr1 = array('i',[1,2,3,4,5,6])

arr2 = array('d',[1.3, 1.5, 1.6])

def accessElement(array,index):
    if index >= len(array):
        print("There is not element in this list")
    else:
        print(array[index])


accessElement(arr1,6)