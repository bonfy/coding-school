# coding: utf-8

class ShippingContainer:

    next_serial = 1

    @classmethod
    def _get_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return serial

    # Class Method 的一种常用方法
    # Create Named structure
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, *items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_serial()
