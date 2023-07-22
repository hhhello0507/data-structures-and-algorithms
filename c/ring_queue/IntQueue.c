#include "IntQueue.h"
#include <stdlib.h>
#include <stdio.h>


int Initialize(IntQueue *q, int max) {
    q->num = q->front = q->rear = 0;
    if ((q->queue = calloc(max, sizeof(int))) == NULL) {
        q->max = 0;
        return -1;
    }
    q->max = max;
    return 0;
}

int InQueue(IntQueue *q, int x) {
    if (q->num >= q->max) {
        return -1;
    }
    q-> num++;
    q->queue[q->rear++] = x;
    if (q->rear == q->max)
        q->rear = 0;
    return 0;
}

int DeQueue(IntQueue *q, int *x) {
    if (q->num <= 0) {
        return -1;
    }
    q->num--;
    *x = q->queue[q->front++];
    if (q->front == q->max) {
        q->front = 0;
    }
    return 0;
}

int Peek(const IntQueue *q, int *x){
    return 0;
}

void Clear(IntQueue *q){

}

int Capacity(const IntQueue *q){
    return 0;

}

int Size(const IntQueue *q){
    return 0;

}

int IsEmpty(const IntQueue *q){
    return 0;

}

int IsFull(const IntQueue *q){
    return 0;

}

int Search(const IntQueue *q, int x){
    if (q->num <= 0) {
        return -1;
    }
    for (int i = 0; i < q->rear; ++i) {
        if (q->queue[(i + q->front) % q->max] == x) {
            return i;
        }
    }
    return -1;
}

void Print(const IntQueue *q){
    for (int i = 0; i < q->num; ++i) {
        printf("%d ", q->queue[(i + q->front) % q->max]);
    }

    putchar('\n');
}

void Terminate(IntQueue *q){
    if (q->queue != NULL) {
        free(q->queue);
    }
    q->max = q->num = q->front = q->rear = 0;
}