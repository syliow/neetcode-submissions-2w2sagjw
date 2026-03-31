class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const new1 = s.split("").sort().join("")
        const new2= t.split("").sort().join("")

        if (new1 === new2) {
            return true
        }else {
            return false
        }
    }
}
