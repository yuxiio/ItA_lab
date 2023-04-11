#include <bits/stdc++.h>
using namespace std;
// int arr[200000+100] = {0};
vector<int> lst;
int tran(char c){
    if (c=='B') return 1;
    else  return 0;
}

int findShortestSubarray(std::vector<int> nums, int targetSum) {
    int n = nums.size();
    int left = 0, right = 0;
    int sum = 0;
    int minCnt = n + 1;
    int cnt_recolor = 0;
    
    while (right < n) {
    	// cout << "right: " << right << endl;
    	// cout << "left: " << left << endl;
    	// cout << "cnt_recolor: " << cnt_recolor << endl;
    	// cout << "minCnt: " << minCnt << endl;
        if(nums[right]==0){
        	sum += 1;
        	cnt_recolor += 1;
        }else sum += nums[right];

        while (sum > targetSum) {
            // sum -= nums[left];
            if(nums[left]==0){
        	    sum -= 1;
        	    cnt_recolor -= 1;
            }else sum -= nums[left];
            left++;
        }

        if (sum == targetSum && cnt_recolor < minCnt) {
            minCnt = cnt_recolor;
        }

        right++;
    }

    return minCnt;
}


int main (void) {
    auto tran_lambda = [](auto c){
        if (c=='B') return 1;
        else return 0;
    };
    int T;
    cin >> T;
    // cout << T;
    while(T--){
    	// cout << "hhh" << endl;
        int n;
        int k;
        int k_temp = 0;
        bool is_ok = false;
        // bool is_continuous = false;
        cin >> n >> k;
        // cout << n << k << endl;
        getchar();//fuck!!!
        for (int i=0;i<n;++i){
        	// cout << i;
            char c;
            scanf("%c",&c);
            // cout << c ;
            // arr[i] = tran_lambda(c);
            int ans = tran_lambda(c);
            // if (arr[i]==1){
                // k_temp++;
                // is_continuous = true;
            // }else{
                // if(is_continuous) lst.push_back(k_temp);
                // is_continuous = false;
                // lst.push_back(0);
                // k_temp=0;
            // }
            // if(i==n-1&&is_continuous){
            	// lst.push_back(k_temp);
            // }
            if(ans==1){
            	k_temp ++;
            }else{
            	k_temp = 0;
            }
            lst.push_back(ans);
            if(k_temp==k) is_ok = true;
        }
        // for (int i=0;i<n;++i){
        //     cout << arr[i];
        // }
        // cout << endl;
        // if(is_ok) cout << 0 << endl;
        // for (int i:lst){
            // cout << i;
        // }
        // cout << endl;
        if(is_ok){
            cout << 0 << endl;
            lst.clear();
            continue;
        }
        
        cout << findShortestSubarray(lst, k) << endl;
        lst.clear();
    }


    return 0;
}