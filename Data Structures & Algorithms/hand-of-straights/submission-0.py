class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #need to make sure each group is equal
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                #start form a group
                for i in range(num, num + groupSize):
                    #if the num count is not 0
                    #otherwise decrement count
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True