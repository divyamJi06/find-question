/* This Program adds two complex numbers..*/

#include <stdio.h>  
#include <math.h>
int main()  
{   int a1,b1,a2,b2,a3,b3;
    printf("Complex Number -1");
    scanf("%d %d", &a1, &b1);
    printf("Complex 1 = %d + %d *i \n", a1,b1);
    printf("Complex Number -2");
    scanf("%d %d", &a2, &b2);
    printf("Complex 2 = %d + %d *i \n", a2,b2);
    a3 = a1 + a2;
    b3 = b1 + b2;
    printf("Sum = %d + %d *i", a3,b3);
    return 0;
}  