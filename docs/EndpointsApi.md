# swagger_client.EndpointsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api**](EndpointsApi.md#get_open_api) | **GET** /api/v2/endpoints/{apiType} | 

# **get_open_api**
> str get_open_api(api_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EndpointsApi()
api_type = 'api_type_example' # str | 

try:
    api_response = api_instance.get_open_api(api_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_open_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_type** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

