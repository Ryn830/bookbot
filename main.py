def sort_by_count(counts):
  return counts["count"]

def main():
  with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    counts = {}

    for word in words:
      for index in range(0, len(word)):
        char = word.lower()[index]
        if char.isalpha():
          if not char in counts:
            counts[char] = { "character": char, "count": 0 }
          counts[char]["count"] += 1

    counts = [*counts.values()]
    counts.sort(reverse=True, key=sort_by_count)

    print("--- Being report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")
    for char in counts:
      print(f"The '{char["character"]}' character was found {char["count"]} times")
    print("--- End report ---")

main()
