import ctypes
import json
from ctypes import *

so_file = "./example.so"
my_functions = CDLL(so_file)

my_functions.square.restype = ctypes.POINTER(ctypes.c_double * 2)


def handler(event, context):

    py_values = event["Values"]
    # py_values = [1.1, 2.2]
    # set argument as array of double
    double_array = (ctypes.c_double * len(py_values))(*py_values)

    result = my_functions.square(double_array)
    double_list = []
    for r in result.contents:
        double_list.append(r)

    result = {"ResultValues": double_list}
    return json.dumps(result)
