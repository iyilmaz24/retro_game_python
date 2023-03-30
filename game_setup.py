

class GameSetUp:
    # this file contains the previous high score and will be overwritten at the end of the game if surpassed
    f = open('highscore.txt', mode='r')
    s = f.read()

    def __init__(self, t1, t2, t3):

        self.window = t1
        self.screen = t2
        self.current_score = t3

        self.score = 0

    def create_window(self):
        # turns window background black, crops window size, and adds label to window
        self.window.title('Breakout Game')
        self.window.bgcolor('black')
        self.window.setup(width=600, height=600)

        #   creates the text: title, score, high score
        self.screen.pen(shown=False, pendown=False, pencolor='white', speed=10)
        self.current_score.pen(shown=False, pendown=False, pencolor='white', speed=10)
        self.screen.goto(110, 240)
        self.screen.write(arg=f'Record: {GameSetUp.s}', move=True, align='left', font=('Arial', 12, 'bold'))
        self.current_score.goto(110, 210)
        self.current_score.write(arg='Current Score: 0', move=True, align='left', font=('Arial', 12, 'bold'))
        self.screen.goto(-260, 240)
        self.screen.write(arg='BREAKOUT GAME', move=True, align='left', font=('Arial', 18, 'bold'))

        # creates white borders around the game area
        self.screen.goto(-275, -275)
        self.screen.pen(pendown='True')
        self.screen.goto(275, -275)
        self.screen.goto(275, 275)
        self.screen.goto(-275, 275)
        self.screen.goto(-275, -275)

    def update_score(self, points):
        # we use the points argument to add itself to self.score
        self.score += points

        # we make the self.current_score turtle clear it's previous drawings and write our most recent current score
        self.current_score.goto(110, 210)
        self.current_score.clear()
        self.current_score.write(arg=f'Current Score: {self.score}', move=True, align='left', font=('Arial', 12, 'bold'))
        return

    def game_over(self):
        self.current_score.clear()
        self.screen.clear()

        self.current_score.pen(pencolor='red')
        self.screen.pen(pencolor='red', pendown=False)

        self.screen.goto(0, 225)
        self.current_score.goto(0, -100)

        self.current_score.write(arg=f'Final Score: {self.score}', move=True, align='center', font=('Times New Roman', 24, 'bold'))
        self.screen.write(arg=f'GAME OVER', move=True, align='center', font=('Times New Roman', 36, 'bold'))

    def game_won(self):
        self.current_score.clear()
        self.screen.clear()

        self.current_score.pen(pencolor='green')
        self.screen.pen(pencolor='green', pendown=False)

        self.screen.goto(0, 225)
        self.current_score.goto(0, -100)

        self.current_score.write(arg=f'Final Score: {self.score}', move=True, align='center', font=('Times New Roman', 24, 'bold'))
        self.screen.write(arg=f'GAME COMPLETE', move=True, align='center', font=('Times New Roman', 36, 'bold'))