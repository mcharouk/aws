from ctypes import *
import ctypes
import json

so_file = "./example.so"
my_functions = CDLL(so_file)

# set function return type as double
my_functions.square.restype = ctypes.POINTER(ctypes.c_double * 2)
# my_functions.square.restype = ctypes.c_double

py_values = [1.1, 2.2]
# set argument as array of double
doubleArray = (ctypes.c_double * len(py_values))(*py_values)

result = my_functions.square(doubleArray)

double_list = []
for r in result.contents:
    double_list.append(r)

result = {
    "ResultValues": double_list
}

print(json.dumps(result))