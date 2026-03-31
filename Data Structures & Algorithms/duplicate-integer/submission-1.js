class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let numSet = new Set()

        for (let n of nums){
            if (numSet.has(n)) return true
            //if does not exist in set, we add it to set
            numSet.add(n)
        }
        return false
    }
}
