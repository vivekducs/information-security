#include <bits/stdc++.h>
using namespace std;

// Remove spaces from plaintext
string cleanText(string text) {
    string out = "";
    for (char c : text)
        if (isalpha(c))
            out += toupper(c);
    return out;
}

// Generate numeric key order
vector<int> getKeyOrder(string key) {
    vector<pair<char,int>> arr;
    vector<int> order(key.size());

    for (int i = 0; i < key.size(); i++)
        arr.push_back({toupper(key[i]), i});

    sort(arr.begin(), arr.end());  // sort by character

    for (int i = 0; i < arr.size(); i++)
        order[i] = arr[i].second;

    return order;
}

// Encryption
string encrypt(string text, string key) {
    text = cleanText(text);

    int rows = ceil((double)text.size() / key.size());
    int cols = key.size();

    // fill matrix row-wise
    vector<vector<char>> mat(rows, vector<char>(cols, 'X'));
    int idx = 0;

    for(int r = 0; r < rows; r++){
        for(int c = 0; c < cols; c++){
            if(idx < text.size())
                mat[r][c] = text[idx++];
        }
    }

    vector<int> order = getKeyOrder(key);
    string cipher = "";

    // read column-wise according to key order
    for (int c : order) {
        for (int r = 0; r < rows; r++)
            cipher += mat[r][c];
    }

    return cipher;
}

// Decryption
string decrypt(string cipher, string key) {
    int cols = key.size();
    int rows = ceil((double)cipher.size() / cols);

    vector<int> order = getKeyOrder(key);

    vector<vector<char>> mat(rows, vector<char>(cols));
    int idx = 0;

    // fill columns by key order
    for (int k = 0; k < order.size(); k++) {
        int col = order[k];
        for (int r = 0; r < rows; r++)
            mat[r][col] = cipher[idx++];
    }

    // read row-wise to get plaintext
    string plain = "";
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            plain += mat[r][c];

    return plain;
}

int main() {
    string text, key;

    cout << "Enter plaintext: ";
    getline(cin, text);

    cout << "Enter key: ";
    getline(cin, key);

    string enc = encrypt(text, key);
    string dec = decrypt(enc, key);

    cout << "\nEncrypted: " << enc << endl;
    cout << "Decrypted: " << dec << endl;

    return 0;
}
