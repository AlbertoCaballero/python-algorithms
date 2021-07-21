import turtle as tu

foo = tu.Turtle()
foo.left(90)
foo.speed(500)
foo.back(200)

# Recursion
def draw(i, a):
    if i < 10:
        return
    else:
        foo.forward(i)
        foo.left(a)
        draw(3*i/4, a)
        foo.right(a*2)
        draw(3*i/4, a)
        foo.left(a)
        foo.backward(i)

draw(100, 75)
