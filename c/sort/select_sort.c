#include <stdio.h>

void print(int arr[]);

int main(void) {
    int arr[8];
    for (int i = 0; i < 8; ++i) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < 8 - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < 8; ++j) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
    print(arr);

    return 0;
}

void print(int arr[]) {
    for (int i = 0; i < 8; ++i) {
        printf("%d ", arr[i]);
    }
}