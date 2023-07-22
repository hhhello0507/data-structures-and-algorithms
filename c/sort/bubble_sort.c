#include <stdio.h>
void print(int arr[]);

int main(void ) {

    int arr[8];

    for (int i = 0; i < 8; ++i) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < 8 - 1; ++i) {
        for (int j = 7; j > i; --j) {
            if (arr[j - 1] > arr[j]) {
                int temp = arr[j - 1];
                arr[j - 1] = arr[j];
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