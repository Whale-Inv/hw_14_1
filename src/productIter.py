class ProductIter:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products_to_list):
            ex_product = self.category.products_to_list[self.index]
            self.index += 1
            return ex_product
        else:
            raise StopIteration
