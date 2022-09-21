class Solution {
public:
    int rob(vector<int>& nums) {
        int dp[nums.size()][2];
        memset(dp, 0 , sizeof(dp));
        int robCurrent = nums[0];
        int robNext =0;
        for(int i =1;i<nums.size();i++){
            int val = robNext;
            robNext = max(robCurrent, robNext);
            robCurrent = nums[i] + val;
         }
        int val = max(robCurrent,robNext );
        return val;
    }
};