while True:
    text = input()
    text_reversed = ""
    if text == "end":
        break

    for ch in reversed(text):
        text_reversed += ch
    print(f"{text} = {text_reversed}")


