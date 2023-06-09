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


class ApplicationCategoriesApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_tag(self, organization_id, **kwargs):  # noqa: E501
        """add_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_tag(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param ApiApplicationCategoryDTO body:
        :return: ApiApplicationCategoryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_tag_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_tag_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def add_tag_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """add_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_tag_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param ApiApplicationCategoryDTO body:
        :return: ApiApplicationCategoryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" ' to method add_tag' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `add_tag`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationCategoryDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def delete_tag(self, organization_id, tag_id, **kwargs):  # noqa: E501
        """delete_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag(organization_id, tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param str tag_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tag_with_http_info(
                organization_id, tag_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_tag_with_http_info(
                organization_id, tag_id, **kwargs
            )  # noqa: E501
            return data

    def delete_tag_with_http_info(
        self, organization_id, tag_id, **kwargs
    ):  # noqa: E501
        """delete_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag_with_http_info(organization_id, tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param str tag_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'tag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method delete_tag' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `delete_tag`'
            )  # noqa: E501
        # verify the required parameter 'tag_id' is set
        if 'tag_id' not in params or params['tag_id'] is None:
            raise ValueError(
                'Missing the required parameter `tag_id` when calling `delete_tag`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}/{tagId}',
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

    def get_applicable_tags(self, organization_id, **kwargs):  # noqa: E501
        """get_applicable_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_tags(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: ApplicableTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applicable_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_applicable_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def get_applicable_tags_with_http_info(
        self, organization_id, **kwargs
    ):  # noqa: E501
        """get_applicable_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_tags_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: ApplicableTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_applicable_tags' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `get_applicable_tags`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}/applicable',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicableTagsDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_applicable_tags_by_application_public_id(
        self, application_public_id, **kwargs
    ):  # noqa: E501
        """get_applicable_tags_by_application_public_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_tags_by_application_public_id(application_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_public_id: (required)
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applicable_tags_by_application_public_id_with_http_info(
                application_public_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_applicable_tags_by_application_public_id_with_http_info(
                application_public_id, **kwargs
            )  # noqa: E501
            return data

    def get_applicable_tags_by_application_public_id_with_http_info(
        self, application_public_id, **kwargs
    ):  # noqa: E501
        """get_applicable_tags_by_application_public_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applicable_tags_by_application_public_id_with_http_info(application_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_public_id: (required)
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_public_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_applicable_tags_by_application_public_id' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_public_id' is set
        if (
            'application_public_id' not in params
            or params['application_public_id'] is None
        ):
            raise ValueError(
                'Missing the required parameter `application_public_id` when calling `get_applicable_tags_by_application_public_id`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_public_id' in params:
            path_params['applicationPublicId'] = params[
                'application_public_id'
            ]  # noqa: E501

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
            '/api/v2/applicationCategories/application/{applicationPublicId}/applicable',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiApplicationCategoryDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_application_applicable_tags(
        self, application_public_id, **kwargs
    ):  # noqa: E501
        """get_application_applicable_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_applicable_tags(application_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_public_id: (required)
        :return: ApplicableTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_applicable_tags_with_http_info(
                application_public_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_application_applicable_tags_with_http_info(
                application_public_id, **kwargs
            )  # noqa: E501
            return data

    def get_application_applicable_tags_with_http_info(
        self, application_public_id, **kwargs
    ):  # noqa: E501
        """get_application_applicable_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_applicable_tags_with_http_info(application_public_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_public_id: (required)
        :return: ApplicableTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_public_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_application_applicable_tags' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_public_id' is set
        if (
            'application_public_id' not in params
            or params['application_public_id'] is None
        ):
            raise ValueError(
                'Missing the required parameter `application_public_id` when calling `get_application_applicable_tags`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_public_id' in params:
            path_params['applicationPublicId'] = params[
                'application_public_id'
            ]  # noqa: E501

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
            '/api/v2/applicationCategories/application/{applicationPublicId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicableTagsDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_applied_policy_tags(self, organization_id, **kwargs):  # noqa: E501
        """get_applied_policy_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applied_policy_tags(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: list[PolicyTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applied_policy_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_applied_policy_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def get_applied_policy_tags_with_http_info(
        self, organization_id, **kwargs
    ):  # noqa: E501
        """get_applied_policy_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applied_policy_tags_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: list[PolicyTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_applied_policy_tags' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `get_applied_policy_tags`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}/policy',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PolicyTag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_applied_tags(self, organization_id, **kwargs):  # noqa: E501
        """get_applied_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applied_tags(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: AppliedTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_applied_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_applied_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def get_applied_tags_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """get_applied_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_applied_tags_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: AppliedTagsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_applied_tags' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `get_applied_tags`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}/applied',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppliedTagsDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_tags(self, organization_id, **kwargs):  # noqa: E501
        """get_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tags_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tags_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def get_tags_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """get_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_tags' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `get_tags`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiApplicationCategoryDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_tags_used_by_applications(self, **kwargs):  # noqa: E501
        """get_tags_used_by_applications  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags_used_by_applications(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tags_used_by_applications_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_tags_used_by_applications_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_tags_used_by_applications_with_http_info(self, **kwargs):  # noqa: E501
        """get_tags_used_by_applications  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags_used_by_applications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiApplicationCategoryDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_tags_used_by_applications' % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/applicationCategories/application',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiApplicationCategoryDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def update_tag(self, organization_id, **kwargs):  # noqa: E501
        """update_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param ApiApplicationCategoryDTO body:
        :return: ApiApplicationCategoryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_tag_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_tag_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def update_tag_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """update_tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :param ApiApplicationCategoryDTO body:
        :return: ApiApplicationCategoryDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method update_tag' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if 'organization_id' not in params or params['organization_id'] is None:
            raise ValueError(
                'Missing the required parameter `organization_id` when calling `update_tag`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

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
            '/api/v2/applicationCategories/organization/{organizationId}',
            'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationCategoryDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
