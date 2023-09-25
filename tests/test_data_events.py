from unittest import TestCase

from tests import fake_factory

from intercom_python_sdk.schemas import (
    DataEventSchema,
    DataEventListSchema
)

from intercom_python_sdk.models import (
    DataEvent,
    DataEventList
)


class TestDataEventSchemaAndModel(TestCase):

    def test_data_event_schema(self):
        data_event, _ = fake_factory.fake_schema(DataEventSchema)
        assert isinstance(data_event, DataEventSchema)

    def test_data_event_schema_validation(self):
        _, data = fake_factory.fake_schema(DataEventSchema)
        assert not DataEventSchema().validate(data)

    def test_data_event_schema_load(self):
        data_event, data = fake_factory.fake_schema(DataEventSchema)
        data_event = DataEventSchema().load(data)
        assert isinstance(data_event, DataEvent)

    def test_data_event_schema_dump_and_load(self):
        data_event, data = fake_factory.fake_schema(DataEventSchema)
        data_event = DataEventSchema().load(data)
        data_event = DataEventSchema().dump(data_event)
        assert not DataEventSchema().validate(data_event), DataEventSchema().validate(data_event)


class TestDataEventListSchemasAndModel(TestCase):

    def test_data_event_list_schema(self):
        data_event_list, _ = fake_factory.fake_schema(DataEventListSchema)
        assert isinstance(data_event_list, DataEventListSchema)

    def test_data_event_list_schema_validation(self):
        _, data = fake_factory.fake_schema(DataEventListSchema)
        assert not DataEventListSchema().validate(data), data

    def test_data_event_list_schema_load(self):
        data_event_list, data = fake_factory.fake_schema(DataEventListSchema)
        data_event_list = DataEventListSchema().load(data)
        assert isinstance(data_event_list, DataEventList)

    def test_data_event_list_schema_dump_and_load(self):
        data_event_list, data = fake_factory.fake_schema(DataEventListSchema)
        data_event_list = DataEventListSchema().load(data)
        data_event_list = DataEventListSchema().dump(data_event_list)
        assert not DataEventListSchema().validate(data_event_list), DataEventListSchema().validate(data_event_list)

    def test_data_event_list_iteration(self):
        _, data = fake_factory.fake_schema(DataEventListSchema)
        data_event_list = DataEventListSchema().load(data)
        for data_event in data_event_list:  # noqa # type: ignore
            assert isinstance(data_event, DataEvent)

    def test_data_event_list_indexing(self):
        _, data = fake_factory.fake_schema(DataEventListSchema)
        data_event_list = DataEventListSchema().load(data)
        assert isinstance(data_event_list[0], DataEvent)  # noqa # type: ignore
