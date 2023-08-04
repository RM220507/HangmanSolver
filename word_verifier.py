import json
from unidecode import unidecode

print("Loading words...", end="")
with open("master-words.txt", "r", encoding="utf-8") as f:
    words = f.readlines()
print("DONE.")

refined_words = {}

print("Scanning words...")
for i, word in enumerate(words):
    word = unidecode(word)
    word = word[:-1]
    word = word.lower()

    if "-" in word:
        continue

    if len(word) not in refined_words.keys():
        refined_words[len(word)] = [word]
    else:
        refined_words[len(word)].append(word)
    
    if i % 10000 == 0:
        print(f"{i} words scanned.")
print("Scanning complete.")

print("Saving refined words...", end="")
with open("refined-words.json", "w", encoding="utf-8") as f:
    json.dump(refined_words, f, ensure_ascii=False)
print("DONE.")

print("Word Verification Complete.")