class Solution {
public:
    
    
    
    int knightDialer(int n) {
        int dp[n+1][10];
        long long int mod = 1000000007;
        memset(dp, 0, sizeof(dp));
        int i, j, k;
        for(i=0;i<10;i++){
            dp[1][i] = 1;
        }
        
        map<int, vector<int>> m;
        m[0] = {4,6};
        m[1] = {6,8};
        m[2] = {7,9};
        m[3] = {4,8};
        m[4] = {3,9, 0};
        m[5] = {};
        m[6] = {7,1, 0};
        m[7] = {2,6};
        m[8] = {1,3};
        m[9]= {2,4};
        
    
        for(i=0;i<10;i++){
            dp[1][i] = 1;
        }
        
        for (i=2;i<=n;i++){
            for(j=0;j<10;j++){
                for(k =0;k<m[j].size();k++){
                    // cout<<j<<" "<<m[j][k]<<"\n";
                    dp[i][j] = (dp[i][j]%mod + dp[i-1][m[j][k]]%mod) %mod;
                }
            }
        }
        long long int total = 0;
        for(i=0;i<10;i++){
            // cout<<i<<" "<<dp[n][i]<<"\n";
            total += dp[n][i]%mod ;
        }
        
        return (total%mod);
        
        
    }
};