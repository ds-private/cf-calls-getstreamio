from cfcalls.protocols import models_pb2 as _models_pb2
from cfcalls.protocols import signal_pb2 as _signal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SfuEvent(_message.Message):
    __slots__ = ("subscriber_offer", "publisher_answer", "connection_quality_changed", "audio_level_changed", "ice_trickle", "change_publish_quality", "participant_joined", "participant_left", "dominant_speaker_changed", "join_response", "health_check_response", "track_published", "track_unpublished", "error", "call_grants_updated", "go_away", "ice_restart", "pins_updated", "call_ended", "participant_updated", "participant_migration_complete")
    SUBSCRIBER_OFFER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_ANSWER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_QUALITY_CHANGED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LEVEL_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ICE_TRICKLE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PUBLISH_QUALITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_JOINED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_LEFT_FIELD_NUMBER: _ClassVar[int]
    DOMINANT_SPEAKER_CHANGED_FIELD_NUMBER: _ClassVar[int]
    JOIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRACK_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    TRACK_UNPUBLISHED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CALL_GRANTS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    GO_AWAY_FIELD_NUMBER: _ClassVar[int]
    ICE_RESTART_FIELD_NUMBER: _ClassVar[int]
    PINS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CALL_ENDED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_MIGRATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    subscriber_offer: SubscriberOffer
    publisher_answer: PublisherAnswer
    connection_quality_changed: ConnectionQualityChanged
    audio_level_changed: AudioLevelChanged
    ice_trickle: _models_pb2.ICETrickle
    change_publish_quality: ChangePublishQuality
    participant_joined: ParticipantJoined
    participant_left: ParticipantLeft
    dominant_speaker_changed: DominantSpeakerChanged
    join_response: JoinResponse
    health_check_response: HealthCheckResponse
    track_published: TrackPublished
    track_unpublished: TrackUnpublished
    error: Error
    call_grants_updated: CallGrantsUpdated
    go_away: GoAway
    ice_restart: ICERestart
    pins_updated: PinsChanged
    call_ended: CallEnded
    participant_updated: ParticipantUpdated
    participant_migration_complete: ParticipantMigrationComplete
    def __init__(self, subscriber_offer: _Optional[_Union[SubscriberOffer, _Mapping]] = ..., publisher_answer: _Optional[_Union[PublisherAnswer, _Mapping]] = ..., connection_quality_changed: _Optional[_Union[ConnectionQualityChanged, _Mapping]] = ..., audio_level_changed: _Optional[_Union[AudioLevelChanged, _Mapping]] = ..., ice_trickle: _Optional[_Union[_models_pb2.ICETrickle, _Mapping]] = ..., change_publish_quality: _Optional[_Union[ChangePublishQuality, _Mapping]] = ..., participant_joined: _Optional[_Union[ParticipantJoined, _Mapping]] = ..., participant_left: _Optional[_Union[ParticipantLeft, _Mapping]] = ..., dominant_speaker_changed: _Optional[_Union[DominantSpeakerChanged, _Mapping]] = ..., join_response: _Optional[_Union[JoinResponse, _Mapping]] = ..., health_check_response: _Optional[_Union[HealthCheckResponse, _Mapping]] = ..., track_published: _Optional[_Union[TrackPublished, _Mapping]] = ..., track_unpublished: _Optional[_Union[TrackUnpublished, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., call_grants_updated: _Optional[_Union[CallGrantsUpdated, _Mapping]] = ..., go_away: _Optional[_Union[GoAway, _Mapping]] = ..., ice_restart: _Optional[_Union[ICERestart, _Mapping]] = ..., pins_updated: _Optional[_Union[PinsChanged, _Mapping]] = ..., call_ended: _Optional[_Union[CallEnded, _Mapping]] = ..., participant_updated: _Optional[_Union[ParticipantUpdated, _Mapping]] = ..., participant_migration_complete: _Optional[_Union[ParticipantMigrationComplete, _Mapping]] = ...) -> None: ...

class ParticipantMigrationComplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PinsChanged(_message.Message):
    __slots__ = ("pins",)
    PINS_FIELD_NUMBER: _ClassVar[int]
    pins: _containers.RepeatedCompositeFieldContainer[_models_pb2.Pin]
    def __init__(self, pins: _Optional[_Iterable[_Union[_models_pb2.Pin, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("error", "reconnect_strategy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    reconnect_strategy: _models_pb2.WebsocketReconnectStrategy
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ..., reconnect_strategy: _Optional[_Union[_models_pb2.WebsocketReconnectStrategy, str]] = ...) -> None: ...

class ICETrickle(_message.Message):
    __slots__ = ("peer_type", "ice_candidate")
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    peer_type: _models_pb2.PeerType
    ice_candidate: str
    def __init__(self, peer_type: _Optional[_Union[_models_pb2.PeerType, str]] = ..., ice_candidate: _Optional[str] = ...) -> None: ...

class ICERestart(_message.Message):
    __slots__ = ("peer_type",)
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    peer_type: _models_pb2.PeerType
    def __init__(self, peer_type: _Optional[_Union[_models_pb2.PeerType, str]] = ...) -> None: ...

class SfuRequest(_message.Message):
    __slots__ = ("join_request", "health_check_request", "leave_call_request")
    JOIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LEAVE_CALL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    join_request: JoinRequest
    health_check_request: HealthCheckRequest
    leave_call_request: LeaveCallRequest
    def __init__(self, join_request: _Optional[_Union[JoinRequest, _Mapping]] = ..., health_check_request: _Optional[_Union[HealthCheckRequest, _Mapping]] = ..., leave_call_request: _Optional[_Union[LeaveCallRequest, _Mapping]] = ...) -> None: ...

class LeaveCallRequest(_message.Message):
    __slots__ = ("session_id", "reason")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    reason: str
    def __init__(self, session_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class HealthCheckRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthCheckResponse(_message.Message):
    __slots__ = ("participant_count",)
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    participant_count: _models_pb2.ParticipantCount
    def __init__(self, participant_count: _Optional[_Union[_models_pb2.ParticipantCount, _Mapping]] = ...) -> None: ...

class TrackPublished(_message.Message):
    __slots__ = ("user_id", "session_id", "type", "participant")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    type: _models_pb2.TrackType
    participant: _models_pb2.Participant
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_models_pb2.TrackType, str]] = ..., participant: _Optional[_Union[_models_pb2.Participant, _Mapping]] = ...) -> None: ...

class TrackUnpublished(_message.Message):
    __slots__ = ("user_id", "session_id", "type", "cause", "participant")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    type: _models_pb2.TrackType
    cause: _models_pb2.TrackUnpublishReason
    participant: _models_pb2.Participant
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[_models_pb2.TrackType, str]] = ..., cause: _Optional[_Union[_models_pb2.TrackUnpublishReason, str]] = ..., participant: _Optional[_Union[_models_pb2.Participant, _Mapping]] = ...) -> None: ...

class JoinRequest(_message.Message):
    __slots__ = ("token", "session_id", "subscriber_sdp", "client_details", "migration", "fast_reconnect", "reconnect_details")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_SDP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FIELD_NUMBER: _ClassVar[int]
    FAST_RECONNECT_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    token: str
    session_id: str
    subscriber_sdp: str
    client_details: _models_pb2.ClientDetails
    migration: Migration
    fast_reconnect: bool
    reconnect_details: ReconnectDetails
    def __init__(self, token: _Optional[str] = ..., session_id: _Optional[str] = ..., subscriber_sdp: _Optional[str] = ..., client_details: _Optional[_Union[_models_pb2.ClientDetails, _Mapping]] = ..., migration: _Optional[_Union[Migration, _Mapping]] = ..., fast_reconnect: bool = ..., reconnect_details: _Optional[_Union[ReconnectDetails, _Mapping]] = ...) -> None: ...

class ReconnectDetails(_message.Message):
    __slots__ = ("strategy", "announced_tracks", "subscriptions", "reconnect_attempt", "from_sfu_id", "previous_session_id")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCED_TRACKS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    RECONNECT_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    FROM_SFU_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    strategy: _models_pb2.WebsocketReconnectStrategy
    announced_tracks: _containers.RepeatedCompositeFieldContainer[_models_pb2.TrackInfo]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_signal_pb2.TrackSubscriptionDetails]
    reconnect_attempt: int
    from_sfu_id: str
    previous_session_id: str
    def __init__(self, strategy: _Optional[_Union[_models_pb2.WebsocketReconnectStrategy, str]] = ..., announced_tracks: _Optional[_Iterable[_Union[_models_pb2.TrackInfo, _Mapping]]] = ..., subscriptions: _Optional[_Iterable[_Union[_signal_pb2.TrackSubscriptionDetails, _Mapping]]] = ..., reconnect_attempt: _Optional[int] = ..., from_sfu_id: _Optional[str] = ..., previous_session_id: _Optional[str] = ...) -> None: ...

class Migration(_message.Message):
    __slots__ = ("from_sfu_id", "announced_tracks", "subscriptions")
    FROM_SFU_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCED_TRACKS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    from_sfu_id: str
    announced_tracks: _containers.RepeatedCompositeFieldContainer[_models_pb2.TrackInfo]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_signal_pb2.TrackSubscriptionDetails]
    def __init__(self, from_sfu_id: _Optional[str] = ..., announced_tracks: _Optional[_Iterable[_Union[_models_pb2.TrackInfo, _Mapping]]] = ..., subscriptions: _Optional[_Iterable[_Union[_signal_pb2.TrackSubscriptionDetails, _Mapping]]] = ...) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = ("call_state", "reconnected", "fast_reconnect_deadline_seconds")
    CALL_STATE_FIELD_NUMBER: _ClassVar[int]
    RECONNECTED_FIELD_NUMBER: _ClassVar[int]
    FAST_RECONNECT_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    call_state: _models_pb2.CallState
    reconnected: bool
    fast_reconnect_deadline_seconds: int
    def __init__(self, call_state: _Optional[_Union[_models_pb2.CallState, _Mapping]] = ..., reconnected: bool = ..., fast_reconnect_deadline_seconds: _Optional[int] = ...) -> None: ...

