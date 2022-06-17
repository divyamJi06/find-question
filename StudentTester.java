package HelloWorld;

import java.util.Scanner;

public class StudentTester{

    private int studentId;
    private String name;
    private float qualifyingExamMarks;
    private char residentialStatus;
    private int yearOfEngg;

    public int getStudentId(){
        return studentId;
    }

    public void setStudentId(int studentId){
        this.studentId = studentId;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public float getQualifyingExamMarks(){
        return qualifyingExamMarks;
    }

    public void setQualifyingExamMarks(float qualifyingExamMarks){
        this.qualifyingExamMarks = qualifyingExamMarks;
    }

    public char getResidentialStatus(){
        return residentialStatus;
    }

    public void setResidentialStatus(char residentialStatus){
        this.residentialStatus = residentialStatus;
    }

    public int getYearOfEngg(){
        return yearOfEngg;
    }

    public void setYearOfEngg(int yearOfEngg){
        this.yearOfEngg = yearOfEngg;
    }


    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int studentId;
        String name;
        float qualifyingExamMarks;
        char residentialStatus;
        int yearOfEngg;

        System.out.println("Enter Student Id:\t");
        studentId = sc.nextInt();
        System.out.println("Enter Student Name:\t");
        name = sc.next();
        System.out.println("Enter Qualifying Marks:\t");
        qualifyingExamMarks = sc.nextFloat();
        System.out.println("Enter Residential Status:\t");
        residentialStatus = sc.next().charAt(0);
        System.out.println("Enter Year of Engg:\t");
        yearOfEngg = sc.nextInt();

        StudentTester s1 = new StudentTester();
        s1.setStudentId(studentId);
        s1.setName(name);
        s1.setQualifyingExamMarks(qualifyingExamMarks);
        s1.setResidentialStatus(residentialStatus);
        s1.setYearOfEngg(yearOfEngg);


        System.out.println("Student Name       :\t" + s1.getName());
        System.out.println("Student Id         :\t" + s1.getStudentId());
        System.out.println("Qualifying marks   :\t" + s1.getQualifyingExamMarks());
        System.out.println("Year of Engineering:\t" + s1.getYearOfEngg());
        if(s1.getResidentialStatus() == 'H')
            System.out.println("Residential status :\tHostellers");
        else
            System.out.println("Residential status :\tDay Scholar");
    }
}
