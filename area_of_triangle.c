/* This Program calculates the area of a triangle..*/

#include <stdio.h>  
#include <math.h>
int main()  
{   int base,height;
    double area;
    printf("BAse -");
    scanf("%d", &base);
    printf("Height - ");
    scanf("%d", &height);
    area = (base*height)/2 ;
    printf("Area = %lf \n", area);
    return 0;
}  