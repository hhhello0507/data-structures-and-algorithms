#ifndef ___IntQueue
#define ___IntQueue

typedef struct {
    int max;
    int num;
    int front;
    int rear;
    int *queue;
} IntQueue;


int Initialize(IntQueue *q, int max);

int InQueue(IntQueue *q, int x);

int DeQueue(IntQueue *q, int *x);

int Peek(const IntQueue *q, int *x);

void Clear(IntQueue *q);

int Capacity(const IntQueue *q);

int Size(const IntQueue *q);

int IsEmpty(const IntQueue *q);

int IsFull(const IntQueue *q);

int Search(const IntQueue *q, int x);

void Print(const IntQueue *q);

void Terminate(IntQueue *q);

#endif