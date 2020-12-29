#zad

import re

text = "SZczecin TO miasto w Polsce, w województwie ZAchodniopomorskim"

pattern_search_long = r"\b([A-Z]{2}[a-z]+)\b"
pattern_search_short = r"\b[A-Z]{2}\b"

result = re.sub(pattern_search_long, lambda  x: x.group(0).capitalize(), text)
short_replacements = re.findall(pattern_search_short, text)
for item in short_replacements:
    user_answer = input(f"Możliwy błąd: {item}. Czy chcesz poprawić (T/N)?\n")
    if user_answer == "T":
        result = re.sub(item, item.capitalize(),  result)

print(result)
