#include <iostream>
using namespace std;

int main() {
  int a,b,c;
  cout << "dej a ";
  cin >> a;
  cout << "dej b ";
  cin >> b;
  cout << "dej c ";
  cin >> c;
  if (a+b>c && a+c>b && b+c>a){
      cout << "da rade ";
  }
  else{
      cout << "No sory nie wypali";
  }
  return 0;
}













