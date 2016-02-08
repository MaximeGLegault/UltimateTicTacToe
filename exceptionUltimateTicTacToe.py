__author__ = 'Maxime Gangon-Legault'
__date__ = "2016/01/10"


class TokenError(Exception):
    """This class is used when both players have chosen the same token."""
    def __init__(self):
        super().__init__()