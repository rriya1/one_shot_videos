#include <iostream>
using namespace std;

//creating an abstract class
class abstractemployee
{
    virtual void getpromo();
};

//creating a class
class employee: abstractemployee
{   //attributes of the class, they are rpivate by default
    string name;
    string company;
    int age;
    //method of a class, makin it public
    public:
    void introduction()
    {
        cout<<"HI! my name is "<<name<<" and i work for "<<company<<endl;
    }

    //making a contructor, a constructor need to be public
    //this constructor is not like the default one, it has arguments
    employee(string na,string comp, int a)
    {
        name=na;
        company=comp;
        age=a;
    }

    //creating getters and setters for the  private attributes so that outsiders can interact with them.
    void setname(string na) //setter
    {
        name=na;
    }
    string getname() //getter 
    {
        return name;
    } 

    //definition for virtual function in abstract class
    void getpromo()
    {
        if(age>18)
        {
            cout<<"yes, "<<name<<" is elidible for promo"<<endl;
        }
    }
}; 

int main()
{
    //creating an instance of the class employee
    //constructing emp1 by invoking the constructor that we made
    employee emp1 = employee("riya","google",22);
    emp1.introduction();
    //another way of using the same constructor
    employee emp2("chuchu","chyu",21);
    emp2.introduction();
}
