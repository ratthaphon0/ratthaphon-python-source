#include <stdio.h>
#define max 10
int main(){
    int A[max][max], B[max][max];
    int choice;
    do {
        printf("=== MENU ===\n");
        printf("1. Transpose 2nd Arrays\n");
        printf("2. Product 2nd Arrays\n");
        printf("3. Exit\n");
        printf("Choice: ");
        scanf("%d",&choice);

    }
    while(choice != 3);
}
