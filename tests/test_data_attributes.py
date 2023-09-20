from unittest import TestCase

from tests import fake_factory

from intercom_python_sdk.schemas import (
    DataAttributeListSchema,
    DataAttributeSchema
)

from intercom_python_sdk.models import (
    DataAttribute,
    DataAttributeList
)


class TestDataAttributeSchemaAndModel(TestCase):

    def test_data_attribute_schema(self):
        data_attribute, _ = fake_factory.fake_schema(DataAttributeSchema)
        assert isinstance(data_attribute, DataAttributeSchema)

    def test_data_attribute_schema_validation(self):
        _, data = fake_factory.fake_schema(DataAttributeSchema)
        assert not DataAttributeSchema().validate(data)

    def test_data_attribute_schema_load(self):
        data_attribute, data = fake_factory.fake_schema(DataAttributeSchema)
        data_attribute = DataAttributeSchema().load(data)
        assert isinstance(data_attribute, DataAttribute)

    def test_data_attribute_schema_dump_and_load(self):
        data_attribute, data = fake_factory.fake_schema(DataAttributeSchema)
        data_attribute = DataAttributeSchema().load(data)
        data_attribute = DataAttributeSchema().dump(data_attribute)
        assert not DataAttributeSchema().validate(data_attribute), DataAttributeSchema().validate(data_attribute)


class TestDataAttributeListSchemasAndModel(TestCase):

    def test_data_attribute_list_schema(self):
        data_attribute_list, _ = fake_factory.fake_schema(DataAttributeListSchema)
        assert isinstance(data_attribute_list, DataAttributeListSchema)

    def test_data_attribute_list_schema_validation(self):
        _, data = fake_factory.fake_schema(DataAttributeListSchema)
        assert not DataAttributeListSchema().validate(data), data

    def test_data_attribute_list_schema_load(self):
        data_attribute_list, data = fake_factory.fake_schema(DataAttributeListSchema)
        data_attribute_list = DataAttributeListSchema().load(data)
        assert isinstance(data_attribute_list, DataAttributeList)

    def test_data_attribute_list_schema_dump_and_load(self):
        data_attribute_list, data = fake_factory.fake_schema(DataAttributeListSchema)
        data_attribute_list = DataAttributeListSchema().load(data)
        data_attribute_list = DataAttributeListSchema().dump(data_attribute_list)
        assert not DataAttributeListSchema().validate(data_attribute_list), \
            DataAttributeListSchema().validate(data_attribute_list)

    def test_data_attribute_list_iteration(self):
        _, data = fake_factory.fake_schema(DataAttributeListSchema)
        data_attribute_list = DataAttributeListSchema().load(data)
        for data_attribute in data_attribute_list:  # noqa # type: ignore
            assert isinstance(data_attribute, DataAttribute)

    def test_data_attribute_list_indexing(self):
        _, data = fake_factory.fake_schema(DataAttributeListSchema)
        data_attribute_list = DataAttributeListSchema().load(data)
        assert isinstance(data_attribute_list[0], DataAttribute)

    def test_data_attribute_list_contains(self):
        _, data = fake_factory.fake_schema(DataAttributeListSchema)
        data_attribute_list = DataAttributeListSchema().load(data)
        assert isinstance(data_attribute_list[0], DataAttribute)
        assert data_attribute_list[0] in data_attribute_list
