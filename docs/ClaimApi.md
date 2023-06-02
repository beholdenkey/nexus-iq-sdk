# swagger_client.ClaimApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](ClaimApi.md#delete) | **DELETE** /api/v2/claim/components/{hash} | 
[**get**](ClaimApi.md#get) | **GET** /api/v2/claim/components/{hash} | 
[**get_all**](ClaimApi.md#get_all) | **GET** /api/v2/claim/components | 
[**set**](ClaimApi.md#set) | **POST** /api/v2/claim/components | 

# **delete**
> delete(hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
hash = 'hash_example' # str | 

try:
    api_instance.delete(hash)
except ApiException as e:
    print("Exception when calling ClaimApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiHashComponentIdentifierDTO get(hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
hash = 'hash_example' # str | 

try:
    api_response = api_instance.get(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  | 

### Return type

[**ApiHashComponentIdentifierDTO**](ApiHashComponentIdentifierDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> ApiHashComponentIdentifiersDTO get_all()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()

try:
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiHashComponentIdentifiersDTO**](ApiHashComponentIdentifiersDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set**
> ApiHashComponentIdentifierDTO set(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
body = swagger_client.ApiHashComponentIdentifierDTO() # ApiHashComponentIdentifierDTO |  (optional)

try:
    api_response = api_instance.set(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiHashComponentIdentifierDTO**](ApiHashComponentIdentifierDTO.md)|  | [optional] 

### Return type

[**ApiHashComponentIdentifierDTO**](ApiHashComponentIdentifierDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

