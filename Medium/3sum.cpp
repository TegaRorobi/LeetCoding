# include <iostream>
# include <string>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        for (int& i : nums){
            for (int& j: nums){
                for (int& k:nums){
                    // cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
                    if (i+j+k == 0){
                        cout << i << ' '<< j << ' ' << k << "sum->" << i+j+k <<endl;
                        if (true){
                            vector<int> val = {i, j, k};
                            ans.push_back(val);
                        }
                    }
                }
            }
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    std::vector<int> v = {-1,0,1,2,-1,-4};   
    Solution.threeSum(v);
    return 0;
}