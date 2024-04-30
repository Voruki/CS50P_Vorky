import pytest
from project import PingPongGame, paddle1_go_up, paddle1_go_down, paddle2_go_up, paddle2_go_down

# This test checks whether Paddle 1 (left) moves upwards by 20 units
# when the paddle1_go_up function is called.
def test_paddle1_go_up():
    paddle = PingPongGame().paddle_1  # Get Paddle 1 instance
    initial_y = paddle.ycor()  # Record initial y-coordinate of the paddle
    paddle1_go_up(paddle)  # Call the function to move the paddle up
    # Assert that the y-coordinate of the paddle has increased by 20 units
    assert paddle.ycor() == initial_y + 20

# This test checks whether Paddle 1 (left) moves downwards by 20 units
# when the paddle1_go_down function is called.
def test_paddle1_go_down():
    paddle = PingPongGame().paddle_1  # Get Paddle 1 instance
    initial_y = paddle.ycor()  # Record initial y-coordinate of the paddle
    paddle1_go_down(paddle)  # Call the function to move the paddle down
    # Assert that the y-coordinate of the paddle has decreased by 20 units
    assert paddle.ycor() == initial_y - 20

# This test checks whether Paddle 2 (right) moves upwards by 20 units
# when the paddle2_go_up function is called.
def test_paddle2_go_up():
    paddle = PingPongGame().paddle_2  # Get Paddle 2 instance
    initial_y = paddle.ycor()  # Record initial y-coordinate of the paddle
    paddle2_go_up(paddle)  # Call the function to move the paddle up
    # Assert that the y-coordinate of the paddle has increased by 20 units
    assert paddle.ycor() == initial_y + 20

# This test checks whether Paddle 2 (right) moves downwards by 20 units
# when the paddle2_go_down function is called.
def test_paddle2_go_down():
    paddle = PingPongGame().paddle_2  # Get Paddle 2 instance
    initial_y = paddle.ycor()  # Record initial y-coordinate of the paddle
    paddle2_go_down(paddle)  # Call the function to move the paddle down
    # Assert that the y-coordinate of the paddle has decreased by 20 units
    assert paddle.ycor() == initial_y - 20

