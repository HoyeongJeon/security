#include <stdio.h>

int main(void) {
        int var = 1;
        int number = 0;
		printf("What number do you want to convert ? ");
		scanf("%d", &number);

        printf("decimal number == %d\n", number);
        printf("binary number == ");
        for(int i = 7; i >= 0; i--) {
                var = 1;
                var = var << i;
                printf("%d ", (number & var) >> i);
        }
        printf("\n");

        return 0;
}
