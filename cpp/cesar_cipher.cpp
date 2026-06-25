#include<bits/stdc++.h>

using namespace std;
string encrypt(string text, int key){
    string result="";
    for(char c : text) {
        if(isalpha(c)) {
            char base = islower(c) ? 'a' : 'A';
            c = (c - base + key) % 26 + base;
        }
        result += c;
    }
    return result;
}

string decrypt(string text, int key) {
    return encrypt(text, 26 - key); 
}

int main(){
    int key;
    string text;

    cout<<"enter text"<<endl;
    getline(cin,text);

    cout<< "enter key"<<endl;
    cin>>key;
    key=key%26;

    string ciphertext=encrypt(text,key);
    cout<<"ciphertext= "<<ciphertext<<endl;

    string originaltext=decrypt(ciphertext,key);
    cout<<"originaltext= "<<originaltext<<endl;

    return 0;
}