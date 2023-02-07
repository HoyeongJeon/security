/*
백준 10845
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는
정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는
경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에
들어있는 정수가 없는 경우에는 -1을 출력한다.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
  int num;
  struct _node *next;
} Node;

Node *head = NULL;
Node *tail = NULL;

void front() {
  if (head == NULL && tail == NULL) {
    printf("-1\n");
  } else {
    printf("%d\n", head->num);
  }
}

void back() {
  if (head == NULL && tail == NULL) {
    printf("-1\n");
  } else {
    printf("%d\n", tail->num);
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
      // while 조건 속 temp가 NULL을 가리키면 while이 종료됨. 여기서 temp = temp
      // -> next는 실행안되니까 temp는 마지막 - 1에서 멈춰있고, count도 올라가지
      // 않게 됨. 출력시 count + 1을 해줘야 전체 갯수를 알 수 있다!
      printf("%d\n", cnt + 1);
    }
  }
}

void empty() {
  if (head == NULL && tail == NULL) {
    printf("1\n");
  } else {
    printf("0\n");
  }
}

void pop() {
  if (head == NULL && tail == NULL) {
    printf("-1\n");
  } else {
    Node *temp = (Node *)malloc(sizeof(Node)); // 대신 큐를 순회할 친구
    if (!head) { // head가 없는 경우, 즉 큐의 모든 노드가 free되어서 head가
                 // 가리키는 곳이 없을 때!
      head = NULL; // 큐가 비어있으므로 head와 tail을 NULL로 변경!
      tail = NULL;
      printf("-1\n");
      return;
    }
    printf("%d\n", head->num); // 큐 맨 앞에 있는 친구 출력
    temp = head;
    temp = temp->next; // 맨 앞 - 1 (즉 큐의 2번재로 temp 이동)
    free(head);        //큐의 1번 친구 free 해줌
    head = temp; // 갈 곳 잃은 head를 temp로 바꿔줌 (pop 이전 큐의 2번째 node를
                 // pop 후 1번 node로 변경!)
  }
}

void push(int x) {
  Node *node = (Node *)malloc(sizeof(Node));
  node->num = x;
  node->next = NULL;
  if (head == NULL && tail == NULL) {
    head = node;
    tail = node;
    return;
  } else {
    Node *temp = (Node *)malloc(sizeof(Node));
    temp = head;
    while (temp->next) {
      temp = temp->next;
    }
    // temp는 queue의 마지막에 와있음
    temp->next = node; // 큐 끝에 추가할 node 추가
    tail = node;       // tail 변경!
    return;
  }
}

int main(void) {

  return 0;
}
