#Challenge from CoderByte


def LongestWord(sen):
  clean_sen = ""
  for letter in sen:
    if letter.isalpha() or letter.isnumeric():
      clean_sen += letter
    else:
      clean_sen += " "
  return max(clean_sen.split(" "),key=len)

# keep this function call here 
print(LongestWord(input()))
