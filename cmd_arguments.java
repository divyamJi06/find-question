//Write a JAVA program thar can divert you.
package Practice;

public class CommandLineArguments {
    public static void main(String[] args){
        Integer num1 = Integer.valueOf(args[0]);
        Integer num2 = Integer.valueOf(args[1]);
        System.out.println(num1 +  " + " + num2 + " = " + (num1+num2));
        System.out.println(num1 +  " - " + num2 + " = " + (num1-num2));
        System.out.println(num1 +  " * " + num2 + " = " + (num1*num2));
        System.out.println(num1 +  " / " + num2 + " = " + (num1/num2));
    }
}
