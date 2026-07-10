class Twitter:
    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)  # (userId: set() -> followeeId)
        self.tweetMap = defaultdict(list)  # (userId: [tweetId, count])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1  # smaller = latest
        self.tweetMap[userId].append([tweetId, self.count])

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        # user should follow themselves
        self.followMap[userId].add(userId)
        # get user following list
        # get tweets from following list
        followList = self.followMap.get(userId)
        for followeeId in followList:
            if self.tweetMap[followeeId]:
                # get latest tweet
                index = len(self.tweetMap.get(followeeId)) - 1
                tweetId, timestamp = self.tweetMap.get(followeeId)[index]
                heapq.heappush(
                    minHeap, [timestamp, tweetId, followeeId, index]
                )  # sort by timestamp
        res = []
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # get next tweet
            if index - 1 >= 0:
                nextTweetId, nextTimestamp = self.tweetMap[followeeId][index - 1]
                heapq.heappush(minHeap, [nextTimestamp, nextTweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)
