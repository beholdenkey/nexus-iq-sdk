# swagger_client.FirewallApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_firewall_auto_unquarantine_config**](FirewallApi.md#get_firewall_auto_unquarantine_config) | **GET** /api/v2/firewall/releaseQuarantine/configuration | 
[**get_firewall_unquarantine_summary**](FirewallApi.md#get_firewall_unquarantine_summary) | **GET** /api/v2/firewall/releaseQuarantine/summary | 
[**get_quarantine_list**](FirewallApi.md#get_quarantine_list) | **GET** /api/v2/firewall/components/quarantined | 
[**get_quarantine_summary**](FirewallApi.md#get_quarantine_summary) | **GET** /api/v2/firewall/quarantine/summary | 
[**get_quarantined_component_view_anonymous_access**](FirewallApi.md#get_quarantined_component_view_anonymous_access) | **GET** /api/v2/firewall/quarantinedComponentView/configuration/anonymousAccess | 
[**get_unquarantine_list**](FirewallApi.md#get_unquarantine_list) | **GET** /api/v2/firewall/components/autoReleasedFromQuarantine | 
[**set_firewall_auto_unquarantine_config**](FirewallApi.md#set_firewall_auto_unquarantine_config) | **PUT** /api/v2/firewall/releaseQuarantine/configuration | 
[**set_quarantined_component_view_anonymous_access**](FirewallApi.md#set_quarantined_component_view_anonymous_access) | **PUT** /api/v2/firewall/quarantinedComponentView/configuration/anonymousAccess/{enabled} | 

# **get_firewall_auto_unquarantine_config**
> list[ApiFirewallReleaseQuarantineConfigDTO] get_firewall_auto_unquarantine_config()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()

try:
    api_response = api_instance.get_firewall_auto_unquarantine_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_auto_unquarantine_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiFirewallReleaseQuarantineConfigDTO]**](ApiFirewallReleaseQuarantineConfigDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_unquarantine_summary**
> ApiFirewallReleaseQuarantineSummaryDTO get_firewall_unquarantine_summary()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()

try:
    api_response = api_instance.get_firewall_unquarantine_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_unquarantine_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiFirewallReleaseQuarantineSummaryDTO**](ApiFirewallReleaseQuarantineSummaryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quarantine_list**
> get_quarantine_list(page=page, page_size=page_size, policy_id=policy_id, sort_by=sort_by, asc=asc)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)
policy_id = 'policy_id_example' # str |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
asc = true # bool |  (optional) (default to true)

try:
    api_instance.get_quarantine_list(page=page, page_size=page_size, policy_id=policy_id, sort_by=sort_by, asc=asc)
except ApiException as e:
    print("Exception when calling FirewallApi->get_quarantine_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **policy_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quarantine_summary**
> ApiFirewallQuarantineSummaryDTO get_quarantine_summary()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()

try:
    api_response = api_instance.get_quarantine_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_quarantine_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiFirewallQuarantineSummaryDTO**](ApiFirewallQuarantineSummaryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quarantined_component_view_anonymous_access**
> get_quarantined_component_view_anonymous_access()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()

try:
    api_instance.get_quarantined_component_view_anonymous_access()
except ApiException as e:
    print("Exception when calling FirewallApi->get_quarantined_component_view_anonymous_access: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unquarantine_list**
> get_unquarantine_list(page=page, page_size=page_size, policy_id=policy_id, sort_by=sort_by, asc=asc)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)
policy_id = 'policy_id_example' # str |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
asc = true # bool |  (optional) (default to true)

try:
    api_instance.get_unquarantine_list(page=page, page_size=page_size, policy_id=policy_id, sort_by=sort_by, asc=asc)
except ApiException as e:
    print("Exception when calling FirewallApi->get_unquarantine_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **policy_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_firewall_auto_unquarantine_config**
> list[ApiFirewallReleaseQuarantineConfigDTO] set_firewall_auto_unquarantine_config(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()
body = [swagger_client.ApiFirewallReleaseQuarantineConfigDTO()] # list[ApiFirewallReleaseQuarantineConfigDTO] |  (optional)

try:
    api_response = api_instance.set_firewall_auto_unquarantine_config(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->set_firewall_auto_unquarantine_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ApiFirewallReleaseQuarantineConfigDTO]**](ApiFirewallReleaseQuarantineConfigDTO.md)|  | [optional] 

### Return type

[**list[ApiFirewallReleaseQuarantineConfigDTO]**](ApiFirewallReleaseQuarantineConfigDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_quarantined_component_view_anonymous_access**
> set_quarantined_component_view_anonymous_access(enabled)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirewallApi()
enabled = true # bool | 

try:
    api_instance.set_quarantined_component_view_anonymous_access(enabled)
except ApiException as e:
    print("Exception when calling FirewallApi->set_quarantined_component_view_anonymous_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

