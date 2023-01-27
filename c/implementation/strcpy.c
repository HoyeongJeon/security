#include <stdio.h>

char *strcpy(char *dest, const char *src);
size_t strlen(const char *s);
int strcmp(const char *s1, const char *s2);

int main(int argc, char *argv[]) {

        char str[20] = "Hello World!!!\n";

        char str2[20] = "Hello World!!!\n";
//      printf("str2: %s\n", str2);

//      strcpy(str2, str);

//      printf("str2: %s\n", str2);

        printf("%d\n", strcmp(str, str2));

        return 0;
}


size_t strlen(const char *s) {

        int count = 0;
        int i = 0;
        if(s != NULL)
        {
                for(int i = 0;; i++)
                {
                                if (*(s + i) != 0)
                                {
                                        count++;
                                } else {
                                        break;
                                }
                }
                return count;
        } else {
                return -1;
        }


}

int strcmp(const char *s1, const char *s2) {
        int i = 0;
        while(1) {
                if(s1[i] == s2[i]) {
                        if(s1[i] == 0 && s2[i] == 0) {
                                return 0;
                        }
                        i++;
                } else {
                        if(s1[i] < s2[i]) {
                                return -1;
                        } else {
                                return 1;
                        }
                }
        }
}

char *strcpy(char *dest, const char *src) {
        int i = 0;
/*
        - strcpy 구현방법 1
        while(*src) {
                *dest++ = *src++;
        }
*/

//        - strcpy 구현방법 2 (strlen도 직접 구현)
        for(i = 0; i < strlen(src); i++)
        {
                dest[i] = src[i];
        }

        return dest;

}
