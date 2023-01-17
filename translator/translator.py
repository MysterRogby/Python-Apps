import json

with open("morse.json") as f:
    dict = json.load(f)

print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
text = input("Enter your text to encode without special characters.\nNormal Text: ")
text = text.upper()
encoded = ""
for char in text:
    encoded = encoded + dict.get(char, "🐧") + " "

print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
print("Encoded Text: ", encoded)
print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
