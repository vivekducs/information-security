#include <iostream>
#include <string>
using namespace std;

char keyMatrix[5][5];
int posR[26], posC[26];   // store row and column of each letter

// Build matrix
void buildMatrix(string key) {
    bool used[26] = {false};
    used['J' - 'A'] = true; // J merges with I

    string k = "";
    for(char c : key) {
        if(isalpha(c)) {
            c = toupper(c);
            if(!used[c - 'A']) {
                used[c - 'A'] = true;
                k += c;
            }
        }
    }

    for(char c = 'A'; c <= 'Z'; c++)
        if(!used[c - 'A'])
            k += c;

    int idx = 0;
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            keyMatrix[i][j] = k[idx];
            posR[k[idx] - 'A'] = i;
            posC[k[idx] - 'A'] = j;
            idx++;
        }
    }
}

// Prepare plaintext
string prepare(string text) {
    string p = "";
    for(char c : text) {
        if(isalpha(c)) {
            c = toupper(c);
            if(c == 'J') c = 'I';
            p += c;
        }
    }

    string res = "";
    for(int i = 0; i < p.size(); i++) {
        res += p[i];

        if(i + 1 < p.size() && p[i] == p[i+1])
            res += 'X';
    }

    if(res.size() % 2 == 1)
        res += 'X';

    return res;
}

// Encrypt a pair
string encPair(char a, char b) {
    int r1 = posR[a - 'A'], c1 = posC[a - 'A'];
    int r2 = posR[b - 'A'], c2 = posC[b - 'A'];

    if(r1 == r2) {  // same row
        c1 = (c1 + 1) % 5;
        c2 = (c2 + 1) % 5;
    }
    else if(c1 == c2) { // same column
        r1 = (r1 + 1) % 5;
        r2 = (r2 + 1) % 5;
    }
    else { // rectangle
        int temp = c1;
        c1 = c2;
        c2 = temp;
    }

    string res = "";
    res += keyMatrix[r1][c1];
    res += keyMatrix[r2][c2];
    return res;
}

// Decrypt a pair
string decPair(char a, char b) {
    int r1 = posR[a - 'A'], c1 = posC[a - 'A'];
    int r2 = posR[b - 'A'], c2 = posC[b - 'A'];

    if(r1 == r2) {   // same row
        c1 = (c1 + 4) % 5;
        c2 = (c2 + 4) % 5;
    }
    else if(c1 == c2) { // same column
        r1 = (r1 + 4) % 5;
        r2 = (r2 + 4) % 5;
    }
    else { // rectangle
        int temp = c1;
        c1 = c2;
        c2 = temp;
    }

    string res = "";
    res += keyMatrix[r1][c1];
    res += keyMatrix[r2][c2];
    return res;
}

string encrypt(string text) {
    string p = prepare(text);
    string out = "";

    for(int i = 0; i < p.size(); i += 2)
        out += encPair(p[i], p[i+1]);

    return out;
}

string decrypt(string text) {
    string out = "";

    for(int i = 0; i < text.size(); i += 2)
        out += decPair(text[i], text[i+1]);

    return out;
}

int main() {
    string key, text;

    cout << "Enter key: ";
    getline(cin, key);

    cout << "Enter text: ";
    getline(cin, text);

    buildMatrix(key);

    string enc = encrypt(text);
    string dec = decrypt(enc);

    cout << "\nEncrypted: " << enc << endl;
    cout << "Decrypted: " << dec << endl;

    return 0;
}
