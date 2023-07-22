#include <stdio.h>
#include <stdlib.h>
#include "ArrayIntQueue.h"

int Initialize(ArrayIntStack *s, int max) {
    s->ptr = 0;

    if ((s->stk = calloc(max, sizeof(int))) == NULL) {
        s-> max = 0;
        return -1;
    }
    s->max = max;
    return 0;
}

int InQueue(ArrayIntStack *s, int x) {
    if (s->ptr >= s->max) {
        return -1;
    }
    s->stk[s->ptr++] = x;
    return 0;
}

int Pop(ArrayIntStack *s, int *x) {
    if (s->ptr <= 0) {
        return -1;
    }
    *x = s->stk[s->ptr - 1];
    s->ptr--;
    return 0;
}

int Rear(const ArrayIntStack *s, int *x) {
    if (s->ptr <= 0) {
        return -1;
    }
    *x = s->stk[s->ptr - 1];
    return 0;
}

void Clear(ArrayIntStack *s) {
    s->ptr = 0;
}

int Capacity(const ArrayIntStack *s) {
    return s->max;
}

int Size(const ArrayIntStack *s) {
    return s->ptr;
}

int IsEmpty(const ArrayIntStack *s) {
    return s->ptr <=0;
}

int IsFull(const ArrayIntStack *s) {
    return s->ptr >= s->max;
}

int Search(const ArrayIntStack *s, int x) {
    for (int i = s->ptr - 1; i >= 0; i--) {
        if (s->stk[i] == x) {
            return i;
        }
    }
    return -1;
}

void Print(const ArrayIntStack *s) {
    if (s->ptr == 0) {
        printf("암것도 없어요");
    }
    for (int i = 0; i < s->ptr; ++i) {
        printf("%d ", s->stk[i]);
    }
    putchar('\n');
}

void Terminate(ArrayIntStack *s) {
    if (s->stk != NULL) {
        free(s->stk);
    }
    s->max = s->ptr = 0;
}

int Dequeue(ArrayIntStack *s) {
    if (s->ptr <= 0) {
        return -1;
    }
    s->ptr--;
    for (int i = 0; i < s->ptr; ++i) {
        s->stk[i] = s->stk[i + 1];
    }
    return 0;
}

int Front(ArrayIntStack *s, int *x) {
    if (s->ptr <= 0) {
        return -1;
    }
    *x = s->stk[0];
    return 0;
}