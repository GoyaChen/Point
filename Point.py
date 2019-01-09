class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def move(this, dx: int, dy: int):
        """Move to (x+dx, y+dy)"""
        this.x += dx
        this.y += dy
        
    def __eq__(self, other: "Point") -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
