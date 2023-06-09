"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.source_control_metrics_api import (  # noqa: E501
    SourceControlMetricsApi,
)
from nexus_iq_sdk.rest import ApiException


class TestSourceControlMetricsApi(unittest.TestCase):
    """SourceControlMetricsApi unit test stubs"""

    def setUp(self):
        self.api = SourceControlMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_source_control(self):
        """Test case for get_source_control"""
        pass


if __name__ == '__main__':
    unittest.main()
