text = input()
final_text = ""
last_character = ""
for current_index in text:
    if current_index != last_character:
        final_text += current_index
        last_character = current_index
print(final_text)