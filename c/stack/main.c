#include <stdio.h>
#include "IntStack.h"

int main(void) {
    IntStack s;
    if (Initialize(&s, 10) == -1) {
        puts("실패 ㅜ");
        return 1;
    }

    Push(&s, 1);
    Push(&s, 3);
    Push(&s, 5);
    Push(&s, 10);
    Print(&s);

    int a;

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