#include <stdio.h>
#include "sum.h"

int main() {

#ifdef DEBUG
	printf("Debug!\n");
	printf("sum : %d\n", sum(1,2));
#else
	printf("Hello!\n");
	printf("sum : %d\n", sum(1,2));
#endif
	return 0;
}
