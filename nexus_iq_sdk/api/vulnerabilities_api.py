"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nexus_iq_sdk.api_client import ApiClient


class VulnerabilitiesApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_security_vulnerability_details(self, ref_id, **kwargs):  # noqa: E501
        """get_security_vulnerability_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_vulnerability_details(ref_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ref_id: (required)
        :param ComponentIdentifier component_identifier:
        :param str identification_source:
        :param str scan_id:
        :param str owner_type:
        :param str owner_id:
        :return: SecurityVulnerabilityData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_vulnerability_details_with_http_info(
                ref_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_security_vulnerability_details_with_http_info(
                ref_id, **kwargs
            )  # noqa: E501
            return data

    def get_security_vulnerability_details_with_http_info(
        self, ref_id, **kwargs
    ):  # noqa: E501
        """get_security_vulnerability_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_vulnerability_details_with_http_info(ref_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ref_id: (required)
        :param ComponentIdentifier component_identifier:
        :param str identification_source:
        :param str scan_id:
        :param str owner_type:
        :param str owner_id:
        :return: SecurityVulnerabilityData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'ref_id',
            'component_identifier',
            'identification_source',
            'scan_id',
            'owner_type',
            'owner_id',
        ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_security_vulnerability_details' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ref_id' is set
        if 'ref_id' not in params or params['ref_id'] is None:
            raise ValueError(
                'Missing the required parameter `ref_id` when calling `get_security_vulnerability_details`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ref_id' in params:
            path_params['refId'] = params['ref_id']  # noqa: E501

        query_params = []
        if 'component_identifier' in params:
            query_params.append(
                ('componentIdentifier', params['component_identifier'])
            )  # noqa: E501
        if 'identification_source' in params:
            query_params.append(
                ('identificationSource', params['identification_source'])
            )  # noqa: E501
        if 'scan_id' in params:
            query_params.append(('scanId', params['scan_id']))  # noqa: E501
        if 'owner_type' in params:
            query_params.append(('ownerType', params['owner_type']))  # noqa: E501
        if 'owner_id' in params:
            query_params.append(('ownerId', params['owner_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/vulnerabilities/{refId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SecurityVulnerabilityData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
