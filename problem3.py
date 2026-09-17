def count_vowels(string):
  """
  string -> number of vowels
  count_vowels takes in a character string and returns the number of vowels in given character string

  >>> count_vowels("September")
  3
  >>> count_vowels("Purple")
  2
  >>> count_vowels("Myth")
  0
  """
  return sum(vowel in "a e i o u" for vowel in string.lower())
