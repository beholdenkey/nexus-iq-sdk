"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.data_retention_policies_api import (  # noqa: E501
    DataRetentionPoliciesApi,
)
from nexus_iq_sdk.rest import ApiException


class TestDataRetentionPoliciesApi(unittest.TestCase):
    """DataRetentionPoliciesApi unit test stubs"""

    def setUp(self):
        self.api = DataRetentionPoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_data_retention_policies(self):
        """Test case for get_data_retention_policies"""
        pass

    def test_set_data_retention_policies(self):
        """Test case for set_data_retention_policies"""
        pass


if __name__ == '__main__':
    unittest.main()
