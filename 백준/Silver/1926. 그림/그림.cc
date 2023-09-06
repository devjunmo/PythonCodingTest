#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
int arr[501][501];
bool visited[501][501];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int bfs(int x, int y) {
    visited[x][y] = true;
    queue<pair<int, int>> q;
    q.push({x, y});

    int area = 0;

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();
        area++;

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                if (arr[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }
    return area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int maxArea = 0;
    int count = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 1 && !visited[i][j]) {
                maxArea = max(maxArea, bfs(i, j));
                count++;
            }
        }
    }

    cout << count << '\n';
    cout << maxArea << '\n';

    return 0;
}
