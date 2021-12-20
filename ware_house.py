import itertools

from utils.io_operations import ReadInputFiles
from entities.article import Article
from entities.product import Product

"""
The WareHouse Class manages warehouse software
"""
class WareHouse:
    def __init__(self):
        self.article_quantity = []      # This array keeps quantities of products in order
        self.article_indexes = {}       # This dict keeps articles names as key and product object as value
        self.product_indexes = {}       # This dict keeps products names as key and product object as value
        self.product_max_numbers = {}   # This dict keeps maximum number of quantity we can have for a product
        self.points = {}                # This dict keeps points of each product that is (Price * Maximum_Quantity)
        self.max_prices = {}            # This dict keeps price of products in order
        self.max_quantities = {}        # This dict keeps maximum quantities of products in order
        self.max_profit = 0             # This field is maximum profit we can have
        self.final_result = []          # This array show final result
        self.final_result_dict = {}     # This dict show final result

    """
    This function calculate maximum number of a product we can have
    @:returns Integer
    """
    def get_max_number_of_one_product(self, input_product: Product = None, input_article: list = []):
        max_number = 0
        product_articles = input_product.articles
        for product_article in product_articles:
            article_stock = input_article[product_article["id"] - 1]
            article_number = product_article["amount"]
            if (article_stock // article_number) < max_number or max_number == 0:
                max_number = article_stock // article_number
                if max_number == 0:
                    break
        return max_number

    """
    This function calculate profit from selling an input product list
    @:returns Integer
    """
    def calculate_profit(self, input_product: list = []):
        profit = 0
        for counter, product in enumerate(input_product):
            profit += product * list(self.product_indexes.values())[counter].price
        return profit

    """
    This function init objects
    """
    def init_objects(self):
        read_input_file = ReadInputFiles()
        articles = read_input_file.read_file("../articles.json")
        articles_list = articles['articles']
        products = read_input_file.read_file("../products.json")
        products_list = products['products']

        for article in articles_list:
            article_object = Article(id=article["id"], name=article["name"], stock=article["stock"])
            self.article_indexes[article["id"]] = article_object
            self.article_quantity.append(article["stock"])

        for product in products_list:
            product_object = Product(name=product["name"], price=product["price"], articles=product["articles"])
            self.product_indexes[product["name"]] = product_object
            self.product_max_numbers[product["name"]] = self.get_max_number_of_one_product(product_object,
                                                                                           self.article_quantity)
            self.points[product["name"]] = self.get_max_number_of_one_product(product_object, self.article_quantity) * \
                                           product["price"]
            self.max_prices[product["name"]] = product["price"]
            self.max_quantities[product["name"]] = self.get_max_number_of_one_product(product_object,
                                                                                      self.article_quantity)

    """
    This function runs algorithm
    """
    def implement_algorithm(self, input_object: dict = {}):
        max_number = self.product_max_numbers[list(input_object.keys())[0]]
        while max_number != 0:
            article_quantity_temp = self.article_quantity.copy()
            final_result_temp = []
            counter = 0
            for point in input_object.keys():
                product_object = self.product_indexes[point]
                if counter == 0:
                    product_number = max_number
                else:
                    product_number = self.get_max_number_of_one_product(product_object, article_quantity_temp)
                if product_number > 0:
                    for product_article in product_object.articles:
                        article_stock = article_quantity_temp[product_article["id"] - 1]
                        article_stock -= product_number * product_article["amount"]
                        article_quantity_temp[product_article["id"] - 1] = article_stock
                final_result_temp.append(product_number)
                counter += 1
            profit = self.calculate_profit(final_result_temp)
            if profit > self.max_profit:
                self.final_result = final_result_temp
                self.max_profit = profit
            max_number -= 1

        for key, value in input_object.items():
            self.final_result_dict[key] = self.final_result[list(input_object.keys()).index(key)]

    """
    This function is first algorithm
    """
    def first_algorithm(self):
        self.init_objects()

        self.points = dict(sorted(self.points.items(), key=lambda item: item[1], reverse=True))

        self.implement_algorithm(input_object=self.points)

        print(self.final_result_dict)

    """
    This function is second algorithm
    """
    def second_algorithm(self):
        self.init_objects()

        self.points = dict(sorted(self.points.items(), key=lambda item: item[1], reverse=True))
        self.implement_algorithm(input_object=self.points)

        self.max_prices = dict(sorted(self.max_prices.items(), key=lambda item: item[1], reverse=True))
        self.implement_algorithm(input_object=self.max_prices)

        self.max_quantities = dict(sorted(self.max_quantities.items(), key=lambda item: item[1], reverse=True))
        self.implement_algorithm(input_object=self.max_quantities)

        print(self.final_result_dict)

    """
    This function is second algorithm
    """
    def third_algorithm(self):
        self.init_objects()

        self.points = dict(sorted(self.points.items(), key=lambda item: item[1], reverse=True))

        for item in itertools.permutations(self.points.items()):
            point_dict = dict((x, y) for x, y in item)
            self.implement_algorithm(input_object=point_dict)

        print(self.final_result_dict)


if __name__ == '__main__':
    ware_house = WareHouse()
    ware_house.first_algorithm()
    # ware_house.second_algorithm()
    # ware_house.third_algorithm()
