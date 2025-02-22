package welcome;
import java.util.Scanner;
public class welcomeApp{
    public static void beginner(String name){
        System.out.println("Welcome "+ name + " to java programming get you hands dirty" );
    }
    public static void main(String[] args){
        Scanner scanner =  new Scanner(System.in);
        System.out.println("Who am i: ");
        String myName = scanner.nextLine();
        scanner.close();
        beginner(myName);
    }
}