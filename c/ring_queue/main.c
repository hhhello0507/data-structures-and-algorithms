#include <stdio.h>
#include "IntQueue.h"


int main(void) {

    IntQueue q;
    int a;
    Initialize(&q, 3);

    InQueue(&q, 1);
    InQueue(&q, 3);
    InQueue(&q, 2);

    Print(&q);
//    printf("%d %d %d\n", q.front, q.rear, q.num);
    DeQueue(&q, &a);
//    printf("%d %d %d\n", q.front, q.rear, q.num);

    Print(&q);
    DeQueue(&q, &a);

    Print(&q);
    DeQueue(&q, &a);

    return 0;
}