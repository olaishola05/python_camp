class User:

    def __init__(self, user_id, name, username):
        self.id = user_id
        self.name = name
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


ade = User("0001", "Adebola Ajayi", "ajay")
peju = User("0002", "Peju Asanke", "peejay")

ade.follow(peju)
peju.follow(ade)

print(ade.follower)
print(ade.following)

print("----- Other User -----")

print(peju.follower)
print(peju.following)
