#include <bits/stdc++.h>
using namespace std;

 
string a;
struct Node{
    char val;
    Node* left;
    Node* right;
    Node(char m):val(m), left(nullptr), right(nullptr){}
};

int i = 0;
char read(){
    if(i >= a.length()){
        return '*';
    }
    return a[i++];
}

void build(Node* &node){
    char now = read();
    if(now == '#'){
        node = nullptr;
        return;
    }
    else{
        node = new Node(now);
        build(node ->left);
        build(node ->right);
    }
}

void find_father(Node* point, Node* to_find){
    if(point == nullptr || to_find == nullptr){
        return;
    }
    if(point ->left == to_find || point ->right == to_find){
        cout << point ->val;
        return;
    }
    else{
        find_father(point ->left, to_find);
        find_father(point ->right, to_find);
    }
}
int main(){
    cin >> a;
    Node* root = new Node('*');
    build(root);
    find_father(root, root ->left ->left);
    return 0;
}

/*void front(Node* root){
    if(root == nullptr){
        return;
    }
    else{
        cout << root ->val;
        front(root ->left);
        front(root ->right);
        return;
    }
}*/
/*#define INF 1000000000
int n, m, x[110], a[110];
long long f[110][110][20], ff[110][110][20];//从i到j分成k段，f是最小，ff是最大

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> x[i];
        if(i == 1){
            a[i] = x[i];
        }
        else{
            a[i] = a[i - 1] + x[i];
        }
    }

    for(int i = n + 1; i <= 2 * n; i++){//变成长度为2n的链
        x[i] = x[i - n];
        a[i] = a[i - 1] + x[i];
    }

    for(int i = 1; i <= 2 * n; i++){
        for(int j = 1; j <= 2 * n; j++){
            for(int k = 0; k <= 20; k++){
                f[i][j][k] = INF;
            }
        }
    }

    for(int i = 1; i <= 2 * n; i++){
        for(int j = i; j <= 2 * n; j++){
            f[i][j][1] = (a[j] - a[i - 1] + INF) % 10;
            ff[i][j][1] = (a[j] - a[i - 1] + INF) % 10;
        }
    }

    for(int i = 1; i <= 2 * n; i++){
        for(int j = i + 1; j <= 2 * n; j++){
            for(int k = 2; k <= m; k++){
                for(int duan = i; duan < j; duan++){
                    f[i][j][k] = min(f[i][j][k], f[i][duan][k - 1] * f[duan + 1][j][1]);
                    ff[i][j][k] = max(ff[i][j][k], ff[i][duan][k - 1] * ff[duan + 1][j][1]);
                }
            }
        }
    }
    long long max1 = 0, min1 = INF;

    for(int i = 1; i <= n; i++){
        max1 = max(ff[i][i + n - 1][m], max1);
        min1 = min(f[i][i + n - 1][m], min1);
    }
    cout << min1 << endl << max1 << endl;
    return 0;
}*/
/*int a, n, m, x, ans;
int k;//k是第二站上下人数

int fei(int p){
    if(p == 1 || p == 2){
        return 1;
    }
    else{
        return(fei(p - 1) + fei(p - 2));
    }
}

int fei_he(int q){
    if(q == 1){
        return 1;
    }
    else{
        return fei(q) + fei_he(q - 1);
    }
}

int main(){
    cin >> a >> n >> m >> x;
    if(n <= 3){
        k = m;
    }
    else{
        k = (m - a)/fei(n - 2);
    }
    if(x <= 2){
        ans = a;
    }
    else if(x == 3){
        ans = 2 * a;
    }
    else{
        ans = a * 2 + k * fei_he(x - 3);
    }
    cout << ans;
    return 0;
}*/
/*int n, m, w, father[10010], dp[10010];

struct yun{
    int money, value;
}y[10010];

int main(){
    cin >> n >> m >> w;
    for(int i = 0; i < n; i++){
        cin >> y[i].money >> y[i].value;
        father[i] = i;
    }
    for(int i = 0; i < m; i++){
        int temp1, temp2;
        cin >> temp1 >> temp2;
        temp1--;
        temp2--;
        if(y[temp2].money == 0 && y[temp1].money == 0){
            continue;
        }
        if(y[temp2].money == 0){
            int t = temp1;
            temp1 = temp2;
            temp2 = t;
        }

        while(father[temp1] != temp1){
            temp1 = father[temp1];
        }
        father[temp2] = temp1;
        y[temp1].money += y[temp2].money;
        y[temp1].value += y[temp2].value;
        y[temp2].money = 0;
        y[temp2].value = 0;
        /*cout << endl;
        for(int i = 0; i < n; i++){
            cout << y[i].money << " " << y[i].value << endl;
        } */
    /* }
    
    for(int i = 0; i < n; i++){
        for(int j = w; j >= y[i].money; j--){
            dp[j] = max(dp[j], dp[j - y[i].money] + y[i].value);
        }
    }
    cout << dp[w];
    return 0;
}*/
/*string n;
long long k, ans = 1;
long long kebian[10], m[10][10];

int main(){
    cin >> n >> k;
    for(int i = 0; i < k; i++){
        int a, b;
        cin >> a >> b;
        if(m[a][b] == 0){
            kebian[a]++;
            m[a][b] = 1;
        }
    }
    
    for(int i = 0; i < n.size(); i++){
        ans *= (kebian[n[i] - '0'] + 1);
    }
    cout << ans;
    return 0;
}*/

