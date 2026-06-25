#include <iostream>
#include <string>
using namespace std;

string generateKey(string text, string key) {
    string newKey = "";
    int j = 0;

    for (int i = 0; i < text.size(); i++) {
        if (isalpha(text[i])) {
            newKey += key[j % key.size()];
            j++;
        } else {
            newKey += text[i]; // keep spaces/symbols
        }
    }
    return newKey;
}

char shiftEncrypt(char p, char k) {
    if (!isalpha(p)) return p;

    bool low = islower(p);
    p = toupper(p);
    k = toupper(k);

    char c = (p - 'A' + (k - 'A')) % 26 + 'A';
    if (low) c = tolower(c);
    return c;
}

char shiftDecrypt(char c, char k) {
    if (!isalpha(c)) return c;

    bool low = islower(c);
    c = toupper(c);
    k = toupper(k);

    char p = (c - 'A' - (k - 'A') + 26) % 26 + 'A';
    if (low) p = tolower(p);
    return p;
}

string encrypt(string text, string key) {
    string newKey = generateKey(text, key);
    string out = "";

    for (int i = 0; i < text.size(); i++)
        out += shiftEncrypt(text[i], newKey[i]);

    return out;
}

string decrypt(string text, string key) {
    string newKey = generateKey(text, key);
    string out = "";

    for (int i = 0; i < text.size(); i++)
        out += shiftDecrypt(text[i], newKey[i]);

    return out;
}

int main() {
    string text, key;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter key: ";
    getline(cin, key);

    string enc = encrypt(text, key);
    string dec = decrypt(enc, key);

    cout << "\nEncrypted: " << enc << endl;
    cout << "Decrypted: " << dec << endl;

    return 0;
}
