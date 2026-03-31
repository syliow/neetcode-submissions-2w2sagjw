class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        //target minus the first item in array, then store it in a value named value1
        // find value 1 in the array and grab the array index for value1 

        for (let i=0; i< nums.length; i++) {
   
           
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i]+ nums[j] === target) {
                return [i,j]
            }
        }
        }
        //else return empty
        return []
    }
}
