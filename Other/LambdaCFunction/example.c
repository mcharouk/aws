#include <stdio.h>
#include <stdlib.h>

double *square(double doubleArray[]) {
    double *ret = malloc(2);
    if(!ret)
        return NULL;

    for (int i = 0; i < 2; i++)
    {
      ret[i] = doubleArray[i] * 2;
    }

    return ret;
}