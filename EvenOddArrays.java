// Code is of no importance



package Practice;
import java.util.Scanner;
public class EvenOddArrays {

    public static void main(String[] args){
        int[] array = new int[10];
        int[] evenarray = new int[10];
        int[] oddarray = new int[10];
        int odd = 0, even = 0, num = 0, evensum = 0, oddsum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Numbers :");
        for (int i = 0; i<10;i++){
            num = sc.nextInt();
            array[i] = num;
        }
        for (int i : array){
            if (i%2 == 0){
                evenarray[even] = i;
                even++;
            }
            else{
                oddarray[odd] = i;
                odd++;
            }
        }
        for (int i : evenarray){
            evensum += i;
        }
        for(int i : oddarray){
            oddsum += i;
        }
        System.out.println("Even Sum : "+evensum);
        System.out.println("Odd Sum : "+oddsum);
        try {
            int arr[] = new int[4];
            arr[0] = sc.nextInt();
        }
        catch (Exception e){
            System.out.println(e);
        }
    }
}
