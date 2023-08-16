class Enemy(Object):
    def __init__(self, enemy):
        for i in range(1, 500):
            print(random())
            if random() % 2:
                enemy.move_left()
                if random() % 3:
                    enemy.move_right()
# There is probably a much better way of doing this