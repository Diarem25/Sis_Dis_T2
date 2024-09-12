class VariableAssemblyLine:
    def __init__(self, storage, product_type):
        self.storage = storage
        self.product_type = product_type

    def set_product_type(self, product_type):
        self.product_type = product_type

    def produce(self, part_index):
        if self.storage.consume_part(part_index):
            return 1  # Assume each line produces one unit per call
        return 0

    def can_produce(self):
        return self.storage.can_produce(self.product_type)
