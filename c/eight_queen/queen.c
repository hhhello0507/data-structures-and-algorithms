#include <stdio.h>


// 한 열에 하나 씩

int pos[8];

void print(void) {
    for (int i = 0; i < 8; ++i) {
        printf("%2d", pos[i]);
    }
    putchar('\n');
}

void set(int i) {
    for (int j = 0; j < 8; ++j) {
        pos[i] = j;
        if (i == 7) {
            print();
        } else {
            set(i + 1);
        }
    }
}

int main(void) {
    set(0);
    return 0;
}