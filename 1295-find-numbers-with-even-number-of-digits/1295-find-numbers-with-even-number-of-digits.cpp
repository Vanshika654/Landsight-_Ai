class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans=0;
        for(int i=0;i<nums.size();i++){
            int m=nums[i];
            int digits=0;
            if(m==0){
                digits=1;
            }else{
                while(m>0){
                m/=10;
                digits++;
            }
            }
            if(digits%2==0){
                ans++;
            }
        }
        return ans;
    }
};