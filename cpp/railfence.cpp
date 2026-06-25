#include <iostream>
#include <string>
#include <vector>
using namespace std;

string encryptRailFence(string text, int key) {
    if (key == 1) return text;

    vector<string> rail(key, "");
    int row = 0;
    bool down = true;

    for (char c : text) {
        rail[row] += c;
        if (row == 0) down = true;
        else if (row == key - 1) down = false;

        row += (down ? 1 : -1);
    }

    string cipher = "";
    for (int i = 0; i < key; i++)
        cipher += rail[i];

    return cipher;
}

string decryptRailFence(string cipher, int key) {
    if (key == 1) return cipher;

    vector<vector<bool>> mark(key, vector<bool>(cipher.size(), false));

    int row = 0;
    bool down = true;

    // 1️⃣ Mark the zigzag pattern positions
    for (int i = 0; i < cipher.size(); i++) {
        mark[row][i] = true;

        if (row == 0) down = true;
        else if (row == key - 1) down = false;

        row += (down ? 1 : -1);
    }

    // 2️⃣ Fill the matrix row-wise with cipher text
    vector<vector<char>> rail(key, vector<char>(cipher.size(), '\n'));

    int index = 0;
    for (int r = 0; r < key; r++) {
        for (int c = 0; c < cipher.size(); c++) {
            if (mark[r][c]) {
                rail[r][c] = cipher[index++];
            }
        }
    }

    // 3️⃣ Read plaintext using zigzag pattern
    string plain = "";
    row = 0;
    down = true;

    for (int i = 0; i < cipher.size(); i++) {
        plain += rail[row][i];

        if (row == 0) down = true;
        else if (row == key - 1) down = false;

        row += (down ? 1 : -1);
    }

    return plain;
}

int main() {
    string text;
    int key;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter key (number of rails): "; 
    cin >> key;

    string cipher = encryptRailFence(text, key);
    string plain = decryptRailFence(cipher, key);

    cout << "\nEncrypted: " << cipher << endl;
    cout << "Decrypted: " << plain << endl;

    return 0;
}
