#include <iostream>
#include <queue>

using namespace std;

bool check_top_rank(int ds_vote_cnt, int etc_max_val) {
    return ds_vote_cnt > etc_max_val;
}

int main() {
    int N, ds_vote_cnt, num, res = 0;
    priority_queue<int> etc_vote_cnt_heap;

    cin >> N >> ds_vote_cnt;

    for (int i = 1; i < N; ++i) {
        cin >> num;
        etc_vote_cnt_heap.push(num);
    }

    if (etc_vote_cnt_heap.empty()) {
        cout << res << endl;
        return 0;
    }

    while (true) {
        if (check_top_rank(ds_vote_cnt, etc_vote_cnt_heap.top())) {
            break;
        }

        int etc_max_val = etc_vote_cnt_heap.top();
        etc_vote_cnt_heap.pop();

        ds_vote_cnt += 1;
        etc_max_val -= 1;

        if (etc_max_val > 0) {
            etc_vote_cnt_heap.push(etc_max_val);
        }

        res += 1;
    }

    cout << res << endl;
    return 0;
}
