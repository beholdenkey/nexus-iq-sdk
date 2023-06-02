# swagger_client.CompositeSourceControlConfigValidatorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_source_control_config**](CompositeSourceControlConfigValidatorApi.md#validate_source_control_config) | **GET** /api/v2/compositeSourceControlConfigValidator/application/{applicationId} | 

# **validate_source_control_config**
> ConfigurationValidationResult validate_source_control_config(application_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompositeSourceControlConfigValidatorApi()
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.validate_source_control_config(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeSourceControlConfigValidatorApi->validate_source_control_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**ConfigurationValidationResult**](ConfigurationValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

