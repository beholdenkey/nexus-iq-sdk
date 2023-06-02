# swagger_client.ConfigProxyServerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration3**](ConfigProxyServerApi.md#delete_configuration3) | **DELETE** /api/v2/config/httpProxyServer | 
[**get_configuration3**](ConfigProxyServerApi.md#get_configuration3) | **GET** /api/v2/config/httpProxyServer | 
[**set_configuration3**](ConfigProxyServerApi.md#set_configuration3) | **PUT** /api/v2/config/httpProxyServer | 

# **delete_configuration3**
> delete_configuration3()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigProxyServerApi()

try:
    api_instance.delete_configuration3()
except ApiException as e:
    print("Exception when calling ConfigProxyServerApi->delete_configuration3: %s\n" % e)
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

# **get_configuration3**
> ApiProxyServerConfigurationDTO get_configuration3()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigProxyServerApi()

try:
    api_response = api_instance.get_configuration3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigProxyServerApi->get_configuration3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiProxyServerConfigurationDTO**](ApiProxyServerConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration3**
> set_configuration3(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigProxyServerApi()
body = swagger_client.ApiProxyServerConfigurationDTO() # ApiProxyServerConfigurationDTO |  (optional)

try:
    api_instance.set_configuration3(body=body)
except ApiException as e:
    print("Exception when calling ConfigProxyServerApi->set_configuration3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiProxyServerConfigurationDTO**](ApiProxyServerConfigurationDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

