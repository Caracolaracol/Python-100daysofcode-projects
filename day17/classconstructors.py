class User:
    def __init__(self, user_id, username): # to create a constructor we use __init__ a special function
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(username="angela",user_id="001" )
user_2 = User("002", "jack")

print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)


