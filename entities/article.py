"""
The Article Class store article objects
"""


class Article:
    def __init__(self, id: int = None, name: str = "", stock: int = None):
        self.id = id            # id of article
        self.name = name        # name of article
        self.stock = stock      # stock of article

    """
    This function get id of article
    @:returns String
    """
    def get_id(self):
        return self.id

    """
    This function get name of article
    @:returns String
    """
    def get_name(self):
        return self.name

    """
    This function get stock of article
    @:returns Integer
    """
    def get_stock(self):
        return self.stock