/*int n, ans = -1;

struct capital{
    int a, b, g, k;
}c[10010];

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> c[i].a >> c[i].b >> c[i].g >> c[i].k;
    }
    int p, q;
    cin >> p >> q;
    for(int i = 1; i <= n; i++){
        if(p >= c[i].a && p <= c[i].a + c[i].g && q >= c[i].b && q <= c[i].b + c[i].k){
            ans = i;
        }
    }
    cout << ans;
    return 0;
}*/
/*long long n, c, ans;
long long fama[1010], pre[1010];

void dfs(long long cur, int index){
    if(cur > c || index < 0 || pre[index] + cur < ans){
        return;
    }
    ans = max(ans, cur);
    dfs(cur + fama[index], index - 1);
    dfs(cur, index - 1);
}
int main(){
    cin >> n >> c;
    for(int i = 1; i <= n; i++){
        cin >> fama[i];
        pre[i] = pre[i - 1] + fama[i];
        if(fama[i] > c){
            n = i;
            break;
        }
    }
    dfs(0, n);
    cout << ans;
    return 0;
}*/
/*int n, m, t, startx, starty, endx, endy;
char a[101][101];
long long dp[101][101][20];
int dirx[4] = {0 , 0, 1, -1};
int diry[4] = {1, -1, 0, 0};

int main(){
    cin >> n >> m >> t;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            cin >> a[i][j];
        }
    }
    cin >> startx >> starty >> endx >> endy;

    dp[startx][starty][0] = 1;

    for(int tt = 1; tt <= t; tt++){
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(a[i][j] == '*'){
                    dp[i][j][tt] = 0;
                }
                else{
                    dp[i][j][tt] = dp[i - 1][j][tt - 1] + dp[i][j - 1][tt - 1] + dp[i + 1][j][tt - 1] + dp[i][j + 1][tt - 1];
                }
            }
        }
    }
    cout << dp[endx][endy][t];
    return 0;
}*/
/*int n, m, t, startx, starty, endx, endy;
char a[101][101];
int memory[101][101][20];
int dirx[4] = {0 , 0, 1, -1};
int diry[4] = {1, -1, 0, 0};

void dfs(int x, int y, int ti){
    if(ti > t){
        return;
    }
    for(int i = 0; i < 4; i++){
        int xx = x + dirx[i], yy = y + diry[i];
        if(xx >= 0 && xx < n && yy >= 0 && yy < m && a[xx][yy] != '*' && ti + 1 <= t){
            if(memory[xx][yy][ti + 1] == -1){
                memory[xx][yy][ti + 1] = memory[x][y][ti];
                dfs(xx, yy, ti + 1);
            }
            else{
                memory[xx][yy][ti + 1] += memory[x][y][ti];
                dfs(xx, yy, ti + 1);
            }
        }
    }
}
int main(){
    cin >> n >> m >> t;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    cin >> startx >> starty >> endx >> endy;
    memset(memory, -1, sizeof(memory));
    memory[startx - 1][starty - 1][0] = 1;
    dfs(startx - 1, starty - 1, 0);
    cout << memory[endx - 1][endy - 1][t];
    return 0;
}*/
/*int h[101][101], m, n;
int dirx[4] = {0 , 0, 1, -1};
int diry[4] = {1, -1, 0, 0};
int memory[101][101];

int dfs(int a, int b){
    if(memory[a][b] != 0){
        return memory[a][b];
    }
    memory[a][b] = 1;
    for(int i = 0; i < 4; i++){
        int xx = a + dirx[i], yy = b + diry[i];
        if(xx >= 0 && xx < m && yy >= 0 && yy < n && h[xx][yy] < h[a][b]){
            memory[a][b] = max(memory[a][b], dfs(xx, yy) + 1);
        }
    }
    return memory[a][b];
}

int main(){
    int ans = 0;
    cin >> m >> n;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cin >> h[i][j];
        }
    }
    memset(memory, 0, sizeof(memory));

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            ans = max(ans, dfs(i, j));
        }
    }
    cout << ans;
    return 0;
}*/
/*int v[10][10], st[10][10];
int dirx[4] = {0, 0, 1, -1};
int diry[4] = {1, -1, 0, 0};
int ans;

int bfs(int sx, int sy, int ex, int ey){
    if(sx == ex && sy == ey){
        return st[ex][ey];
    }
    queue<pair<int, int>>q;
    q.push({sx, sy});
    while(!q.empty()){
        int xx = q.front().first, yy = q.front().second;
        v[xx][yy] = 1;
        q.pop();
        for(int i = 0; i < 4; i++){
            int mx = xx + dirx[i], my = yy + diry[i];
            if(mx > 0 && mx <= 8 && my > 0 && my <= 8 && v[mx][my] == 0){
                q.push({mx, my});
                st[mx][my] = st[xx][yy] + 1; 
            }
        }
    }
}

int main(){
    int sx, sy, ex, ey;
    string s, e;
    while(scanf("%s %s", &s, &e) != EOF){
        sx = s[1] - '0';
        sy = s[0] - 'a' + 1;
        ex = e[1] - '0';
        ey = s[0] - 'a' + 1;
        memset(v, 0, sizeof(v));
        memset(st, 0, sizeof(st));
        bfs(sx, sy, ex, ey);
        printf("To get from %s to %s takes %d knight moves.\n", s, e, bfs(sx, sy, ex, ey));
    }
    return 0;
}*/
/*int n;
char b[101];

int main(){
    cin >> n;
    cin >> b;
    for(int i = 0; i < n; i++){
        int opt;
        cin >> opt;
        if(opt == 1){
            char in[101];
            cin >> in;
            strcat(b, in);
            cout << b << endl;
        }
        else if(opt == 2){
            int begin, end;
            char in[101];
            cin >> begin >> end;
            b[begin + end] = '\0';
            strcpy(in, &b[begin]);
            strcpy(b, in);
            cout << b << endl;
        }
        else if(opt == 3){
            int a;
            char in[101];
            cin >> a >> in;
            strcat(in, &b[a]);
            b[a] = '\0';
            strcat(b, in);
            cout << b << endl;
        }
        else if(opt == 4){
            char in[101];
            char *ans = strstr(b, in);
			printf("%d\n", ans != NULL ? (int)(ans - b) : -1);
        }
    }
    return 0;
}*/
/*string web[1010], r[1010];
int wlen, rlen, ans, sec, result;
double kpm;

int main(){
    string s1;
    int n = 0;
    while(getline(cin, s1), s1 != "EOF"){
        n++;
        for(char a : s1){
            if(a == '<'){
                if(!web[n].empty()){
                    web[n].pop_back();
                }
            }
            else{
                web[n].push_back(a);
            }
        }
    }
    wlen = n;
    int m = 0;
    while(getline(cin, s1), s1 != "EOF"){
        m++;
        if(m > n){
            break;
        }
        for(char a : s1){
            if(a == '<'){
                if(!r[m].empty()){
                    r[m].pop_back();
                }
            }
            else{
                r[m].push_back(a);
            }
        }
        for(int i = 0; i < min(web[m].size(), r[m].size()); i++){
            if(web[m][i] == r[m][i]){
                ans++;
            }
        }
    }
    cin >> sec;
    result = (ans * 60.0 / sec) + 0.5;
    cout << result;
    return 0;
}*/
/*#define MAX 100000000
int n, a[110], dp_min[110][110], dp_max[110][110];

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        dp_min[i][i] = dp_max[i][i] = a[i];
    }
    memset(dp_min, MAX, sizeof(dp_min));
    for(int len = 2; len <= n; len++){
        for(int i = 0; i < n - len + 1; i++){
            for(int j = i; j < i + len - 1; j++){
                dp_min[i][i + len - 1] = min(dp_min[i][i + len - 1], dp_min[i][j] + dp_min[j + 1][i + len - 1]);
                dp_max[i][i + len - 1] = max(dp_max[i][i + len - 1], dp_max[i][j] + dp_max[j + 1][i + len - 1]);
            }
        }
    }
    cout << dp_min[0][n - 1] <<endl << dp_max[0][n - 1];
    return 0;
}*/
/*#define MOD 100000000
long long n, f, ans;
long long a[2020], dp[1000105];

int main(){
    cin >> n >> f;
    for(long long i = 0; i < n; i++){
        cin >> a[i];
    }
    dp[0] = 1;
    for(long long i = 0; i < n; i++){
        for(long long j = 500 * f; j >= a[i]; j--){
            dp[j] = (dp[j] + dp[j - a[i]]) % MOD;
        }
    }
    for(long long i = f; i <= 500 * f; i += f){
        ans = (ans + dp[i]) % MOD;
    }
    cout << ans % MOD;
    return 0;
}*/
/*int m, n, k[105], dp[1010], zushu;
struct xiaozu{
    int w, v;
}zu[105][1010];//第几组第几个物品；注意，按照下面代码，没有第0个物品

struct wupin{
    int weight, value, belong;
}thing[1010];

int main(){
    cin >> m >> n;
    for(int i = 0; i < n; i++){
        cin >> thing[i].weight >> thing[i].value >> thing[i].belong;
        zu[thing[i].belong][++k[thing[i].belong]].w = thing[i].weight;
        zu[thing[i].belong][k[thing[i].belong]].v = thing[i].value;
    }
    for(int i = 0; i < 105; i++){//枚举所有组
        if(k[i]){//这组不是空的
            for(int p = m; p >= 0; p--){//先枚举总重
                for(int j = 1; j <= k[i]; j++){//再枚举组里所有物品
                    if(p >= zu[i][j].w)
                        dp[p] = max(dp[p], dp[p - zu[i][j].w] + zu[i][j].v);
                }
            }
        }
    }
    cout << dp[m] << endl;
    return 0;
}*/
/*int t;

int main(){
    cin >> t;
    while(t--){
        int n, ans;
        cin >> n;
        vector<int> a(n);   
        ans = n;
        vector<int>dp(25001, 0);
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        dp[0] = 1;
        sort(a.begin(), a.end());
        for(int i = 0; i < n; i++){
            if(dp[a[i]]){
                ans--;
                continue;
            }
            for(int j = a[i]; j <= a[n - 1]; j++){
                dp[j] += dp[j - a[i]];
            }
        }
        cout << ans << endl;
    }
    return 0;
}*/
/*int n, m, t, dp[210][210];

struct wish{
    int money, time;
}w[110];

int main(){
    cin >> n >> m >> t;
    for(int i = 0; i < n; i++){
        cin >> w[i].money >> w[i].time;
    }
    for(int i = 0; i < n; i++){
        for(int j = m; j >= w[i].money; j--){
            for(int k = t; k >= w[i].time; k--){
                dp[j][k] = max(dp[j][k], dp[j - w[i].money][k - w[i].time] + 1);
            }
        }
    }
    cout << dp[m][t];
    return 0;
}*/
/*int n, ans, v[21];
string a[21];
char h;

void dfs(string t){
    ans = max(ans, int(t.size()));
    for(int i = 0; i < n; i++){
        if(v[i] >= 2)continue;
        for(int j = 1; j < min(a[i].size(), t.size()); j++){
            if(t.substr(t.size() - j) == a[i].substr(0, j)){
                v[i]++;
                dfs(t + a[i].substr(j));
                v[i]--;
            }
        }
    }
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    cin >> h;
    for(int i = 0; i < n; i++){
        if(a[i][0] == h){
            v[i]++;
            dfs(a[i]);
            v[i]--;
        }
    }
    cout << ans;
    return 0;
}*/
/*int a[110][110], s[110][110], n, m, ans;

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            cin >> a[i][j];
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j];
        }
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(!a[i][j])continue;
            for(int p = i, q = j; p <= n && q <= m; p++, q++){
                if(!a[p][q])break;
                int t = s[p][q] - s[i - 1][q] - s[p][j - 1] + s[i - 1][j - 1];
                if(t == pow((p - i + 1), 2)){
                    ans = max(ans, (p - i + 1));
                }
            }
        }
    }
    cout << ans;
    return 0;
}*/
/*int n, m;
int a[1010][1010];

int main(){
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for(int p = x1; p <= x2; p++){
            for(int q = y1; q <= y2; q++){
                a[p][q]++;
            }
        }
        
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}*/
/*int n, m, ans;
int s[5010][5010];

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        int tx, ty, ts;
        cin >> tx >> ty >> ts;
        s[tx + 1][ty + 1] = ts;
    }
    for(int i = 1; i <= 5001; i++){
        for(int j = 1; j <= 5001; j++){
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + s[i][j];//这里包含边了
        }
    }
    for(int i = m; i <= 5001; i++){
        for(int j = m; j <= 5001; j++){
            int r = s[i][j] - s[i - m][j] - s[i][j - m] + s[i - m][j - m];//这里实际上把左下两条边和除了右上的三个角都剪掉了
            ans = max(r, ans);
        }
    }
    cout << ans << endl;
    return 0;
}*/
/*char a[10];
bool f = true;
int main(){
    int j = 0;
    while(char t = getchar()){
        if(t != '\n'){
            a[j] = t;
            j++;
        }
        else{
            break;
        }
    }
    vector<int>aa(j);
    vector<int>bb(j);

    for(int i = j - 1; i >= 0; i--){
        if(a[i] == 'Z' && i != j - 1 && a[i + 1] != 'Z'){
            f = false;
            break;
        }
        if(a[i] == 'Z'){
            aa[i] = bb[i] = 0;
        }
        if(a[i] == 'X'){
            aa[i] = 8;
            bb[i] = 7;
        }
        if(a[i] == 'Y'){
            aa[i] = 6;
            bb[i] = 7;
        }
    }

    if(!f){
        cout << "-1";
    }
    else{
        for(int i = 0; i < j; i++){
            cout << aa[i];
        }
        cout << endl;
        for(int i = 0; i < j; i++){
            cout << bb[i];
        }
    }
    return 0;
}*/
/*int n, f, ans;
int a[50005], first[7], last[7];

int main(){
    cin >> n;
    memset(first, -1, sizeof(first));
    first[0] = 0;
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        if(i != 0)a[i] += a[i - 1];
        if(first[a[i] % 7] == -1){
            first[a[i] % 7] = i;
        }
        last[a[i] % 7] = i;
        ans = max(ans, last[a[i] % 7] - first[a[i] % 7]);
    }
    cout << ans;
    return 0;
}*/
/*int n, m[505][505];
int ans;

int main(){
    cin >> n;
    for(int i = 0; i < n - 1; i++){
        for(int j = i + 1; j < n; j++){
            cin >> m[i][j];
            m[j][i] = m[i][j];
        }
    }
    for(int i = 0; i < n; i++){
        sort(m[i], m[i] + n);
        ans = ans > m[i][n - 2] ? ans : m[i][n - 2];
    }
    cout << "1" << endl << ans << endl;
    return 0;
}*/
/*long long n, m, ans;

struct milk{
    int price, mount;
}mi[50002];

bool cmp(milk a, milk b){
    return a.price <= b.price;
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        cin >> mi[i].price >> mi[i].mount;
    }
    sort(mi, mi + m, cmp);
    for(int i = 0; i < m; i++){
        if(n > mi[i].mount){
            ans += mi[i].price * mi[i].mount;
            n -= mi[i].mount;
        }
        else if(n <= mi[i].mount){
            ans += mi[i].price * n;
            break;
        }
    }
    cout << ans;
    return 0;
}*/
/*int gongbeishu(int a, int b){
    for(int i = min(a, b); i <= a * b; i++){
        if(i % a == 0 && i % b == 0){
            return i;
        }
    }
}

int main(){
    int a, b;
    cin >> a >> b;
    cout << gongbeishu(a, b) << endl;
    return 0;
}*/
/*int num;
int b[13][40];
int main()
{
  int a[100]={5,6,8,6,9,1,6,1,2,4,9,1,9,8,2,3,6,4,7,7,5,9,5,0,3,8,7,5,8,1,5,8,6,1,8,3,0,3,7,9,2,7,0,5,8,8,5,7,0,9,9,1,9,4,4,6,8,6,3,3,8,5,1,6,3,4,6,7,0,7,8,2,7,6,8,9,5,6,5,6,1,4,0,1,0,0,9,4,8,0,9,1,2,8,5,0,2,5,3,3};
  int month[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
  for(int i=0;i<100;i++)
  {
    if(a[i]==2)
    {
      for(int j=i+1;j<100;j++)
      {
        if(a[j]==0)
        {
          for(int k=j+1;k<100;k++)
          {
            if(a[k]==2)
            {
              for(int l=k+1;l<100;l++)
              {
                if(a[l]==3)
                {
                  for(int m=l+1;m<100;m++)
                  {
                    if(a[m]<=1)
                    {
                      for(int n=m+1;n<100;n++)
                      {
                        if((a[m]==1&&a[n]<=2)||(a[m]==0&&a[n]>=1))
                        {
                            for(int l=n+1;l<=100;l++)
                            {
                                int mon=a[m]*10+a[n];
                                for(int o=l+1;o<100;o++)
                                {
                                  int day=a[l]*10+a[o];
                                  if(day>0&&day<=month[mon]&&b[mon][day]==0)
                                  {
                                    num++;
                                    b[mon][day]=1;
                                  }

                                }
                            }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  cout<<num;
  return 0;
}*/

/*double h;
int len = 23333333, ans;

int main(){
    for(int i = 0; i <= len / 2; i++){
        double a = static_cast<double>(i) / len, b = 1 - a;
        h = - a * i * log2(a) - b * (len - i) * log2(b);
        long long h0 = h * 10000, r = 116259075798;
        if(h0 == r){
            ans = i;
            break;
        }
    }
    cout << ans;
    return 0;
}*/

/*int n, m, ans, num = 0;
int pre[100001];

struct road{
    int x, y ,t;
}r[100001];

bool cmp(road a, road b){
    return a.t <= b.t;
}

int find_fa(int a){
    if(pre[a] == a){
        return a;
    }
    else{
        return find_fa(pre[a]);
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        cin >> r[i].x >> r[i].y >> r[i].t;
    }
    sort(r, r + m, cmp);
    for(int i = 1; i <= n; i++){
        pre[i] = i;
    }
    for(int i = 0; i < m; i++){
        int x = find_fa(r[i].x);
        int y = find_fa(r[i].y);
        if(x == y)continue;
        else{
            pre[x] = y;
            num++;
            ans = max(ans, r[i].t);
        }
    }
    if(num != n - 1){
        cout << "-1";
    }
    else
        cout << ans;
    return 0;
}*/
/*int n;

void dfs(int n){
    if(n == 0){
        return;
    }
    if(n == 1){
        cout << "2(0)";
        return;
    }
    if(n == 2){
        cout << "2";
        return;
    }
    int i = 0;
    while(pow(2, i) <= n){
        i++;
    }
    i--;
    cout << "2";
    if(i > 1){
        cout << "(";
        dfs(i);
        cout << ")";
    }
    n -= pow(2, i);
    if(n != 0){
        cout << "+";
    }
    dfs(n);
    
}
int main(){
    cin >> n;
    dfs(n);
    return 0;
}*/
/*int main(){
    long long a, b, p, r = 1, aa, bb;
    cin >> a >> b >> p;
    aa = a;
    bb = b;
    while(b){
        if(b % 2 == 1){
            b -= 1;
            r = a * r % p;
        }
        a = a * a % p;
        b /= 2;
    }
    cout << aa << "^" << bb << " mod " << p << "=" << r % p;
    return 0;
}*/
/*int t, n, m, ans, ans1;
int a[10][10], v[10][10];

void dfs(int hang, int lie){//即将考虑第几行第几列
    if(hang <= 0 || lie <= 0){
        return;
    }
    if(hang > n){
        ans = max(ans, ans1);
        return;
    }
    if(lie > m){
        dfs(hang + 1, 1);
    }
    if(v[hang][lie] != 0){
        dfs(hang, lie + 1);
        return;
    }
    ans1 += a[hang][lie];
    v[hang][lie] = 1;
    if(hang - 1 > 0)v[hang - 1][lie] = 1;
    if(hang + 1 <= n)v[hang + 1][lie] = 1;
    
    if(lie + 1 <= m)v[hang][lie + 1] = 1;
    if(lie - 1 > 0)v[hang][lie - 1] = 1;
    dfs(hang, lie + 1);
    ans1 -= a[hang][lie];
    v[hang][lie] = 0;
    if(hang - 1 > 0)v[hang - 1][lie] = 0;
    if(hang + 1 <= n)v[hang + 1][lie] = 0;
    if(lie + 1 <= m)v[hang][lie + 1] = 0;
    if(lie - 1 > 0)v[hang][lie - 1] = 0;
    dfs(hang, lie + 1);
}
int main(){
    cin >> t;
    for(int k = 0; k < t; k++){
        cin >> n >> m;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                cin >> a[i][j];
            }
        }
        dfs(1, 1);
        cout << ans << endl;
        memset(v, 0, sizeof(v)); 
        ans = 0;
        ans1 = 0;
    }
    return 0;
}*/
/*int n, m;
int a[1001][1001], result[100001], book[1001][1001];
int dirx[4] = {1, -1, 0, 0};
int diry[4] = {0, 0, 1, -1};

struct point{
    int x, y;
}p[100001];

bool hefa(int x, int y){
    if(x > 0 && x <= n && y > 0 && y <= n){
        return true;
    }
    else{
        return false;
    }
}
int bfs(int x, int y){
    if(book[x][y] != 0){
        return book[x][y];
    }
    bool v[1001][1001];
    int ans = 0;
    queue<pair<int, int>> q;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            v[i][j] = false;
        }
    }
    q.push({x, y});
    while(!q.empty()){
        int tx = q.front().first;
        int ty = q.front().second;
        q.pop();
        if(v[tx][ty] == true){
            continue;
        }
        v[tx][ty] = true;
        ans++;
        int txx, tyy;
        for(int i = 0; i < 4; i++){
            txx = tx + dirx[i];
            tyy = ty + diry[i];
            if(hefa(txx, tyy) && a[tx][ty] != a[txx][tyy] && v[txx][tyy] == false){
                q.push({txx, tyy});
            }
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(v[i][j]){
                    book[i][j] = ans;
                }
            }
        }
    }
    return ans;
}
int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        string t;
        cin >> t;
        for(int j = 1; j <= n; j++){
            a[i][j] = t[j - 1] - '0';
        }
    }
    for(int i = 0; i < m; i++){
        cin >> p[i].x >> p[i].y;
        result[i] = bfs(p[i].x, p[i].y);
        
    }
    for(int i = 0; i < m; i++){
        cout << result[i] << endl;
    }
    return 0;
}*/
/*int n, m;
int a[100009];
long long p[100009];

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    return 0;
}*/

