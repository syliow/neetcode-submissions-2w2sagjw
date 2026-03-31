class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
      nums.sort((a,b)=>a-b);
      for (let i= 1; i < nums.length; i++){
        //compare against prev number
        if (nums[i]=== nums[i-1]){
            return true;
        }
      }
     return false;
    }
}
