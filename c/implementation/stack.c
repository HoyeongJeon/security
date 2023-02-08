/*
백준 10828
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는
정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를
출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는
경우에는 -1을 출력한다.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
  int num;
  struct _node *next;
} Node;

Node *head = NULL;
Node *tail = NULL;

void find(int num) {
	int i = 0; 
	int count = 0;
	for(i = 0; i < num; i++){
		if(head == NULL && tail == NULL) {
			printf("no nodes in this stack...\n");	
			return ;
		} 
	
	}
}

void size() {
  if (head == NULL && tail == NULL) {
    printf("0\n");
  } else {
    Node *temp = head;
    int cnt = 0;
    while (temp->next) { // 마지막을 찾아간다....
      temp = temp->next;
      cnt++; // 몇개가 있는지 count
    }
    // while 조건 속 temp가 NULL을 가리키면 while이 종료됨. 여기서 temp = temp
    // -> next는 실행안되니까 temp는 마지막 - 1에서 멈춰있고, count도 올라가지
    // 않게 됨. 출력시 count + 1을 해줘야 전체 갯수를 알 수 있다!

    printf("%d\n", cnt + 1);
  }
}

void empty() {
  if (head == NULL && tail == NULL) {
    printf("1\n");
  } else {
    printf("0\n");
  }
}

void top() {
  if (head == NULL && tail == NULL) {
    printf("-1\n");
  } else {
    printf("%d\n", tail->num);
  }
}

void pop() {
  if (head == NULL && tail == NULL) {
    printf("-1\n");
    return;
  } else {
    Node *temp = head; // 대신 리스트를 달려가 줄 친구
    Node *before = NULL; // 마지막 - 1 노드. 이 녀석이 있어야 pop 을 한 뒤
                         // tail을 이어줄 수 있음!
    while (temp->next) {
      before = temp;     // temp 현재
      temp = temp->next; // temp 하나 이후
    }
    printf("%d\n", temp->num);
    tail = before; // temp 출력 후 tail을 현재 temp - 1과 이어줘야 함.
    if (before == NULL) {
      head = NULL;
      return;
    }
    before->next = NULL; // pop한 노드와 리스트의 연결 끊기
    free(temp); // pop한 노드를 free해줘야 함!! memory leak 방지!
    return;
  }

  return;
}

void push(int x) {
  Node *data = (Node *)malloc(sizeof(Node));
  data->num = x;
  data->next = NULL;
  if (head == NULL && tail == NULL) { // 스택에 아무것도 없는 경우
    head = data;
    tail = data;
    return;
  } else {               // 스택이 비어있지 않은 경우
    Node *temp = head;   // 대신 연결리스트를 달려줄 애
    while (temp->next) { // 마지막을 찾아간다....
      temp = temp->next;
    }
    temp->next = data; // 마지막까지 왔으니까 그 다음에 추가
    tail = data;       // tail이 가리키는 부분도 바꿔줌!
    return;
  }
  return;
}

int main(void) {

  return 0;
}
