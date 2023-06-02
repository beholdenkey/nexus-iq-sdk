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


class UserTokensApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user_token(self, **kwargs):  # noqa: E501
        """create_user_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiUserTokenDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_user_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_user_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_user_token_with_http_info(self, **kwargs):  # noqa: E501
        """create_user_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiUserTokenDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_token" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/currentUser",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiUserTokenDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_current_user_token(self, **kwargs):  # noqa: E501
        """delete_current_user_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_current_user_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_current_user_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_current_user_token_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def delete_current_user_token_with_http_info(self, **kwargs):  # noqa: E501
        """delete_current_user_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_current_user_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_current_user_token" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/currentUser",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_user_token_by_user_code(self, user_code, **kwargs):  # noqa: E501
        """delete_user_token_by_user_code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_token_by_user_code(user_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_user_token_by_user_code_with_http_info(
                user_code, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_user_token_by_user_code_with_http_info(
                user_code, **kwargs
            )  # noqa: E501
            return data

    def delete_user_token_by_user_code_with_http_info(
        self, user_code, **kwargs
    ):  # noqa: E501
        """delete_user_token_by_user_code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_token_by_user_code_with_http_info(user_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["user_code"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_token_by_user_code" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'user_code' is set
        if "user_code" not in params or params["user_code"] is None:
            raise ValueError(
                "Missing the required parameter `user_code` when calling `delete_user_token_by_user_code`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "user_code" in params:
            path_params["userCode"] = params["user_code"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/userCode/{userCode}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_user_token_by_username_and_realm_id(self, username, **kwargs):  # noqa: E501
        """get_user_token_by_username_and_realm_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_token_by_username_and_realm_id(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :param str realm:
        :return: ApiUserTokenDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_user_token_by_username_and_realm_id_with_http_info(
                username, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_user_token_by_username_and_realm_id_with_http_info(
                username, **kwargs
            )  # noqa: E501
            return data

    def get_user_token_by_username_and_realm_id_with_http_info(
        self, username, **kwargs
    ):  # noqa: E501
        """get_user_token_by_username_and_realm_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_token_by_username_and_realm_id_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :param str realm:
        :return: ApiUserTokenDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["username", "realm"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_token_by_username_and_realm_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'username' is set
        if "username" not in params or params["username"] is None:
            raise ValueError(
                "Missing the required parameter `username` when calling `get_user_token_by_username_and_realm_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "username" in params:
            path_params["username"] = params["username"]  # noqa: E501

        query_params = []
        if "realm" in params:
            query_params.append(("realm", params["realm"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/{username}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiUserTokenDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_user_token_exists_for_current_user(self, **kwargs):  # noqa: E501
        """get_user_token_exists_for_current_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_token_exists_for_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiUserTokenExistsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_user_token_exists_for_current_user_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_user_token_exists_for_current_user_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_user_token_exists_for_current_user_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """get_user_token_exists_for_current_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_token_exists_for_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiUserTokenExistsDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_token_exists_for_current_user" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/currentUser/hasToken",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiUserTokenExistsDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_user_tokens_by_created_between_and_realm_id(self, **kwargs):  # noqa: E501
        """get_user_tokens_by_created_between_and_realm_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_tokens_by_created_between_and_realm_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str created_after:
        :param str created_before:
        :param str realm:
        :return: list[ApiUserTokenDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_user_tokens_by_created_between_and_realm_id_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_user_tokens_by_created_between_and_realm_id_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_user_tokens_by_created_between_and_realm_id_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """get_user_tokens_by_created_between_and_realm_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_tokens_by_created_between_and_realm_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str created_after:
        :param str created_before:
        :param str realm:
        :return: list[ApiUserTokenDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["created_after", "created_before", "realm"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_tokens_by_created_between_and_realm_id" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "created_after" in params:
            query_params.append(("createdAfter", params["created_after"]))  # noqa: E501
        if "created_before" in params:
            query_params.append(
                ("createdBefore", params["created_before"])
            )  # noqa: E501
        if "realm" in params:
            query_params.append(("realm", params["realm"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ApiUserTokenDTO]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def purge_user_tokens(self, **kwargs):  # noqa: E501
        """purge_user_tokens  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_user_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.purge_user_tokens_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purge_user_tokens_with_http_info(**kwargs)  # noqa: E501
            return data

    def purge_user_tokens_with_http_info(self, **kwargs):  # noqa: E501
        """purge_user_tokens  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purge_user_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purge_user_tokens" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/userTokens/purge",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
