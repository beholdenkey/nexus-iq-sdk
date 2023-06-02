# swagger_client.ScanApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scan_status**](ScanApi.md#get_scan_status) | **GET** /api/v2/scan/applications/{applicationId}/status/{scanRequestId} | 
[**scan_components**](ScanApi.md#scan_components) | **POST** /api/v2/scan/applications/{applicationId}/sources/{source} | 

# **get_scan_status**
> ApiThirdPartyScanResultDTO get_scan_status(application_id, scan_request_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScanApi()
application_id = 'application_id_example' # str | 
scan_request_id = 'scan_request_id_example' # str | 

try:
    api_response = api_instance.get_scan_status(application_id, scan_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->get_scan_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **scan_request_id** | **str**|  | 

### Return type

[**ApiThirdPartyScanResultDTO**](ApiThirdPartyScanResultDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_components**
> scan_components(application_id, source, body=body, stage_id=stage_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScanApi()
application_id = 'application_id_example' # str | 
source = 'source_example' # str | 
body = 'body_example' # str |  (optional)
stage_id = 'build' # str |  (optional) (default to build)

try:
    api_instance.scan_components(application_id, source, body=body, stage_id=stage_id)
except ApiException as e:
    print("Exception when calling ScanApi->scan_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **source** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **stage_id** | **str**|  | [optional] [default to build]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

