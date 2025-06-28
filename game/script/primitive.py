class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect2():
    def __init__(self, x, y, w, h):
        self.position = Vector2(x, y)
        self.size = Vector2(w, h)

    def inside_rect(self, rect):
        return self.position.x > rect[0] and self.position.x < rect[0] + rect[2] and self.position.y > rect[1] and self.position.y < rect[1] + rect[3]

    def overlap(self, rect):
        x = self.position.x > rect.position.x - rect.size.x / 2 - self.size.x / 2 and self.position.x < rect.position.x + rect.size.x / 2 + self.size.x / 2
        y = self.position.y > rect.position.y - rect.size.y / 2 - self.size.y / 2 and self.position.y < rect.position.y + rect.size.y / 2 + self.size.y / 2
        return x and y