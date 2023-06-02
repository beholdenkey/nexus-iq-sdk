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


class OrganizationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_organization(self, **kwargs):  # noqa: E501
        """add_organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_organization(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiOrganizationDTO body:
        :return: ApiOrganizationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_organization_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_organization_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_organization_with_http_info(self, **kwargs):  # noqa: E501
        """add_organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_organization_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiOrganizationDTO body:
        :return: ApiOrganizationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_organization" % key
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
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/v2/organizations",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiOrganizationDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_organization(self, organization_id, **kwargs):  # noqa: E501
        """get_organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: ApiOrganizationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_organization_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_organization_with_http_info(
                organization_id, **kwargs
            )  # noqa: E501
            return data

    def get_organization_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """get_organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: (required)
        :return: ApiOrganizationDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'organization_id' is set
        if "organization_id" not in params or params["organization_id"] is None:
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `get_organization`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization_id" in params:
            path_params["organizationId"] = params["organization_id"]  # noqa: E501

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
            "/api/v2/organizations/{organizationId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiOrganizationDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_organizations(self, **kwargs):  # noqa: E501
        """get_organizations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organizations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organization_name:
        :return: ApiOrganizationListDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_organizations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_organizations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_organizations_with_http_info(self, **kwargs):  # noqa: E501
        """get_organizations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organizations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] organization_name:
        :return: ApiOrganizationListDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organizations" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "organization_name" in params:
            query_params.append(
                ("organizationName", params["organization_name"])
            )  # noqa: E501
            collection_formats["organizationName"] = "multi"  # noqa: E501

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
            "/api/v2/organizations",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiOrganizationListDTO",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
