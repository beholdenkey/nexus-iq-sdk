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
from nexus_iq_sdk.api.policy_waiver_api import PolicyWaiverApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestPolicyWaiverApi(unittest.TestCase):
    """PolicyWaiverApi unit test stubs"""

    def setUp(self):
        self.api = PolicyWaiverApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_policy_waiver(self):
        """Test case for add_policy_waiver

        """
        pass


if __name__ == '__main__':
    unittest.main()
