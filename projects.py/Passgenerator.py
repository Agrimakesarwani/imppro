import random
import string

print(
    "Hello ! This code generate a random password  , If you want to generate the password then enter the desired lenghth below - "
)

pass_len = int(input("Enter here \n"))
# combine all the characters type

chars = string.ascii_letters + string.digits + string.punctuation
# create passwors by picking random one

while True:

    passwords = "".join(
        random.choice(chars) for i in range(pass_len)
    )  #''is separator (empty string,so no spaces)
    print("\n Your generated password is : ", passwords)
    choice = (
        input("\n Do you like this password ? (yes/no) or (y/n) :  ").strip().lower()
    )

    if choice in ["yes", "y"]:
        print("\n Password is accepted by the user ")
        break

    else:
        print("\n Generating a new passwords ")
