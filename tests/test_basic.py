import importlib
import inspect

from unittest import TestCase


class TestImports(TestCase):
    def test_import_intercom(self):
        from intercom_python_sdk import Intercom
        assert Intercom

    def test_import_configuration(self):
        from intercom_python_sdk import Configuration
        assert Configuration

    def test_import_models(self):
        self._import_all_from('intercom_python_sdk.models')

    def test_import_apis(self):
        self._import_all_from('intercom_python_sdk.apis')

    def _import_all_from(self, arg0):
        models = importlib.import_module(arg0)
        public_attrs = {
            k: v
            for k, v in models.__dict__.items()
            if not k.startswith('_') and not inspect.ismodule(v)
        }
        locals().update(public_attrs)
        assert models


class TestCreateIntercom(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_create_intercom(self):
        from intercom_python_sdk import Intercom
        intercom = Intercom('TEST')
        assert isinstance(intercom, Intercom)

    def test_intercom_subapis(self):
        from intercom_python_sdk import Intercom
        from intercom_python_sdk.apis import tags_to_api_dict
        from intercom_python_sdk.core.api_base import APIProxyInterface

        intercom = Intercom('TEST')

        for api_name, api in tags_to_api_dict.items():
            assert hasattr(intercom, api_name), f"\
                {api_name} is not an attribute of Intercom despite \
                being in tags_to_api_dict."

            api_interface = getattr(intercom, api_name)
            assert isinstance(api_interface, APIProxyInterface)

            assert hasattr(api_interface, 'api_object')
            api_object = getattr(api_interface, 'api_object')

            assert isinstance(api_object, api), f"\
                {api_name} is not an instance of {api}"
