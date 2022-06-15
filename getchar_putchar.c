/*Getchar is to take a single char as input, putchar is to print a single char*/
#include <stdio.h>
#include <ctype.h>
int main()
{
    char c;
    char ch1='a', ch2; 
    char ch3='X', ch4;
    char ch5='8';
    printf("Enter some character..\n");
    c = getchar();
    printf("Entered character is: ");
    putchar(c);
    printf("\n");
    printf("%i /n",islower(c));
    ch2 = toupper(ch1);
    printf("%c %c \n",ch1,ch2);
    ch4 = tolower(ch3); 
    printf("%c %c \n",ch3,ch4);
    printf("%d\n",isdigit(ch5));
    printf("%d\n",islower(ch1));
    printf("%d\n",isalpha(ch5));
    return(0);
}