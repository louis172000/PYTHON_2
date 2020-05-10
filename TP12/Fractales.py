import turtle as tu
tu.setup(1920, 1080)
tu.up()
tu.left(135)
tu.forward(300)
tu.left(-135)

tu.down()
tu.ht()
tu.speed(0)

def draw_curve(tu, l, order):
    if order == 0:
        tu.forward(l)
        return
    else:
        l /= 3
        draw_curve(tu, l, order-1)
        tu.left(60)
        draw_curve(tu, l, order-1)
        tu.left(-120)
        draw_curve(tu, l, order-1)
        tu.left(60)
        draw_curve(tu, l, order-1)

def darw_full_curve(tu, l, order):
    draw_curve(tu, l, order)
    tu.left(-120)
    draw_curve(tu, l, order)
    tu.left(-120)
    draw_curve(tu, l, order)
    tu.left(-120)


darw_full_curve(tu, 300, 2)
tu.exitonclick()
