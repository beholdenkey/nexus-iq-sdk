# coding: utf-8

"""
    Sonatype Nexus IQ Server

    This documents the available APIs into [Sonatype Nexus IQ Server](https://www.sonatype.com/products/open-source-security-dependency-management) (also knwon as Nexus Lifecycle).   # noqa: E501

    OpenAPI spec version: 156
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nexus_iq_sdk.api_client import ApiClient


class LabelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_label(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """add_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_label(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiLabelDTO body:
        :return: ApiLabelDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_label_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_label_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
            return data

    def add_label_with_http_info(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """add_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_label_with_http_info(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiLabelDTO body:
        :return: ApiLabelDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `add_label`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `add_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiLabelDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_label(self, owner_type, owner_id, label_id, **kwargs):  # noqa: E501
        """delete_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_label(owner_type, owner_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param str label_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_label_with_http_info(owner_type, owner_id, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_label_with_http_info(owner_type, owner_id, label_id, **kwargs)  # noqa: E501
            return data

    def delete_label_with_http_info(self, owner_type, owner_id, label_id, **kwargs):  # noqa: E501
        """delete_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_label_with_http_info(owner_type, owner_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param str label_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id', 'label_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `delete_label`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `delete_label`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params or
                params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `delete_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}/{labelId}', 'DELETE',
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
            collection_formats=collection_formats)

    def get_applicable_contexts(self, owner_type, owner_id, label_id, **kwargs):  # noqa: E501
        """get_applicable_contexts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_contexts(owner_type, owner_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param str label_id: (required)
        :return: ApplicableContext
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applicable_contexts_with_http_info(owner_type, owner_id, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_applicable_contexts_with_http_info(owner_type, owner_id, label_id, **kwargs)  # noqa: E501
            return data

    def get_applicable_contexts_with_http_info(self, owner_type, owner_id, label_id, **kwargs):  # noqa: E501
        """get_applicable_contexts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_contexts_with_http_info(owner_type, owner_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param str label_id: (required)
        :return: ApplicableContext
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id', 'label_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_applicable_contexts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `get_applicable_contexts`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `get_applicable_contexts`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params or
                params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `get_applicable_contexts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}/applicable/context/{labelId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicableContext',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_applicable_labels(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """get_applicable_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_labels(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :return: ApplicableLabels
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applicable_labels_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_applicable_labels_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
            return data

    def get_applicable_labels_with_http_info(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """get_applicable_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_labels_with_http_info(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :return: ApplicableLabels
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_applicable_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `get_applicable_labels`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `get_applicable_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}/applicable', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicableLabels',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_labels(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """get_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param bool inherit:
        :return: list[ApiLabelDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_labels_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_labels_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
            return data

    def get_labels_with_http_info(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """get_labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels_with_http_info(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param bool inherit:
        :return: list[ApiLabelDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id', 'inherit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `get_labels`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `get_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501

        query_params = []
        if 'inherit' in params:
            query_params.append(('inherit', params['inherit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiLabelDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_label(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """update_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_label(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiLabelDTO body:
        :return: ApiLabelDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_label_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_label_with_http_info(owner_type, owner_id, **kwargs)  # noqa: E501
            return data

    def update_label_with_http_info(self, owner_type, owner_id, **kwargs):  # noqa: E501
        """update_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_label_with_http_info(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiLabelDTO body:
        :return: ApiLabelDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_type', 'owner_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if ('owner_type' not in params or
                params['owner_type'] is None):
            raise ValueError("Missing the required parameter `owner_type` when calling `update_label`")  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `update_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/labels/{ownerType}/{ownerId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiLabelDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
