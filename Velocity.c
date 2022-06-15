/* This Program calculates the velocity..*/

#include <stdio.h>  
#include <math.h>
int main()  
{   int vo,a,x,x0;
    double velocity;
    printf("Values-");
    scanf("%d %d %d %d", &vo, &a, &x, &x0);
    velocity = sqrt(pow(vo,2) - 2*a*(x-x0));
    printf("Velocity - %f\n", velocity);
    return 0;
}  