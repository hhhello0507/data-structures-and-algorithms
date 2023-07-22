#include <stdio.h>

void print(int arr[]);

int main(void) {
    int arr[8];
    for (int i = 0; i < 8; ++i) {
        scanf("%d", &arr[i]);
    }

    for (int i = 1; i < 8; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] < arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    print(arr);
    return 0;
}

void print(int arr[]) {
    for (int i = 0; i < 8; ++i) {
        printf("%d ", arr[i]);
    }
}