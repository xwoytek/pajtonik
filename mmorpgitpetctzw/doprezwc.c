#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Dej a");
    scanf("%d", &a);
    printf("Dej b");
    scanf("%d", &b);
    printf("Dej c");
    scanf("%d", &c);
    if (a+b>c && a+c>b && b+c>a){
        printf("To wypali");
    }
    else{
        printf("Nie da rady szefunciu");
    }
    

    return 0;
}
