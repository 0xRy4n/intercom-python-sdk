from unittest import TestCase

from tests import fake_factory

from intercom_python_sdk.schemas import AdminSchema
from intercom_python_sdk.models import Admin


class TestAdminSchemasAndModels(TestCase):

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
