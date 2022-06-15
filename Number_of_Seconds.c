/* This Program converts number of seconds into number of hours minutes and seconds*/

#include <stdio.h>  
#include <math.h>
int main()  
{   int seconds, hours, minutes, second;
    printf("Enter number of Seconds- ");
    scanf("%d", &seconds);
    hours = seconds/3600;
    minutes = (seconds - (hours*3600))/60;
    second = (seconds - (hours*3600) - (minutes*60));
    printf("\n %d is equivalent to %d hour(s), %d minute(s) and %d second(s)",seconds,hours,minutes,second);
    return 0;
}  