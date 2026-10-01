"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
length_before = len(raw_message)
new_message = raw_message

# Apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper

new_message = new_message.strip()
new_message.title()

new_message = list(new_message)
for i, char in enumerate(new_message):
    if new_message[i-1] == " " and new_message[i-2] == ".":
        new_message[i] = new_message[i].upper()
    else:
        new_message[i] = new_message[i].lower()

new_message[0] = new_message[0].upper()
new_message = "".join(new_message)
new_message = ' '.join(new_message.split())
# Display the original and cleaned messages
print(f"Before: {raw_message}")
print(f"After: {new_message}")

# Extension: display the character counts for each version
print(f"Raw messsage length: {length_before}")
print(f"New message length: {len(new_message)}")
