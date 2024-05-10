# Extract a function from emoji converter

def emoji_converter(message):
    words = msg.split(" ")
    emojis = {
        ":)": "😊",
        ":(":"😒"
    }

    new_msg = ""

    for word in words:
        new_msg += f"{emojis.get(word, word)} "

    return new_msg
 

msg = input("> ")
print(emoji_converter(msg))   