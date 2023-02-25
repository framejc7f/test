from TikTokApi import TikTokApi

api = TikTokApi()

# Provide the user registration information
username = "Glebiy"
password = "password"
email = "amil.204323goma@gmail.com"
phone_number = "89786515844"

# Call the register function to create a new TikTok account
api.register(email=email, password=password, phone_number=phone_number, username=username)
