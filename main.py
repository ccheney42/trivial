import random
import tmdbsimple
import tmdbsimple as tmdb

tmdb.API_KEY = '850aabc6c6caca2df31887c0ac123bbb'

def main():
  print "Would you like to play a game?"
  number = input()
  movie = tmdb.Movies(number)
  score = 0
  print "keywords are:"
  keywords = movie.keywords()
  keyword_list = keywords['keywords']
  for keyword_struct in keyword_list:
    score = score + 1
    print keyword_struct['name']
    guess = input()
    if guess == movie.title():
      print "Correct! Guesses: ", score
      break
  print "all done!"

if __name__ == "__main__":
  main()
