package HelloWorld;

public class CommandLineArguments {
    public static void main(String args[]){
        System.out.println(args.length);
        System.out.println("Command Line Arguments received -" + "\n" + args[0] +"\n" + args[1]);
    }
}
