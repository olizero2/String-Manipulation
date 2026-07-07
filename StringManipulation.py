sentence = "I like dogs"

print(sentence.find("dogs"))


list = ["Diana ", "Mola ", "Aba "]

newsentence = "no i ".join(list)

print(newsentence)

choice = input("Whats your name?")

if choice.strip().lower().startswith("o"):
    print("no i dont like people with O")