#ifndef ___ArrayIntQueue
#define ___ArrayIntQueue

typedef struct {
    int max;
    int ptr;
    int *stk;
} ArrayIntStack;

int Initialize(ArrayIntStack *s, int max);

int InQueue(ArrayIntStack *s, int x);

int Pop(ArrayIntStack *s, int *x);

int Rear(const ArrayIntStack *s, int *x);

void Clear(ArrayIntStack *s);

int Capacity(const ArrayIntStack *s);

int Size(const ArrayIntStack *s);

int IsEmpty(const ArrayIntStack *s);

int IsFull(const ArrayIntStack *s);

int Search(const ArrayIntStack *s, int x);

void Print(const ArrayIntStack *s);

void Terminate(ArrayIntStack *s);

int Dequeue(ArrayIntStack *s);

int Front(ArrayIntStack *s, int *x);

#endif