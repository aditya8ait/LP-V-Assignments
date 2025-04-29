import java.rmi.*;
import java.util.Scanner;

public class Client {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {

            String serverURL = "rmi://localhost/Server";
            ServerIntf serverIntf = (ServerIntf) Naming.lookup(serverURL);

            System.out.println("Enter first number:");
            double num1 = sc.nextDouble();

            System.out.println("Enter first number:");
            double num2 = sc.nextDouble();

            System.out.println("First number is:"+num1);
            System.out.println("Second Number is:"+num2);
            
            System.out.println("---------RESULT----------");
            System.out.println("Addition is:"+serverIntf.Add(num1, num2));
            System.out.println("Subtraction is:"+serverIntf.Sub(num1, num2));
            System.out.println("Multiplication is:"+serverIntf.Mul(num1, num2));
            System.out.println("Division is:"+serverIntf.Div(num1, num2));
            
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Exception occured"+e.getMessage());
        }
        sc.close();
    }
}