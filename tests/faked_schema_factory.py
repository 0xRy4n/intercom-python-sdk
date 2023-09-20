import faker

from typing import (
    Optional,
    Callable,
    Type
)

from marshmallow import Schema, fields


class FakedSchemaFactory:
    def __init__(self):
        self.fake = faker.Faker()

        self.schema_map = {
            fields.String: self.fake.pystr,
            fields.Integer: self.fake.random_int,
            fields.Float: self.fake.pyfloat,
            fields.Boolean: self.fake.pybool,
            fields.DateTime: self.fake.date_time,
            fields.Date: self.fake.date_object,
            fields.Time: self.fake.time_object,
            fields.Decimal: self.fake.pydecimal,
            fields.Email: self.fake.email,
            fields.URL: self.fake.url,
            fields.UUID: self.fake.uuid4,
        }

    def _fake_list(self, field: fields.List):
        def fake_list():
            inner = field.inner

            if isinstance(inner, fields.Nested):
                list_val = lambda: self.fake_schema(inner.nested)[1]  # noqa # type: ignore
            else:
                list_val = self.schema_map[inner.__class__]  # noqa # type: ignore

            return [list_val() for _ in range(self.fake.random_int(min=1, max=10))]

        return fake_list

    def _fake_tuple(self, field: fields.Tuple):
        def fake_tuple():
            return tuple(self._fake_list(field)())  # noqa # type: ignore

        return fake_tuple

    def _get_faker_method_by_attr_name(self, attr_name: str) -> Optional[Callable]:
        if getattr(self.fake, attr_name, None):
            return getattr(self.fake, attr_name)

    def get_faker_method_for_field(self, field: fields.Field):
        if faker_method := self._get_faker_method_by_attr_name(field.name):
            return faker_method

        elif field.__class__ in self.schema_map:
            return self.schema_map[field.__class__]

        elif isinstance(field, fields.Nested):
            if field.many:
                return lambda: [
                    self.fake_schema(field.nested)[1]
                    for _ in range(self.fake.random_int(min=1, max=10))
                ]
            else:
                return lambda: self.fake_schema(field.nested)  # noqa # type: ignore

        elif isinstance(field, fields.List):
            return self._fake_list(field)

        elif isinstance(field, fields.Tuple):
            return self._fake_tuple(field)

        elif isinstance(field, fields.Dict):
            if not (value_type := field.value_field):
                return self.fake.pydict

            if isinstance(value_type, fields.Nested):
                return lambda: {self.fake.pystr(): self.fake_schema(value_type)}  # noqa # type: ignore
            else:
                return lambda: {self.fake.pystr(): self.schema_map[value_type.__class__]()}  # noqa # type: ignore
        else:
            raise NotImplementedError(f"Cannot fake field: {field}")

    def fake_schema(self, schema: Type[Schema]):
        schema_obj = schema()  # noqa # type: ignore
        data = {}

        for field_name, field in schema_obj.fields.items():
            if field.dump_default:
                setattr(schema_obj, field_name, field.dump_default)
                faker_val = field.dump_default
            else:
                faker_method = self.get_faker_method_for_field(field)
                setattr(schema_obj, field_name, faker_method())

                faker_val = faker_method()
                faker_val = self._get_last_of_tuple(faker_val)

                if isinstance(faker_val, list):
                    faker_val = [self._get_last_of_tuple(val) for val in faker_val]

                data[field_name] = faker_val
        return schema_obj, data

    def _get_last_of_tuple(self, val):
        return self._get_last_of_tuple(val[-1]) if isinstance(val, tuple) else val
