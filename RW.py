from gettext import find

with open("C:/Users/olafg/OneDrive/Documents/randomtext.txt", "r") as file:
    content = file.read().lower()

    print("""
    """)
    print("-----")
    print(content)

    if "oli" in content:
        print("Okay you're there")
    else:
        print("you're not there, so ill add you")
        with open("C:/Users/olafg/OneDrive/Documents/randomtext.txt", "a") as file:
            file.write(" oli")