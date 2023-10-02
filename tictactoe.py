"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
-feito
2. What happens when someone taps a taken spot?
-o programa nao desenharia e uma mesangem seria exibida 'lugar ocupado, escolha outro'
3. How would you detect when someone has won?
-quando uma linha reta passar pela sequencia que foi ganha
4. How could you create a computer player?
-------------------
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    color('red') #mudanca na cor do X
    line(x+30, y+30, x + 90, y + 90) #mudou a posicao do X, deixando mais no centro e menor
    line(x+30, y + 90, x + 90, y+30)

def drawo(x, y):
    color('blue') #mudanca na cor da bola
    up()
    goto(x + 67, y + 30) #mudanca na posicao da bola
    down()
    circle(35) #mudanca no tamnho do circulo
    

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