/*int t;

int main(){
    cin >> t;
    for(int i = 0; i < t; i++){
        int n, a[1001], b[1001], m[1001], ans = 1e9;
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        for(int i = 0; i < n; i++){
            cin >> b[i];
            m[i] = a[i] * b[i];
            ans = min(ans, m[i]);
        }
        cout << ans << endl;
    }
    return 0;
}*/
/*int n, m, k;
long long a[201], b[201], c[201];
long long ans;

int main(){
    cin >> n >> m >> k;
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for(int i = 0; i < m; i++){
        scanf("%d", &b[i]);
    }
    for(int i = 0; i < k; i++){
        scanf("%d", &c[i]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            for(int p = 0; p < k; p++){
                long long t= (a[i] * b[j]) % c[p];
                ans = max(ans, t);
            }
        }
    }
    cout << ans << endl;
    return 0;
}*/
/*bool is_chuxian[100];
long long ans = 0;

int zhi(long long a, long long b){
    while(a >= 10){
        a /= 10;
    }
    while(b >= 10){
        b /= 10;
    }
    return a * b;
}

int main(){
    for(int i = 0; i < 100; i++){
        is_chuxian[i] = false;
    }

    for(int i = 1; i < 2000; i++){
        long long a = pow(2, i), b = pow(5, i);
        long long t = zhi(a, b);
        if(is_chuxian[t] == false){
            ans += t;
            is_chuxian[t] = true;
        }
    }
    cout << ans;
    return 0;
}*/
/*int c  = 0;

bool runnian(int y){
    if((y % 4 == 0 && y % 100 != 0) || y % 400 == 0){
        return true;
    }
    else return false;
}
int main(){
    for(int i = 2026; i < 2116; i++){
        if(runnian(i)){
            c++;
        }
    }
    cout << (26 * 366 + 64 * 365 + 274);//33150
    return 0;
}*/
/*struct point{
    int x, y, v;
};

int n, m;
point p[10001];

bool cmp1(point a, point b){
    return a.x < b.x;
}

bool cmp2(piont a, point b){
    return a.y < b.y;
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> p[i].x >> p[i].y >> p[i].v;
    }
    sort(p, p + n, cmp1);
    
    return 0;
}*/
/*double x1, x2, x3;
double a, b, c, d, num;
double l, r;

double f(double x){
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d;
}
int main(){
    cin >> a >> b >> c >> d;
    for(int i = -100; i < 100; i++){
        l = (double)i;
        r = (double)(i + 1);
        if(f(l) == 0){
            printf("%.2lf ", l);
            num++;
        }
        if(f(l) * f(r) < 0){
            while(r - l >= 0.001){
                double middle = (r + l) / 2;
                if(f(middle) * f(l) < 0){
                    r = middle;
                }
                else{
                    l = middle;
                }
            }
            printf("%.2lf ", r);
            num++;
        }
        if(num == 3){
            break;
        }
    }
    return 0;
}*/
/*int n, k, ans, a[8];

void dfs(int m, int i){//m：还剩多少没分,i：分到第多少份
    if(m == 0 && i == k + 1){
        ans++;
        return;
    }
    if(i > k + 1 || m < (k - i + 1)){
        return;
    }
    for(int j = a[i - 1]; j <= m;j++){
        if(m - j < k - i){
            break;
        }
        a[i] = j;
        dfs(m - j, i + 1);
    }
}

int main(){
    cin >> n >> k;
    a[0] = 1;
    dfs(n, 1);
    cout << ans;
    return 0;
}*/
/*int n, t, m, ans = 0;
int ti[30];

void dfs(int die, int left, int song, int used){//第几张碟片，这张碟片剩多长时间，第几首歌，已经放进去几首歌了
    if(die >= m || song >= n){
        ans = max(ans, used);
        return;
    }
    dfs(die, left, song + 1, used);
    if(ti[song] < left){
        dfs(die, left - ti[song], song + 1, used + 1);
    }
    else if(ti[song] == left){
        dfs(die + 1, t, song + 1, used + 1);
    }
    else{
        dfs(die + 1, t, song, used);
    }
}
int main(){
    cin >> n >> t >> m;
    for(int i = 0; i < n; i++){
        cin >> ti[i];
    }
    dfs(0, t, 0, 0);
    cout << ans << endl;
    return 0;
}*/
/*int main(){
    
    int a,b,c,d,e,f,g,h,i,j,in,x=0;  
    cin>>in;  
    for (a=1;a<=3;a++)  
    {  
        for (b=1;b<=3;b++)  
        {  
            for (c=1;c<=3;c++)  
            {  
                for (d=1;d<=3;d++)  
                {  
                    for (e=1;e<=3;e++)  
                    {  
                        for (f=1;f<=3;f++)  
                        {  
                            for (g=1;g<=3;g++)  
                            {  
                                for(h=1;h<=3;h++)  
                                {  
                                    for (i=1;i<=3;i++)  
                                    {  
                                        for (j=1;j<=3;j++)  
                                        {  
                                            if (a+b+c+d+e+f+g+h+i+j==in)  
                                            {  
                                                x++;  
                                            }  
                                        }  
                                    }  
                                }  
                            }  
                        }  
                    }  
                }  
            }  
        }  
    }  
    cout<<x<<endl;  
    for (a=1;a<=3;a++)  
    {  
        for (b=1;b<=3;b++)  
        {  
            for (c=1;c<=3;c++)  
            {  
                for (d=1;d<=3;d++)  
                {  
                    for (e=1;e<=3;e++)  
                    {  
                        for (f=1;f<=3;f++)  
                        {  
                            for (g=1;g<=3;g++)  
                            {  
                                for(h=1;h<=3;h++)  
                                {  
                                    for (i=1;i<=3;i++)  
                                    {  
                                        for (j=1;j<=3;j++)  
                                        {  
                                            if (a+b+c+d+e+f+g+h+i+j==in)  
                                            {  
                                                cout<<a<<" ";  
                                                cout<<b<<" ";  
                                                cout<<c<<" ";  
                                                cout<<d<<" ";  
                                                cout<<e<<" ";  
                                                cout<<f<<" ";  
                                                cout<<g<<" ";  
                                                cout<<h<<" ";  
                                                cout<<i<<" ";  
                                                cout<<j<<endl;  
                                            }  
                                        }  
                                    }  
                                }  
                            }  
                        }  
                    }  
                }  
            }  
        }  
    }  
  
    return 0;
}*/
/*struct node{
    int x, y, w, col;
    bool magic;
    bool operator<(const node& o) const { return w > o.w; }
};

int m, n, ans = 1e9;
int color[110][110], a[110][110];
priority_queue<node>q;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main(){
    cin >> m >> n;
    memset(color, -1, sizeof(color));
    memset(a, 0x3f, sizeof(a));
    for(int i = 1; i <= n; i++){
        int t1, t2, t3;
        cin >> t1 >> t2 >> t3;
        color[t1][t2] = t3;
    }
    a[1][1] = 0;
    q.push({1, 1, 0, color[1][1], 0});
    while(!q.empty()){
        node z = q.top();
        q.pop();
        if(z.w > a[z.x][z.y]) continue;
        if(z.x == m && z.y == m){
            ans = z.w;
            break;
        }
        for(int i = 0; i < 4; i++){
            int nx = z.x + dx[i], ny = z.y + dy[i];
            if(nx < 1 || nx > m || ny < 1 || ny > m || (z.magic == 1 && color[nx][ny] == -1)){
                continue;
            }
            if(z.magic == 0){
                if(color[nx][ny] != -1){
                    if(z.col == color[nx][ny]){
                        if(a[nx][ny] > z.w){
                            a[nx][ny] = z.w;
                            q.push({nx, ny, a[nx][ny], color[nx][ny], 0});
                        }
                        
                    }
                    else{
                        if(a[nx][ny] > z.w + 1){
                            a[nx][ny] = z.w + 1;
                            q.push({nx, ny, a[nx][ny], color[nx][ny], 0});
                        }
                    }
                }
                else{
                    if(a[nx][ny] > z.w + 2){
                        a[nx][ny] = z.w + 2;
                        q.push({nx, ny, a[nx][ny], z.col, 1});
                    }
                }
            }
            else{
                if(color[nx][ny] == z.col){
                    if(a[nx][ny] > z.w){
                        a[nx][ny] = z.w;
                        q.push({nx, ny, a[nx][ny], color[nx][ny], 0});
                    }
                }
                else{
                    if(a[nx][ny] > z.w + 1){
                        a[nx][ny] = z.w + 1;
                        q.push({nx, ny, a[nx][ny], color[nx][ny], 0});
                    }
                }
            }
        }
    }
    cout << (ans == 1e9 ? -1 : ans);
    return 0;
}*/
/*int main(){
    cin >> m >> n;
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= m; j++){
            color[i][j] = 2;
            v[i][j] = 0;
        }
    }
    for(int i = 0 ;i < n; i++){
        int tx, ty, c;
        cin >> tx >> ty >> c;
        color[tx][ty] = c;
    }
    q.push({1, 1, 0, 2});
    v[1][1] = 1;
    while(!q.empty()){
        int x = get<0>(q.front()), y = get<1>(q.front()), cost = get<2>(q.front()), magic = get<3>(q.front());
        if (x == m && y == m) {
            ans = min(ans, cost);
            q.pop();
            continue;
        }
        q.pop();
        for(int i = 0; i < 4; i++){
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if(new_x > 0 && new_x <= m && new_y > 0 &&  new_y <= m && v[new_x][new_y] == 0){
                if(color[x][y] != 2 && color[x][y] == color[new_x][new_y]){
                    q.push({new_x, new_y, cost, 2});
                    v[new_x][new_y] = 1;
                }
                else if(color[x][y] != 2 && color[new_x][new_y] != 2 && color[x][y] != color[new_x][new_y]){
                    q.push({new_x, new_y, cost + 1, 2});
                    v[new_x][new_y] = 1;
                }
                else if(color[x][y] != 2 && color[new_x][new_y] == 2){
                    q.push({new_x, new_y, cost + 2, color[x][y]});
                    v[new_x][new_y] = 1;
                }
                else if(color[x][y] == 2 && color[new_x][new_y] != 2){
                    if(magic == color[new_x][new_y]){
                        q.push({new_x, new_y, cost, 2});
                        v[new_x][new_y] = 1;
                    }
                    else{
                        q.push({new_x, new_y, cost + 1, 2});
                        v[new_x][new_y] = 1;
                    }
                }
            }
        }
    }
    if(ans == 1e9){
        cout << "-1";
    }
    else{
        cout << ans;
    }
    return 0;
}*/
/*int m, n;
int color[110][111];
int momey[111][111], v[111][111];

void dfs(int x, int y){
    if(x == m && y == m){
        momey[m][m] = min(momey[m][m], momey[x][y]);
        return;
    }
    v[x][y] = 1;
    if((x + 1) <= m && !v[x + 1][y]){
        if((color[x][y] != 3 && color[x][y] == color[x + 1][y])){
            momey[x + 1][y] = min(momey[x + 1][y], momey[x][y]);
            dfs(x + 1, y);
            v[x + 1][y] = 0;
        }
        else if((color[x][y] == 0 && color[x + 1][y] == 1) || (color[x][y] == 1 && color[x + 1][y] == 0)){
            momey[x + 1][y] = min(momey[x + 1][y], momey[x][y] + 1);
            dfs(x + 1, y);
            v[x + 1][y] = 0;
        }
        else if(color[x][y] == 3 && color[x + 1][y] != 3){
            momey[x + 1][y] = min(momey[x + 1][y], momey[x][y] + 2);
            dfs(x + 1, y);
            v[x + 1][y] = 0;
        }
    }
    if((x - 1) >= 1 && !v[x - 1][y]){
        if((color[x][y] != 3 && color[x][y] == color[x - 1][y])){
            momey[x - 1][y] = min(momey[x - 1][y], momey[x][y]);
            dfs(x - 1, y);
            v[x - 1][y] = 0;
        }
        else if((color[x][y] == 0 && color[x - 1][y] == 1) || (color[x][y] == 1 && color[x - 1][y] == 0)){
            momey[x - 1][y] = min(momey[x - 1][y], momey[x][y] + 1);
            dfs(x - 1, y);
            v[x - 1][y] = 0;
        }
        else if(color[x][y] == 3 && color[x - 1][y] != 3){
            momey[x - 1][y] = min(momey[x - 1][y], momey[x][y] + 2);
            dfs(x - 1, y);
            v[x - 1][y] = 0;
        }
    }
    if((y - 1) >= 1 && !v[x][y - 1]){
        if((color[x][y] != 3 && color[x][y] == color[x][y - 1])){
            momey[x][y - 1] = min(momey[x][y - 1], momey[x][y]);
            dfs(x, y - 1);
            v[x][y - 1] = 0;
        }
        else if((color[x][y] == 0 && color[x][y - 1] == 1) || (color[x][y] == 1 && color[x][y - 1] == 0)){
            momey[x][y - 1] = min(momey[x][y - 1], momey[x][y] + 1);
            dfs(x, y - 1);
            v[x][y - 1] = 0;
        }
        else if(color[x][y] == 3 && color[x][y - 1] != 3){
            momey[x][y - 1] = min(momey[x][y - 1], momey[x][y] + 2);
            dfs(x, y - 1);
            v[x][y - 1] = 0;
        }
    }
    if((y + 1) <= m && !v[x][y + 1]){
        if((color[x][y] != 3 && color[x][y] == color[x][y + 1])){
            momey[x][y + 1] = min(momey[x][y + 1], momey[x][y]);
            dfs(x, y + 1);
            v[x][y + 1] = 0;
        }
        else if((color[x][y] == 0 && color[x][y + 1] == 1) || (color[x][y] == 1 && color[x][y + 1] == 0)){
            momey[x][y + 1] = min(momey[x][y + 1], momey[x][y] + 1);
            dfs(x, y + 1);
            v[x][y + 1] = 0;
        }
        else if(color[x][y] == 3 && color[x][y + 1] != 3){
            momey[x][y + 1] = min(momey[x][y + 1], momey[x][y] + 2);
            dfs(x, y + 1);
            v[x][y + 1] = 0;
        }
    }
    v[x][y] = 0;
}

int main(){
    cin >> m >> n;
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= m; j++){
            color[i][j] = 3;
            momey[i][j] = 1e9;
        }
    }
    momey[1][1] = 0;
    for(int i = 1; i <= n; i++){
        int ti, tj, t;
        cin >> ti >> tj;
        cin >> t;
        color[ti][tj] = t;
    }
    dfs(1, 1);
    if(momey[m][m] != 1e9)cout << momey[m][m];
    else cout << "-1";
    return 0;
}*/
/*int f[10000];
int a;

int main(){
    cin >> a;  
    for(int i = 1; i <= a; i++){
        for(int j = 1; j <= i / 2; j++){
            f[i] += f[j];
        }
        f[i]++;
    }
    cout << f[a];
    return 0;
}*/
/*string x;

void reverse(int a, int b){
    while(a < b){
        char temp = x[a];
        x[a] = x[b];
        x[b] = temp;
        a++;
        b--;
    }
}
int main(){
    int s = 0, e;
    cin >> x;
    e = x.size() - 1;
    if(x == "0"){
        cout << "0";
        return 0;
    }

    if(x[0] == '-'){
        s = 1;
    }
    while(x[e] == '0'){
        x[e] = '\0';
        e--;
    }

    reverse(s, e);
    cout << x;
    return 0;
}*/
/*int main(){
    int n, k = 0, i = 0;
    cin >> n;
    while(k < n){
        i++;
        k += i;
    }
    
    int z = n - (k - i);
    if(i % 2 == 0)
        cout << z << "/" << i - z + 1;
    else{
        cout << i - z + 1 << "/" << z;
    }
    
    return 0;
}*/
/*int main(){
    double k, i = 1;
    double n = 0.0;
    cin >> k;
    while(n <= k){
        double t = 1 / i;
        n += t;
        i++;
    }
    cout << i - 1;
    return 0;
}*/
/*int main(){
    int a[10], b[10], m = 0, ans;
    for(int i = 1; i < 8; i++){
        cin >> a[i] >> b[i];
        if(m < a[i] + b[i]){
            ans = i;
            m = a[i] + b[i];
        }
    }
    if(m <= 8){
        ans = 0;
    }
    cout << ans;
    return 0;
}*/
/*int main(){
    int cost[20];
    int mom = 0, jinjin = 0, ans = 0;

    for(int i = 1; i < 13; i++){
        cin >> cost[i];
    }
    for(int i = 1; i < 13; i++){
        jinjin += 300;
        jinjin -= cost[i];
        if(jinjin < 0){
            ans = 0 - i;
            break;
        }
        if(jinjin / 100 != 0){
            int give = (jinjin / 100) * 100;
            mom += give;
            jinjin -= give;
        }
    }
    if(ans == 0){
        ans = mom * 1.2 + jinjin;
    }
    cout << ans;
    return 0;
}*/
/*int n;
int a[3], b[3],res[3], ans = 1e9;

int main(){
    cin >> n;
    for(int i = 0; i < 3; i++){
        int temp;
        cin >> a[i] >> b[i];
        if(n % a[i] != 0){
            temp = n / a[i] + 1;
        }
        else temp = n / a[i];
        res[i] = temp * b[i];
        ans = min(ans, res[i]);
    }
    cout << ans;
    return 0;
}*/
/*long long mem[10000002], m;
long long fib(long long i){
    if(mem[i])return mem[i];
    if(i == 1 || i == 2)return mem[i] = 1;
    else return mem[i] = (mem[i - 2] + mem[i - 1]) % m;
}

int main(){
    cin >> m;
    int i = 2;
    while(!(fib(i) == 1 && fib(i - 1) == 0)){
        i++;
    }
    cout << i - 1;
    return 0;
}*/
/*int n, x, y, x2, y2;
int m[1010][1010], step[1010][1010];
queue<pair<int, int>>w;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        string t;
        cin >> t;
        for(int j = 0; j < n; j++){
            m[i][j] = t[j] - '0';
            step[i][j] = 1e9;
        }
    }
    cin >> x >> y >> x2 >> y2;
    x--;
    y--;
    x2--;
    y2--;

    w.push({x, y});
    step[x][y] = 0;
    m[x][y] =1;
    while(!w.empty()){
        int tx = w.front().first;
        int ty = w.front().second;
        w.pop();
        if(tx - 1 >= 0 && m[tx - 1][ty] == 0){
            step[tx - 1][ty] = min(step[tx - 1][ty], step[tx][ty] + 1);
            m[tx - 1][ty] = 1;
            w.push({tx - 1, ty});
        }
        if(tx + 1 < n && m[tx + 1][ty] == 0){
            step[tx + 1][ty] = min(step[tx + 1][ty], step[tx][ty] + 1);
            m[tx + 1][ty] = 1;
            w.push({tx + 1, ty});
        }
        if(ty + 1 < n && m[tx][ty + 1] == 0){
            step[tx][ty + 1] = min(step[tx][ty + 1], step[tx][ty] + 1);
            m[tx][ty + 1] = 1;
            w.push({tx, ty + 1});
        }
        if(ty - 1 >= 0 && m[tx][ty - 1] == 0){
            step[tx][ty - 1] = min(step[tx][ty - 1], step[tx][ty] + 1);
            m[tx][ty - 1] = 1;
            w.push({tx, ty - 1});
        }
    }
    cout << step[x2][y2];
    return 0;
}*/

