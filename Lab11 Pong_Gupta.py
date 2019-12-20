# Sarvesh Gupta
# Pong

from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)


class Ball(games.Sprite):

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.overlapping_sprites:
             self.dy = -self.dy

        if self.top < 0:
            self.dy = -self.dy

        if self.bottom > games.screen.height: # end the game
            self.end_game()
            self.destroy()

    def end_game(self):
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Paddle(games.Sprite):
    image = games.load_image("paddle.png")

    def __init__(self):
        super(Paddle, self).__init__(image = Paddle.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """  Check if catch pizzas. """
        for i in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10

def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    ball_image = games.load_image("ball.png")
    the_ball = Ball(image=ball_image,
                      x=games.screen.width / 2,
                      y=games.screen.height / 2,
                      dx=5,
                      dy=5)
    games.screen.add(the_ball)

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False
    games.screen.event_grab = True


    games.screen.mainloop()


main()
