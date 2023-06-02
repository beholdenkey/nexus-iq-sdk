# swagger_client.PolicyWaiverApi

All URIs are relative to _/_

| Method                                                        | HTTP request                                                  | Description |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ----------- |
| [**add_policy_waiver**](PolicyWaiverApi.md#add_policy_waiver) | **POST** /api/v2/policyWaiver/{policyViolationId}/{ownerType} |

# **add_policy_waiver**

> add_policy_waiver(policy_violation_id, owner_type, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyWaiverApi()
policy_violation_id = 'policy_violation_id_example' # str |
owner_type = 'owner_type_example' # str |
body = 'body_example' # str |  (optional)

try:
    api_instance.add_policy_waiver(policy_violation_id, owner_type, body=body)
except ApiException as e:
    print("Exception when calling PolicyWaiverApi->add_policy_waiver: %s\n" % e)
```

### Parameters

| Name                    | Type              | Description | Notes      |
| ----------------------- | ----------------- | ----------- | ---------- |
| **policy_violation_id** | **str**           |             |
| **owner_type**          | **str**           |             |
| **body**                | [**str**](str.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
