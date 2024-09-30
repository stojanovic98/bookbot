
def main():
  report()

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def count_words(text):
  file_contents = text
  words = file_contents.split()
  return len(words)

def count_characters(text):
  characters = {}
  for c in text:
    lowered = c.lower()
    if(lowered in characters):
      characters[lowered] += 1
    else:
      characters[lowered] = 1
  return characters

def sort_on(dict):
  return dict["num"]

def report():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = count_words(text)
  character_count = count_characters(text)
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print("")
  to_list = []
  for c in character_count:
    dict = {}
    if(c.isalpha()):
      dict["letter"] = c
      dict["num"] = character_count[c]
      to_list.append(dict)
  to_list.sort(reverse=True, key=sort_on)
  for item in to_list:
      print(f"The '{item['letter']}' character was found {item['num']} times")
  print("--- End report ---")
main()