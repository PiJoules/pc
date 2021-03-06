#ifndef _MYPYC_H
#define _MYPYC_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// pi is not required to be defined in standard C
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Object properties
#define OBJECT_ATTRIBUTES(type) \
    (char*) (*__str__)(type self);

// Builtin functions/objects
#include <list_obj.h>
#include <string_obj.h>

#endif
