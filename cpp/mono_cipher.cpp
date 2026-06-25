#include<bits/stdc++.h>

using namespace std;

string encrypt(string text, string key){
    string result="";
    for(auto it:text){
        if(isalpha(it)){
            int indx=it-'A';
            char ch=key[indx];
            result+=ch;
        }
        else{
            result+=it;
        }
    }

    return result;
}

string generate(string text){
    string ans(26,'A');
    for(int i=0;i<26;i++){
        int indx=text[i]-'A';
        ans[indx]='A'+i;
    }

    return ans;
}



int main(){
    string text="";
    string key="QWERTYUIOPASDFGHJKLZXCVBNM";
    string invkey=generate(key);

    cout<<"enter text (uppercase only)"<<endl;
    getline(cin,text);

    string ciphertext=encrypt(text,key);
    cout<<"ciphertext= "<<ciphertext<<endl;

    string plaintext=encrypt(ciphertext,invkey);
    cout<<"plaintext= "<<plaintext<<endl;


    return 0;
}