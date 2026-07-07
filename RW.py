from gettext import find

with open("C:/Users/olafg/OneDrive/Documents/randomtext.txt", "r") as file:
    content = file.read().lower()

    print("""
    """)
    print("-----")
    print(content)

    place = content.find("oli")
    print(f"'oli' starts in the {place} place!")