
def hashtag(word):
    word.lower()
    if (len(word)) > 0:
      word = word.replace(' ', '')
      print(word)
    else :
      print('false')
hashtag('Hello There How Are You Doing')
hashtag ('   hello world   ')
hashtag('')