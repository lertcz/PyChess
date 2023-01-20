class Piece:
    def __init__(self, isWhite, pieceName) -> None:
        self.isWhite = isWhite
        self.name = pieceName
        self.image = None