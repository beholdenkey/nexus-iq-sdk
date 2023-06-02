# swagger_client.ConfigSourceControlApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration5**](ConfigSourceControlApi.md#delete_configuration5) | **DELETE** /api/v2/config/sourceControl | 
[**get_configuration5**](ConfigSourceControlApi.md#get_configuration5) | **GET** /api/v2/config/sourceControl | 
[**set_configuration5**](ConfigSourceControlApi.md#set_configuration5) | **PUT** /api/v2/config/sourceControl | 

# **delete_configuration5**
> delete_configuration5()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSourceControlApi()

try:
    api_instance.delete_configuration5()
except ApiException as e:
    print("Exception when calling ConfigSourceControlApi->delete_configuration5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration5**
> ApiSourceControlConfigurationDTO get_configuration5()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSourceControlApi()

try:
    api_response = api_instance.get_configuration5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigSourceControlApi->get_configuration5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSourceControlConfigurationDTO**](ApiSourceControlConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration5**
> set_configuration5(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSourceControlApi()
body = swagger_client.JsonNode() # JsonNode |  (optional)

try:
    api_instance.set_configuration5(body=body)
except ApiException as e:
    print("Exception when calling ConfigSourceControlApi->set_configuration5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonNode**](JsonNode.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

