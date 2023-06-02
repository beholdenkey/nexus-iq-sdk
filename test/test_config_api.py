# coding: utf-8

"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.config_api import ConfigApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_configuration(self):
        """Test case for delete_configuration"""
        pass

    def test_disable_feature(self):
        """Test case for disable_feature"""
        pass

    def test_enabled_feature(self):
        """Test case for enabled_feature"""
        pass

    def test_get_configuration(self):
        """Test case for get_configuration"""
        pass

    def test_set_configuration(self):
        """Test case for set_configuration"""
        pass


if __name__ == "__main__":
    unittest.main()
