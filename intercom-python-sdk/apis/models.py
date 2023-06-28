"""
Extensible models applicable to all APIS.
"""

class ModelMeta(type):
    """
    Meta-class for models.

    - Raises a not implemented error when setting a property with no setter.
    """
    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, property) and not attr_value.fset:
                attrs[attr_name] = ModelMeta.create_not_implemented_property(attr_value)
        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def create_not_implemented_property(property_obj):
        """
        Raises a not implemented error when setting a property with no setter.
        """
        def getter(self):
            raise NotImplementedError(f"Setting {property_obj.fget.__name__} is not either not supported by the API or not implemented in the SDK.")
        
        return property(getter)
