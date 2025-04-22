VOWELS = set("aeiou")

def is_acceptable(word):
    has_vowel = False
    vowel_streak = 0
    consonant_streak = 0
    prev_char = ""

    for ch in word:
        if ch in VOWELS:
            has_vowel = True
            vowel_streak += 1
            consonant_streak = 0
        else:
            consonant_streak += 1
            vowel_streak = 0

        if vowel_streak >= 3 or consonant_streak >= 3:
            return False

        if ch == prev_char and ch not in "eo":
            return False

        prev_char = ch

    return has_vowel

def solve():
    while True:
        word = input()
        if word == 'end':
            break
        if is_acceptable(word):
            print(f"<{word}> is acceptable.")
        else:
            print(f"<{word}> is not acceptable.")

if __name__ == "__main__":
    solve()
