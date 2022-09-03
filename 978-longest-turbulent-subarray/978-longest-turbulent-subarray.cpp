class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int i, j, ans = 1, flag = 0;
        int val;
        for(i=0;i<arr.size();i++){
            for(j=i+1;j<arr.size();j++){
                // cout<<"Start "<<i<<" "<<j<<"\n";
                // cout<<"IN "<<arr[j-1]<<" "<<arr[j]<<" "<<flag<<"\n";
                if(((arr[j] > arr[j-1]) && (flag == -1 || flag == 0))){
                    // cout<<"Went in 1\n";
                    flag = 1;
                }
                else if(((arr[j-1]> arr[j]) && (flag == 1 || flag == 0) )) {
                    // cout<<"Went in 2\n";
                    flag = -1;
                }
                else{
                    // cout<<"Caught "<<i<<" "<<j<<" "<<flag<<"\n";
                    val = (j-1)-i+1;
                    if(j-i == 1){
                        i = j-1;
                    }
                    else{
                        i = j-2;
                    }
                    flag = 0;
                    if(ans < val){
                        ans = val;
                    }
                    break;
                }
            }
            if(flag == 1 || flag == -1){
                val = (j-1)-i+1; 
                if(ans < val){
                        ans = val;
                }
            }
        }
        return ans;
    }
};