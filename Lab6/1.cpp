#include <bits/stdc++.h>

using namespace std;

int arr[200000+200] = {0};
int op[200000+200] = {0};

int main(void){
    int T;
    cin >> T;
    while (T--){
        int n;
        int k;
        cin >> n >> k;
        for(int i=0;i<n;++i){
            scanf("%1d",&arr[i]);
        }
        for (int i=0;i<n;i++)
        	op[i] = 0;
        if(k==0){
        	for(int i=0;i<n;i++){
        		cout << arr[i];
        	}
        	cout << "\n";
        	for (int i=0;i<n;i++){
                cout << 0 << " ";
            }
            cout << "\n";
            continue;
        }
        if (k%2){
            //奇数
            for (int i=0;i<n;i++){
                if(arr[i]) {
                    --k;
                    op[i] += 1;
                }else {
                    ;
                }
                if(k==0){
                    break;
                }
            }
            if (k!=0){
                op[n-1] += k;
            }
            for (int i=0;i<n;i++){
                if(op[i]%2) cout << arr[i];
                else cout << !arr[i];
            }
            cout << '\n';
            for (int i=0;i<n;i++){
                cout << op[i] << " ";
            }
            cout << '\n';
        }
        else{
            //偶数
            for (int i=0;i<n;i++){
                if(arr[i]) {
                    ;
                }else {
                    --k;
                    op[i] += 1;
                }
                if(k==0){
                    break;
                }
            }
            if (k!=0){
                op[n-1] += k;
            }
            for (int i=0;i<n;i++){
                if(op[i]%2) cout << !arr[i];
                else cout << arr[i];
            }
            cout << '\n';
            for (int i=0;i<n;i++){
                cout << op[i] << " ";
            }
            cout << '\n';
        }
    }


    return 0;
}