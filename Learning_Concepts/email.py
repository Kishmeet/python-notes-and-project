email=input("enter your email: ")
username=email[:email.index("@")]
domain=email[email.index("@")+1:email.index(".")]
print(f"your username is {username} and your domain is {domain}")