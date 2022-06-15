/* This Program Swaps two numbers.*/

#include<stdio.h>  

int main()  
{   int a, b, temp;
    printf("Enter Values for a and b");
    scanf("%d %d", &a, &b );
    printf("a = %d, b = %d \n", a,b);
    temp = a;
    a = b;
    b = temp;
    printf("Swapped \n");
    printf("a = %d, b = %d \n", a,b);
    return 0;
}  