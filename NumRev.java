package HelloWorld;

import java.util.Scanner;

public class NumRev {
    public int revWhile(int num){
        int rev = 0;
        int ld;
        while(num>0){
            ld = num%10;
            rev = rev*10 + ld;
            num = num/10;
        }
        return rev;
    }
    public int revDoWhile(int num){
        int rev = 0;
        int ld;
        do{
            ld = num%10;
            rev = rev*10 + ld;
            num = num/10;
        }
        while (num>0);
        return rev;
    }
    public int revFor(int num){
        int rev = 0 ,ld;
        for(;num>0;num = num/10){
            ld = num%10;
            rev = rev*10 + ld;
        }
        return rev;


//        String num2;
//        String rev = "";
//        int rev2;
//        num2 = String.valueOf(num);
//        for (int i = 0 ; i<num2.length(); i++){
//            rev = num2.charAt(i) + rev;
//        }
//        rev2 = Integer.parseInt(rev);
//        return rev2;
    }
    public static void main(String[] args){

        int number,rev1,rev2,rev3;
        Scanner sc = new Scanner(System.in);
        NumRev reverser = new NumRev();

        System.out.print("Enter a number :");
        number = sc.nextInt();

        rev1 = reverser.revWhile(number);
        rev2 = reverser.revDoWhile(number);
        rev3 = reverser.revFor(number);

        System.out.println("Reverse of the given Number is -\n1.Using While: " + rev1 + "\n2.Using Do While: "
                + rev2 + "\n3.Using For: " + rev3);

    }
}
