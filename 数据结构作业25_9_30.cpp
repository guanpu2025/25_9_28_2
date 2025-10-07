#include <bits/stdc++.h>
using namespace std;

struct Node{
    int val;
    Node* left;
    Node* right;
    Node(int a): val(a),left(nullptr), right(nullptr){}
};

int n, value, father, l_or_r;
Node* point;

void find_father(Node* root, int v){
    if(root ->val == v){
        point = root;
    }
    else{
        if(root ->left)
            find_father(root ->left, v);
        if(root ->right)
            find_father(root ->right, v);
    }
}

void front(Node* root){
    if(root != nullptr){
        cout << root ->val << " ";
        front(root ->left);
        front(root ->right);
    }
}

int main(){
    cin >> n;
    cin >> value >> father >> l_or_r;
    Node* root = new Node(value);
    for(int i = 0; i < n - 1; i++){
        cin >> value >> father >> l_or_r;
        Node* cur = new Node(value);
        find_father(root, father);
        if(l_or_r == -1){
            point ->left = cur;
        }
        else{
            point ->right = cur;
        }
    }
    front(root);
    return 0;
}
/*
第四题
stack<int>a;
queue<int>b;
int n, flag = 1;
string line1, line2;

int main(){
    cin >> n;
    cin.ignore();
    getline(cin, line1);
    istringstream is1(line1);

    getline(cin, line2);
    istringstream is2(line2);
    int y;
    while(is2 >> y){
        b.push(y);
    }

    int x;
    while(is1 >> x){
        a.push(x);
        if(a.size() > n){
            flag = 0;
            break;
        }
        while(!a.empty() && !b.empty() && a.top() == b.front()){
            a.pop();
            b.pop();
        }
    }

    if(flag == 1 && a.empty() && b.empty()){
        cout << "yes" << endl;
    }
    else{
        cout << "no" << endl;
    }
    return 0;
}*/
/*
第三题
stack<int> a;
int n, num, flag = 1;
char work;
int c;

int main(){
    cin >> n;
    if(n != 0){
        for(int i = 0; i < n; i++){
            int x;
            cin >> x;
            a.push(x);
        }
    }
    cin >> num;
    for(int i = 0; i < num; i++){
        cin >> work >> c;
        if(work == 'i'){
            a.push(c);
        }
        else{
            if(c > a.size()){
                flag = 0;
                break;
            }
            else{
                for(int i = 0; i < c; i++){
                    a.pop();
                }
            }   
        }
    }
    if(flag == 0){
        cout << "FAIL" << endl;
    }
    else if(a.empty()){
        cout << "-1" << endl;
    }
    else{
        while(!a.empty()){
            cout << a.top() << " ";
            a.pop();
        }
    }
    return 0;
}*/
/*
第二题
int n, num;
queue<int> car;

int main(){
    cin >> n >> num;
    for(int i = 0; i < num; i++){
        int x;
        cin >> x;
        car.push(x);
    }
    if(num > n){
        for(int i = 0; i < (num - n); i++){
            car.pop();
        }
    }
    int max_car = 0;
    for(int i = 0; i < n; i++){
        if(max_car < car.front()){
            max_car = car.front();
        }
        car.pop();
    }
    cout << max_car << endl;
    return 0;
}*/
/*
第一题
int n;
queue<int> a;
char work;
int num = 0;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        a.push(x);
    }
    int flag = 1;//是否合法
    cin >> work >> num;
    if(work == 'i'){
        for(int i = 0; i < num; i++){
            int x;
            cin >> x;
            a.push(x);
        }
    }
    else{
        for(int i = 0; i < num; i++){
            int x;
            cin >> x;
            int cur = a.front();
            if(x != cur){
                flag = 0;
            }
            a.pop();
        }
    }
    if(flag == 1){
        cout << a.size() << endl;
    }
    else{
        cout << "FAIL" << endl;
    }
    return 0;
}*/
