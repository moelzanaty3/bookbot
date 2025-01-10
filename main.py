def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)

  print_report(book_path, num_words, chars_dict)


def print_report(book_path, num_words, chars_dict):
  print(f"--- Begin report of {book_path} ---")

  print(f"{num_words} words found in the document")
  print()

  for char, count in chars_dict.items():
    if not char.isalpha():
      continue
    print(f"The {char} character was found {count} times")

  print("--- End report ---")


def get_chars_dict(str):
  chars = {}
  for char in str:
    lowered = char.lower()
    count = 0
    if lowered in chars:
      count = chars.get(lowered) + 1
    chars[lowered] = count

  return chars


def get_num_words(str):
  words = str.split()
  return len(words)


def get_book_text(path):
  with open(path) as f:
    return f.read()


main()
