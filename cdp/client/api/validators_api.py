"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from typing import Annotated, Any

from pydantic import Field, StrictFloat, StrictInt, StrictStr, validate_call

from cdp.client.api_client import ApiClient, RequestSerialized
from cdp.client.api_response import ApiResponse
from cdp.client.models.validator import Validator
from cdp.client.models.validator_list import ValidatorList
from cdp.client.models.validator_status import ValidatorStatus
from cdp.client.rest import RESTResponseType


class ValidatorsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_validator(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validator for.")
        ],
        validator_id: Annotated[
            StrictStr, Field(description="The unique id of the validator to fetch details for.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Validator:
        """Get a validator belonging to the CDP project

        Get a validator belonging to the user for a given network, asset and id.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validator for. (required)
        :type asset_id: str
        :param validator_id: The unique id of the validator to fetch details for. (required)
        :type validator_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_validator_serialize(
            network_id=network_id,
            asset_id=asset_id,
            validator_id=validator_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "Validator",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_validator_with_http_info(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validator for.")
        ],
        validator_id: Annotated[
            StrictStr, Field(description="The unique id of the validator to fetch details for.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Validator]:
        """Get a validator belonging to the CDP project

        Get a validator belonging to the user for a given network, asset and id.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validator for. (required)
        :type asset_id: str
        :param validator_id: The unique id of the validator to fetch details for. (required)
        :type validator_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_validator_serialize(
            network_id=network_id,
            asset_id=asset_id,
            validator_id=validator_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "Validator",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_validator_without_preload_content(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validator for.")
        ],
        validator_id: Annotated[
            StrictStr, Field(description="The unique id of the validator to fetch details for.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get a validator belonging to the CDP project

        Get a validator belonging to the user for a given network, asset and id.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validator for. (required)
        :type asset_id: str
        :param validator_id: The unique id of the validator to fetch details for. (required)
        :type validator_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_validator_serialize(
            network_id=network_id,
            asset_id=asset_id,
            validator_id=validator_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "Validator",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_validator_serialize(
        self,
        network_id,
        asset_id,
        validator_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if network_id is not None:
            _path_params["network_id"] = network_id
        if asset_id is not None:
            _path_params["asset_id"] = asset_id
        if validator_id is not None:
            _path_params["validator_id"] = validator_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # authentication setting
        _auth_settings: list[str] = []

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/v1/networks/{network_id}/assets/{asset_id}/validators/{validator_id}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def list_validators(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validators for.")
        ],
        status: Annotated[
            ValidatorStatus | None,
            Field(description="A filter to list validators based on a status."),
        ] = None,
        limit: Annotated[
            StrictInt | None,
            Field(
                description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50."
            ),
        ] = None,
        page: Annotated[
            Annotated[str, Field(strict=True, max_length=5000)] | None,
            Field(
                description="A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            ),
        ] = None,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ValidatorList:
        """List validators belonging to the CDP project

        List validators belonging to the user for a given network and asset.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validators for. (required)
        :type asset_id: str
        :param status: A filter to list validators based on a status.
        :type status: ValidatorStatus
        :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50.
        :type limit: int
        :param page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
        :type page: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._list_validators_serialize(
            network_id=network_id,
            asset_id=asset_id,
            status=status,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "ValidatorList",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def list_validators_with_http_info(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validators for.")
        ],
        status: Annotated[
            ValidatorStatus | None,
            Field(description="A filter to list validators based on a status."),
        ] = None,
        limit: Annotated[
            StrictInt | None,
            Field(
                description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50."
            ),
        ] = None,
        page: Annotated[
            Annotated[str, Field(strict=True, max_length=5000)] | None,
            Field(
                description="A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            ),
        ] = None,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ValidatorList]:
        """List validators belonging to the CDP project

        List validators belonging to the user for a given network and asset.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validators for. (required)
        :type asset_id: str
        :param status: A filter to list validators based on a status.
        :type status: ValidatorStatus
        :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50.
        :type limit: int
        :param page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
        :type page: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._list_validators_serialize(
            network_id=network_id,
            asset_id=asset_id,
            status=status,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "ValidatorList",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def list_validators_without_preload_content(
        self,
        network_id: Annotated[StrictStr, Field(description="The ID of the blockchain network.")],
        asset_id: Annotated[
            StrictStr, Field(description="The symbol of the asset to get the validators for.")
        ],
        status: Annotated[
            ValidatorStatus | None,
            Field(description="A filter to list validators based on a status."),
        ] = None,
        limit: Annotated[
            StrictInt | None,
            Field(
                description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50."
            ),
        ] = None,
        page: Annotated[
            Annotated[str, Field(strict=True, max_length=5000)] | None,
            Field(
                description="A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            ),
        ] = None,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List validators belonging to the CDP project

        List validators belonging to the user for a given network and asset.

        :param network_id: The ID of the blockchain network. (required)
        :type network_id: str
        :param asset_id: The symbol of the asset to get the validators for. (required)
        :type asset_id: str
        :param status: A filter to list validators based on a status.
        :type status: ValidatorStatus
        :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 50.
        :type limit: int
        :param page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
        :type page: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._list_validators_serialize(
            network_id=network_id,
            asset_id=asset_id,
            status=status,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "ValidatorList",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _list_validators_serialize(
        self,
        network_id,
        asset_id,
        status,
        limit,
        page,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if network_id is not None:
            _path_params["network_id"] = network_id
        if asset_id is not None:
            _path_params["asset_id"] = asset_id
        # process the query parameters
        if status is not None:
            _query_params.append(("status", status.value))

        if limit is not None:
            _query_params.append(("limit", limit))

        if page is not None:
            _query_params.append(("page", page))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # authentication setting
        _auth_settings: list[str] = []

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/v1/networks/{network_id}/assets/{asset_id}/validators",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
