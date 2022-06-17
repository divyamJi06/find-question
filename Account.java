package HelloWorld;

public class Account {
    private double balance = 500.00; //state variable
    public double getBalance(long AccNo){
        return balance;
    }
    public static void main(String[] args){

        Account ac1 = new Account();
        long accNo = 123456;
        double value = ac1.getBalance(accNo);
        System.out.println("Balance for the Account "+accNo+" is : "+ value);
    }

}
