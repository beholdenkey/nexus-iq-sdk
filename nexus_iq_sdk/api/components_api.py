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


class ComponentsApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_component_label(
        self, owner_type, internal_owner_id, component_hash, label_name, **kwargs
    ):  # noqa: E501
        """delete_component_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_component_label(owner_type, internal_owner_id, component_hash, label_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :param str component_hash: (required)
        :param str label_name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_component_label_with_http_info(
                owner_type, internal_owner_id, component_hash, label_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_component_label_with_http_info(
                owner_type, internal_owner_id, component_hash, label_name, **kwargs
            )  # noqa: E501
            return data

    def delete_component_label_with_http_info(
        self, owner_type, internal_owner_id, component_hash, label_name, **kwargs
    ):  # noqa: E501
        """delete_component_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_component_label_with_http_info(owner_type, internal_owner_id, component_hash, label_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :param str component_hash: (required)
        :param str label_name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'owner_type',
            'internal_owner_id',
            'component_hash',
            'label_name',
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
                    ' to method delete_component_label' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if 'owner_type' not in params or params['owner_type'] is None:
            raise ValueError(
                'Missing the required parameter `owner_type` when calling `delete_component_label`'
            )  # noqa: E501
        # verify the required parameter 'internal_owner_id' is set
        if 'internal_owner_id' not in params or params['internal_owner_id'] is None:
            raise ValueError(
                'Missing the required parameter `internal_owner_id` when calling `delete_component_label`'
            )  # noqa: E501
        # verify the required parameter 'component_hash' is set
        if 'component_hash' not in params or params['component_hash'] is None:
            raise ValueError(
                'Missing the required parameter `component_hash` when calling `delete_component_label`'
            )  # noqa: E501
        # verify the required parameter 'label_name' is set
        if 'label_name' not in params or params['label_name'] is None:
            raise ValueError(
                'Missing the required parameter `label_name` when calling `delete_component_label`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'internal_owner_id' in params:
            path_params['internalOwnerId'] = params['internal_owner_id']  # noqa: E501
        if 'component_hash' in params:
            path_params['componentHash'] = params['component_hash']  # noqa: E501
        if 'label_name' in params:
            path_params['labelName'] = params['label_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId}',
            'DELETE',
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

    def get_component_details(self, **kwargs):  # noqa: E501
        """get_component_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiComponentDetailsRequestDTOV2 body:
        :return: ApiComponentDetailsResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_component_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_component_details_with_http_info(self, **kwargs):  # noqa: E501
        """get_component_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiComponentDetailsRequestDTOV2 body:
        :return: ApiComponentDetailsResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_component_details' % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
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
            '/api/v2/components/details',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiComponentDetailsResultDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_component_versions(self, **kwargs):  # noqa: E501
        """get_component_versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_versions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiComponentOrPurlIdentifierDTOV2 body:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_versions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_component_versions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_component_versions_with_http_info(self, **kwargs):  # noqa: E501
        """get_component_versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_versions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiComponentOrPurlIdentifierDTOV2 body:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_component_versions' % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
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
            '/api/v2/components/versions',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_suggested_remediation_for_component(
        self, owner_type, owner_id, **kwargs
    ):  # noqa: E501
        """get_suggested_remediation_for_component  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_suggested_remediation_for_component(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiComponentDTOV2 body:
        :param str stage_id:
        :param str identification_source:
        :param str scan_id:
        :return: ApiComponentRemediationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_suggested_remediation_for_component_with_http_info(
                owner_type, owner_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_suggested_remediation_for_component_with_http_info(
                owner_type, owner_id, **kwargs
            )  # noqa: E501
            return data

    def get_suggested_remediation_for_component_with_http_info(
        self, owner_type, owner_id, **kwargs
    ):  # noqa: E501
        """get_suggested_remediation_for_component  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_suggested_remediation_for_component_with_http_info(owner_type, owner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str owner_id: (required)
        :param ApiComponentDTOV2 body:
        :param str stage_id:
        :param str identification_source:
        :param str scan_id:
        :return: ApiComponentRemediationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'owner_type',
            'owner_id',
            'body',
            'stage_id',
            'identification_source',
            'scan_id',
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
                    ' to method get_suggested_remediation_for_component' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if 'owner_type' not in params or params['owner_type'] is None:
            raise ValueError(
                'Missing the required parameter `owner_type` when calling `get_suggested_remediation_for_component`'
            )  # noqa: E501
        # verify the required parameter 'owner_id' is set
        if 'owner_id' not in params or params['owner_id'] is None:
            raise ValueError(
                'Missing the required parameter `owner_id` when calling `get_suggested_remediation_for_component`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501

        query_params = []
        if 'stage_id' in params:
            query_params.append(('stageId', params['stage_id']))  # noqa: E501
        if 'identification_source' in params:
            query_params.append(
                ('identificationSource', params['identification_source'])
            )  # noqa: E501
        if 'scan_id' in params:
            query_params.append(('scanId', params['scan_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
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
            '/api/v2/components/remediation/{ownerType}/{ownerId}',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiComponentRemediationDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def set_component_label(
        self, owner_type, internal_owner_id, component_hash, label_name, **kwargs
    ):  # noqa: E501
        """set_component_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_component_label(owner_type, internal_owner_id, component_hash, label_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :param str component_hash: (required)
        :param str label_name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_component_label_with_http_info(
                owner_type, internal_owner_id, component_hash, label_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.set_component_label_with_http_info(
                owner_type, internal_owner_id, component_hash, label_name, **kwargs
            )  # noqa: E501
            return data

    def set_component_label_with_http_info(
        self, owner_type, internal_owner_id, component_hash, label_name, **kwargs
    ):  # noqa: E501
        """set_component_label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_component_label_with_http_info(owner_type, internal_owner_id, component_hash, label_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_type: (required)
        :param str internal_owner_id: (required)
        :param str component_hash: (required)
        :param str label_name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'owner_type',
            'internal_owner_id',
            'component_hash',
            'label_name',
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
                    ' to method set_component_label' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_type' is set
        if 'owner_type' not in params or params['owner_type'] is None:
            raise ValueError(
                'Missing the required parameter `owner_type` when calling `set_component_label`'
            )  # noqa: E501
        # verify the required parameter 'internal_owner_id' is set
        if 'internal_owner_id' not in params or params['internal_owner_id'] is None:
            raise ValueError(
                'Missing the required parameter `internal_owner_id` when calling `set_component_label`'
            )  # noqa: E501
        # verify the required parameter 'component_hash' is set
        if 'component_hash' not in params or params['component_hash'] is None:
            raise ValueError(
                'Missing the required parameter `component_hash` when calling `set_component_label`'
            )  # noqa: E501
        # verify the required parameter 'label_name' is set
        if 'label_name' not in params or params['label_name'] is None:
            raise ValueError(
                'Missing the required parameter `label_name` when calling `set_component_label`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_type' in params:
            path_params['ownerType'] = params['owner_type']  # noqa: E501
        if 'internal_owner_id' in params:
            path_params['internalOwnerId'] = params['internal_owner_id']  # noqa: E501
        if 'component_hash' in params:
            path_params['componentHash'] = params['component_hash']  # noqa: E501
        if 'label_name' in params:
            path_params['labelName'] = params['label_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId}',
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
