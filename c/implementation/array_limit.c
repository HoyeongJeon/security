#include <stdio.h>

#define MAX 200

int g_h_total = 0; // 총 인구수


// 사람을 추가하는 함수
void add_h(int * h_num) {
	h_num[g_h_total++] = (g_h_total + 1) * 2; // 총 인구(g_h_total)가 한명 늘어나면 주민번호를 주는 느낌!	
}

// 배열의 전체를 출력하는 함수
void print_all(int * h_num){
	int i = 0;
	while(*(h_num + i)) { // (h_num + i) 배열은 포인터와 같다... 하나 그러므로 i가 하나씩 늘어나면 자연스레 배열도 하나씩 추가됨!! 
		printf("h_num[%d] = %d\n", i, *(h_num + i));
		i++;
		if(i > MAX){
			break;
		}	
	 }
}

int main(int argc, char * argv[]){
	
	int h_num[MAX] = {0,};
	for(int i = 0; i < MAX; i++) {
		add_h(h_num);
		printf("h_num[%d] = %d\n", i, h_num[i]);
	}

	return 0;
}

