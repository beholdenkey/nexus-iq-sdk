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
from nexus_iq_sdk.api.evaluation_api import EvaluationApi  # noqa: E501
from nexus_iq_sdk.rest import ApiException


class TestEvaluationApi(unittest.TestCase):
    """EvaluationApi unit test stubs"""

    def setUp(self):
        self.api = EvaluationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deprecated_manifest_evaluation(self):
        """Test case for deprecated_manifest_evaluation"""
        pass

    def test_evaluate_components(self):
        """Test case for evaluate_components"""
        pass

    def test_evaluate_source_control(self):
        """Test case for evaluate_source_control"""
        pass

    def test_get_application_evaluation_status(self):
        """Test case for get_application_evaluation_status"""
        pass

    def test_get_component_evaluation(self):
        """Test case for get_component_evaluation"""
        pass

    def test_promote_scan(self):
        """Test case for promote_scan"""
        pass


if __name__ == "__main__":
    unittest.main()
