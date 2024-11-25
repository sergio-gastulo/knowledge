#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target)
{
    vector<int> ret;
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == target && i != j)
            {
                ret.push_back(i); ret.push_back(j);
                return ret;
            };
        };
    };
    return ret;
};

int main(){

    int targets = 6;
    vector<int> nums= {3,3};

    for( int i : twoSum(nums, targets)){
        cout << i << " ";
    }; cout << endl; 

    return 0;
}