/*int a[7][7];
int ans = 0;

void dfs(int i, int j, int white, int black){
    if(i == 6 && j == 1 && white == 13 && black == 12){
        ans++;
    }
    if(white > 13 || black > 12){
        return;
    }
    if(a[i][j] == -1){
        for(int n = 0; n <= 1; n++){
            int t = 0;
            for(int hang = 1; hang < 6; hang++){
                if(a[hang][j] != n){
                    t = 1;
                    break;
                } 
            }
            if(t == 1){
                for(int lie = 1; lie < 6; lie++){
                    if(a[i][lie] != n){
                        t = 2;
                        break;
                    }
                }
            }
            if(t == 2){
                if(i == j){
                    for(int i = 1; i < 6; i++){
                        if(a[i][i] != n){
                            t = 3;
                            break;
                        }
                    }
                    if(t == 3){
                        for(int i = 1; i < 6; i++){
                            if(a[i][6 - i] != n){
                                t = 4;
                                break;
                            }
                        }
                    }
                }
                else{
                    t = 4;
                }
            }
            if(t == 4){
                if(j + 1 > 5){
                    if(n == 0){
                        dfs(i + 1, 1, white + 1, black);
                        a[i][j] = -1;
                    }
                    if(n == 1){
                        dfs(i + 1, 1, white, black + 1);
                        a[i][j] = -1;
                    }
                }
                else{
                    if(n == 0){
                        dfs(i, j + 1, white + 1, black);
                        a[i][j] = -1;
                    }
                    if(n == 1){
                        dfs(i, j + 1, white, black + 1);
                        a[i][j] = -1;
                    }
                }
            }
        }
    }
}
int main(){
    for(int i = 1; i < 6; i++){
        for(int j = 1; j < 6; j++){
            a[i][j] = -1;
        }
    }
    dfs(1, 1, 0, 0);
    cout << ans;
    return 0;
}*/
/*int a[12][12];

void dfs(int i, int j){
    if(i == 10 && j == 1){
        for(int i = 1; i < 10; i++){
            for(int j = 1; j < 10; j++){
                cout << a[i][j] << " ";
            }
            cout << endl;
        }
        return;
    }
    if(a[i][j] == 0){
        for(int n = 1; n < 10; n++){
            int t = 1;
            for(int hang = 1; hang < 10; hang++){
                if(a[hang][j] == n){
                    t = 0;
                    break;
                }
            }
            if(t == 1){
                for(int lie = 1; lie < 10; lie++){
                    if(a[i][lie] == n){
                        t = 0;
                        break;
                    }
                }
            }
            if(t == 1){
                int p = i, q = j;
                while(p % 3 != 1){
                    p--;
                }
                while(q % 3 != 1){
                    q--;
                }
                for(int aa = p; aa <= p + 2; aa++){
                    for(int bb = q; bb <= q + 2; bb++){
                        if(a[aa][bb] == n){
                            t = 0;
                            break;
                        }
                    }
                }
            }
            if(t == 1){
                a[i][j] = n;
                if(j + 1 == 10){
                    dfs(i + 1, 1);
                    a[i][j] = 0;
                }
                else{
                    dfs(i, j + 1);
                    a[i][j] = 0;
                }
            }
        }
        
    }
    else{
        if(j + 1 == 10){
            dfs(i + 1, 1);
        }
        else{
            dfs(i, j + 1);
        }
    }
}
int main(){
    for(int i = 1; i < 10; i++){
        for(int j = 1; j < 10; j++){
            cin >> a[i][j];
        }
    }
    dfs(1, 1);
    return 0;
}*/
/*int n, ans = 0, last = 0;
int a[30];
int m[30][30], dp[30];
vector<int>pre(50, -1);

void dfs(int x){
    if(pre[x] != -1)
        dfs(pre[x]);
    cout << x + 1 << " ";
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n - 1; i ++){
        for(int j = i + 1; j < n; j++){
            cin >> m[i][j];
            m[j][i] = m[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        dp[i] = a[i]; // 每个节点初始权重
        if(a[i] > ans){
            ans = a[i];
            last = i;
        }
    }

    for(int i = 1; i < n; i++){
        for(int j = i - 1; j >= 0; j--){
            if(m[i][j] && (dp[j] + a[i]) > dp[i]){
                dp[i] = dp[j] + a[i];
                pre[i] = j;
            }
            if(ans < dp[i]){
                ans = dp[i];
                last = i;
            }
        }
    }
    dfs(last);
    cout << endl;
    cout << ans;
    
    return 0;
}*/
/*int n, m, a, b;

int main(){
    cin >> n >> m >> a >> b;
    vector<vector<int>>shouling(b, vector<int>(2, 0));
    vector<vector<int>>yuan(a, vector<int>(2, 0));
    for(int i = 0; i < a; i++){
        cin >> yuan[i][0] >>  yuan[i][1];
    }
    for(int i = 0; i < b; i++){
        cin >> shouling[i][0] >> shouling[i][1];
    }
    vector<int>result(b, 0);
    for(int i = 0; i < b; i++){
        int temp = 1e10;
        for(int j = 0; j < a; j++){
            temp = min(temp, abs(yuan[j][0] - shouling[i][0]) + abs(yuan[j][1] - shouling[i][1]));
        }
        result[i] = temp;
    }
    for(int i = 0; i < b; i++){
        cout << result[i] << endl;
    }
    return 0;
}*/
/*int n, k, num;
long long cnt[2000], ok[2000];
long long dp[15][2000][100];//已经放了i行，i行什么状态，用了多少国王， dp意思是有多少种放法

int main(){
    cin >> n >> k;
    //每一行用1表示放了，0表示不放，连起来就统共有2^n个二进制状态
    for(int i = 0; i < (1 << n); i++){//枚举这些状态
        int tot = 0, s1 = i;//几个1
        while(s1){
            if((s1 & 1) == 1)tot++;
            s1 >>= 1;
        }
        cnt[i] = tot;//预处理这个状态有多少个1；
        if((((i<<1)|(i>>1))&i)==0)ok[num++] = i;//即这个状态在一行里是合法的
    }
    dp[0][0][0] = 1;
    for(int i = 1; i <= n; i++){//枚举每一行
        for(int j = 0; j < num; j++){//枚举这一行状态
            int s1 = ok[j];
            for(int m = 0; m < num; m++){//枚举上一行状态
                int s2 = ok[m];
                if(((s2 | (s2 << 1) | (s2 >> 1)) & s1) == 0){//合法
                    for(int k1 = 0; k1 <= k; k1++){//枚举之前已经放了多少国王
                        if(k1 - cnt[s1] >= 0){
                            dp[i][s1][k1] += dp[i - 1][s2][k1 - cnt[s1]];
                        }
                    }
                }
            }
        }
    }
    long long ans = 0;
    for(int i = 0; i < num; i++){
        ans += dp[n][ok[i]][k];
    }
    cout << ans;
    return 0;
}*/
/*struct object{
    int v, w, belong, f1, f2;
}obj[62];

int n, m;
int all[300][2];
int dp[300][200010];

int main(){
    cin >> n >> m;
    for(int i = 1; i <= m; i++){
        cin >> obj[i].v >> obj[i].w >> obj[i].belong;
        obj[i].f1 = -1;
        obj[i].f2 = -1;
        if(obj[i].belong != 0){
            if(obj[obj[i].belong].f1 > 0){
                obj[obj[i].belong].f2 = i;
            } 
            else obj[obj[i].belong].f1 = i;
        }
    }
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            if(obj[i].belong > 0)dp[i][j] = dp[i - 1][j];
            else{
                int fu1 = obj[i].f1;
                int fu2 = obj[i].f2;
                int t = dp[i - 1][j];
                if(j >= obj[i].v){
                    t = max(t, dp[i - 1][j - obj[i].v] + obj[i].v * obj[i].w);
                }
                if(fu1 > 0 && j >= obj[i].v + obj[fu1].v){
                    t = max(t, dp[i - 1][j - obj[i].v - obj[fu1].v] + obj[i].w * obj[i].v + obj[fu1].w * obj[fu1].v);
                }
                if(fu2 > 0 && j >= obj[i].v + obj[fu2].v){
                    t = max(t, dp[i - 1][j - obj[i].v - obj[fu2].v] + obj[i].w * obj[i].v + obj[fu2].w * obj[fu2].v);
                }
                if(fu1 > 0 && fu2 > 0 && j >= obj[i].v + obj[fu1].v + obj[fu2].v){
                    t = max(t, dp[i - 1][j - obj[i].v - obj[fu1].v - obj[fu2].v] + obj[i].w * obj[i].v + obj[fu1].w * obj[fu1].v + obj[fu2].w * obj[fu2].v);
                }
                dp[i][j] = t;
            }
        }
    }
    cout << dp[m][n];
    return 0;
}*/

