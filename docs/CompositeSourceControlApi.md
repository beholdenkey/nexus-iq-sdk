# swagger_client.CompositeSourceControlApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_composite_source_control_by_owner**](CompositeSourceControlApi.md#get_composite_source_control_by_owner) | **GET** /api/v2/compositeSourceControl/{ownerType}/{internalOwnerId} | 

# **get_composite_source_control_by_owner**
> ApiCompositeSourceControlDTO get_composite_source_control_by_owner(owner_type, internal_owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompositeSourceControlApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 

try:
    api_response = api_instance.get_composite_source_control_by_owner(owner_type, internal_owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompositeSourceControlApi->get_composite_source_control_by_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 

### Return type

[**ApiCompositeSourceControlDTO**](ApiCompositeSourceControlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

