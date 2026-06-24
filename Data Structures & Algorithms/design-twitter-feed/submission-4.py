class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followMap = defaultdict(set) #[followerId: followeeId]
        self.tweetMap = defaultdict(list) #[userId: tweetId, timestamp]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1 #smaller = recent
        self.tweetMap[userId].append([tweetId, self.timestamp])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        
        self.followMap[userId].add(userId)
        #fetch the tweets from user follow list 
        for followeeId in self.followMap.get(userId):
            if followeeId in self.tweetMap:
                #get latest tweet
                index = len(self.tweetMap.get(followeeId)) - 1
                tweetId, timestamp = self.tweetMap.get(followeeId)[index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index])
        
        res = [] #tweetId
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index - 1 >= 0:
                nextTweetId, nextTimestamp = self.tweetMap[followeeId][index - 1]
                heapq.heappush(minHeap, [nextTimestamp, nextTweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId != followerId:
            self.followMap[followerId].discard(followeeId)