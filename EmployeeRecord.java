package HelloWorld;

public class EmployeeRecord {
    public static void main(String[] args){

        double[] salary = {23500.0, 25080.0, 28760.0, 22340.0, 19890.0};
        double avgSalary;
        double sumSalary = 0;
        int len = salary.length;
        int lessThan =0, greaterThan = 0;
        for (double s: salary){
            sumSalary += s;
        }
        avgSalary = sumSalary/len;

        for(double s: salary){
            if (s<avgSalary) greaterThan++;
            else lessThan++;
        }

        System.out.println("Average Salary of employees: "+avgSalary);
        System.out.println("The number of employees whose salary is greater than the average: "+greaterThan);
        System.out.println("The number of employees whose salary is lesser than the average: "+lessThan);

    }
}
