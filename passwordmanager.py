import random
import string

passwords = {}
MASTER_PASSWORD = "admin123"  # yeh change kr lena apni marzi se

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(" : ")
            passwords[website] = pwd
except:
    pass


def save_to_file():
    with open("password.txt", "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site} : {pwd}\n")


def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%!&?"
    password = "".join(random.choice(chars) for _ in range(12))
    return password


def check_strength(pwd):
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in "@#$%!&?" for c in pwd)
    length_ok = len(pwd) >= 8

    score = sum([has_upper, has_lower, has_digit, has_special, length_ok])

    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


def smart_suggest(site):
    # site ke naam se thora mix banao
    base = site[:3] if len(site) >= 3 else site
    mixed = base[0].upper() + base[1:].lower()
    extras = "".join(random.choice("@#$%!&?") for _ in range(2))
    nums = "".join(random.choice(string.digits) for _ in range(3))
    rest = "".join(random.choice(string.ascii_letters) for _ in range(4))
    return mixed + rest + nums + extras


# ========= MASTER PASSWORD CHECK =========
print("\n==============PERSONAL PASSWORD MANAGER==============")
attempts = 3
while attempts > 0:
    master = input("Enter master password: ")
    if master == MASTER_PASSWORD:
        print("Welcome! ✅")
        break
    else:
        attempts -= 1
        print(f"Wrong password! {attempts} attempts left ❌")

if attempts == 0:
    print("Access denied! Exiting...")
    exit()


# ========= MAIN MENU =========
while True:

    print("\n==============PERSONAL PASSWORD MANAGER==============")
    print("1. Save password ")
    print("2. View password ")
    print("3. Generate password ")
    print("4. Search password ")
    print("5. Update password ")
    print("6. Delete password ")
    print("7. Exit ")

    choice = input("enter your choice? :")

    if choice == "1":
        site = input("enter website: ")
        pwd = input("enter password: ")
        strength = check_strength(pwd)
        print(f"Password Strength: {strength}")
        passwords[site] = pwd
        save_to_file()
        print("saved! ")

    elif choice == "2":
        if not passwords:
            print("no data ")
        else:
            for site, pwd in passwords.items():
                print(site, " : ", pwd)

    elif choice == "3":
        site = input("enter website name for smart suggestion: ")
        suggested = smart_suggest(site)
        print(f"Suggested password: {suggested}")
        print(f"Strength: {check_strength(suggested)}")
        use = input("use this password? (y/n): ")
        if use == "y":
            passwords[site] = suggested
            save_to_file()
            print("saved! ")

    elif choice == "4":
        site = input("enter website to search: ")
        if site in passwords:
            print(site, " : ", passwords[site])
        else:
            print("not found! ")

    elif choice == "5":
        site = input("enter website to update: ")
        if site in passwords:
            new_pwd = input("enter new password: ")
            strength = check_strength(new_pwd)
            print(f"Password Strength: {strength}")
            passwords[site] = new_pwd
            save_to_file()
            print("updated! ")
        else:
            print("not found! ")

    elif choice == "6":
        site = input("enter website to delete: ")
        if site in passwords:
            del passwords[site]
            save_to_file()
            print("deleted! ")
        else:
            print("not found! ")

    elif choice == "7":
        print("bye !")
        break

    else:
        print("INVALID OUTPUT")