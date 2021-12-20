"""
The Product Class store product objects
"""


class Product:
    def __init__(self, name: str = "", price: int = None, articles: list = []):
        self.name = name            # name of product
        self.price = price          # price of product
        self.articles = articles    # articles of product

    """
    This function get name of product
    @:returns String
    """
    def get_name(self):
        return self.name

    """
    This function get price of product
    @:returns Integer
    """
    def get_price(self):
        return self.price

    """
    This function get article list of product
    @:returns List
    """
    def get_articles(self):
        return self.articles
