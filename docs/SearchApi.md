# swagger_client.SearchApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_search_index_async**](SearchApi.md#create_search_index_async) | **POST** /api/v2/search/advanced/index | 
[**get_export_results**](SearchApi.md#get_export_results) | **GET** /api/v2/search/advanced/export/csv | 
[**search_component**](SearchApi.md#search_component) | **GET** /api/v2/search/component | 
[**search_index**](SearchApi.md#search_index) | **GET** /api/v2/search/advanced | 

# **create_search_index_async**
> create_search_index_async()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()

try:
    api_instance.create_search_index_async()
except ApiException as e:
    print("Exception when calling SearchApi->create_search_index_async: %s\n" % e)
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

# **get_export_results**
> get_export_results(query=query, all_components=all_components)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
query = 'query_example' # str |  (optional)
all_components = false # bool |  (optional) (default to false)

try:
    api_instance.get_export_results(query=query, all_components=all_components)
except ApiException as e:
    print("Exception when calling SearchApi->get_export_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **all_components** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_component**
> ApiSearchResultsDTOV2 search_component(stage_id=stage_id, hash=hash, component_identifier=component_identifier, package_url=package_url)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
stage_id = 'stage_id_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)

try:
    api_response = api_instance.search_component(stage_id=stage_id, hash=hash, component_identifier=component_identifier, package_url=package_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_id** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 
 **component_identifier** | [**ComponentIdentifier**](.md)|  | [optional] 
 **package_url** | **str**|  | [optional] 

### Return type

[**ApiSearchResultsDTOV2**](ApiSearchResultsDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_index**
> SearchResultDTO search_index(query=query, page_size=page_size, page=page, all_components=all_components)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
query = 'query_example' # str |  (optional)
page_size = 10 # int |  (optional) (default to 10)
page = 56 # int |  (optional)
all_components = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.search_index(query=query, page_size=page_size, page=page, all_components=all_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 10]
 **page** | **int**|  | [optional] 
 **all_components** | **bool**|  | [optional] [default to false]

### Return type

[**SearchResultDTO**](SearchResultDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

