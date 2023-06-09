"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.config_source_control_api import (  # noqa: E501
    ConfigSourceControlApi,
)
from nexus_iq_sdk.rest import ApiException


class TestConfigSourceControlApi(unittest.TestCase):
    """ConfigSourceControlApi unit test stubs"""

    def setUp(self):
        self.api = ConfigSourceControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_configuration5(self):
        """Test case for delete_configuration5"""
        pass

    def test_get_configuration5(self):
        """Test case for get_configuration5"""
        pass

    def test_set_configuration5(self):
        """Test case for set_configuration5"""
        pass


if __name__ == '__main__':
    unittest.main()
