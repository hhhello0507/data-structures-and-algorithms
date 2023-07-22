#include <stdio.h>

int pos[8];
int flag[8];
int flag_a[15]; // y = -x
int flag_b[15]; // y = x
int sum = 0;

void print(void) {
    for (int i = 0; i < 8; ++i) {
        printf("%2d", pos[i]);
    }
    putchar('\n');
}

void set(int i) {
    for (int j = 0; j < 8; ++j) {
        if (!flag[j] && !flag_a[i + j] && !flag_b[i - j + 7]) {
            pos[i] = j;
            if (i == 7) {
                sum++;
                print();
            } else {
                flag[j] = flag_a[i + j] = flag_b[i - j + 7] = 1;
                set(i + 1);
                flag[j] = flag_a[i + j] = flag_b[i - j + 7] = 0;
            }
        }
    }
}

int main(void) {
    set(0);
    printf("result - %d\n", sum);
    return 0;
}