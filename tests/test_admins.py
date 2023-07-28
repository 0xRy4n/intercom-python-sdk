from unittest import TestCase

from tests import fake_factory

from intercom_python_sdk.schemas import AdminSchema, AdminListSchema
from intercom_python_sdk.models import Admin, AdminList


class TestAdminSchemaAndModel(TestCase):

    def test_admin_schema(self):
        admin, _ = fake_factory.fake_schema(AdminSchema)
        assert isinstance(admin, AdminSchema)

    def test_admin_schema_validation(self):
        _, data = fake_factory.fake_schema(AdminSchema)
        assert not AdminSchema().validate(data)

    def test_admin_schema_load(self):
        admin, data = fake_factory.fake_schema(AdminSchema)
        admin = AdminSchema().load(data)
        assert isinstance(admin, Admin)

    def test_admin_schema_dump_and_load(self):
        admin, data = fake_factory.fake_schema(AdminSchema)
        admin = AdminSchema().load(data)
        admin = AdminSchema().dump(admin)
        assert not AdminSchema().validate(admin), AdminSchema().validate(admin)


class TestAdminListSchemasAndModel(TestCase):

    def test_admin_list_schema(self):
        admin_list, _ = fake_factory.fake_schema(AdminListSchema)
        assert isinstance(admin_list, AdminListSchema)

    def test_admin_list_schema_validation(self):
        _, data = fake_factory.fake_schema(AdminListSchema)
        assert not AdminListSchema().validate(data), data

    def test_admin_list_schema_load(self):
        admin_list, data = fake_factory.fake_schema(AdminListSchema)
        admin_list = AdminListSchema().load(data)
        assert isinstance(admin_list, AdminList)

    def test_admin_list_schema_dump_and_load(self):
        admin_list, data = fake_factory.fake_schema(AdminListSchema)
        admin_list = AdminListSchema().load(data)
        admin_list = AdminListSchema().dump(admin_list)
        assert not AdminListSchema().validate(admin_list), AdminListSchema().validate(admin_list)

    def test_admin_list_iteration(self):
        _, data = fake_factory.fake_schema(AdminListSchema)
        admin_list = AdminListSchema().load(data)
        for admin in admin_list:  # noqa # type: ignore
            assert isinstance(admin, Admin)

    def test_admin_list_indexing(self):
        _, data = fake_factory.fake_schema(AdminListSchema)
        admin_list = AdminListSchema().load(data)
        assert isinstance(admin_list[0], Admin)  # noqa # type: ignore

    def test_admin_list_length(self):
        _, data = fake_factory.fake_schema(AdminListSchema)
        admin_list = AdminListSchema().load(data)
        assert len(admin_list) == len(admin_list.admins)  # noqa # type: ignore
