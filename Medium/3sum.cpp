# include <iostream>
# include <string>
# include <vector>
# include <bits/stdc++.h>
using std::cout;
using std::vector;
using std::endl;


// class Solution {
// public:
// vector<vector<int>> threeSum(vector<int>& nums) {
//     vector<vector<int>> ans;
//     for (int& i : nums){
//         for (int& j: nums){
//             for (int& k:nums){
//                 // cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
//                 if (i+j+k == 0){
//                     // cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
//                     vector<int> val = {i, j, k};
//                     ans.push_back(val);
//                 }
//             }
//         }
//     return ans;
//     }
// };


vector<vector<int>> threeSum(vector<int> &nums, int target)
{   
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); ++i)
    {
        if ((i>0)&&(nums[i] == nums[i-1])){
            continue;
        }

        int l=i+1, r=nums.size()-1;

        while(l < r){

            int threesum = nums[i] + nums[l] + nums[r];

            if(threesum < target){
                l++;


            } else if(threesum > target){
                r--;


            } else {
                vector<int> ansVec = {nums[i], nums[l], nums[r]};
                res.push_back(ansVec);
                l++;

                while ((l>0) && (nums[l]==nums[l-1])){
                    l++;
                };
            }

        }
    }
    return res;
}


int main()
{
    vector<int> v = {-1,0,1,2,-1,-4};   
    vector<vector<int>>res = threeSum(v, 0);
    for (vector<int> arr: res){
        cout << "[ ";

        for (int num:arr){
            cout << num << " ";
        }

        cout << "]\n";
    }
    cout << endl << "End main function";

    return 0;
}