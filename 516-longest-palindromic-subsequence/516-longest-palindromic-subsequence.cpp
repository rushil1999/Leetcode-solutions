class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int dp[s.length()][s.length()];
        memset(dp, 0 , sizeof(dp));
        
        int i, j;
        for( i=0;i<s.length();i++){
            dp[i][i] = 1;
        }
        
        for(i=s.length()-1;i>=0;i--){
            for(j=i+1;j<s.length();j++){
                if(s[i] == s[j]){
                    // cout<<i<<" "<<j<<"\n";
                    dp[i][j] = 2 + dp[i+1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][s.length()-1];
    }
};