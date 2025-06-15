class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect2():
    def __init__(self, x, y, w, h):
        self.position = Vector2(x, y)
        self.size = Vector2(w, h)