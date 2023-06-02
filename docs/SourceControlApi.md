# swagger_client.SourceControlApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_update_source_control**](SourceControlApi.md#add_or_update_source_control) | **POST** /api/v2/sourceControl | 
[**add_source_control**](SourceControlApi.md#add_source_control) | **POST** /api/v2/sourceControl/{ownerType}/{internalOwnerId} | 
[**delete_source_control**](SourceControlApi.md#delete_source_control) | **DELETE** /api/v2/sourceControl/{ownerType}/{internalOwnerId} | 
[**get_source_control1**](SourceControlApi.md#get_source_control1) | **GET** /api/v2/sourceControl/{ownerType}/{internalOwnerId} | 
[**update_source_control**](SourceControlApi.md#update_source_control) | **PUT** /api/v2/sourceControl/{ownerType}/{internalOwnerId} | 

# **add_or_update_source_control**
> ApiSourceControlDTO add_or_update_source_control(public_id=public_id, repository_url=repository_url)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlApi()
public_id = 'public_id_example' # str |  (optional)
repository_url = 'repository_url_example' # str |  (optional)

try:
    api_response = api_instance.add_or_update_source_control(public_id=public_id, repository_url=repository_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceControlApi->add_or_update_source_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | [optional] 
 **repository_url** | **str**|  | [optional] 

### Return type

[**ApiSourceControlDTO**](ApiSourceControlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_source_control**
> ApiSourceControlDTO add_source_control(owner_type, internal_owner_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
body = swagger_client.ApiSourceControlDTO() # ApiSourceControlDTO |  (optional)

try:
    api_response = api_instance.add_source_control(owner_type, internal_owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceControlApi->add_source_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **body** | [**ApiSourceControlDTO**](ApiSourceControlDTO.md)|  | [optional] 

### Return type

[**ApiSourceControlDTO**](ApiSourceControlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_control**
> delete_source_control(owner_type, internal_owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 

try:
    api_instance.delete_source_control(owner_type, internal_owner_id)
except ApiException as e:
    print("Exception when calling SourceControlApi->delete_source_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_control1**
> ApiSourceControlDTO get_source_control1(owner_type, internal_owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 

try:
    api_response = api_instance.get_source_control1(owner_type, internal_owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceControlApi->get_source_control1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 

### Return type

[**ApiSourceControlDTO**](ApiSourceControlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source_control**
> ApiSourceControlDTO update_source_control(owner_type, internal_owner_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceControlApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
body = swagger_client.ApiSourceControlDTO() # ApiSourceControlDTO |  (optional)

try:
    api_response = api_instance.update_source_control(owner_type, internal_owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceControlApi->update_source_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **body** | [**ApiSourceControlDTO**](ApiSourceControlDTO.md)|  | [optional] 

### Return type

[**ApiSourceControlDTO**](ApiSourceControlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

