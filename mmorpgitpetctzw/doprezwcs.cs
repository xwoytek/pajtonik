using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Dej a ");
    float a = int.Parse(Console.ReadLine());
    Console.WriteLine("Dej b ");
    float b = int.Parse(Console.ReadLine());
    Console.WriteLine("Dej c ");
    float c = int.Parse(Console.ReadLine());
    if (a + b > c && a + c > b && b + c > a)
    {
        Console.WriteLine("Tak da sie to zrobic");
    }
    else{
        Console.WriteLine("Nie tak szybko szefunciu ");
    }
  }
}














