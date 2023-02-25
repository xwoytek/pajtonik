import java.util.Scanner;

class trojkat
{
  public static void main(String[] string) {
  
    float a,b,c;
    System.out.print("dej a ");
    Scanner r = new Scanner(System.in);
    a = r.nextFloat();
    System.out.print("dej b ");
    b = r.nextFloat();
    System.out.print("dej c ");
    c = r.nextFloat();
  if (a + b > c && a + c > b && b + c > a) {
    System.out.print("Tak da sie zrobic");
  }
  else{
    System.out.print("to nie wypali");
  }
  }
}
