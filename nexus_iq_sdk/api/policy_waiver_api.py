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


class PolicyWaiverApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_policy_waiver(
        self, policy_violation_id, owner_type, **kwargs
    ):  # noqa: E501
        """add_policy_waiver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_policy_waiver(policy_violation_id, owner_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_violation_id: (required)
        :param str owner_type: (required)
        :param str body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_policy_waiver_with_http_info(
                policy_violation_id, owner_type, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_policy_waiver_with_http_info(
                policy_violation_id, owner_type, **kwargs
            )  # noqa: E501
            return data

    def add_policy_waiver_with_http_info(
        self, policy_violation_id, owner_type, **kwargs
    ):  # noqa: E501
        """add_policy_waiver  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_policy_waiver_with_http_info(policy_violation_id, owner_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_violation_id: (required)
        :param str owner_type: (required)
        :param str body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_violation_id', 'owner_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method add_policy_waiver' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_violation_id' is set
        if 'policy_violation_id' not in params or params['policy_violation_id'] is None:
            raise ValueError(
                'Missing the required parameter `policy_violation_id` when calling `add_policy_waiver`'
            )  # noqa: E501
        # verify the required parameter 'owner_type' is set
        if 'owner_type' not in params or params['owner_type'] is None:
            raise ValueError(
                'Missing the required parameter `owner_type` when calling `add_policy_waiver`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_violation_id' in params:
            path_params['policyViolationId'] = params[
                'policy_violation_id'
            ]  # noqa: E501
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*']
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/policyWaiver/{policyViolationId}/{ownerType}',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
