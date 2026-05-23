class Twitter:

    def __init__(self):
        #count -> decreasing timestamp for tweet order
        #follow map -> followerId: set (followeeId)
        #tweet map -> userId: [tweetId, timestamp]
        self.count = 0
        self.followMap = defaultdict(set) #set (followeeId)
        self.tweetMap = defaultdict(list) #userId -> [tweetId, count]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1 #smaller means more recent
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        #min heap = timestamp smaller = latest
        minHeap = []
        heapq.heapify(minHeap)

        #make sure user follow themselves
        self.followMap[userId].add(userId)
        
        #get user following list
        followList = self.followMap.get(userId)
        #loop each user and fetch their most recent tweets (last index)
        for followeeId in followList:
            if followeeId in self.tweetMap:
                #grab latest tweet
                index = len(self.tweetMap.get(followeeId)) - 1
                #get timestamp and tweetId from latest tweet
                timestamp, tweetId = self.tweetMap[followeeId][index]
                #push to minheap
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index])
        
        res = [] #tweetId
        #fetch 10 latest tweet, res must be < 10
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            #push tweetid to res
            res.append(tweetId)

            #check if user has anymore tweets, if yes push back to heap
            if index - 1 >= 0:
                count, tweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
               
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #only proceed if followeeId is in followerId follow
        if followeeId in self.followMap.get(followerId, set()):
            self.followMap[followerId].remove(followeeId)
