import turtle
import winsound
from pygame import mixer

def main():
    # Initialize and run the Ping Pong game
    game = PingPongGame()
    game.run()

def paddle1_go_up(paddle):
    # Move paddle 1 up within boundary
    y = paddle.ycor()
    if y < 250:
        y += 20
    paddle.sety(y)

def paddle1_go_down(paddle):
    # Move paddle 1 down within boundary
    y = paddle.ycor()
    if y > -250:
        y -= 20
    paddle.sety(y)

def paddle2_go_up(paddle):
    # Move paddle 2 up within boundary
    y = paddle.ycor()
    if y < 250:
        y += 20
    paddle.sety(y)

def paddle2_go_down(paddle):
    # Move paddle 2 down within boundary
    y = paddle.ycor()
    if y > -250:
        y -= 20
    paddle.sety(y)

class PingPongGame:
    def __init__(self):
        # GUI Setup
        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.title("Simple Table Tennis Game 🏓")
        self.window.bgcolor("#191970")
        self.window.setup(width=1000, height=750)
        self.window.bgpic("Ping Pong Table.gif")

        # Game Background Music
        mixer.init()
        mixer.music.load("Simple Ping Pong BGM.wav")
        mixer.music.play(loops=-1)

        # Initialize paddles, ball, and scoreboard
        self.init_paddles()
        self.init_ball()
        self.init_scoreboard()

        # Bind paddle movements to keyboard keys
        self.window.listen()
        self.window.onkeypress(lambda: paddle1_go_up(self.paddle_1), "w")
        self.window.onkeypress(lambda: paddle1_go_up(self.paddle_1), "W")
        self.window.onkeypress(lambda: paddle1_go_down(self.paddle_1), "s")
        self.window.onkeypress(lambda: paddle1_go_down(self.paddle_1), "S")
        self.window.onkeypress(lambda: paddle2_go_up(self.paddle_2), "Up")
        self.window.onkeypress(lambda: paddle2_go_down(self.paddle_2), "Down")

    def init_paddles(self):
        # Create and position paddles
        self.paddle_1 = self.create_paddle(-450, "red")
        self.paddle_2 = self.create_paddle(450, "red")

    def create_paddle(self, x_pos, color):
        # Helper function to create and configure a paddle
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color(color)
        paddle.shapesize(stretch_wid=10, stretch_len=1)
        paddle.penup()
        paddle.goto(x_pos, 0)
        return paddle

    def init_ball(self):
        # Create and configure the ball
        self.pp_ball = turtle.Turtle()
        self.pp_ball.speed(0)
        self.pp_ball.shape("circle")
        self.pp_ball.color("#d3d3d3")
        self.pp_ball.shapesize(stretch_wid=2, stretch_len=2)
        self.pp_ball.penup()
        self.pp_ball.goto(0, 0)
        self.pp_ball.dx = 0.2  # Ball's horizontal velocity
        self.pp_ball.dy = 0.2  # Ball's vertical velocity

    def init_scoreboard(self):
        # Create and configure the scoreboard
        self.scoreboard = turtle.Turtle()
        self.scoreboard.speed(0)
        self.scoreboard.color("black")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 310)
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update the scoreboard with current scores
        self.scoreboard.clear()
        self.scoreboard.write(f"🎮 : {self.score_1}   💥   🕹 : {self.score_2}",
                              align="center", font=("Comic Sans MS", 30, "bold"))

    def run(self):
        # Main game loop
        while True:
            self.window.update()
            self.move_ball()
            self.check_border_collisions()
            self.check_paddle_collisions()

    def move_ball(self):
        # Move the ball
        self.pp_ball.setx(self.pp_ball.xcor() + self.pp_ball.dx)
        self.pp_ball.sety(self.pp_ball.ycor() + self.pp_ball.dy)

    def check_border_collisions(self):
        # Check collisions with top and bottom borders
        if self.pp_ball.ycor() > 365 or self.pp_ball.ycor() < -365:
            self.pp_ball.dy *= -1
            winsound.PlaySound("Hit Border Sound.wav", winsound.SND_ASYNC)

        # Check collisions with left and right borders
        if self.pp_ball.xcor() < -490 or self.pp_ball.xcor() > 490:
            self.handle_border_collision()

    def handle_border_collision(self):
        # Handle collisions with left and right borders
        if self.pp_ball.xcor() < -490:
            self.score_2 += 1
            winsound.PlaySound("Winning Sound.wav", winsound.SND_ASYNC)
        else:
            self.score_1 += 1
            winsound.PlaySound("Winning Sound.wav", winsound.SND_ASYNC)
        self.update_scoreboard()
        if self.score_1 == 3 or self.score_2 == 3:
            self.end_game()

    def end_game(self):
        # End the game
        winner = "🎮" if self.score_1 == 3 else "🕹"
        self.scoreboard.clear()
        self.scoreboard.write(f"{winner} WINS THE GAME!!!",
                              align="center", font=("Comic Sans MS", 30, "bold"))
        turtle.done()

    def check_paddle_collisions(self):
        # Check collisions with paddles
        if (-450 < self.pp_ball.xcor() < -440 and self.paddle_1.ycor() - 120 < self.pp_ball.ycor() < self.paddle_1.ycor() + 120) \
                or (440 < self.pp_ball.xcor() < 450 and self.paddle_2.ycor() - 120 < self.pp_ball.ycor() < self.paddle_2.ycor() + 120):
            self.pp_ball.dx *= -1
            winsound.PlaySound("Pong Sound.wav", winsound.SND_ASYNC)

if __name__ == "__main__":
    main()

