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


class TelemetryApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_external_telemetry(self, **kwargs):  # noqa: E501
        """post_external_telemetry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_external_telemetry(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict(str, str) body:
        :param str user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_external_telemetry_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_external_telemetry_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_external_telemetry_with_http_info(self, **kwargs):  # noqa: E501
        """post_external_telemetry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_external_telemetry_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict(str, str) body:
        :param str user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method post_external_telemetry' % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_agent' in params:
            header_params['user-agent'] = params['user_agent']  # noqa: E501

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
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/telemetry',
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
