# swagger_client.PolicyViolationsApi

All URIs are relative to _/_

| Method                                                                                                                                            | HTTP request                                                                       | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| [**get_applicable_waivers**](PolicyViolationsApi.md#get_applicable_waivers)                                                                       | **GET** /api/v2/policyViolations/{violationId}/applicableWaivers                   |
| [**get_cross_stage_policy_violation_by_constituent_id**](PolicyViolationsApi.md#get_cross_stage_policy_violation_by_constituent_id)               | **GET** /api/v2/policyViolations/crossStage                                        |
| [**get_cross_stage_policy_violation_by_id**](PolicyViolationsApi.md#get_cross_stage_policy_violation_by_id)                                       | **GET** /api/v2/policyViolations/crossStage/{violationId}                          |
| [**get_policy_violations**](PolicyViolationsApi.md#get_policy_violations)                                                                         | **GET** /api/v2/policyViolations                                                   |
| [**get_transitive_policy_violations_by_app_scan_component**](PolicyViolationsApi.md#get_transitive_policy_violations_by_app_scan_component)       | **GET** /api/v2/policyViolations/transitive/{ownerType}/{ownerId}/{scanId}         |
| [**get_transitive_policy_violations_by_owner_stage_component**](PolicyViolationsApi.md#get_transitive_policy_violations_by_owner_stage_component) | **GET** /api/v2/policyViolations/transitive/{ownerType}/{ownerId}/stages/{stageId} |

# **get_applicable_waivers**

> ApiPolicyWaiversApplicableToViolationDTO get_applicable_waivers(violation_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
violation_id = 'violation_id_example' # str |

try:
    api_response = api_instance.get_applicable_waivers(violation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_applicable_waivers: %s\n" % e)
```

### Parameters

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **violation_id** | **str** |             |

### Return type

[**ApiPolicyWaiversApplicableToViolationDTO**](ApiPolicyWaiversApplicableToViolationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_stage_policy_violation_by_constituent_id**

> ApiCrossStageViolationDTOV2 get_cross_stage_policy_violation_by_constituent_id(constituent_id=constituent_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
constituent_id = 'constituent_id_example' # str |  (optional)

try:
    api_response = api_instance.get_cross_stage_policy_violation_by_constituent_id(constituent_id=constituent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_cross_stage_policy_violation_by_constituent_id: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **constituent_id** | **str** |             | [optional] |

### Return type

[**ApiCrossStageViolationDTOV2**](ApiCrossStageViolationDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_stage_policy_violation_by_id**

> ApiCrossStageViolationDTOV2 get_cross_stage_policy_violation_by_id(violation_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
violation_id = 'violation_id_example' # str |

try:
    api_response = api_instance.get_cross_stage_policy_violation_by_id(violation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_cross_stage_policy_violation_by_id: %s\n" % e)
```

### Parameters

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **violation_id** | **str** |             |

### Return type

[**ApiCrossStageViolationDTOV2**](ApiCrossStageViolationDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_violations**

> ApiApplicationViolationListDTOV2 get_policy_violations(p=p)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
p = ['p_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_policy_violations(p=p)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_policy_violations: %s\n" % e)
```

### Parameters

| Name  | Type                    | Description | Notes      |
| ----- | ----------------------- | ----------- | ---------- |
| **p** | [**list[str]**](str.md) |             | [optional] |

### Return type

[**ApiApplicationViolationListDTOV2**](ApiApplicationViolationListDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transitive_policy_violations_by_app_scan_component**

> ApiComponentTransitivePolicyViolationsDTO get_transitive_policy_violations_by_app_scan_component(owner_type, owner_id, scan_id, component_identifier=component_identifier, package_url=package_url, hash=hash)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
scan_id = 'scan_id_example' # str |
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    api_response = api_instance.get_transitive_policy_violations_by_app_scan_component(owner_type, owner_id, scan_id, component_identifier=component_identifier, package_url=package_url, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_transitive_policy_violations_by_app_scan_component: %s\n" % e)
```

### Parameters

| Name                     | Type                           | Description | Notes      |
| ------------------------ | ------------------------------ | ----------- | ---------- |
| **owner_type**           | **str**                        |             |
| **owner_id**             | **str**                        |             |
| **scan_id**              | **str**                        |             |
| **component_identifier** | [**ComponentIdentifier**](.md) |             | [optional] |
| **package_url**          | **str**                        |             | [optional] |
| **hash**                 | **str**                        |             | [optional] |

### Return type

[**ApiComponentTransitivePolicyViolationsDTO**](ApiComponentTransitivePolicyViolationsDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transitive_policy_violations_by_owner_stage_component**

> ApiComponentTransitivePolicyViolationsDTO get_transitive_policy_violations_by_owner_stage_component(owner_type, owner_id, stage_id, component_identifier=component_identifier, package_url=package_url, hash=hash)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyViolationsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
stage_id = 'stage_id_example' # str |
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    api_response = api_instance.get_transitive_policy_violations_by_owner_stage_component(owner_type, owner_id, stage_id, component_identifier=component_identifier, package_url=package_url, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyViolationsApi->get_transitive_policy_violations_by_owner_stage_component: %s\n" % e)
```

### Parameters

| Name                     | Type                           | Description | Notes      |
| ------------------------ | ------------------------------ | ----------- | ---------- |
| **owner_type**           | **str**                        |             |
| **owner_id**             | **str**                        |             |
| **stage_id**             | **str**                        |             |
| **component_identifier** | [**ComponentIdentifier**](.md) |             | [optional] |
| **package_url**          | **str**                        |             | [optional] |
| **hash**                 | **str**                        |             | [optional] |

### Return type

[**ApiComponentTransitivePolicyViolationsDTO**](ApiComponentTransitivePolicyViolationsDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
