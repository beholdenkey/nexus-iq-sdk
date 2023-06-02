# swagger_client.ApplicationsApi

All URIs are relative to _/_

| Method                                                                                            | HTTP request                                                                       | Description |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| [**add_application**](ApplicationsApi.md#add_application)                                         | **POST** /api/v2/applications                                                      |
| [**clone_application**](ApplicationsApi.md#clone_application)                                     | **POST** /api/v2/applications/{sourceApplicationId}/clone                          |
| [**delete_application**](ApplicationsApi.md#delete_application)                                   | **DELETE** /api/v2/applications/{applicationId}                                    |
| [**get_application**](ApplicationsApi.md#get_application)                                         | **GET** /api/v2/applications/{applicationId}                                       |
| [**get_applications**](ApplicationsApi.md#get_applications)                                       | **GET** /api/v2/applications                                                       |
| [**get_applications_by_organization_id**](ApplicationsApi.md#get_applications_by_organization_id) | **GET** /api/v2/applications/organization/{organizationId}                         |
| [**get_data**](ApplicationsApi.md#get_data)                                                       | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}                |
| [**get_dependency_tree**](ApplicationsApi.md#get_dependency_tree)                                 | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/dependencyTree |
| [**get_policy_violation_diff**](ApplicationsApi.md#get_policy_violation_diff)                     | **GET** /api/v2/applications/{applicationPublicId}/reports/policyViolations/diff   |
| [**get_policy_violations1**](ApplicationsApi.md#get_policy_violations1)                           | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/policy         |
| [**get_raw_data**](ApplicationsApi.md#get_raw_data)                                               | **GET** /api/v2/applications/{applicationPublicId}/reports/{scanId}/raw            |
| [**move_application**](ApplicationsApi.md#move_application)                                       | **POST** /api/v2/applications/{applicationId}/move/organization/{organizationId}   |
| [**update_application**](ApplicationsApi.md#update_application)                                   | **PUT** /api/v2/applications/{applicationId}                                       |

# **add_application**

> ApiApplicationDTO add_application(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
body = swagger_client.ApiApplicationDTO() # ApiApplicationDTO |  (optional)

try:
    api_response = api_instance.add_application(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->add_application: %s\n" % e)
```

### Parameters

| Name     | Type                                          | Description | Notes      |
| -------- | --------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiApplicationDTO**](ApiApplicationDTO.md) |             | [optional] |

### Return type

[**ApiApplicationDTO**](ApiApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_application**

> ApiApplicationDTO clone_application(source_application_id, cloned_application_name=cloned_application_name, cloned_application_public_id=cloned_application_public_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
source_application_id = 'source_application_id_example' # str |
cloned_application_name = 'cloned_application_name_example' # str |  (optional)
cloned_application_public_id = 'cloned_application_public_id_example' # str |  (optional)

try:
    api_response = api_instance.clone_application(source_application_id, cloned_application_name=cloned_application_name, cloned_application_public_id=cloned_application_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->clone_application: %s\n" % e)
```

### Parameters

| Name                             | Type    | Description | Notes      |
| -------------------------------- | ------- | ----------- | ---------- |
| **source_application_id**        | **str** |             |
| **cloned_application_name**      | **str** |             | [optional] |
| **cloned_application_public_id** | **str** |             | [optional] |

### Return type

[**ApiApplicationDTO**](ApiApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**

> delete_application(application_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_id = 'application_id_example' # str |

try:
    api_instance.delete_application(application_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**

> ApiApplicationDTO get_application(application_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_id = 'application_id_example' # str |

try:
    api_response = api_instance.get_application(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |

### Return type

[**ApiApplicationDTO**](ApiApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**

> list[ApiApplicationDTO] get_applications(public_id=public_id, include_categories=include_categories)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
public_id = ['public_id_example'] # list[str] |  (optional)
include_categories = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_applications(public_id=public_id, include_categories=include_categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_applications: %s\n" % e)
```

### Parameters

| Name                   | Type                    | Description | Notes                         |
| ---------------------- | ----------------------- | ----------- | ----------------------------- |
| **public_id**          | [**list[str]**](str.md) |             | [optional]                    |
| **include_categories** | **bool**                |             | [optional] [default to false] |

### Return type

[**list[ApiApplicationDTO]**](ApiApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_by_organization_id**

> ApiApplicationListDTO get_applications_by_organization_id(organization_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
organization_id = 'organization_id_example' # str |

try:
    api_response = api_instance.get_applications_by_organization_id(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_applications_by_organization_id: %s\n" % e)
```

### Parameters

| Name                | Type    | Description | Notes |
| ------------------- | ------- | ----------- | ----- |
| **organization_id** | **str** |             |

### Return type

[**ApiApplicationListDTO**](ApiApplicationListDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data**

> get_data(application_public_id, scan_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_public_id = 'application_public_id_example' # str |
scan_id = 'scan_id_example' # str |

try:
    api_instance.get_data(application_public_id, scan_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_data: %s\n" % e)
```

### Parameters

| Name                      | Type    | Description | Notes |
| ------------------------- | ------- | ----------- | ----- |
| **application_public_id** | **str** |             |
| **scan_id**               | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependency_tree**

> ApiDependencyTreeResponseDTO get_dependency_tree(application_public_id, scan_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_public_id = 'application_public_id_example' # str |
scan_id = 'scan_id_example' # str |

try:
    api_response = api_instance.get_dependency_tree(application_public_id, scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_dependency_tree: %s\n" % e)
```

### Parameters

| Name                      | Type    | Description | Notes |
| ------------------------- | ------- | ----------- | ----- |
| **application_public_id** | **str** |             |
| **scan_id**               | **str** |             |

### Return type

[**ApiDependencyTreeResponseDTO**](ApiDependencyTreeResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_violation_diff**

> ApiPolicyViolationDiffDTO get_policy_violation_diff(application_public_id, from_commit=from_commit, to_commit=to_commit, from_policy_evaluation_id=from_policy_evaluation_id, to_policy_evaluation_id=to_policy_evaluation_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_public_id = 'application_public_id_example' # str |
from_commit = 'from_commit_example' # str |  (optional)
to_commit = 'to_commit_example' # str |  (optional)
from_policy_evaluation_id = 'from_policy_evaluation_id_example' # str |  (optional)
to_policy_evaluation_id = 'to_policy_evaluation_id_example' # str |  (optional)

try:
    api_response = api_instance.get_policy_violation_diff(application_public_id, from_commit=from_commit, to_commit=to_commit, from_policy_evaluation_id=from_policy_evaluation_id, to_policy_evaluation_id=to_policy_evaluation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_policy_violation_diff: %s\n" % e)
```

### Parameters

| Name                          | Type    | Description | Notes      |
| ----------------------------- | ------- | ----------- | ---------- |
| **application_public_id**     | **str** |             |
| **from_commit**               | **str** |             | [optional] |
| **to_commit**                 | **str** |             | [optional] |
| **from_policy_evaluation_id** | **str** |             | [optional] |
| **to_policy_evaluation_id**   | **str** |             | [optional] |

### Return type

[**ApiPolicyViolationDiffDTO**](ApiPolicyViolationDiffDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_violations1**

> ApiReportPolicyDataDTOV2 get_policy_violations1(application_public_id, scan_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_public_id = 'application_public_id_example' # str |
scan_id = 'scan_id_example' # str |

try:
    api_response = api_instance.get_policy_violations1(application_public_id, scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_policy_violations1: %s\n" % e)
```

### Parameters

| Name                      | Type    | Description | Notes |
| ------------------------- | ------- | ----------- | ----- |
| **application_public_id** | **str** |             |
| **scan_id**               | **str** |             |

### Return type

[**ApiReportPolicyDataDTOV2**](ApiReportPolicyDataDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_data**

> ApiReportRawDataDTOV2 get_raw_data(application_public_id, scan_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_public_id = 'application_public_id_example' # str |
scan_id = 'scan_id_example' # str |

try:
    api_response = api_instance.get_raw_data(application_public_id, scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_raw_data: %s\n" % e)
```

### Parameters

| Name                      | Type    | Description | Notes |
| ------------------------- | ------- | ----------- | ----- |
| **application_public_id** | **str** |             |
| **scan_id**               | **str** |             |

### Return type

[**ApiReportRawDataDTOV2**](ApiReportRawDataDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_application**

> ApiMoveApplicationResponseDTOV2 move_application(application_id, organization_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_id = 'application_id_example' # str |
organization_id = 'organization_id_example' # str |

try:
    api_response = api_instance.move_application(application_id, organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->move_application: %s\n" % e)
```

### Parameters

| Name                | Type    | Description | Notes |
| ------------------- | ------- | ----------- | ----- |
| **application_id**  | **str** |             |
| **organization_id** | **str** |             |

### Return type

[**ApiMoveApplicationResponseDTOV2**](ApiMoveApplicationResponseDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**

> ApiApplicationDTO update_application(application_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
application_id = 'application_id_example' # str |
body = swagger_client.ApiApplicationDTO() # ApiApplicationDTO |  (optional)

try:
    api_response = api_instance.update_application(application_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->update_application: %s\n" % e)
```

### Parameters

| Name               | Type                                          | Description | Notes      |
| ------------------ | --------------------------------------------- | ----------- | ---------- |
| **application_id** | **str**                                       |             |
| **body**           | [**ApiApplicationDTO**](ApiApplicationDTO.md) |             | [optional] |

### Return type

[**ApiApplicationDTO**](ApiApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
