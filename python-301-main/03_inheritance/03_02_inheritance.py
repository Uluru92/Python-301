# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?
class Movie():
    def __init__(self, year:int, title:str, duration:int, rate:int, in_movie_festivals):
        self.year = year
        self.title = title
        self.duration = duration
        self.rate = rate
        self.in_movie_festivals = in_movie_festivals
        
class RomCom(Movie):
    def __init__(self, year, title, duration, rate, in_movie_festivals, couples:int, ticket_price:int):
        super().__init__(year, title, duration, rate,in_movie_festivals)
        self.couples = couples
        self.ticket_price = ticket_price
    def happy_ending(self):
        if self.couples:
            print(f"The couples that ended together in the movie {self.title} are:")
            for couple in self.couples:
                print(f"{couple} had a happy ending!")
    
class ActionMovie(Movie):
    def __init__(self, year, title, duration, rate,in_movie_festivals, pg:int, ticket_price:int):
        super().__init__(year, title, duration, rate,in_movie_festivals)
        self.pg = 13
        self.ticket_price = ticket_price

# Lets create some RomCom movies!

romcom_movie_1 = RomCom(1992,
                        "Julieta y Romeo",
                        215,
                        4.5,
                        ["Vecine","Cannes","Sundance Film Festival"],
                        ["Romeo and Juliet","Charles and Mary","Amanda and Josh"],
                        100)
                        
romcom_movie_2 = RomCom(2024,
                        "Sex and the City",
                        180,
                        4.8,
                        ["Berlinale","Sundance Film Festival"],
                        ["Carrie Bradshaw and Mr. Big", "Charlotte and Harry","Miranda and Steve"],
                        125)

# Lets check the couples that ended together for each RomCom movie!
romcom_movie_1.happy_ending()
romcom_movie_2.happy_ending()