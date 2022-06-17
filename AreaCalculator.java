package HelloWorld;

class Rectangle {

    public int length;
    public int breadth;

    public void setLength(int length) {
        this.length = length;
    }

    public void setBreadth(int breadth) {
        this.breadth = breadth;
    }

    public int area() {
        return length * breadth;
    }
    public static void main(String[] args){
    }

}
public class AreaCalculator {
    public static void main(String args[]){
        Rectangle r1 = new Rectangle();
        r1.setBreadth(10);
        r1.setLength(20);
        System.out.println("Rectangle r1 Properties-");
        System.out.println("Length = "+r1.length);
        System.out.println("Breadth = "+r1.breadth);
        System.out.println("Area = "+r1.area());
    }
}
