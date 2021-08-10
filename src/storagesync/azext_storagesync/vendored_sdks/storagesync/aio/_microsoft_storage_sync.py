# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MicrosoftStorageSyncConfiguration
from .operations import Operations
from .operations import StorageSyncServicesOperations
from .operations import SyncGroupsOperations
from .operations import CloudEndpointsOperations
from .operations import ServerEndpointsOperations
from .operations import RegisteredServersOperations
from .operations import WorkflowsOperations
from .operations import OperationStatusOperations
from .. import models


class MicrosoftStorageSync(object):
    """Microsoft Storage Sync Service API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storagesync.aio.operations.Operations
    :ivar storage_sync_services: StorageSyncServicesOperations operations
    :vartype storage_sync_services: azure.mgmt.storagesync.aio.operations.StorageSyncServicesOperations
    :ivar sync_groups: SyncGroupsOperations operations
    :vartype sync_groups: azure.mgmt.storagesync.aio.operations.SyncGroupsOperations
    :ivar cloud_endpoints: CloudEndpointsOperations operations
    :vartype cloud_endpoints: azure.mgmt.storagesync.aio.operations.CloudEndpointsOperations
    :ivar server_endpoints: ServerEndpointsOperations operations
    :vartype server_endpoints: azure.mgmt.storagesync.aio.operations.ServerEndpointsOperations
    :ivar registered_servers: RegisteredServersOperations operations
    :vartype registered_servers: azure.mgmt.storagesync.aio.operations.RegisteredServersOperations
    :ivar workflows: WorkflowsOperations operations
    :vartype workflows: azure.mgmt.storagesync.aio.operations.WorkflowsOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: azure.mgmt.storagesync.aio.operations.OperationStatusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftStorageSyncConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_sync_services = StorageSyncServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sync_groups = SyncGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_endpoints = CloudEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_endpoints = ServerEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_servers = RegisteredServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflows = WorkflowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MicrosoftStorageSync":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
