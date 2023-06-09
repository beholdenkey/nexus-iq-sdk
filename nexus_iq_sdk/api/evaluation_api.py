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


class EvaluationApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deprecated_manifest_evaluation(self, application_id, **kwargs):  # noqa: E501
        """deprecated_manifest_evaluation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deprecated_manifest_evaluation(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiSourceControlEvaluationRequestDTO body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deprecated_manifest_evaluation_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.deprecated_manifest_evaluation_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
            return data

    def deprecated_manifest_evaluation_with_http_info(
        self, application_id, **kwargs
    ):  # noqa: E501
        """deprecated_manifest_evaluation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deprecated_manifest_evaluation_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiSourceControlEvaluationRequestDTO body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method deprecated_manifest_evaluation' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `deprecated_manifest_evaluation`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}/manifestEvaluation',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationEvaluationStatusDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def evaluate_components(self, application_id, **kwargs):  # noqa: E501
        """evaluate_components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.evaluate_components(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiComponentEvaluationRequestDTOV2 body:
        :return: ApiComponentEvaluationTicketDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.evaluate_components_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.evaluate_components_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
            return data

    def evaluate_components_with_http_info(
        self, application_id, **kwargs
    ):  # noqa: E501
        """evaluate_components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.evaluate_components_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiComponentEvaluationRequestDTOV2 body:
        :return: ApiComponentEvaluationTicketDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method evaluate_components' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `evaluate_components`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiComponentEvaluationTicketDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def evaluate_source_control(self, application_id, **kwargs):  # noqa: E501
        """evaluate_source_control  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.evaluate_source_control(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiSourceControlEvaluationRequestDTO body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.evaluate_source_control_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.evaluate_source_control_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
            return data

    def evaluate_source_control_with_http_info(
        self, application_id, **kwargs
    ):  # noqa: E501
        """evaluate_source_control  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.evaluate_source_control_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiSourceControlEvaluationRequestDTO body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method evaluate_source_control' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `evaluate_source_control`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}/sourceControlEvaluation',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationEvaluationStatusDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_application_evaluation_status(
        self, application_id, status_id, **kwargs
    ):  # noqa: E501
        """get_application_evaluation_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_evaluation_status(application_id, status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param str status_id: (required)
        :return: ApiApplicationEvaluationResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_evaluation_status_with_http_info(
                application_id, status_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_application_evaluation_status_with_http_info(
                application_id, status_id, **kwargs
            )  # noqa: E501
            return data

    def get_application_evaluation_status_with_http_info(
        self, application_id, status_id, **kwargs
    ):  # noqa: E501
        """get_application_evaluation_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_evaluation_status_with_http_info(application_id, status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param str status_id: (required)
        :return: ApiApplicationEvaluationResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'status_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_application_evaluation_status' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `get_application_evaluation_status`'
            )  # noqa: E501
        # verify the required parameter 'status_id' is set
        if 'status_id' not in params or params['status_id'] is None:
            raise ValueError(
                'Missing the required parameter `status_id` when calling `get_application_evaluation_status`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501
        if 'status_id' in params:
            path_params['statusId'] = params['status_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}/status/{statusId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationEvaluationResultDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def get_component_evaluation(
        self, application_id, result_id, **kwargs
    ):  # noqa: E501
        """get_component_evaluation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_evaluation(application_id, result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param str result_id: (required)
        :return: ApiComponentEvaluationResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_evaluation_with_http_info(
                application_id, result_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_component_evaluation_with_http_info(
                application_id, result_id, **kwargs
            )  # noqa: E501
            return data

    def get_component_evaluation_with_http_info(
        self, application_id, result_id, **kwargs
    ):  # noqa: E501
        """get_component_evaluation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_evaluation_with_http_info(application_id, result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param str result_id: (required)
        :return: ApiComponentEvaluationResultDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'result_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method get_component_evaluation' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `get_component_evaluation`'
            )  # noqa: E501
        # verify the required parameter 'result_id' is set
        if 'result_id' not in params or params['result_id'] is None:
            raise ValueError(
                'Missing the required parameter `result_id` when calling `get_component_evaluation`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501
        if 'result_id' in params:
            path_params['resultId'] = params['result_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}/results/{resultId}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiComponentEvaluationResultDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def promote_scan(self, application_id, **kwargs):  # noqa: E501
        """promote_scan  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.promote_scan(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiPromoteScanRequestDTOV2 body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.promote_scan_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.promote_scan_with_http_info(
                application_id, **kwargs
            )  # noqa: E501
            return data

    def promote_scan_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """promote_scan  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.promote_scan_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: (required)
        :param ApiPromoteScanRequestDTOV2 body:
        :return: ApiApplicationEvaluationStatusDTOV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method promote_scan' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if 'application_id' not in params or params['application_id'] is None:
            raise ValueError(
                'Missing the required parameter `application_id` when calling `promote_scan`'
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['applicationId'] = params['application_id']  # noqa: E501

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
            '/api/v2/evaluation/applications/{applicationId}/promoteScan',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiApplicationEvaluationStatusDTOV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
