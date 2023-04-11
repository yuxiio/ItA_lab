#include <iostream>
#include <vector>

using namespace std;

long long cnt;
long long level;    //层数
long long zongshu = 1;  //总数
vector<long long> q;

void init(long long x)
{
    if (x == 2 || x == 3) return;

    init(x / 2);
    level ++;
}

void count(int level)
{
    if (level == 0) 
    {
        zongshu = 7;
        return;
    }

    for (int i = 1; i <= level + 2; i ++ )
    {
        zongshu *= 2;
    }
    zongshu -= 1;
}

void did(long long x, long long l, long long r)
{
    if (x == 1 || x == 0) 
    {
        cnt ++;
        if (cnt >= l && cnt <= r) q.push_back(x);
        return;
    }

    level = 0;
    zongshu = 1;
    init(x);
    count(level);
    long long length = (zongshu - 1) / 2;

    if (cnt <= r) 
    {
        if (cnt >= l || l <= length + cnt)
        {
            did(x / 2, l, r);
            did(x % 2, l, r);
            did(x / 2, l, r);
        }
        else 
        {
            cnt += length;
            did(x % 2, l, r);
            did(x / 2, l, r);
        }
    }
    else return;
}

int main()
{
    long long sum = 0;
    long long n, l, r;
    cin >> n >> l >> r;

    did(n, l, r);
    for (int i = 0; i < q.size(); i ++ )
    {
        sum += q[i];
        //cout << q[i] << ' ';
    }

    cout << sum << endl;

    return 0;
}