/*int v, n;
int a[32], dp[32][20010];//研究到第几个，能用多少钱

int main(){
    cin >> v >> n;
    for(int i = 1; i <= n; i++){
        cin >> a[i];
    }

    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= v; j++){
            if(j >= a[i])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + a[i]);
            else dp[i][j] = dp[i - 1][j];
        }
    }
    cout << v - dp[n][v];
    return 0;
}*/
/*int n, k;
int a[1000001];
int head, tail;
vector<int>res_max;
vector<int>res_min;
vector<int>q_max;
vector<int>q_min;

int main(){
    
    cin >> n >> k;

    vector<int>res_max(n);
    vector<int>res_min(n);
    vector<int>q_max(n);
    vector<int>q_min(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    head = 1;
    tail = 0;
    for(int i = 0; i < n; i++){//找最小的
        while(tail >= head && a[i] < q_min[tail]){//把老且大的元素踢出去
            tail--;
        }
        q_min[++tail] = a[i];//a[i]放进来;
        while(tail >= head && i - k  + 1 > head){//太老的踢出去
            head++;
        }
        if(i >= k - 1)
            res_min[i - k + 1] = q_min[head];
    }
    head = 1;
    tail = 0;
    for(int i = 0; i < n; i++){
        while(tail >= head && a[i] > q_max[tail]){//把老且小的元素踢出去
            tail--;
        }
        q_max[++tail] = a[i];//a[i]放进来;
        while(tail >= head && i - k  + 1 > head){//太老的踢出去
            head++;
        }
        if(i >= k - 1)
            res_max[i - k + 1] = q_max[head];
    }
    for(int i = 0; i < n - k + 1; i++){
        cout << res_min[i] << " ";
    }
    cout << endl;
    for(int i = 0; i < n - k + 1; i++){
        cout << res_max[i] << " ";
    }
    return 0;
}*/
/*int n, k, a[1000001];
int min1 = 1e9, max1, temp;

int main(){
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < k; i++){
        temp += a[i];
    }
    min1 = min(min1, temp);
    max1 = max(max1, temp);
    for(int i = 0; i < n - k; i++){
        temp += a[i + k];
        temp -= a[i];
        min1 = min(min1, temp);
        max1 = max(max1, temp);
    }
    cout << 
    return 0;
}*/
/*int n, k;
int dp[1001][1001];

int main(){
    cin >> n >> k;
    for(int i = 0; i <= n; i++){
        dp[i][0] = 1;
    }
    for(int i = 2; i <= n; i++){
        for(int j = 1; j <= k; j++){
            dp[i][j] = (dp[i - 1][j] *(j + 1) + dp[i - 1][j - 1] * (i - j)) % 2015;
        }
    }
    cout << dp[n][k] % 2015;
    return 0;
}*/
/*string a, b, c;
string ans[101][101][101];
int dp[101][101][101];
int lena, lenb, lenc;

int main(){
    cin >> a >> b >> c;
    lena = a.size();
    lenb = b.size();
    lenc = c.size();

    for(int i = 0; i < lena; i++){
        for(int j = 0; j < lenb; j++){
            for(int k = 0; k < lenc; k++){
                if(a[i] == b[j] && b[j] == c[k]){
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], dp[i][j][k] + 1);
                    ans[i+ 1][j + 1][k + 1] = ans[i][j][k] + a[i];
                }
                else {
					if (dp[i + 1][j + 1][k + 1] < dp[i][j + 1][k + 1]){
						dp[i + 1][j + 1][k + 1] = dp[i][j + 1][k + 1];
						ans[i + 1][j + 1][k + 1] = ans[i][j + 1][k + 1];
					}
					if (dp[i + 1][j + 1][k + 1] < dp[i + 1][j][k + 1]){
						dp[i + 1][j + 1][k + 1] = dp[i + 1][j][k + 1];
						ans[i + 1][j + 1][k + 1] = ans[i + 1][j][k + 1];
					}
					if (dp[i + 1][j + 1][k + 1] < dp[i + 1][j + 1][k]){
						dp[i + 1][j + 1][k + 1] = dp[i + 1][j + 1][k];
						ans[i + 1][j + 1][k + 1] = ans[i + 1][j + 1][k];
                    }    
                }
            }
        }
    cout << ans[lena][lenb][lenc];
    return 0;
    }
}*/
/*int n, ans;

int main(){
    cin >> n;
    vector<int>a(n + 1, 0);
    vector<int>b(n + 1, 0);
    vector<int>m(n + 1, 0);
    vector<int>result;

    for(int i = 1; i <= n; i++){
        cin >> a[i];
        m[a[i]] = i;
    }
    for(int i = 1; i <= n; i++){
        cin >> b[i];
        b[i] = m[b[i]];
    }

    for(int i = 1; i <= n; i++){
        auto it = lower_bound(result.begin(), result.end(), b[i]);
        if (it == result.end()) {
            result.push_back(b[i]);
        } else {
            *it = b[i];
        }
        
    }
    
    cout << result.size();
    return 0;
}*/
/*struct every_stone{
    int k, m;//体积和需要的体力
}stone[10001];

int v, n, c, dp[10001];//使用的体力不超过多少，dp意思是最大价值
int ans;

int main(){
    cin >> v >> n >> c;
    for(int i = 0; i < n; i++){
        cin >> stone[i].k >> stone[i].m;
    }
    for(int i = 0; i < n; i++){
        dp[i] = 0;
    }

    for(int i = 0; i < n; i++){
        for(int j = c; j >= stone[i].m; j--){
            dp[j] = max(dp[j], dp[j - stone[i].m] + stone[i].k);
        }
    }

    if(dp[c] < v)cout << "Impossible";
    else{
        for(int i = 0; i <= c; i++){
            if(dp[i] >= v){
                ans = c - i;
                break;
            }
        }
        cout << ans;
    }
    return 0;
}*/
/*struct dian{
    int x, y;
}point[1001];

int n;
double dp[1001][1001], ans = 1e30;

bool cmp(const dian &a, const dian &b){
    return a.x < b.x;
}

double dis(const dian &a, const dian &b){
    return sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2));
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> point[i].x >> point[i].y;
    }
    sort(point, point + n, cmp);

    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= n; j++){
            dp[i][j] = 1e30;
        }
    }
    dp[0][1] = dis(point[0], point[1]);

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(i == 0 && j == 0)continue;
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + dis(point[j], point[j + 1]));
            dp[j][j + 1] = min(dp[j][j + 1], dp[i][j] + dis(point[i], point[j + 1]));
        }
    }
    for(int i = 0; i < n - 1; i++){
        ans = min(ans, dp[i][n - 1] + dis(point[i], point[n - 1]));
    }
    cout << fixed << setprecision(2) << ans  << endl;
    return 0;
}*/
/*string str;
int n, k;
long long num[50][50], dp[50][50];//dp含义：前i个数，j个格挡

int main(){
    cin >> n >> k >> str;
    str = ' ' + str;
     for(int i = 1; i <= n; i++){
        for(int j = i; j <= n; j++){
            num[i][j] = num[i][j - 1] * 10 + str[j] - '0';
        }
    }
    memset(dp, 0, sizeof(dp));
    for(int i = 1; i <= n; i++){
        dp[i][0] = num[1][i];
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= k; j++){
            if(j >= i)break;
            for(int k = j; k < i; k++){
                dp[i][j] = max(dp[i][j], dp[k][j - 1] * num[k + 1][i]);
            }
        }
    }
    cout << dp[n][k];
    return 0;
}*/
/*long long a[101];
long long n;
long long fenzi[101], fenmu[101];
int m, c;

long long gcd(long long a, long long b)
{
    if(a<b) swap(a,b);
    if(b==1) return a;
    return gcd(b,a/b);
}

bool cmp(long long a, long long b){
    return a > b;
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a, a + n, cmp);
    for(int i = 0; i < n - 1; i++){
        if(a[i] != a[i + 1]){
            fenzi[c] = a[i];
            fenmu[c] = a[i + 1];
            c++;
        }
    }
    long long f1 = fenzi[0];
    long long f2 = fenmu[0];
    for(int i = 1; i < c; i++){
        f1 = gcd(f1, fenzi[i]);
        f2 = gcd(f2, fenmu[i]);
    }
    cout << f1 << "/" << f2 << endl;
    return 0;
}*/
/*const int N = 1e9 + 7;

int  d, t, m;
long long dp[3001][1501];//时间，用了多少体力，dp为方案数

int main(){
    cin >> d >> t >> m;
    dp[0][0] = 1;
    for(int i = 1; i <= t; i++){
        for(int j = m; j >= 0; j--){
            long long len = d - i + 2 * j;
            if(len > 0){
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % N;
            }
        }
    }
    cout << dp[t][m] % N;
    return 0;
}*/
/*int n, a[101], res;
bool dp[10001];
int gcd(int a, int b){
    if(b == 0)return a;
    else return gcd(b, a % b);
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int g = a[0];
    for(int i = 1; i < n; i++){
        g = gcd(g, a[i]);
    }    
    if(g > 1){
        cout << "INF";
        return 0;
    }
    sort(a, a + n);
    dp[0] = 1;
    for(int i = 1; i < 10001; i++){
        dp[i] = 0;
        for(int j = 0; j < n; j++){
            if(i >= a[j] && dp[i - a[j]]){
                dp[i] = 1;
                break;
            }
        }  
        if(dp[i] == 0)res++;
    }
    cout << res;
    return 0;
}*/
/*struct gouzi{
    long long r, l;
}Gou[100001];


const int N = 2e6 + 5;
long long n, m, nn[N], result[100001];

int main(){
    cin >> n >> m;
    for(long long i = 0; i < n; i++){
        long long tl, tr;
        cin >> tl >> tr;
        nn[tr + tl]++;
    }
    
    for(long long i = 1; i < N; i++){
        nn[i] += nn[i - 1];
    }

    for(int i = 1; i <= m; i++){
        long long a, b;
        cin >> a >> b;
        cout << nn[b * 2] - nn[a * 2 - 1] << endl;
    }
    return 0;
}*/
/*#define int long long

struct doll{
    int r, l, len;
}Doll[10010];

struct gouzi{
    int r, l, len;
}Gou[10010];

int n, m, result[10010];

bool cmp(doll a, doll b){
    return a.l > b.l;
}
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> Doll[i].l >> Doll[i].r;
        Doll[i].len = Doll[i].r - Doll[i].l;
    }
    for(int i = 0; i < m; i++){
        cin >> Gou[i].l >> Gou[i].r;
        Gou[i].len = Gou[i].r - Gou[i].l;
    }

    sort(Doll, Doll + n, cmp);

    for(int i = 0; i < m; i++){//钩子
        for(int j = 0; j < n; j++){//娃娃
            if(Gou[i].len < Doll[j].len / 2)continue;
            if (Doll[j].r <= Gou[i].l) continue; 
            if(Doll[j].l > Gou[i].r)break;
            else if(Doll[j].l >= Gou[i].l){
                if(Doll[j].r <= Gou[i].r) 
                    result[i]++;
                else if((Gou[i].r - Doll[j].l) >= Doll[j].len / 2) 
                    result[i]++;
            }
            else if(Doll[j].l < Gou[i].l){
                if((Doll[j].r - Gou[i].l) >= Doll[j].len / 2)
                    result[i]++;
            }
        }
    }
    for(int i = 0; i < m; i++){
        cout << result[i] << endl;
    }
    return 0;
}*/
/*string s, ans[10010], now;
long long a, b, size, sum;

void dfs(int x, int y, int k){
    if(k == size){
        ans[++sum] = now, void();
    }
    int temp = s[k] - '0';
    long long lx = a - x;
    long long ly = b - y;
    if(9 - temp <= lx){//到9
        now[k] = 9 + '0';
        dfs(x + (9 - temp), y, k + 1);
    }
    if(temp + 1 <= ly){
        now[k] = 9 + '0';
        dfs(x, y + (temp + 1), k + 1);
    }
    if(9 - temp > lx && temp + 1 > ly){
        now[k] = temp + lx + '0';
        dfs(a, y, k + 1);
    }
    
}
int main(){
    cin >> s >> a >> b;
    now = s;
    size = s.size();
    dfs(0, 0, 0);
    sort(ans + 1, ans + sum + 1);
    cout << ans[sum];

    return 0;
}*/
/*bool basketball(int year, int month, int day){
    int bihua = 0;
    int temp = year * 10000 + month * 100 + day;
    while(temp != 0){
        int t = temp % 10;
        if(t == 0)bihua += 13;
        else if(t == 1)bihua += 1;
        else if(t == 2 || t ==7 || t == 8 ||t == 9)bihua += 2;
        else if(t == 3)bihua += 3;
        else if(t == 4)bihua += 5;
        else bihua += 4;
        temp /= 10;
    }
    return bihua > 50;
}
int main(){
    int ans = 0;
    int year = 2000, month = 1, day = 1;
    while(year < 2024 || (year == 2024 && (month < 4 || (month == 4 && day < 14)))){
        if(basketball(year, month, day))ans++;
        if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10){
            if(day == 31){
                month++;
                day = 1;
            }
            else day++;
        }
        else if(month == 4 || month == 6 || month == 9 || month == 11){
            if(day == 30){
                month++;
                day = 1;
            }
            else day++;
        }
        else if(month == 2 && year % 4 != 0){//平年
            if(day == 28){
                month++;
                day = 1;
            }
            else day++;
        }
        else if(month == 2 && year % 4 == 0){
            if(day == 29){
                month++;
                day = 1;
            }
            else day++;
        }
        else if(month == 12){
            if(day == 31){
                year++;
                month = 1;
                day = 1;
            }
            else day++;
        }
    }
    cout << ans;
    return 0;
}*/
/*int gongyueshu(int a, int b){
    int r = a % b;
    while(r){
        a = b;
        b = r;
        r = a % b;
    }
    return b;
}
int ans2(){
    int c = 0;
    for(int i = 1; i <= 2020; i++){
        for(int j = 1; j <= 2020; j++){
            if(gongyueshu(i, j) == 1)c++;
        }
    }
    return c;
}*/
/*int ans3(int n){
    int c  = 1;
    for(int i = 1; i < n; i++){
        c += 4 * i;
    }
    return c;
}*/


