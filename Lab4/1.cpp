#include <iostream>
#include <vector>
#include <unordered_map>
#include <limits>
#include <chrono>
#include <cstdlib>
#include <ctime>


using namespace std;

unordered_map<int, unordered_map<string, int>> get_info(const vector<int>& arr) {
    unordered_map<int, int> is_exist;
    unordered_map<int, unordered_map<string, int>> info;
    for (int i = 0; i < arr.size(); i++) {
        info[i] = {{"left", numeric_limits<int>::lowest()}, {"right", numeric_limits<int>::max()}};
        if (is_exist.find(arr[i]) != is_exist.end()) {
            info[i]["left"] = is_exist[arr[i]];
            info[is_exist[arr[i]]]["right"] = i;
        }
        is_exist[arr[i]] = i;
    }
    return info;
}

unordered_map<int, unordered_map<string, int>> dic;

bool is_unique_point(int start, int end, int index) {
    if (dic[index]["left"] < start && dic[index]["right"] > end) {
        return true;
    }
    else {
        return false;
    }
}

bool is_non_boring(int start, int end) {
    int r = start;
    int l = end;
    if (start >= end) {
        return true;
    }
    while (r <= l) {
        if (is_unique_point(start, end, r)) {
            return is_non_boring(start, r - 1) && is_non_boring(r + 1, end);
        }
        if (is_unique_point(start, end, l)) {
            return is_non_boring(start, l - 1) && is_non_boring(l + 1, end);
        }
        r += 1;
        l -= 1;
    }
    return false;
}

vector<int> generateRandomList(int length, int minVal, int maxVal) {
    vector<int> lst(length);

    // 初始化随机数生成器
    srand(time(NULL));

    // 生成随机数并添加到列表中
    for (int i = 0; i < length; i++) {
        lst[i] = minVal + rand() % (maxVal - minVal + 1);
    }

    return lst;
}

int main() {
    vector<int> arr = generateRandomList(200000, 1, 10000000);

    auto start = chrono::high_resolution_clock::now();
    dic = get_info(arr);
    if (is_non_boring(0, arr.size() - 1)) {
        cout << "non-boring" << endl;
    }
    else {
        cout << "boring" << endl;
    }
    // 在这里放置你要计时的代码
    // ...

    // 停止计时
    auto stop = chrono::high_resolution_clock::now();

    // 计算运行时间并输出
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout << "运行时间: " << duration.count() << " 微秒" << endl;



    // int t;
    // cin >> t;
    // while (t > 0) {
    //     t -= 1;
    //     int n;
    //     cin >> n;
    //     vector<int> arr(n);
    //     for (int i = 0; i < n; i++) {
    //         cin >> arr[i];
    //     }
    //     dic = get_info(arr);
    //     if (is_non_boring(0, arr.size() - 1)) {
    //         cout << "non-boring" << endl;
    //     }
    //     else {
    //         cout << "boring" << endl;
    //     }
    // }
    return 0;
}

