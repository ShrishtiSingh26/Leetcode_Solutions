// Last updated: 7/5/2026, 7:40:53 PM
class Solution {
 public:
  bool check(vector<int>& nums) {
    const int n = nums.size();
    int rotates = 0;

    for (int i = 0; i < n; ++i)
      if (nums[i] > nums[(i + 1) % n] && ++rotates > 1)
        return false;

    return true;
  }
};