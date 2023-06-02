# swagger_client.DataRetentionPoliciesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_retention_policies**](DataRetentionPoliciesApi.md#get_data_retention_policies) | **GET** /api/v2/dataRetentionPolicies/organizations/{organizationId} | 
[**set_data_retention_policies**](DataRetentionPoliciesApi.md#set_data_retention_policies) | **PUT** /api/v2/dataRetentionPolicies/organizations/{organizationId} | 

# **get_data_retention_policies**
> ApiDataRetentionPoliciesDTO get_data_retention_policies(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataRetentionPoliciesApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_data_retention_policies(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRetentionPoliciesApi->get_data_retention_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**ApiDataRetentionPoliciesDTO**](ApiDataRetentionPoliciesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_retention_policies**
> set_data_retention_policies(organization_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataRetentionPoliciesApi()
organization_id = 'organization_id_example' # str | 
body = swagger_client.ApiDataRetentionPoliciesDTO() # ApiDataRetentionPoliciesDTO |  (optional)

try:
    api_instance.set_data_retention_policies(organization_id, body=body)
except ApiException as e:
    print("Exception when calling DataRetentionPoliciesApi->set_data_retention_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **body** | [**ApiDataRetentionPoliciesDTO**](ApiDataRetentionPoliciesDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

