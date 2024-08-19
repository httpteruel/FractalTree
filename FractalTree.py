import turtle

t = turtle.Turtle(shape="turtle")

t.lt(90)
lv = 13  # Nível máximo da árvore
l = 120  # Comprimento do tronco inicial
s = 17  # Ângulo de rotação

t.width(lv)
t.penup()
t.bk(l)
t.pendown()
t.fd(l)

# Função recursiva

def draw_tree(l, level):
    width = t.width()
    t.width(width * 3.0 / 4.0)  # largura dos galhos

    l *= 3.0 / 4.0  # comprimento dos galhos

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)

    t.bk(l)
    t.rt(2 * s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)

    t.bk(l)
    t.lt(s)

    t.width(width)

t.speed("fastest")  # velocidade de geração

draw_tree(l, 2)

turtle.done()
