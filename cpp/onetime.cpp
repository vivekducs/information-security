#include<bits/stdc++.h>

using namespace std;

string generatekey(int n){
    string ans="";

    for(int i=0;i<n;i++){
        ans+='A'+(rand()%26);
    }
    return ans;
}

string encrypt(string text, string key){
    
    string ans="";
    
    for(int i=0;i<text.size();i++){
        if(isalpha(text[i])){
            ans+=(((text[i]-'A') + (key[i]-'A'))%26) + 'A';
        }
        else{
            ans+=text[i];
        }
    }
    
    return ans;
}

string decrypt(string text, string key){
    string ans="";
    
    for(int i=0;i<text.size();i++){
        if(isalpha(text[i])){
            ans+=((((text[i]-'A') - (key[i]-'A'))+26)%26) + 'A';
        }
        else{
            ans+=text[i];
        }
    }
    
    return ans;
}

int main(){
    string text="";
    
    cout<<"enter text"<<endl;
    getline(cin,text);
    
    string key=generatekey(text.size());

    string enc=encrypt(text,key);
    cout<<"ciphertext= "<<enc<<endl;
    
    string dec=decrypt(enc,key);
    cout<<"plaintext= "<<dec<<endl;

    return 0;
}