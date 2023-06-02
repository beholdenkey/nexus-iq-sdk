# swagger_client.SecurityOverridesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_vulnerability_overrides**](SecurityOverridesApi.md#get_security_vulnerability_overrides) | **GET** /api/v2/securityOverrides | 

# **get_security_vulnerability_overrides**
> ApiSecurityVulnerabilityOverrideResponseDTOV2 get_security_vulnerability_overrides(ref_id=ref_id, component_purl=component_purl, owner_id=owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityOverridesApi()
ref_id = 'ref_id_example' # str |  (optional)
component_purl = 'component_purl_example' # str |  (optional)
owner_id = 'owner_id_example' # str |  (optional)

try:
    api_response = api_instance.get_security_vulnerability_overrides(ref_id=ref_id, component_purl=component_purl, owner_id=owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOverridesApi->get_security_vulnerability_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_id** | **str**|  | [optional] 
 **component_purl** | **str**|  | [optional] 
 **owner_id** | **str**|  | [optional] 

### Return type

[**ApiSecurityVulnerabilityOverrideResponseDTOV2**](ApiSecurityVulnerabilityOverrideResponseDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

