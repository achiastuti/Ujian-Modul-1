def hashtag(word):
  hashtag = ""
  if (len(word)) > 0:
    spl = word.split(' ')
    for i in range (0, len(spl)):
      hashtag += spl[i].capitalize()
    return '#'+hashtag
  else :
    return False

print(hashtag('Hello There How Are You Doing'))
print(hashtag ('   hello world   '))
print(hashtag(''))