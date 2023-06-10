# include <iostream>
# include <string>
# include <vector>
using std::cout;
using std::vector;
using std::endl;


// class Solution {
// public:
vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> ans;
    for (int& i : nums){
        for (int& j: nums){
            for (int& k:nums){
                // cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
                if (i+j+k == 0){
                    // cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
                    vector<int> val = {i, j, k};
                    ans.push_back(val);
                }
            }
        }
    return ans;
    }
};


// vector<vector<int>> threeSum(vector<int> &nums)
// {   
//     ind = 0
//     for (int& a: nums)
//     {   

//         int l = ind+1;
//         int r = nums.size() -1;
        
//         while(l < r)

//         ind++
//     }
// }

int main(int argc, char const *argv[])
{
    vector<int> v = {-1,0,1,2,-1,-4};   
    vector<vector<int>>res = threeSum(v);
    for (auto arr: v)
    {
        cout <<arr;
        for (auto num:arr)
        {
            cout << '[';
            cout << num;
            cout << "], ";
        }
        // cout << "]";
    }
}