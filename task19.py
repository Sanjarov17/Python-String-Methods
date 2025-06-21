matn =input("Matn kiriting:  ")

matn_kichik = matn.lower()

if not matn_kichik.isdigit():
    print(True)
else:
    print(False)