/*int n, m;
vector<int>value;
vector<vector<int>>con;
vector<int>flag;

void send(int start, int weight){
    for(int i = 0; i < n; i++){
        if(con[start][i] == 1 && flag[i] == 0){
            value[i] += weight;
            flag[i] = 1;
            send(i, weight);
        }
    }
    return;
}

int main(){
    cin >> n >> m;
    vector<int>value(n, 0);
    vector<vector<int>>con(n, vector<int>(n, 0));
    for(int i = 0; i < n; i++){
        con[i][i] = 1;
    }
    for(int i = 0; i < m; i++){
        int t1, t2, t3;
        cin >> t1 >> t2 >> t3;
        if(t1 == 1)con[t2][t3] = con[t3][t2] = 1;
        else{
            vector<int>flag(n, 0);
            send(t2, t3);
        }

    }
    for(int i = 0; i < n; i++){
        cout << value[i] << " ";
    }
    return 0;
}*/
/*long long n, ans;

bool cmp(int a, int b){
    return a >= b;
}

int main(){
    cin >> n;
    vector<long long>w(n);
    for(int i = 0; i < n; i++){
        cin >> w[i];
    }
    sort(w.begin(), w.end(), cmp);
    for(long long i = 0; i < n - 1; i++){
        ans += w[i] * w[i + 1];
        w[i + 1] += w[i];
    }
    cout << ans;
    return 0;
}*/
/*struct soldier{
    int p, c;
}soldier[100001];

int main(){
    long long s;
    int n;
    long long cost = 0;
    cin >> n >> s;
    for(int i = 0; i < n; i++){
        cin >> soldier[i].p >> soldier[i].c;
    }
    while(1){
        int min1 = 1000000000;
        for(int i = 0; i < n; i++){
            if(soldier[i].c > 0)min1 = min(min1, soldier[i].c);//最少的那个要训练几次
        }
        if(min1 == 1000000000) break;
        long long total = 0;
        for(int i = 0; i < n; i++){
            if(soldier[i].c != 0)total += soldier[i].p;//每个单独训练要多少钱
        }
        if(total >= s){     
            cost += s * min1;                        //如果组团合适,花s块钱
            for(int i = 0; i < n; i++){            
                if(soldier[i].c > 0)soldier[i].c -= min1;//每个要训练的都被训练了这些次
            }
        }
        else break;//组团不合适了，接下来都单独练
    }

    for(int i = 0; i < n; i++){
        if(soldier[i].c != 0){
            cost += (long long)soldier[i].p * soldier[i].c;
        }
    }
    cout << cost;
    return 0;
}*/
/*int max_len = 0, n;

struct liangtou{
    int left, right;
}a[100001];
int main(){
    cin >> n;
    vector<int>dp(11, 0);
    for(int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        a[i].right = temp % 10;
        while(temp >= 10)temp /= 10;
        a[i].left = temp;
    }
    for(int i = 0; i < n; i++){
        dp[a[i].right] = max(dp[a[i].right], dp[a[i].left] + 1);
    }
    for(int i = 0; i <= 10; i++){
        max_len = max(max_len, dp[i]);
    }
    cout << n - max_len;
    return 0;
} */
/*int main(){
    cin >> n;
    vector<int>a(n, 0);
    vector<vector<int>>dp(n, vector<int>(n, 0));
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        int temp = 0;
        for(int j = i; j  < n; j++){
            temp ^= a[j];
            result += temp;
        }
    }
    cout << result << endl;
    return 0;
}*/
/*string a;
bool dp[5001][5001];
long long len;

int main(){
    cin >> a;
    len = a.size();
    for(int i = 0; i < len; i++){
        dp[i][i] = 0;
    }
    long long result = 0;
    for(int len1 = 1; len1 < len; len1++){
        for(int i = 0; i < len - len1; i++){
            int j = i + len1;
            if(len1 == 1){
                if(a[i] > a[j]) dp[i][j] = 1;
                else dp[i][j] = 0;
                continue;
            }
            if(a[i] > a[j]) dp[i][j] = 1;
            else if(a[i] == a[j]) dp[i][j] = dp[i + 1][j - 1];
            else dp[i][j] = 0;
        }
    }
    for(int i = 0; i < len - 1; i++){
        for(int j = i + 1; j < len; j++){
            if(dp[i][j])result++;
        }
    }
    cout << result << endl;
    return 0;
}*/
/*int l, r, num;

int main(){
    cin >> l >> r;
    for(int i = l; i <= r; i++){
        if(i % 2)num++;
        else if(i % 4 == 0)num++;
    }
    cout << num;
    return 0;
}*/
/*long long n, height[200005], cut[200005], m = 0, t;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> height[i];
        cut[i] = height[i];
        long long c = 0;
        while(cut[i] - 1){
            cut[i] = sqrtl(cut[i] / 2 + 1);
            c++;
            m = max(m, c);
        }
        cut[i] = c; 
    }
    long long m1 = m;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(cut[j] == m1){
                if(height[j] != height[j + 1])t++;
                cut[j]--;
                height[j] = sqrtl(height[j] / 2 + 1);
            }
        }
        m1--;
    }
    cout << t;
    return 0;
}*/
/*struct plane{
    int t, d, l;
}P[11];

int T, v[11], n;
bool flag;

void dfs(int deep, int now_time){
    if(deep == n){
        flag = 1;
        return;
    }
    for(int i = 0; i < n; i++){
        if(v[i] == 0 && P[i].t + P[i].d < now_time)return;
        if(v[i] == 0){
            v[i] = 1;
            if(P[i].t <= now_time){
                dfs(deep + 1, now_time + P[i].l);
            } 
            else dfs(deep + 1, P[i].t + P[i].l);
            v[i] = 0;
        }
    }
}
int main(){
    cin >> T;
    while(T--){
        flag = 0;
        cin >> n;
        for(int i = 0; i < n; i++){
            v[i] = 0;
            cin >> P[i].t >> P[i].d >> P[i].l;
        }
        for(int i = 0; i < n; i++){
            v[i] = 1;
            dfs(1, P[i].t + P[i].l);
            v[i] = 0;
        }
        if(flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}*/
/*int m, n;
int a[3550], c[5];
int dp[41][41][41][41]; //四张卡片用了多少

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < m; i++){
        int temp;
        cin >> temp;
        c[temp]++;
    }
    dp[0][0][0][0] = a[0];
    for(int i = 0; i <= c[1]; i++){
        for(int j = 0; j <= c[2]; j++){
            for(int p = 0; p <= c[3]; p++){
                for(int q = 0; q <= c[4]; q++){
                    if(i == 0 && j ==0 && p == 0 && q == 0)continue;
                    int temp = 0;
                    int now = i + 2 * j + 3 * p + 4 * q;
                    if(i != 0)temp = max(temp, dp[i - 1][j][p][q] + a[now]);
                    if(j != 0)temp = max(temp, dp[i][j - 1][p][q] + a[now]);
                    if(p != 0)temp = max(temp, dp[i][j][p - 1][q] + a[now]);
                    if(q != 0)temp = max(temp, dp[i][j][p][q - 1] + a[now]);
                    dp[i][j][p][q] = max(temp, dp[i][j][p][q]);
                }
            }
        }
    }
    cout << dp[c[1]][c[2]][c[3]][c[4]];
    return 0;
}*/