class ParticipantJoined(_message.Message):
    __slots__ = ("call_cid", "participant")
    CALL_CID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    call_cid: str
    participant: _models_pb2.Participant
    def __init__(self, call_cid: _Optional[str] = ..., participant: _Optional[_Union[_models_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantLeft(_message.Message):
    __slots__ = ("call_cid", "participant")
    CALL_CID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    call_cid: str
    participant: _models_pb2.Participant
    def __init__(self, call_cid: _Optional[str] = ..., participant: _Optional[_Union[_models_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantUpdated(_message.Message):
    __slots__ = ("call_cid", "participant")
    CALL_CID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    call_cid: str
    participant: _models_pb2.Participant
    def __init__(self, call_cid: _Optional[str] = ..., participant: _Optional[_Union[_models_pb2.Participant, _Mapping]] = ...) -> None: ...

class SubscriberOffer(_message.Message):
    __slots__ = ("ice_restart", "sdp")
    ICE_RESTART_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    ice_restart: bool
    sdp: str
    def __init__(self, ice_restart: bool = ..., sdp: _Optional[str] = ...) -> None: ...

class PublisherAnswer(_message.Message):
    __slots__ = ("sdp",)
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    def __init__(self, sdp: _Optional[str] = ...) -> None: ...

class ConnectionQualityChanged(_message.Message):
    __slots__ = ("connection_quality_updates",)
    CONNECTION_QUALITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
    connection_quality_updates: _containers.RepeatedCompositeFieldContainer[ConnectionQualityInfo]
    def __init__(self, connection_quality_updates: _Optional[_Iterable[_Union[ConnectionQualityInfo, _Mapping]]] = ...) -> None: ...

class ConnectionQualityInfo(_message.Message):
    __slots__ = ("user_id", "session_id", "connection_quality")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_QUALITY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    connection_quality: _models_pb2.ConnectionQuality
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., connection_quality: _Optional[_Union[_models_pb2.ConnectionQuality, str]] = ...) -> None: ...

class DominantSpeakerChanged(_message.Message):
    __slots__ = ("user_id", "session_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class AudioLevel(_message.Message):
    __slots__ = ("user_id", "session_id", "level", "is_speaking")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_SPEAKING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    level: float
    is_speaking: bool
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., level: _Optional[float] = ..., is_speaking: bool = ...) -> None: ...

class AudioLevelChanged(_message.Message):
    __slots__ = ("audio_levels",)
    AUDIO_LEVELS_FIELD_NUMBER: _ClassVar[int]
    audio_levels: _containers.RepeatedCompositeFieldContainer[AudioLevel]
    def __init__(self, audio_levels: _Optional[_Iterable[_Union[AudioLevel, _Mapping]]] = ...) -> None: ...

class AudioSender(_message.Message):
    __slots__ = ("codec",)
    CODEC_FIELD_NUMBER: _ClassVar[int]
    codec: _models_pb2.Codec
    def __init__(self, codec: _Optional[_Union[_models_pb2.Codec, _Mapping]] = ...) -> None: ...

class VideoLayerSetting(_message.Message):
    __slots__ = ("name", "active", "max_bitrate", "scale_resolution_down_by", "codec", "max_framerate", "scalability_mode")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MAX_BITRATE_FIELD_NUMBER: _ClassVar[int]
    SCALE_RESOLUTION_DOWN_BY_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    MAX_FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    SCALABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    active: bool
    max_bitrate: int
    scale_resolution_down_by: float
    codec: _models_pb2.Codec
    max_framerate: int
    scalability_mode: str
    def __init__(self, name: _Optional[str] = ..., active: bool = ..., max_bitrate: _Optional[int] = ..., scale_resolution_down_by: _Optional[float] = ..., codec: _Optional[_Union[_models_pb2.Codec, _Mapping]] = ..., max_framerate: _Optional[int] = ..., scalability_mode: _Optional[str] = ...) -> None: ...

class VideoSender(_message.Message):
    __slots__ = ("codec", "layers")
    CODEC_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    codec: _models_pb2.Codec
    layers: _containers.RepeatedCompositeFieldContainer[VideoLayerSetting]
    def __init__(self, codec: _Optional[_Union[_models_pb2.Codec, _Mapping]] = ..., layers: _Optional[_Iterable[_Union[VideoLayerSetting, _Mapping]]] = ...) -> None: ...

class ChangePublishQuality(_message.Message):
    __slots__ = ("audio_senders", "video_senders")
    AUDIO_SENDERS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SENDERS_FIELD_NUMBER: _ClassVar[int]
    audio_senders: _containers.RepeatedCompositeFieldContainer[AudioSender]
    video_senders: _containers.RepeatedCompositeFieldContainer[VideoSender]
    def __init__(self, audio_senders: _Optional[_Iterable[_Union[AudioSender, _Mapping]]] = ..., video_senders: _Optional[_Iterable[_Union[VideoSender, _Mapping]]] = ...) -> None: ...

class CallGrantsUpdated(_message.Message):
    __slots__ = ("current_grants", "message")
    CURRENT_GRANTS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    current_grants: _models_pb2.CallGrants
    message: str
    def __init__(self, current_grants: _Optional[_Union[_models_pb2.CallGrants, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class GoAway(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _models_pb2.GoAwayReason
    def __init__(self, reason: _Optional[_Union[_models_pb2.GoAwayReason, str]] = ...) -> None: ...

class CallEnded(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _models_pb2.CallEndedReason
    def __init__(self, reason: _Optional[_Union[_models_pb2.CallEndedReason, str]] = ...) -> None: ...
