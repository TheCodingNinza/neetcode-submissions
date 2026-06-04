class Twitter:

    def __init__(self):
        self.time  = 0
        self.followerFolloweeMap = {}
        self.followeeFollowerMap = {}
        self.usersTweetsMap = {}
        self.usersNewsfeedMap = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followerFolloweeMap and userId not in self.followeeFollowerMap:
            self.followerFolloweeMap[userId] = [userId]
            self.followeeFollowerMap[userId] = [userId]
        self.time -= 1
        if userId not in self.usersTweetsMap:
            self.usersTweetsMap[userId] = []
        self.usersTweetsMap[userId].append((tweetId, self.time))

        if userId not in self.followeeFollowerMap:
            self.followeeFollowerMap[userId] = [] 
        followers = self.followeeFollowerMap[userId]

        for follower in followers:
            self.insertPostIntoNewsfeed(follower, tweetId, self.time)  

        # print(self.usersNewsfeedMap)     

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.usersNewsfeedMap)
        if userId not in self.usersNewsfeedMap:
            self.usersNewsfeedMap[userId] = []

        content = self.usersNewsfeedMap[userId].copy()

        maxValue = 0

        if len(content) < 10:
            maxValue = len(content) 
        else:
            maxValue = 10

        tweets = []

        for i in range(maxValue):
            (timestamp, tweetId) = heapq.heappop(content)
            # print("timestamp: "+str(timestamp))
            # print("tweetId: "+str(tweetId))
            tweets.append(tweetId)

        # print(tweets)    

        return tweets    

        
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if  followerId not in self.followerFolloweeMap:
            self.followerFolloweeMap[followerId] = []

        if followeeId not in  self.followeeFollowerMap:   
            self.followeeFollowerMap[followeeId] = []    

        if followeeId  in self.followerFolloweeMap[followerId]:
            return

        self.followerFolloweeMap[followerId].append(followeeId)
        self.followeeFollowerMap[followeeId].append(followerId)       
 
        if followeeId not in self.usersTweetsMap:
            self.usersTweetsMap[followeeId] = []
        tweets =  self.usersTweetsMap[followeeId]
        for tweet in tweets:
            self.insertPostIntoNewsfeed(followerId, tweet[0], tweet[1])
               

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerFolloweeMap:
            self.followerFolloweeMap[followerId] = []
            self.followeeFollowerMap[followeeId] = []
        if followerId == followeeId:
            return
        if followeeId in self.followerFolloweeMap[followerId]:
            self.followerFolloweeMap[followerId].remove(followeeId)
         
        if followerId in self.followeeFollowerMap[followeeId]:
            self.followeeFollowerMap[followeeId].remove(followerId)    

        self.deletePostFromNewsfeed(followerId, followeeId)    


    def insertPostIntoNewsfeed(self, userId: int, tweetId: int, time: int) -> None:
        if userId not in self.usersNewsfeedMap:
            self.usersNewsfeedMap[userId] = []   
        heapq.heappush(self.usersNewsfeedMap[userId], (time, tweetId))

    def deletePostFromNewsfeed(self, userId: int, followeeId: int) -> None:
        if userId not in self.usersNewsfeedMap:
            self.usersNewsfeedMap[userId] = []

        followeeTweets = self.usersTweetsMap[followeeId]
        print("followeeTweets: " + str(followeeTweets))
        followeeTweetIds = []   
        for i in range(len(followeeTweets)):
            followeeTweetIds.append(followeeTweets[i][0])
         
        print(followeeTweetIds)  
        tweets = self.usersNewsfeedMap[userId]
        removedTweets = []

        while tweets:
            (timestamp, tweetId) = heapq.heappop(tweets)
            
            if tweetId not in followeeTweetIds:
                removedTweets.append((timestamp, tweetId)) 

        for i in range(len(removedTweets)):
            heapq.heappush(tweets, removedTweets[i])       
        