/*long long n, k, p;
long long a[101][101];
long long dp[101][101][10000];

int main(){
    cin >> n >> k;
    for(int i = 1; i <= n; ++ i)
		for(int j = 0; j <= n; ++ j)
			for(int l = 0; l <= k; ++ l)
				dp[i][j][l] = -3e9;
    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= i; j++){
            cin >> a[i][j];
        }
    }
    for(long long i = 1; i <= n; i++){
        for(int j = 1; j <= i; j++){
            for(int l = 0; l <= min(k, i); l++){
                if(l == 0)
                    dp[i][j][l] = max(dp[i - 1][j - 1][l], dp[i - 1][j][l]) + a[i][j];
                else{
                    dp[i][j][l] = max(dp[i - 1][j - 1][l], dp[i - 1][j][l]) + a[i][j];
                    dp[i][j][l] = max(dp[i][j][l], max(dp[i - 1][j - 1][l - 1], dp[i - 1][j][l - 1]) + a[i][j] * 3);
                }
            }
            
        }
    }
    long long result = 0;
    for(int j = 1; j <= n; j++){
        for(int l = 0; l <= min(k, n); l++){
            result = max(result, dp[n][j][l]);
        }
    }
    cout << result;
    return 0;
}*/
/*double h, s, v, l, k, n;

int main(){
    cin >> h >> s >> v >> l >> k >> n;
    double t1 = pow(((h - k) / 5), 0.5);
    double t2 = pow((h / 5), 0.5);

    int n_max = (int)min((s + l - t1 * v), n);
    int  n_min = (int)max((s - t2 * v), 0.0);
    cout << n_max - n_min;
    return 0;
}*/
/*long long n, zerox, zeroy;
queue<long long>q;
int a[3][3];
const int turnx[4] = {1, -1, 0, 0};
const int turny[4] = {0, 0, 1, -1};
map<long long, long long>m;

int main(){
    cin >> n;
    q.push(n);
    while(!q.empty()){
        int u = q.front();
        int uu = u;
        if(u == 123804765)break;
        q.pop();
        for(int i = 2; i >=0; i--){
            for(int j = 2; j >= 0; j--){
                a[i][j] = u % 10;
                u /= 10;
                if(a[i][j] == 0){
                    zerox = i;
                    zeroy = j;
                }
            }
        }
        for(int i = 0; i < 4; i++){
            int tx = zerox + turnx[i];
            int ty = zeroy + turny[i];
            if(tx < 0 || ty < 0 || tx >= 3 || ty >= 3)continue;
            swap(a[tx][ty], a[zerox][zeroy]);
            long long v = 0;
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    v = v * 10 + a[i][j];
                }
            }
            if(!m.count(v)){
                m[v] = m[uu] + 1;
                q.push(v);
            }
            swap(a[tx][ty], a[zerox][zeroy]);
        }
    }
    cout << m[123804765]<< endl;
    return 0;
}*/

/*long long n, c;
unordered_map<int, int> s;
long long res = 0;

int main(){
    cin >> n  >> c;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
        s[a[i]]++;
    }
    
    for(int i = 0; i < n; i++){
        res += s[a[i] - c];
    } 
    cout << res;
    return 0;
}*/
/*const int maxn = 2510;
#define INF 1e9
vector<pair<int, int>>e[maxn];
int d[maxn];

void dijkstra(int s){
    priority_queue<pair<int, int>>q;
    d[s] = 0;
    q.push(make_pair(-d[s], s));

    while(!q.empty()){
        int now = q.top().second;
        q.pop();

        for(int i = 0; i < e[now].size(); i++){
            int v = e[now][i].first;
            if (d[v] > d[now] + e[now][i].second) { // 松弛操作
                d[v] = d[now] + e[now][i].second; // 更新距离
                q.push(make_pair(-d[v], v)); 
            }
        }
    }
}

int main(){
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    for(int i = 0; i < maxn; i++){
        e[i].clear(), d[i] = INF;
    }
    for(int i = 0; i <= m; i++){
        int u, v, d;
        cin >> u >> v >> d;
        e[u].push_back(make_pair(v, d)); 
        e[v].push_back(make_pair(u, d));
    }

    dijkstra(s);
    cout << d[t];
    return 0;
}*/
/*int a,
b, c;
bool v[21][21][21];
bool rec[21];

void dfs(int o, int p, int q){//a, b, c三个桶里面现在有多少
    if(v[o][p][q])return;
    else v[o][p][q] = true;
    if(o == 0 && rec[c] == 0)rec[q] = true;

    if(c - q >= o){//a往c里倒
        dfs(0, p, q + o);
    }
    else{
        dfs(o - (c - q), p, c);
    }
    if(a - o >= q)dfs(o + q, p, 0);//c往a里倒
    else dfs(a, p, q - (a - o));
    if(b - p >= o)dfs(0, p + o, q);//a往b里倒
    else dfs(o - (b - p), b, q);
    if(a - o >= p)dfs(o + p, 0, q);//b往a里倒
    else dfs(a, p - (a - o), q);
    if(c - q >= p)dfs(o, 0, q + p);//b往c里倒
    else dfs(o, p - (c - q), c);
    if(b - p >= q)dfs(o, p + q, 0);//c往b里倒
    else dfs(o, b, q - (b - p));
}

int main(){
    cin >> a >> b >> c;
    dfs(0, 0, c);

    for(int i = 0; i <= 20; i++){
        if(rec[i]){
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}*/
/*int m, s, c;
int a[1000], b[1000];

bool cmp(int x, int y){
    return x > y;
}

int main(){
    cin >> m >> s >> c;
    
    for(int i = 0; i < c; i++){
        cin >> a[i];
    }
    sort(a, a + c);
    int res = a[c - 1] - a[0];
    for(int i = 1; i < c; i++){
        b[i - 1] = a[i] - a[i - 1] - 1;
    }

    sort(b, b + c - 1, cmp);
    for(int i = 0; i < m - 1; i++){
        res -= b[i];
    }
    cout << res + 1;
    return 0;
}*/
/*int a[51][51], b[55][55], queue[10000][4], v[55][55][4];//queue:横(y)，纵(x)，朝向，第几步
int n, m, sy, sx, endy, endx, sd;//d == 0, 1, 2, 3分别表示东南西北 
char start_d;
int front = 0; rear = 0;

void to_line(int **a, int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j]){
                b[i][j] = b[i][j + 1] = b[i + 1][j] = b[i + 1][j + 1] = 1;
            }
        }
    }
}

void bfs(){
    int x, y, d, step;
    while(rear > front){
        x = queue[front][0];
        y = queue[front][1];
        d = queue[front][2];
        step = queue[front][3];
        if(v[x][y][d] == 1){
            continue;
        }
        if(x == sx && y == sy){
            cout << step;
            return;
        }
        if(d == 2 && b[x - 1][y] == 1){
            v[x - 1][y][3] = 1;
            queue[rear][0] = x - 1;
            queue[rear][1] = y;
            queue[rear][2] = 3;
            queue[rear++][3] = step + 1;
        }
        if(d == 2 && b[x + 1][y] == 1){
            v[x + 1][y][1] = 1;
            queue[rear][0] = x + 1;
            queue[rear][1] = y;
            queue[rear][2] = 1;
            queue[rear++][3] = step + 1;
        }
        if(d == 1 && b[x][y - 1] == 1){
            v[x][y - 1][2] = 1;
            queue[rear][0] = x;
            queue[rear][1] = y - 1;
            queue[rear][2] = 2;
            queue[rear++][3] = step + 1;
        }
        if(d == 1 && b[x][y + 1] == 1){
            v[x][y - 1][0] = 1;
            queue[rear][0] = x;
            queue[rear][1] = y + 1;
            queue[rear][2] = 0;
            queue[rear++][3] = step + 1;
        }
        if(d == 0 && b[x + 1][y] == 1){
            v[x + 1][y][1] = 1;
            queue[rear][0] = x + 1;
            queue[rear][1] = y;
            queue[rear][2] = 1;
            queue[rear++][3] = step + 1;
        }
        if(d == 0 && b[x - 1][y] == 1){
            v[x - 1][y][3] = 1;
            queue[rear][0] = x - 1;
            queue[rear][1] = y;
            queue[rear][2] = 3;
            queue[rear++][3] = step + 1;
        }
        if(d == 3 && b[x][y - 1] == 1){
            v[x][y - 1][2] = 1;
            queue[rear][0] = x - 1;
            queue[rear][1] = y;
            queue[rear][2] = 2;
            queue[rear++][3] = step + 1;
        }
        if(d == 3 && b[x][y + 1] == 1){
            v[x][y + 1][0] = 1;
            queue[rear][0] = x - 1;
            queue[rear][1] = y;
            queue[rear][2] = 0;
            queue[rear++][3] = step + 1;
        }
        for(int i = 1; i <= 3; i++){
            if(d == 0 && b[x + 1][y] == 0 && b[x + i][y] == 0 && x + i < m){
                v[x + i][y][0] = 1;
                queue[rear][0] = x + i;       
                queue[rear][1] = y;
                queue[rear][2] = 0;
                queue[rear++][3] = step + 1;  
            }
            if(d == 2 && b[x - 1][y] == 0 && b[x - i][y] == 0 && x - i > 0){
                v[x - i][y][0] = 1;
                queue[rear][0] = x - i;       
                queue[rear][1] = y;
                queue[rear][2] = 0;
                queue[rear++][3] = step + 1;  
            }
            if(d == 3 && b[x][y] == 0 && b[x - i][y] == 0 && x - i > 0){
                v[x - i][y][0] = 1;
                queue[rear][0] = x - i;       
                queue[rear][1] = y;
                queue[rear][2] = 0;
                queue[rear++][3] = step + 1;  
            }
        }
    }
}
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    cin >> sy >> sx >> endy >> endx >>start_d;
    to_line(a, n, m);
    if(start_d == 'E') sd = 0;
    else if(start_d == 'W') sd = 1;
    else if(start_d == 'S') sd = 2;
    else sd = 3;

    return 0;
}*/
/*int m, n, k, l, d;
int x[2001], y[2001], p[2001], q[2002];

struct road{
    int x, n;
}roadx[1010], roady[1010];

bool cmp1(road a, road b){
    return a.n > b.n;
}

bool cmp2(road a, road b){
    return a.x < b.x;
}
int main(){
    cin >> m >> n >> k >> l >> d;
    for(int i = 0; i < d; i++){
        cin >> x[i] >> y[i] >> p[i] >> q[i];
    }
    for(int i = 0; i < d; i++){
        if(x[i] != p[i]){
            roadx[min(x[i], p[i])].x = min(x[i], p[i]);
            roadx[min(x[i], p[i])].n++;
        }
        if(y[i] != q[i]){
            roady[min(y[i], q[i])].x = min(y[i], q[i]);
            roady[min(y[i], q[i])].n++;
        }
    }
 
    sort(roadx, roadx + 1000, cmp1);
    sort(roady, roady + 1000, cmp1);
    sort(roadx, roadx + k, cmp2);
    sort(roady, roady + l, cmp2);
    for(int i = 0; i < k; i++){
        if(roadx[i].n){
            cout << roadx[i].x << " ";
        }
    }
    cout << endl;
    for(int i = 0; i < l; i++){
        if(roady[i].n){
            cout << roady[i].x << " ";
        }
    }
    return 0;
}*/
/*int n, avrage, sum1 = 0, step = 0;
int a[101];

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        sum1 += a[i];
    }
    avrage = sum1 / n;
    for(int i = 0; i < n; i++){
        if(a[i] == avrage){
            continue;
        }
        else if(a[i] < avrage){
            a[i + 1] -=(avrage - a[i]);
            step++;
        }
        else{
            a[i + 1] += (a[i] - avrage);
            step++;
        }
    }
    cout << step;
    return 0;
}*/
/*int m, n, k, a[25][25], b = 0, res = 0, sum = 0;

struct node{
    int x, y, v;
}No[1000];

bool cmp(node p, node q){
    return p.v > q.v;
}

int main(){
    cin >> m >> n >> k;
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            cin >> a[i][j];
            No[++b] = {i, j, a[i][j]};
        }
    }
    sort(No + 1, No + b + 1, cmp);
    No[0] = {0, No[1].y, 0};
    for(int i = 1; i <= b; i++){
        sum += abs(No[i - 1].x - No[i].x) + abs(No[i - 1].y - No[i].y) + 1;
        if(sum + No[i].x <= k && No[i].v){
            res += No[i].v;
        }
        else{
            break;
        }
    }
    cout << res;
    return 0;
}*/
/*long long n, a[10010][3], dp[10010][3][2];//位置，高度，比两边低还是高
long long ans = 0;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < 3; j++){
            cin >> a[i][j];
        }
    }

    for(int j = 0; j < 3; j++){
        dp[0][j][0] = dp[0][j][1] = a[0][j];
        for(int i = 1; i < n; i++){
            dp[i][0][0] = max(dp[i - 1][1][1] , dp[i - 1][2][1]) + a[i][0];
            dp[i][1][0] = dp[i - 1][2][1] + a[i][1];     
            dp[i][1][1] = dp[i - 1][0][0] + a[i][1];
            dp[i][2][1] = max(dp[i - 1][1][0], dp[i - 1][0][0]) + a[i][2];
        }
        for(int i = 0; i < j; i++){
            ans = max(ans, dp[n - 1][i][0]);
        }
        for(int i = 2; i > j; i--){
            ans = max(ans, dp[n - 1][i][1]);
        }
    }
    cout << ans;
    return 0;
}*/
/*long long n;
long long a[2200], dp[2200][2200];
int main(){
    cin >> n;
   
    for(int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        a[i] = temp;
        a[i + n] = temp;
    }
    n *= 2;
    for(int len = 2; len < n; len++){//序列长度
        for(int i = 0; i <= n - len; i++){//开头
            int j = i + len;//结尾
            for(int k = i + 1; k < j; k++){//断点
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]);
            }
        }
    }
    cout << dp[0][n - 1] / 2;
    return 0;
}*/
/*int n, m, cx, cy;
long long dp[23][23];
bool ma[23][23];
const int mo[8][2] = {{1, 2}, {1, -2}, {2, 1}, {2, -1}, {-1, 2}, {-1, -2}, {-2, 1}, {-2, -1}};

int main(){
    cin >> n >> m >> cx >> cy;
    ma[cx][cy] = 1;
    for(int i = 0; i < 8; i++){ 
        int tx = cx + mo[i][0], ty = cy + mo[i][1];
        if(tx >= 0 && tx <= n && ty >= 0 && ty <= m){
            ma[tx][ty] = 1;
        }
    }
    dp[0][0] = 1;
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= m; j++){
            if(ma[i][j] == 0){
                if(i != 0)
                    dp[i][j] += dp[i - 1][j];
                if(j != 0)
                    dp[i][j] += dp[i][j - 1];
            }
        }
    }
    cout << dp[n][m];
    return 0;
}*/

