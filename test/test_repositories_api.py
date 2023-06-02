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
from nexus_iq_sdk.api.repositories_api import RepositoriesApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = RepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_quarantined_by_path(self):
        """Test case for get_quarantined_by_path"""
        pass

    def test_release_quarantine_without_re_eval(self):
        """Test case for release_quarantine_without_re_eval"""
        pass


if __name__ == "__main__":
    unittest.main()
