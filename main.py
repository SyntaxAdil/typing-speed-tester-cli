import random
import time

sentences = [
    "Python makes it easy to build useful tools.",
    "Practice every day to improve your typing speed.",
    "Programming is the art of solving problems.",
    "Small steps can lead to great achievements.",
    "Consistency is more important than perfection."
]

print("=" * 35)
print("      PYTHON TYPING SPEED TEST")
print("=" * 35)

target = random.choice(sentences)

print("\nType this sentence:\n")
print(target)

input("\nPress Enter when you are ready to start...")
print("\nStart typing:\n")
print(target)

start_time = time.perf_counter()
typed_text = input("\n> ")
end_time = time.perf_counter()

# Calculate elapsed time
elapsed = end_time - start_time
minutes = elapsed / 60

# Calculate typing speed (standard: 5 characters = 1 word)
if minutes > 0:
    wpm = (len(typed_text) / 5) / minutes
else:
    wpm = 0

# Calculate accuracy
correct_chars = sum(
    1 for expected, actual in zip(target, typed_text)
    if expected == actual
)

total_chars = max(len(target), len(typed_text), 1)
accuracy = (correct_chars / total_chars) * 100

# Display results
print("\n" + "=" * 35)
print("             RESULTS")
print("=" * 35)
print(f"Time taken : {elapsed:.2f} seconds")
print(f"Speed      : {wpm:.2f} WPM")
print(f"Accuracy   : {accuracy:.2f}%")
print(f"Characters : {len(typed_text)}")
print("=" * 35)