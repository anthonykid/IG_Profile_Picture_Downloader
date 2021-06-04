import instaloader

bot = instaloader.Instaloader()
username = "github" #you need to input the username inside here to download the profile picture that you want to
print(bot.download_profile(username, profile_pic_only=True))