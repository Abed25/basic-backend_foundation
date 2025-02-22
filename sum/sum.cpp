#include<iostream>
int sum(int a, int b){
return a + b;
}
int main (){
    int num1,num2;
    std::cout << "Enter two numbers ";
    std::cin>> num1 >>num2;
    int results = sum(num1,num2);
    std::cout<<results;
    return(0);
}