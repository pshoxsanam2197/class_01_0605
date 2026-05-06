# 10-m
class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self._duration = duration
        self.__rating = rating
    def play(self):
        print(f"Playing {self.title}")

    def rate(self, x):
        self.__rating = x

    def info(self):
        print(f"Rating:{self.__rating}")

movie = Movie("Avengers", 120, 8)
movie.play()
movie.rate(9)
movie.info()
