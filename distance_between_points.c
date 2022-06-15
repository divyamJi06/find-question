/* This Program calculates the distance between two points..*/

#include <stdio.h>  
#include <math.h>
int main()  
{   int x1,x2,y1,y2;
    double distance;
    printf("Point 1-");
    scanf("%d %d", &x1, &y1 );
    printf("Point 2-");
    scanf("%d %d", &x2, &y2 );
    distance = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
    distance = sqrt(distance);
    printf("Distance between the Two points = %12.6f \n", distance);
    return 0;
}  