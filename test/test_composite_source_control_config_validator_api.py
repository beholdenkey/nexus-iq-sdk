"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.composite_source_control_config_validator_api import (  # noqa: E501
    CompositeSourceControlConfigValidatorApi,
)
from nexus_iq_sdk.rest import ApiException


class TestCompositeSourceControlConfigValidatorApi(unittest.TestCase):
    """CompositeSourceControlConfigValidatorApi unit test stubs"""

    def setUp(self):
        self.api = CompositeSourceControlConfigValidatorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validate_source_control_config(self):
        """Test case for validate_source_control_config"""
        pass


if __name__ == '__main__':
    unittest.main()
