class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Songs([
    "May God bless you,",
    "Have a sunshine on you,",
    "Happy birthday to you!"
])
happy_bday.sing_me_a_song()

