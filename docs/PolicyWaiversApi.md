# swagger_client.PolicyWaiversApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_waiver_by_policy_violation_id**](PolicyWaiversApi.md#add_policy_waiver_by_policy_violation_id) | **POST** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyViolationId} | 
[**add_waiver_to_transitive_policy_violations_by_app_scan_component**](PolicyWaiversApi.md#add_waiver_to_transitive_policy_violations_by_app_scan_component) | **POST** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/{scanId} | 
[**add_waiver_to_transitive_policy_violations_by_owner_stage_component**](PolicyWaiversApi.md#add_waiver_to_transitive_policy_violations_by_owner_stage_component) | **POST** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/stages/{stageId} | 
[**delete_policy_waiver**](PolicyWaiversApi.md#delete_policy_waiver) | **DELETE** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyWaiverId} | 
[**get_policy_waiver**](PolicyWaiversApi.md#get_policy_waiver) | **GET** /api/v2/policyWaivers/{ownerType}/{ownerId}/{policyWaiverId} | 
[**get_policy_waivers**](PolicyWaiversApi.md#get_policy_waivers) | **GET** /api/v2/policyWaivers/{ownerType}/{ownerId} | 
[**get_transitive_policy_waivers_by_app_scan_component**](PolicyWaiversApi.md#get_transitive_policy_waivers_by_app_scan_component) | **GET** /api/v2/policyWaivers/transitive/{ownerType}/{ownerId}/{scanId} | 

# **add_policy_waiver_by_policy_violation_id**
> add_policy_waiver_by_policy_violation_id(owner_type, owner_id, policy_violation_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
policy_violation_id = 'policy_violation_id_example' # str | 
body = swagger_client.ApiWaiverOptionsDTO() # ApiWaiverOptionsDTO |  (optional)

try:
    api_instance.add_policy_waiver_by_policy_violation_id(owner_type, owner_id, policy_violation_id, body=body)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->add_policy_waiver_by_policy_violation_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **policy_violation_id** | **str**|  | 
 **body** | [**ApiWaiverOptionsDTO**](ApiWaiverOptionsDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_waiver_to_transitive_policy_violations_by_app_scan_component**
> add_waiver_to_transitive_policy_violations_by_app_scan_component(owner_type, owner_id, scan_id, body=body, component_identifier=component_identifier, package_url=package_url, hash=hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
scan_id = 'scan_id_example' # str | 
body = swagger_client.ApiWaiverOptionsDTO() # ApiWaiverOptionsDTO |  (optional)
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    api_instance.add_waiver_to_transitive_policy_violations_by_app_scan_component(owner_type, owner_id, scan_id, body=body, component_identifier=component_identifier, package_url=package_url, hash=hash)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->add_waiver_to_transitive_policy_violations_by_app_scan_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **scan_id** | **str**|  | 
 **body** | [**ApiWaiverOptionsDTO**](ApiWaiverOptionsDTO.md)|  | [optional] 
 **component_identifier** | [**ComponentIdentifier**](.md)|  | [optional] 
 **package_url** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_waiver_to_transitive_policy_violations_by_owner_stage_component**
> add_waiver_to_transitive_policy_violations_by_owner_stage_component(owner_type, owner_id, stage_id, body=body, component_identifier=component_identifier, package_url=package_url, hash=hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
stage_id = 'stage_id_example' # str | 
body = swagger_client.ApiWaiverOptionsDTO() # ApiWaiverOptionsDTO |  (optional)
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    api_instance.add_waiver_to_transitive_policy_violations_by_owner_stage_component(owner_type, owner_id, stage_id, body=body, component_identifier=component_identifier, package_url=package_url, hash=hash)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->add_waiver_to_transitive_policy_violations_by_owner_stage_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **stage_id** | **str**|  | 
 **body** | [**ApiWaiverOptionsDTO**](ApiWaiverOptionsDTO.md)|  | [optional] 
 **component_identifier** | [**ComponentIdentifier**](.md)|  | [optional] 
 **package_url** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_waiver**
> delete_policy_waiver(owner_type, owner_id, policy_waiver_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
policy_waiver_id = 'policy_waiver_id_example' # str | 

try:
    api_instance.delete_policy_waiver(owner_type, owner_id, policy_waiver_id)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->delete_policy_waiver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **policy_waiver_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_waiver**
> ApiPolicyWaiverDTO get_policy_waiver(owner_type, owner_id, policy_waiver_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
policy_waiver_id = 'policy_waiver_id_example' # str | 

try:
    api_response = api_instance.get_policy_waiver(owner_type, owner_id, policy_waiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->get_policy_waiver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **policy_waiver_id** | **str**|  | 

### Return type

[**ApiPolicyWaiverDTO**](ApiPolicyWaiverDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_waivers**
> list[ApiPolicyWaiverDTO] get_policy_waivers(owner_type, owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 

try:
    api_response = api_instance.get_policy_waivers(owner_type, owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->get_policy_waivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 

### Return type

[**list[ApiPolicyWaiverDTO]**](ApiPolicyWaiverDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transitive_policy_waivers_by_app_scan_component**
> ApiComponentPolicyWaiversDTO get_transitive_policy_waivers_by_app_scan_component(owner_type, owner_id, scan_id, component_identifier=component_identifier, package_url=package_url, hash=hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiversApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
scan_id = 'scan_id_example' # str | 
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    api_response = api_instance.get_transitive_policy_waivers_by_app_scan_component(owner_type, owner_id, scan_id, component_identifier=component_identifier, package_url=package_url, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyWaiversApi->get_transitive_policy_waivers_by_app_scan_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **scan_id** | **str**|  | 
 **component_identifier** | [**ComponentIdentifier**](.md)|  | [optional] 
 **package_url** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 

### Return type

[**ApiComponentPolicyWaiversDTO**](ApiComponentPolicyWaiversDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

