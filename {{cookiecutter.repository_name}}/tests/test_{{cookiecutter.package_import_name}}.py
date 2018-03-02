# -*- coding: utf-8 -*-

"""Main test script."""

from django.test import TestCase

import {{ cookiecutter.package_import_name }}


class MainTestCase(TestCase):
    """Main Django test case."""

    def setUp(self):
        """Setup method."""
        self.package = {{ cookiecutter.package_import_name }}

    def test_main(self):
        """Main test method."""
        assert self.package

    def tearDown(self):
        """Tear down method."""
        del self.package
