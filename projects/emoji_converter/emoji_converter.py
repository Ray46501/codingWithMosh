msg = input("> ")
words = msg.split(" ")
emojis = {
":)": "😄",
":(":"🙁"
}

new_msg = ""

for word in words:
    new_msg += f"{emojis.get(word, word)} "

print(new_msg)    