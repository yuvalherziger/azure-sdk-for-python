# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import CloudService
    from ._models_py3 import CloudServiceExtensionProfile
    from ._models_py3 import CloudServiceExtensionProperties
    from ._models_py3 import CloudServiceInstanceView
    from ._models_py3 import CloudServiceListResult
    from ._models_py3 import CloudServiceNetworkProfile
    from ._models_py3 import CloudServiceOsProfile
    from ._models_py3 import CloudServiceProperties
    from ._models_py3 import CloudServiceRole
    from ._models_py3 import CloudServiceRoleListResult
    from ._models_py3 import CloudServiceRoleProfile
    from ._models_py3 import CloudServiceRoleProfileProperties
    from ._models_py3 import CloudServiceRoleProperties
    from ._models_py3 import CloudServiceRoleSku
    from ._models_py3 import CloudServiceUpdate
    from ._models_py3 import CloudServiceVaultAndSecretReference
    from ._models_py3 import CloudServiceVaultCertificate
    from ._models_py3 import CloudServiceVaultSecretGroup
    from ._models_py3 import Extension
    from ._models_py3 import InnerError
    from ._models_py3 import InstanceSku
    from ._models_py3 import InstanceViewStatusesSummary
    from ._models_py3 import LoadBalancerConfiguration
    from ._models_py3 import LoadBalancerConfigurationProperties
    from ._models_py3 import LoadBalancerFrontendIPConfiguration
    from ._models_py3 import LoadBalancerFrontendIPConfigurationProperties
    from ._models_py3 import ResourceInstanceViewStatus
    from ._models_py3 import RoleInstance
    from ._models_py3 import RoleInstanceListResult
    from ._models_py3 import RoleInstanceNetworkProfile
    from ._models_py3 import RoleInstanceProperties
    from ._models_py3 import RoleInstanceView
    from ._models_py3 import RoleInstances
    from ._models_py3 import StatusCodeCount
    from ._models_py3 import SubResource
    from ._models_py3 import UpdateDomain
    from ._models_py3 import UpdateDomainListResult
except (SyntaxError, ImportError):
    from ._models import ApiError  # type: ignore
    from ._models import ApiErrorBase  # type: ignore
    from ._models import CloudService  # type: ignore
    from ._models import CloudServiceExtensionProfile  # type: ignore
    from ._models import CloudServiceExtensionProperties  # type: ignore
    from ._models import CloudServiceInstanceView  # type: ignore
    from ._models import CloudServiceListResult  # type: ignore
    from ._models import CloudServiceNetworkProfile  # type: ignore
    from ._models import CloudServiceOsProfile  # type: ignore
    from ._models import CloudServiceProperties  # type: ignore
    from ._models import CloudServiceRole  # type: ignore
    from ._models import CloudServiceRoleListResult  # type: ignore
    from ._models import CloudServiceRoleProfile  # type: ignore
    from ._models import CloudServiceRoleProfileProperties  # type: ignore
    from ._models import CloudServiceRoleProperties  # type: ignore
    from ._models import CloudServiceRoleSku  # type: ignore
    from ._models import CloudServiceUpdate  # type: ignore
    from ._models import CloudServiceVaultAndSecretReference  # type: ignore
    from ._models import CloudServiceVaultCertificate  # type: ignore
    from ._models import CloudServiceVaultSecretGroup  # type: ignore
    from ._models import Extension  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import InstanceSku  # type: ignore
    from ._models import InstanceViewStatusesSummary  # type: ignore
    from ._models import LoadBalancerConfiguration  # type: ignore
    from ._models import LoadBalancerConfigurationProperties  # type: ignore
    from ._models import LoadBalancerFrontendIPConfiguration  # type: ignore
    from ._models import LoadBalancerFrontendIPConfigurationProperties  # type: ignore
    from ._models import ResourceInstanceViewStatus  # type: ignore
    from ._models import RoleInstance  # type: ignore
    from ._models import RoleInstanceListResult  # type: ignore
    from ._models import RoleInstanceNetworkProfile  # type: ignore
    from ._models import RoleInstanceProperties  # type: ignore
    from ._models import RoleInstanceView  # type: ignore
    from ._models import RoleInstances  # type: ignore
    from ._models import StatusCodeCount  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import UpdateDomain  # type: ignore
    from ._models import UpdateDomainListResult  # type: ignore

from ._compute_management_client_enums import (
    CloudServiceUpgradeMode,
    StatusLevelTypes,
)

__all__ = [
    'ApiError',
    'ApiErrorBase',
    'CloudService',
    'CloudServiceExtensionProfile',
    'CloudServiceExtensionProperties',
    'CloudServiceInstanceView',
    'CloudServiceListResult',
    'CloudServiceNetworkProfile',
    'CloudServiceOsProfile',
    'CloudServiceProperties',
    'CloudServiceRole',
    'CloudServiceRoleListResult',
    'CloudServiceRoleProfile',
    'CloudServiceRoleProfileProperties',
    'CloudServiceRoleProperties',
    'CloudServiceRoleSku',
    'CloudServiceUpdate',
    'CloudServiceVaultAndSecretReference',
    'CloudServiceVaultCertificate',
    'CloudServiceVaultSecretGroup',
    'Extension',
    'InnerError',
    'InstanceSku',
    'InstanceViewStatusesSummary',
    'LoadBalancerConfiguration',
    'LoadBalancerConfigurationProperties',
    'LoadBalancerFrontendIPConfiguration',
    'LoadBalancerFrontendIPConfigurationProperties',
    'ResourceInstanceViewStatus',
    'RoleInstance',
    'RoleInstanceListResult',
    'RoleInstanceNetworkProfile',
    'RoleInstanceProperties',
    'RoleInstanceView',
    'RoleInstances',
    'StatusCodeCount',
    'SubResource',
    'UpdateDomain',
    'UpdateDomainListResult',
    'CloudServiceUpgradeMode',
    'StatusLevelTypes',
]
