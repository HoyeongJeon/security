#include "sum.h"

#ifdef VER2
int sum(int a, int b){

	return a + b;
}
#else
int sum(int a, int b){

	return a * b;
}

#endif