/*int n, m, a[2001][2001];
int dp[2002][2002];//第几步让小组几完成
int res = 1e12;

int main(){
    cin >> n >> m;//几步， 小组几
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            cin >> a[i][j];
        }
    }

    for(int i = 1; i < m; i++){
        dp[0][i] = 0;
    }   

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(j == 1){
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][m]) + a[j][i];
            }
            else 
                dp[i][j] = min(dp[i - 1][j] + a[j][i], dp[i - 1][j - 1] + a[j][i]);
        }
    }

    for(int i = 1; i < m; i++){
        res = min(res, dp[n][i]);
    }
    cout << res;
    return 0;
}*/
/*int n, l[5001], w[5001], t = 0;


struct gun{
    int l, w;
}Gun[5002];

int cmp(gun a, gun b){
    if(a.l == b.l){
        return a.w < b.w;
    }
    else{
        return a.l < b.l;
    }
}
int main(){
    cin >> n;
    vector<int>dp(n, 1);
    for(int i = 0; i < n; i++){
        cin >> Gun[i].l >> Gun[i].w;
    }
    sort(Gun,Gun + n,cmp);

    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(Gun[i].l > Gun[j].l ||(Gun[i].l <= Gun[j].l && Gun[i].w > Gun[j].w)){
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        t = max(t, dp[i]);
    }
    cout << t;
    return 0;
}*/
/*vector<int>a;
int i = 0, m = 0, m2 = 0;
int x;

int main(){
    while( cin >> x){
        a.push_back(x);
        if(getchar() == '\n'){
            break;
        }
    }
    int n = a.size();
    vector<int>dp1(n, 1);  
    vector<int>dp2(n, 1);

    for(i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(a[j] >= a[i]){
                dp1[i] = max(dp1[i], dp1[j] + 1);
            }
        }
        m = max(m, dp1[i]);
    }
    
    for(i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(a[j] < a[i]){
                dp2[i] = max(dp2[i], dp2[j] + 1);
            }
        }
        m2 = max(m2, dp2[i]);
    }
    cout << m << endl << m2;
    return 0;
}*/

/*long long m, n;

int main(){
    cin >> m >> n;
    cout << (1 << m) * (n + 1);
    return 0;
}*/
/*int n, m;
int price[105],dp[10005];
int cou = 0;

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> price[i];
    }
    dp[0] = 1;
    for(int i = 0; i < n; i++){
        for(int j = m; j >= price[i]; j--){
            dp[j] += dp[j - price[i]];
        }
    }
    
    cout << dp[m];
    return 0;
}*/
/*int n, m;
int price[30], value[30];
int dp[1000009];
int main(){
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        int temp;
        cin >> price[i] >> temp;
        value[i] = price[i] * temp;
    }

    for(int i = 0; i <= m; i++){
        for(int j = n; j >= price[i]; j--){
            dp[j] = max(dp[j], dp[j - price[i]] + value[i]);
        }
    }
    cout << dp[n];
    return 0;
}
*/
/*int main(){
    int l, r, count = 0;
    cin >> l >> r;
    for(int k = l; k <= r; k++){
        for(int i = 0; i * i <= k; i++){//大的
            int ifang = i * i;
            for(int j = 0; j <= i; j++){
                if(ifang - j * j == k){
                    count++;
                }
            }
        }
    }
    cout << count;
    return 0;
}*/
/*int count1 = 0;
void dfs(int number, int score){//答了几道题，已经得了多少分
    if(score == 70){
        count1++;
    }
    if(score >= 100 || number >= 30){
        return;
    }
    
    dfs(number + 1, score + 10);
    dfs(number + 1, 0);
}

int main(){
    dfs(0, 0);
    cout << count1;    
    return 0;
}*/
/*int main(){
    string s;
    long a, count = 0;
    for(long i = 1; i < 100000000; i++){
        int r1 = 0, r2 = 0;
        s=to_string(i);
        if(s.size() % 2 == 0){
            for(int j = 0; j < s.size() / 2; j++){
                r1 += s[j] - '0';
            }
            for(int j = s.size() / 2; j < s.size(); j++){
                r2 += s[j] - '0';
            }
            if(r1 ==r2){
                count++;
            }
        }
    }
    cout << count;
    return 0;
}*/
/*long long n, value[16010], f[16010], result = -2147483647;
vector<long long>a[16010];

void dfs(long long t, long long father){
    f[t] = value[t];
    for(int i = 0; i < a[t].size(); i++){
        long long temp = a[t][i];//节点t可以连到哪
        if(temp != father){
            dfs(temp, t);
            if(f[temp] > 0){
                f[t] += f[temp];
            }
        }
    }
}
int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> value[i];
    }
    for(int i = 1; i < n; i++){
        int x, y;
        cin >> x >> y;
        a[x].push_back(y);
        a[y].push_back(x);
    }
    dfs(1, 0);
    for(int i = 1; i <= n; i++){
        result = max(result, f[i]);
    }
    if(result < 0){
        result = 0;
    }
    cout << result;
    return 0;
}*/
/*int w, m, n;
int mx, my, nx, ny;

void zuobiao(int a, int b){
    mx = (a - 1) / w;
    nx = (b - 1) / w;
    if(mx % 2 == 0){
        my = a % w;
    }
    else{
        my = w - a % w + 1;
    }
    if(nx % 2 == 0){
        ny = b % w;
    }
    else{
        ny = w - b % w + 1;
    }
}

int main(){
    cin >> w >> m >> n;
    zuobiao(m, n);
    int far = abs(mx - nx) + abs(my - ny);
    cout << far;
    return 0;
}*/
/*const int P =1e9 + 7;
int n, m, k;
vector<vector<int>>a;
long long memory[51][51][13][13];

bool hefa(int a, int b){
    return a < n && b < m;
}
int dfs(int x, int y, int max, int k1){//位置坐标，手里最大的数是多少,现在手里有几个
    if(memory[x][y][max][k1] != -1){
        return memory[x][y][max][k1];
    }
    long long c = 0;
    if(x == n - 1 && y == m - 1){
        if(k1 == k){
            c++;
        } 
    }
    if(hefa(x + 1, y)){
        c += dfs(x + 1, y, max, k1);
        if(a[x + 1][y] > max)
            c = (c + dfs(x + 1, y, a[x + 1][y], k1 + 1)) % P;
    }
    if(hefa(x, y + 1)){
        c += dfs(x, y + 1, max, k1);
        if(a[x][y + 1] > max)
            c = (c + dfs(x, y + 1, a[x][y + 1], k1 + 1)) % P;
    }

    memory[x][y][max][k1] = c % P;
    return memory[x][y][max][k1];
}
int main(){
    cin >> n >> m >> k;
    a.resize(n, vector<int>(m));
    memset(memory, -1, sizeof(memory));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    long long result = dfs(0, 0, 0, 0);
    cout << result % P;
    return 0;
}*/
/*int main(){
    cin >> n;
    int count;
    vector<int>a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    int right = 0, left = 0;//右侧向左，左侧向右
    for(int i = 1; i < n; i++){
        if(abs(a[i]) > abs(a[0]) && a[i] < 0){
            right++;
        }
        if(abs(a[i]) < abs(a[0]) && a[i] > 0){
            left++;
        }
    }
    if((a[0] > 0 && right == 0) || (a[0] < 0 && left ==0)){
        count = 1;
    }
    else{ 
        count = right + left + 1;
    }
    cout << count;
    return 0;
}*/
/*const int N = 100010;

int n;
struct edge{
    int id, w;
};
int dist[N];
vector<edge>h[N];

void dfs(int u, int father, int dis){
    dist[u] = dis;
    for(auto node : h[u]){
        if(node.id != father){
            dfs(node.id, u, dis + node.w);
        }
    }
}


int main(){
    cin >> n;
    for(int i = 0; i < n - 1; i++){
        int p, q, d;
        cin >> p >> q >> d;
        h[p].push_back({q, d});
        h[q].push_back({p, d});
    }
    dfs(1,-1,0);
    int u = 1;
    for(int i = 1; i <= n; i++){
        if(dist[i] > dist[u]){
            u = i;
        }
    }
    dfs(u, -1, 0);
    for(int i = 1; i <= n; i++){
        if(dist[i] > dist[u]){
            u = i;
        }
    }
    int s = dist[u];
    printf("%lld",10*s+s*(s+1ll)/2);
    return 0;
}*/
/*struct d{
    int x;
    int y;
};
int n;
vector<vector<int>>a;
vector<int>vis;
queue<d>b;

int bfs(int m, int di){//从x到y能不能到，有多远，到不了就返回-1，能到就返回有多远。
    d point1;
    point1.x = m;
    point1.y = 0;
    b.push(point1); 
    vis[m] = 1;
    while(!b.empty()){
        d temp = b.front();
        b.pop();
        if(temp.x == di)
            return temp.y;
        else{
            for(int i = 1; i <= n; i++){
                if(vis[i] == 0 && a[temp.x][i] != 0){
                    d temp2;
                    temp2.x = i;
                    temp2.y = temp.y + a[temp.x][i];
                    vis[i] = 1;
                    b.push(temp2);
                }
            }
        }
    }
    return -1;      
}

int cost(int far){
    int c = 0;
    for(int i = 1; i <= far; i++){
        c = c + 10 + i;
    }
    return c;
}

int main(){
    cin >> n;
    a.resize(n + 1, vector<int>(n + 1, 0)); 
    vis.resize(n + 1, 0); 
    int max = 0;
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n; j++){
            a[i][j] = 0;
        }
    }
    for(int i = 0; i < n - 1; i++){
        int p, q, d;
        cin >> p >> q >> d;
        a[p][q] = d;
        a[q][p] = d;
    }
    for(int i = 1; i <= n; i++){
        for(int j = i + 1; j <= n; j++){
            fill(vis.begin(), vis.end(), 0);
            int t = bfs(i, j);
            max = max > t ? max : t;
        }
    }
    cout << cost(max);
    return 0;
}*/
/*int nums[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; 
int x;

int become(int a, int b){
    int sum = 0;
    for(int i = a; i <= b; i++){
        sum = sum * 10 + nums[i];
    }
    return sum;
}
int main(){
    cin >> x;
    int count = 0;
    do{
        for(int i = 0; i < 10; i++){
            for(int j = i + 1; j < 8; j++){
                int o = become(0, i);
                int p = become(i + 1, j);
                int q = become(j + 1, 8);
                if(o + p / q == x && p % q == 0){
                    count++;
                }
            }
        }
    }while(next_permutation(nums, nums + 9));
    cout << count <<endl;
    return 0;
}*/