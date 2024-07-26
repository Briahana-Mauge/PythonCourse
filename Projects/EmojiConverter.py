# When a user enters text with emoticons, reprint their text with the emoji equivalent

message = input("Enter text here: ")
words = message.split(" ")
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
print(result)