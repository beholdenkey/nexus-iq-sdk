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
from nexus_iq_sdk.api.config_artifactory_connection_api import (  # noqa: E501
    ConfigArtifactoryConnectionApi,
)
from nexus_iq_sdk.rest import ApiException


class TestConfigArtifactoryConnectionApi(unittest.TestCase):
    """ConfigArtifactoryConnectionApi unit test stubs"""

    def setUp(self):
        self.api = ConfigArtifactoryConnectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_artifactory_connection(self):
        """Test case for add_artifactory_connection"""
        pass

    def test_delete_artifactory_connection(self):
        """Test case for delete_artifactory_connection"""
        pass

    def test_get_artifactory_connection(self):
        """Test case for get_artifactory_connection"""
        pass

    def test_get_owner_artifactory_connection(self):
        """Test case for get_owner_artifactory_connection"""
        pass

    def test_test_artifactory_connection(self):
        """Test case for test_artifactory_connection"""
        pass

    def test_test_artifactory_connection1(self):
        """Test case for test_artifactory_connection1"""
        pass

    def test_update_artifactory_connection(self):
        """Test case for update_artifactory_connection"""
        pass

    def test_update_owner_artifactory_connection_status(self):
        """Test case for update_owner_artifactory_connection_status"""
        pass


if __name__ == "__main__":
    unittest.main()
