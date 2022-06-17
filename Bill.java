package HelloWorld;

import java.util.Scanner;

public class Bill {
    public static void main(String[] args){

        int discount=0;
        double discountedBillAmount, billAmount;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter BillAmount: ");
        billAmount = sc.nextDouble();
        System.out.print("Enter Discount percentage: ");
        discount = sc.nextInt();
        discountedBillAmount = billAmount - billAmount * (((float)discount)/100);
        System.out.printf("Discounted Amount: %5.2f",discountedBillAmount);

    }
}
