#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size();

        // Build the hash table
        for (int i = 0; i < n; i++) {
            numMap[nums[i]] = i;
        }

        // debugging hashmap as it was new to me
        for (const auto& pair : numMap)
        {
            cout << "Key: " << pair.first << " Value: " << pair.second << endl;
        };
        

        // Find the complement
        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.count(complement) && numMap[complement] != i) {
                return {i, numMap[complement]};
            }
        }

        return {}; // No solution found
    }

int main(){

    int target = 9;
    vector<int> nums= {2,7,11,15};

    twoSum(nums, target);

    return 0;
}