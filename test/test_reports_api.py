"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nexus_iq_sdk
from nexus_iq_sdk.api.reports_api import ReportsApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all1(self):
        """Test case for get_all1"""
        pass

    def test_get_by_application_id(self):
        """Test case for get_by_application_id"""
        pass

    def test_get_components_in_quarantine(self):
        """Test case for get_components_in_quarantine"""
        pass

    def test_get_components_with_waivers(self):
        """Test case for get_components_with_waivers"""
        pass

    def test_get_metrics(self):
        """Test case for get_metrics"""
        pass

    def test_get_report_history_for_application(self):
        """Test case for get_report_history_for_application"""
        pass

    def test_get_stale_waivers(self):
        """Test case for get_stale_waivers"""
        pass


if __name__ == '__main__':
    unittest.main()
