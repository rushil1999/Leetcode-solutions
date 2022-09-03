class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int i, j=0, ans = 1, flag = 0;
        int val, start=0;
        for(j=start+1;j<arr.size();j++){
            // if(flag == 0){
            //     start = j;
            // }
            // cout<<"Start " <<start<<" "<<j<<"\n";
            if(((arr[j] > arr[j-1]) && (flag == -1 || flag == 0))){
                flag = 1;
            }
            else if(((arr[j-1]> arr[j]) && (flag == 1 || flag == 0) )) {
                flag = -1;
            }
            else{
                // cout<<"Caught "<<j<<"\n";
                val = (j-1)-start+1;
                if(j-start == 1){
                    // cout<<"Hey\n";
                    start = j;
                }
                else{
                    start = j-1;
                }
                j = start;
                flag = 0;
                if(ans < val){
                    ans = val;
                }
                // break;
            }
        }
        if(flag == 1 || flag == -1){
            // cout<<"Final "<<start<<" "<<j<<"\n";
            val = (j-1)-start+1; 
            if(ans < val){
                    ans = val;
            }
        }
        
        return ans;
    }
};