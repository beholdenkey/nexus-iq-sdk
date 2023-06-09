"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.cyclone_dx_api import CycloneDxApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestCycloneDxApi(unittest.TestCase):
    """CycloneDxApi unit test stubs"""

    def setUp(self):
        self.api = CycloneDxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_by_report_id(self):
        """Test case for get_by_report_id"""
        pass

    def test_get_by_report_id1(self):
        """Test case for get_by_report_id1"""
        pass

    def test_get_latest(self):
        """Test case for get_latest"""
        pass

    def test_get_latest1(self):
        """Test case for get_latest1"""
        pass


if __name__ == '__main__':
    unittest.main()
