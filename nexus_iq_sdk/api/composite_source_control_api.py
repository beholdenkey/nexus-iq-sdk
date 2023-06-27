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


class CompositeSourceControlApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_composite_source_control_by_owner(
        self, owner_type, internal_owner_id, **kwargs
    ):  # noqa: E501
        """get_composite_source_control_by_owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_composite_source_control_by_owner(owner_type, internal_owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :return: ApiCompositeSourceControlDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_composite_source_control_by_owner_with_http_info(
                owner_type, internal_owner_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_composite_source_control_by_owner_with_http_info(
                owner_type, internal_owner_id, **kwargs
            )  # noqa: E501
            return data

    def get_composite_source_control_by_owner_with_http_info(
        self, owner_type, internal_owner_id, **kwargs
    ):  # noqa: E501
        """get_composite_source_control_by_owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_composite_source_control_by_owner_with_http_info(owner_type, internal_owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :return: ApiCompositeSourceControlDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'internal_owner_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_composite_source_control_by_owner' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if 'owner_type' not in params or params['owner_type'] is None:
            raise ValueError(
                'Missing the required parameter `owner_type` when calling `get_composite_source_control_by_owner`'
            )  # noqa: E501
        # verify the required parameter 'internal_owner_id' is set
        if 'internal_owner_id' not in params or params['internal_owner_id'] is None:
            raise ValueError(
                'Missing the required parameter `internal_owner_id` when calling `get_composite_source_control_by_owner`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'internal_owner_id' in params:
            path_params['internalOwnerId'] = params['internal_owner_id']  # noqa: E501

        query_params = []

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
            '/api/v2/compositeSourceControl/{ownerType}/{internalOwnerId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiCompositeSourceControlDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
