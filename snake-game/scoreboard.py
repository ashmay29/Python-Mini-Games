from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('C:\\Users\\Aanshuvi Shah\\Desktop\\udemypy\\python-mini-games\\snake-game\\data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}" ,align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER" ,align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:\\Users\\Aanshuvi Shah\\Desktop\\udemypy\\python-mini-games\\snake-game\\data.txt',mode="w") as data:
                data.write(f"{self.high_score}")
        
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

         