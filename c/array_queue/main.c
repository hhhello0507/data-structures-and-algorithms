#include <stdio.h>
#include "ArrayIntQueue.h"

int main(void) {
    ArrayIntStack s;
    if (Initialize(&s, 10) == -1) {
        puts("실패 ㅜ");
        return 1;
    }
    int a;

    InQueue(&s, 1);
    InQueue(&s, 3);
    InQueue(&s, 5);
    InQueue(&s, 10);

    Print(&s);

    Front(&s, &a);
    printf("%d\n", a);
    Dequeue(&s);

    Front(&s, &a);
    printf("%d\n", a);
    Dequeue(&s);

    Front(&s, &a);
    printf("%d\n", a);
    Print(&s);


    Pop(&s, &a);
    Print(&s);
    printf("%d\n", a);
    Pop(&s, &a);
    printf("%d\n", a);

    Print(&s);

    Clear(&s);
    Print(&s);

    return 0;
}