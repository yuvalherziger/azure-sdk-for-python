# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest
import pytest
import utils._test_utils as _test_utils
import utils._test_constants as _test_constants

from typing import List
from parameterized import parameterized
from azure.communication.callingserver import (CreateCallOptions, MediaType,
    EventSubscriptionType, JoinCallOptions, CommunicationIdentifier, CommunicationUserIdentifier, PhoneNumberIdentifier)
try:
    from unittest.mock import Mock, patch
except ImportError:  # python < 3.3
    from mock import Mock, patch  # type: ignore


def data_source_test_create_connection():
    options = CreateCallOptions(
            callback_uri=_test_constants.CALLBACK_URI,
            requested_media_types=[MediaType.AUDIO],
            requested_call_events=[EventSubscriptionType.PARTICIPANTS_UPDATED])
    options.subject=_test_constants.CALL_SUBJECT
    options.alternate_Caller_Id = PhoneNumberIdentifier(_test_constants.PHONE_NUMBER)

    parameters = []
    parameters.append((
        _test_constants.ClientType_ConnectionString,
        CommunicationUserIdentifier(_test_constants.RESOURCE_SOURCE),
        [CommunicationUserIdentifier(_test_constants.RESOURCE_TARGET), PhoneNumberIdentifier(_test_constants.PHONE_NUMBER)],
        options,
        ))

    parameters.append((
        _test_constants.ClientType_ManagedIdentity,
        CommunicationUserIdentifier(_test_constants.RESOURCE_SOURCE),
        [CommunicationUserIdentifier(_test_constants.RESOURCE_TARGET), PhoneNumberIdentifier(_test_constants.PHONE_NUMBER)],
        options,
        True,
        ))

    return parameters

def data_source_test_join_call():
    options = JoinCallOptions(
            callback_uri=_test_constants.CALLBACK_URI,
            requested_media_types=[MediaType.AUDIO],
            requested_call_events=[EventSubscriptionType.PARTICIPANTS_UPDATED])
    options.subject=_test_constants.CALL_SUBJECT

    parameters = []
    parameters.append((
        _test_constants.ClientType_ConnectionString,
        _test_constants.SEVERCALL_ID,
        CommunicationUserIdentifier(_test_constants.RESOURCE_SOURCE),
        options,
        ))

    parameters.append((
        _test_constants.ClientType_ManagedIdentity,
        _test_constants.SEVERCALL_ID,
        CommunicationUserIdentifier(_test_constants.RESOURCE_SOURCE),
        options,
        True,
        ))

    return parameters

class TestCallingServerClient(unittest.TestCase):

    @parameterized.expand(data_source_test_create_connection())
    def test_create_connection_succeed(
        self,
        test_name, # type: str
        source_user, # type: CommunicationIdentifier
        target_users, # type: List[CommunicationIdentifier]
        options, # type: CreateCallOptions,
        use_managed_identity = False # type: bool
        ):

        calling_server_client = _test_utils.create_mock_calling_server_client(
            status_code=201,
            payload=_test_constants.CreateOrJoinCallPayload,
            use_managed_identity = use_managed_identity
            )

        call_connection = calling_server_client.create_call_connection(source_user,
            target_users, options)
        assert call_connection.call_connection_id == _test_constants.CALL_ID

    @parameterized.expand(data_source_test_create_connection())
    def test_create_connection_failed(
        self,
        test_name, # type: str
        source_user, # type: CommunicationIdentifier
        target_users, # type: List[CommunicationIdentifier]
        options, # type: CreateCallOptions,
        use_managed_identity = False # type: bool
        ):

        calling_server_client = _test_utils.create_mock_calling_server_client(
            status_code=404,
            payload=_test_constants.ErrorPayload,
            use_managed_identity = use_managed_identity
            )

        raised = False
        try:
            calling_server_client.create_call_connection(source_user, target_users, options)
        except:
            raised = True
        assert raised == True

    @parameterized.expand(data_source_test_join_call())
    def test_join_call_succeed(
        self,
        test_name, # type: str
        servercall_id, # type: str
        source_user, # type: CommunicationIdentifier
        options, # type: JoinCallOptions,
        use_managed_identity = False # type: bool
        ):

        calling_server_client = _test_utils.create_mock_calling_server_client(
            status_code=202,
            payload=_test_constants.CreateOrJoinCallPayload,
            use_managed_identity = use_managed_identity
            )

        call_connection = calling_server_client.join_call(
            servercall_id,
            source_user,
            options
            )

        assert call_connection.call_connection_id == _test_constants.CALL_ID

    @parameterized.expand(data_source_test_join_call())
    def test_join_call_failed(
        self,
        test_name, # type: str
        servercall_id, # type: str
        source_user, # type: CommunicationIdentifier
        options, # type: JoinCallOptions
        use_managed_identity = False # type: bool
        ):

        calling_server_client = _test_utils.create_mock_calling_server_client(
            status_code=404,
            payload=_test_constants.ErrorPayload,
            use_managed_identity = use_managed_identity
            )

        raised = False
        try:
            calling_server_client.join_call(
                servercall_id,
                source_user,
                options
                )
        except:
            raised = True
        assert raised == True