//DECODE AX+B FORM
#include <iostream>
#include <string>
using namespace std;

int solve(int ab,int ans);
int verify(int d,int e);
int mod(int value);

int main() {
    // Array to map each letter to a number
    int letterToNumber[26];
    char A[100]="abcdefghijklmnopqrstuvwxyz";
    int B;
    cout<<"Value of a :";
    cin>>B;

    // Assigning numbers to each letter (assuming lowercase letters)
    for (int i = 0; i < 26; ++i) {
        letterToNumber[i] = i + 1; // You can assign any numbers you want
    }

    std::string input;
    std::cout << "Enter a string of lowercase letters: ";
    std::cin >> input;

    // Converting each letter to its corresponding number
    for (char letter : input) 
    {
        if (letter >= 'a' && letter <= 'z') 
            {
            int number = letterToNumber[letter - 'a'];
            for(int i=0;i<26;i++)
            {
            if(i<25)
            {
             int b=number-i+26;
             int z=mod(b);
             int ab=B;
             int ANS=verify(ab,z);
             cout<<"  "<<A[ANS];
            }
            else
            {
                cout<<" "<<endl;
            }
            }
            }
        else 
        {
            std::cerr << "Invalid input: " << letter << " is not a lowercase letter." << std::endl;
        }
    }
    return 0;
}

int verify(int d, int e) {
    for (int j = 0; j < 26; j++) {
        int p = d * j;
        int q = mod(p);
        if (q == e) {
            return j;
        }
    }
    // If no match found, return a default value
    return -1;
}

int mod(int value)
{
    if(value<26)
    {
        return value;
    }
    else
    {
        int x=value/26;
        int y=value - (x*26);
        return y;
    };
}
