# swagger_client.EvaluationApi

All URIs are relative to _/_

| Method                                                                                      | HTTP request                                                                     | Description |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------- |
| [**deprecated_manifest_evaluation**](EvaluationApi.md#deprecated_manifest_evaluation)       | **POST** /api/v2/evaluation/applications/{applicationId}/manifestEvaluation      |
| [**evaluate_components**](EvaluationApi.md#evaluate_components)                             | **POST** /api/v2/evaluation/applications/{applicationId}                         |
| [**evaluate_source_control**](EvaluationApi.md#evaluate_source_control)                     | **POST** /api/v2/evaluation/applications/{applicationId}/sourceControlEvaluation |
| [**get_application_evaluation_status**](EvaluationApi.md#get_application_evaluation_status) | **GET** /api/v2/evaluation/applications/{applicationId}/status/{statusId}        |
| [**get_component_evaluation**](EvaluationApi.md#get_component_evaluation)                   | **GET** /api/v2/evaluation/applications/{applicationId}/results/{resultId}       |
| [**promote_scan**](EvaluationApi.md#promote_scan)                                           | **POST** /api/v2/evaluation/applications/{applicationId}/promoteScan             |

# **deprecated_manifest_evaluation**

> ApiApplicationEvaluationStatusDTOV2 deprecated_manifest_evaluation(application_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
body = swagger_client.ApiSourceControlEvaluationRequestDTO() # ApiSourceControlEvaluationRequestDTO |  (optional)

try:
    api_response = api_instance.deprecated_manifest_evaluation(application_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->deprecated_manifest_evaluation: %s\n" % e)
```

### Parameters

| Name               | Type                                                                                | Description | Notes      |
| ------------------ | ----------------------------------------------------------------------------------- | ----------- | ---------- |
| **application_id** | **str**                                                                             |             |
| **body**           | [**ApiSourceControlEvaluationRequestDTO**](ApiSourceControlEvaluationRequestDTO.md) |             | [optional] |

### Return type

[**ApiApplicationEvaluationStatusDTOV2**](ApiApplicationEvaluationStatusDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_components**

> ApiComponentEvaluationTicketDTOV2 evaluate_components(application_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
body = swagger_client.ApiComponentEvaluationRequestDTOV2() # ApiComponentEvaluationRequestDTOV2 |  (optional)

try:
    api_response = api_instance.evaluate_components(application_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->evaluate_components: %s\n" % e)
```

### Parameters

| Name               | Type                                                                            | Description | Notes      |
| ------------------ | ------------------------------------------------------------------------------- | ----------- | ---------- |
| **application_id** | **str**                                                                         |             |
| **body**           | [**ApiComponentEvaluationRequestDTOV2**](ApiComponentEvaluationRequestDTOV2.md) |             | [optional] |

### Return type

[**ApiComponentEvaluationTicketDTOV2**](ApiComponentEvaluationTicketDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_source_control**

> ApiApplicationEvaluationStatusDTOV2 evaluate_source_control(application_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
body = swagger_client.ApiSourceControlEvaluationRequestDTO() # ApiSourceControlEvaluationRequestDTO |  (optional)

try:
    api_response = api_instance.evaluate_source_control(application_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->evaluate_source_control: %s\n" % e)
```

### Parameters

| Name               | Type                                                                                | Description | Notes      |
| ------------------ | ----------------------------------------------------------------------------------- | ----------- | ---------- |
| **application_id** | **str**                                                                             |             |
| **body**           | [**ApiSourceControlEvaluationRequestDTO**](ApiSourceControlEvaluationRequestDTO.md) |             | [optional] |

### Return type

[**ApiApplicationEvaluationStatusDTOV2**](ApiApplicationEvaluationStatusDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_evaluation_status**

> ApiApplicationEvaluationResultDTOV2 get_application_evaluation_status(application_id, status_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
status_id = 'status_id_example' # str |

try:
    api_response = api_instance.get_application_evaluation_status(application_id, status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->get_application_evaluation_status: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **status_id**      | **str** |             |

### Return type

[**ApiApplicationEvaluationResultDTOV2**](ApiApplicationEvaluationResultDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_evaluation**

> ApiComponentEvaluationResultDTOV2 get_component_evaluation(application_id, result_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
result_id = 'result_id_example' # str |

try:
    api_response = api_instance.get_component_evaluation(application_id, result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->get_component_evaluation: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **result_id**      | **str** |             |

### Return type

[**ApiComponentEvaluationResultDTOV2**](ApiComponentEvaluationResultDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_scan**

> ApiApplicationEvaluationStatusDTOV2 promote_scan(application_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvaluationApi()
application_id = 'application_id_example' # str |
body = swagger_client.ApiPromoteScanRequestDTOV2() # ApiPromoteScanRequestDTOV2 |  (optional)

try:
    api_response = api_instance.promote_scan(application_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->promote_scan: %s\n" % e)
```

### Parameters

| Name               | Type                                                            | Description | Notes      |
| ------------------ | --------------------------------------------------------------- | ----------- | ---------- |
| **application_id** | **str**                                                         |             |
| **body**           | [**ApiPromoteScanRequestDTOV2**](ApiPromoteScanRequestDTOV2.md) |             | [optional] |

### Return type

[**ApiApplicationEvaluationStatusDTOV2**](ApiApplicationEvaluationStatusDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
