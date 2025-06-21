username = input("GitHub username kiriting: ")

tozalangan = username.replace("-","" )

if tozalangan.isalnum():
    print(True)
else:
    print(False)
