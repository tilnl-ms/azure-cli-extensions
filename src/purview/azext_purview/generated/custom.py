# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def purview_account_list(client,
                         resource_group_name=None,
                         skip_token=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             skip_token=skip_token)
    return client.list_by_subscription(skip_token=skip_token)


def purview_account_show(client,
                         resource_group_name,
                         account_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name)


def purview_account_create(client,
                           resource_group_name,
                           account_name,
                           location=None,
                           tags=None,
                           sku=None,
                           managed_resource_group_name=None,
                           public_network_access=None,
                           no_wait=False):
    account = {}
    if location is not None:
        account['location'] = location
    if tags is not None:
        account['tags'] = tags
    account['identity'] = {}
    account['identity']['type'] = "SystemAssigned"
    if len(account['identity']) == 0:
        del account['identity']
    if sku is not None:
        account['sku'] = sku
    if managed_resource_group_name is not None:
        account['managed_resource_group_name'] = managed_resource_group_name
    if public_network_access is not None:
        account['public_network_access'] = public_network_access
    else:
        account['public_network_access'] = "Enabled"
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       account_name=account_name,
                       account=account)


def purview_account_update(client,
                           resource_group_name,
                           account_name,
                           tags=None,
                           managed_resource_group_name=None,
                           public_network_access=None,
                           no_wait=False):
    account_update_parameters = {}
    if tags is not None:
        account_update_parameters['tags'] = tags
    account_update_parameters['properties'] = {}
    if managed_resource_group_name is not None:
        account_update_parameters['properties']['managed_resource_group_name'] = managed_resource_group_name
    if public_network_access is not None:
        account_update_parameters['properties']['public_network_access'] = public_network_access
    else:
        account_update_parameters['properties']['public_network_access'] = "Enabled"
    if len(account_update_parameters['properties']) == 0:
        del account_update_parameters['properties']
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       account_name=account_name,
                       account_update_parameters=account_update_parameters)


def purview_account_delete(client,
                           resource_group_name,
                           account_name,
                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       account_name=account_name)


def purview_account_add_root_collection_admin(client,
                                              resource_group_name,
                                              account_name,
                                              object_id=None):
    collection_admin_update = {}
    if object_id is not None:
        collection_admin_update['object_id'] = object_id
    return client.add_root_collection_admin(resource_group_name=resource_group_name,
                                            account_name=account_name,
                                            collection_admin_update=collection_admin_update)


def purview_account_list_key(client,
                             resource_group_name,
                             account_name):
    return client.list_keys(resource_group_name=resource_group_name,
                            account_name=account_name)


def purview_default_account_show(client,
                                 scope_tenant_id,
                                 scope_type,
                                 scope=None):
    return client.get(scope_tenant_id=scope_tenant_id,
                      scope_type=scope_type,
                      scope=scope)


def purview_default_account_remove(client,
                                   scope_tenant_id,
                                   scope_type,
                                   scope=None):
    return client.remove(scope_tenant_id=scope_tenant_id,
                         scope_type=scope_type,
                         scope=scope)


def purview_default_account_set(client,
                                account_name=None,
                                resource_group_name=None,
                                scope=None,
                                scope_tenant_id=None,
                                scope_type=None,
                                subscription_id=None):
    default_account_payload = {}
    if account_name is not None:
        default_account_payload['account_name'] = account_name
    if resource_group_name is not None:
        default_account_payload['resource_group_name'] = resource_group_name
    if scope is not None:
        default_account_payload['scope'] = scope
    if scope_tenant_id is not None:
        default_account_payload['scope_tenant_id'] = scope_tenant_id
    if scope_type is not None:
        default_account_payload['scope_type'] = scope_type
    if subscription_id is not None:
        default_account_payload['subscription_id'] = subscription_id
    return client.set(default_account_payload=default_account_payload)
