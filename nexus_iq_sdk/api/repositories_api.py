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


class RepositoriesApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_quarantined_by_path(
        self, repository_manager_instance_id, repository_public_id, **kwargs
    ):  # noqa: E501
        """get_quarantined_by_path  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quarantined_by_path(repository_manager_instance_id, repository_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_manager_instance_id: (required)
        :param str repository_public_id: (required)
        :param list[str] body:
        :return: ApiRepositoryPathResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quarantined_by_path_with_http_info(
                repository_manager_instance_id, repository_public_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_quarantined_by_path_with_http_info(
                repository_manager_instance_id, repository_public_id, **kwargs
            )  # noqa: E501
            return data

    def get_quarantined_by_path_with_http_info(
        self, repository_manager_instance_id, repository_public_id, **kwargs
    ):  # noqa: E501
        """get_quarantined_by_path  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quarantined_by_path_with_http_info(repository_manager_instance_id, repository_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_manager_instance_id: (required)
        :param str repository_public_id: (required)
        :param list[str] body:
        :return: ApiRepositoryPathResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'repository_manager_instance_id',
            'repository_public_id',
            'body',
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
                    ' to method get_quarantined_by_path' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_manager_instance_id' is set
        if (
            'repository_manager_instance_id' not in params
            or params['repository_manager_instance_id'] is None
        ):
            raise ValueError(
                'Missing the required parameter `repository_manager_instance_id` when calling `get_quarantined_by_path`'
            )  # noqa: E501
        # verify the required parameter 'repository_public_id' is set
        if (
            'repository_public_id' not in params
            or params['repository_public_id'] is None
        ):
            raise ValueError(
                'Missing the required parameter `repository_public_id` when calling `get_quarantined_by_path`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_manager_instance_id' in params:
            path_params['repositoryManagerInstanceId'] = params[
                'repository_manager_instance_id'
            ]  # noqa: E501
        if 'repository_public_id' in params:
            path_params['repositoryPublicId'] = params[
                'repository_public_id'
            ]  # noqa: E501

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
            '/api/v2/repositories/{repositoryManagerInstanceId}/{repositoryPublicId}/components/quarantined/pathnames',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiRepositoryPathResponseDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def release_quarantine_without_re_eval(self, quarantine_id, **kwargs):  # noqa: E501
        """release_quarantine_without_re_eval  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_quarantine_without_re_eval(quarantine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_id: (required)
        :param str body:
        :return: ApiComponentReleasedFromQuarantineDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.release_quarantine_without_re_eval_with_http_info(
                quarantine_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.release_quarantine_without_re_eval_with_http_info(
                quarantine_id, **kwargs
            )  # noqa: E501
            return data

    def release_quarantine_without_re_eval_with_http_info(
        self, quarantine_id, **kwargs
    ):  # noqa: E501
        """release_quarantine_without_re_eval  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_quarantine_without_re_eval_with_http_info(quarantine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_id: (required)
        :param str body:
        :return: ApiComponentReleasedFromQuarantineDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quarantine_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method release_quarantine_without_re_eval' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quarantine_id' is set
        if 'quarantine_id' not in params or params['quarantine_id'] is None:
            raise ValueError(
                'Missing the required parameter `quarantine_id` when calling `release_quarantine_without_re_eval`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quarantine_id' in params:
            path_params['quarantineId'] = params['quarantine_id']  # noqa: E501

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
            ['text/plain']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/repositories/quarantine/{quarantineId}/release',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiComponentReleasedFromQuarantineDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
