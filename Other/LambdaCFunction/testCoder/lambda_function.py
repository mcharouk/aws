import ctypes
import json
from ctypes import *

so_file = "./testCoderDLL.so"
my_functions = CDLL(so_file)


def lambda_handler(event, context):

    input_array = event["Values"]

    # set argument as array of double
    double_array = (ctypes.c_double * len(input_array))(*input_array)
    result_array = (c_double * 31)()

    result = my_functions.testCoderDLL(double_array, result_array)

    result = {"ResultValues": list(result_array)}
    return json.dumps(result)
