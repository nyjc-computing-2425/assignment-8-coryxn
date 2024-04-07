# Built-in imports
def reverse(text):
  """
  reverses a given string text

  Paranthesis
  -----------
  text: str
    text to be reversed

  Returns
  --------
  str
    the reversed text
  """
  if len(text) > 0:
    return reverse(text[1:]) + text[0]
  return ''

# print(reverse('hello'))

def is_palindrome(x):
  """
  takes in an input string and checks whether it is a valid palindrome

  Parenthesis
  ------------
  x: str
    input string

  Returns
  --------
  bool
    true or false
  """
  i = []
  for char in x: # use `for` for strings, `range` for int
    if char.isdigit() or char.isalpha():
      i.append(char)
  for char in range(len(i)):
    if i[0] == i[-1]:
      return is_palindrome(i[1:-1]) # delete 1st and last char
    else:
      return False
  return True

# print(is_palindrome('43neten34'))
  
  