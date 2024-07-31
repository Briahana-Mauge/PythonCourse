def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")


# print("start")
# greet_user("bri")
# greet_user("mary")
# print("end")


def square(number):
    return number * number

# print(square(3))


#Problem: rewrite the emoji converter program into a reusable function

message = input("Enter text here: ")
def emoji_converter(text):
    words = text.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "🙁",
        "):": "🙃",
        ":D": "😀",
        ":P": "😛",
        "xP": "😝",
        ";P": "😜",
        "XD": "😆",
        "=)": "😃",
        ";)": "😉",
        ":-*": "😘",
        "(<3)": "🫶🏽",
        "<3": "♡❤️",
        ":o":"😯",
        ":O": "😮",
        ":-?": "🤔"
    }
    new_sentence = []

    for word in words:
        if emojis.get(word):
            new_sentence.append(emojis[word])
        else: 
            new_sentence.append(word)

    result = " ".join(new_sentence)
    return result

print(emoji_converter(message))