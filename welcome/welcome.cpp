#include<iostream>
#include<string>
// using namespace std;

void welcome(std::string name){
    std::cout << "Welcome to DSA crush with C++ "<< name;
}
int main (){
    std::string myName;
    std::cout<<"Who should i call you? :";
    std::cin>>myName;
    welcome(myName);
    return (0);
}