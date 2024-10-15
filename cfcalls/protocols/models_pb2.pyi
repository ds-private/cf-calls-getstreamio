from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PEER_TYPE_PUBLISHER_UNSPECIFIED: _ClassVar[PeerType]
    PEER_TYPE_SUBSCRIBER: _ClassVar[PeerType]

class ConnectionQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_QUALITY_UNSPECIFIED: _ClassVar[ConnectionQuality]
    CONNECTION_QUALITY_POOR: _ClassVar[ConnectionQuality]
    CONNECTION_QUALITY_GOOD: _ClassVar[ConnectionQuality]
    CONNECTION_QUALITY_EXCELLENT: _ClassVar[ConnectionQuality]

class VideoQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_QUALITY_LOW_UNSPECIFIED: _ClassVar[VideoQuality]
    VIDEO_QUALITY_MID: _ClassVar[VideoQuality]
    VIDEO_QUALITY_HIGH: _ClassVar[VideoQuality]
    VIDEO_QUALITY_OFF: _ClassVar[VideoQuality]

class TrackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACK_TYPE_UNSPECIFIED: _ClassVar[TrackType]
    TRACK_TYPE_AUDIO: _ClassVar[TrackType]
    TRACK_TYPE_VIDEO: _ClassVar[TrackType]
    TRACK_TYPE_SCREEN_SHARE: _ClassVar[TrackType]
    TRACK_TYPE_SCREEN_SHARE_AUDIO: _ClassVar[TrackType]

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CODE_UNSPECIFIED: _ClassVar[ErrorCode]
    ERROR_CODE_PUBLISH_TRACK_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_PUBLISH_TRACKS_MISMATCH: _ClassVar[ErrorCode]
    ERROR_CODE_PUBLISH_TRACK_OUT_OF_ORDER: _ClassVar[ErrorCode]
    ERROR_CODE_PUBLISH_TRACK_VIDEO_LAYER_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_LIVE_ENDED: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_MIGRATING_OUT: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_MIGRATION_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_MIGRATING: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_RECONNECT_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_PARTICIPANT_MEDIA_TRANSPORT_FAILURE: _ClassVar[ErrorCode]
    ERROR_CODE_CALL_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_REQUEST_VALIDATION_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_UNAUTHENTICATED: _ClassVar[ErrorCode]
    ERROR_CODE_PERMISSION_DENIED: _ClassVar[ErrorCode]
    ERROR_CODE_TOO_MANY_REQUESTS: _ClassVar[ErrorCode]
    ERROR_CODE_INTERNAL_SERVER_ERROR: _ClassVar[ErrorCode]
    ERROR_CODE_SFU_SHUTTING_DOWN: _ClassVar[ErrorCode]
    ERROR_CODE_SFU_FULL: _ClassVar[ErrorCode]

class SdkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SDK_TYPE_UNSPECIFIED: _ClassVar[SdkType]
    SDK_TYPE_REACT: _ClassVar[SdkType]
    SDK_TYPE_ANGULAR: _ClassVar[SdkType]
    SDK_TYPE_ANDROID: _ClassVar[SdkType]
    SDK_TYPE_IOS: _ClassVar[SdkType]
    SDK_TYPE_FLUTTER: _ClassVar[SdkType]
    SDK_TYPE_REACT_NATIVE: _ClassVar[SdkType]
    SDK_TYPE_UNITY: _ClassVar[SdkType]
    SDK_TYPE_GO: _ClassVar[SdkType]
    SDK_TYPE_PLAIN_JAVASCRIPT: _ClassVar[SdkType]

class TrackUnpublishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACK_UNPUBLISH_REASON_UNSPECIFIED: _ClassVar[TrackUnpublishReason]
    TRACK_UNPUBLISH_REASON_USER_MUTED: _ClassVar[TrackUnpublishReason]
    TRACK_UNPUBLISH_REASON_PERMISSION_REVOKED: _ClassVar[TrackUnpublishReason]
    TRACK_UNPUBLISH_REASON_MODERATION: _ClassVar[TrackUnpublishReason]

class GoAwayReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GO_AWAY_REASON_UNSPECIFIED: _ClassVar[GoAwayReason]
    GO_AWAY_REASON_SHUTTING_DOWN: _ClassVar[GoAwayReason]
    GO_AWAY_REASON_REBALANCE: _ClassVar[GoAwayReason]

class CallEndedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALL_ENDED_REASON_UNSPECIFIED: _ClassVar[CallEndedReason]
    CALL_ENDED_REASON_ENDED: _ClassVar[CallEndedReason]
    CALL_ENDED_REASON_LIVE_ENDED: _ClassVar[CallEndedReason]
    CALL_ENDED_REASON_KICKED: _ClassVar[CallEndedReason]
    CALL_ENDED_REASON_SESSION_ENDED: _ClassVar[CallEndedReason]

class WebsocketReconnectStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEBSOCKET_RECONNECT_STRATEGY_UNSPECIFIED: _ClassVar[WebsocketReconnectStrategy]
    WEBSOCKET_RECONNECT_STRATEGY_DISCONNECT: _ClassVar[WebsocketReconnectStrategy]
    WEBSOCKET_RECONNECT_STRATEGY_FAST: _ClassVar[WebsocketReconnectStrategy]
    WEBSOCKET_RECONNECT_STRATEGY_REJOIN: _ClassVar[WebsocketReconnectStrategy]
    WEBSOCKET_RECONNECT_STRATEGY_MIGRATE: _ClassVar[WebsocketReconnectStrategy]

class AndroidThermalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANDROID_THERMAL_STATE_UNSPECIFIED: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_NONE: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_LIGHT: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_MODERATE: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_SEVERE: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_CRITICAL: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_EMERGENCY: _ClassVar[AndroidThermalState]
    ANDROID_THERMAL_STATE_SHUTDOWN: _ClassVar[AndroidThermalState]

class AppleThermalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPLE_THERMAL_STATE_UNSPECIFIED: _ClassVar[AppleThermalState]
    APPLE_THERMAL_STATE_NOMINAL: _ClassVar[AppleThermalState]
    APPLE_THERMAL_STATE_FAIR: _ClassVar[AppleThermalState]
    APPLE_THERMAL_STATE_SERIOUS: _ClassVar[AppleThermalState]
    APPLE_THERMAL_STATE_CRITICAL: _ClassVar[AppleThermalState]
PEER_TYPE_PUBLISHER_UNSPECIFIED: PeerType
PEER_TYPE_SUBSCRIBER: PeerType
CONNECTION_QUALITY_UNSPECIFIED: ConnectionQuality
CONNECTION_QUALITY_POOR: ConnectionQuality
CONNECTION_QUALITY_GOOD: ConnectionQuality
CONNECTION_QUALITY_EXCELLENT: ConnectionQuality
VIDEO_QUALITY_LOW_UNSPECIFIED: VideoQuality
VIDEO_QUALITY_MID: VideoQuality
VIDEO_QUALITY_HIGH: VideoQuality
VIDEO_QUALITY_OFF: VideoQuality
TRACK_TYPE_UNSPECIFIED: TrackType
TRACK_TYPE_AUDIO: TrackType
TRACK_TYPE_VIDEO: TrackType
TRACK_TYPE_SCREEN_SHARE: TrackType
TRACK_TYPE_SCREEN_SHARE_AUDIO: TrackType
ERROR_CODE_UNSPECIFIED: ErrorCode
ERROR_CODE_PUBLISH_TRACK_NOT_FOUND: ErrorCode
ERROR_CODE_PUBLISH_TRACKS_MISMATCH: ErrorCode
ERROR_CODE_PUBLISH_TRACK_OUT_OF_ORDER: ErrorCode
ERROR_CODE_PUBLISH_TRACK_VIDEO_LAYER_NOT_FOUND: ErrorCode
ERROR_CODE_LIVE_ENDED: ErrorCode
ERROR_CODE_PARTICIPANT_NOT_FOUND: ErrorCode
ERROR_CODE_PARTICIPANT_MIGRATING_OUT: ErrorCode
ERROR_CODE_PARTICIPANT_MIGRATION_FAILED: ErrorCode
ERROR_CODE_PARTICIPANT_MIGRATING: ErrorCode
ERROR_CODE_PARTICIPANT_RECONNECT_FAILED: ErrorCode
ERROR_CODE_PARTICIPANT_MEDIA_TRANSPORT_FAILURE: ErrorCode
ERROR_CODE_CALL_NOT_FOUND: ErrorCode
ERROR_CODE_REQUEST_VALIDATION_FAILED: ErrorCode
ERROR_CODE_UNAUTHENTICATED: ErrorCode
ERROR_CODE_PERMISSION_DENIED: ErrorCode
ERROR_CODE_TOO_MANY_REQUESTS: ErrorCode
ERROR_CODE_INTERNAL_SERVER_ERROR: ErrorCode
ERROR_CODE_SFU_SHUTTING_DOWN: ErrorCode
ERROR_CODE_SFU_FULL: ErrorCode
SDK_TYPE_UNSPECIFIED: SdkType
SDK_TYPE_REACT: SdkType
SDK_TYPE_ANGULAR: SdkType
SDK_TYPE_ANDROID: SdkType
SDK_TYPE_IOS: SdkType
SDK_TYPE_FLUTTER: SdkType
SDK_TYPE_REACT_NATIVE: SdkType
SDK_TYPE_UNITY: SdkType
SDK_TYPE_GO: SdkType
SDK_TYPE_PLAIN_JAVASCRIPT: SdkType
TRACK_UNPUBLISH_REASON_UNSPECIFIED: TrackUnpublishReason
TRACK_UNPUBLISH_REASON_USER_MUTED: TrackUnpublishReason
TRACK_UNPUBLISH_REASON_PERMISSION_REVOKED: TrackUnpublishReason
TRACK_UNPUBLISH_REASON_MODERATION: TrackUnpublishReason
GO_AWAY_REASON_UNSPECIFIED: GoAwayReason
GO_AWAY_REASON_SHUTTING_DOWN: GoAwayReason
GO_AWAY_REASON_REBALANCE: GoAwayReason
CALL_ENDED_REASON_UNSPECIFIED: CallEndedReason
CALL_ENDED_REASON_ENDED: CallEndedReason
CALL_ENDED_REASON_LIVE_ENDED: CallEndedReason
CALL_ENDED_REASON_KICKED: CallEndedReason
CALL_ENDED_REASON_SESSION_ENDED: CallEndedReason
WEBSOCKET_RECONNECT_STRATEGY_UNSPECIFIED: WebsocketReconnectStrategy
WEBSOCKET_RECONNECT_STRATEGY_DISCONNECT: WebsocketReconnectStrategy
WEBSOCKET_RECONNECT_STRATEGY_FAST: WebsocketReconnectStrategy
WEBSOCKET_RECONNECT_STRATEGY_REJOIN: WebsocketReconnectStrategy
WEBSOCKET_RECONNECT_STRATEGY_MIGRATE: WebsocketReconnectStrategy
ANDROID_THERMAL_STATE_UNSPECIFIED: AndroidThermalState
ANDROID_THERMAL_STATE_NONE: AndroidThermalState
ANDROID_THERMAL_STATE_LIGHT: AndroidThermalState
ANDROID_THERMAL_STATE_MODERATE: AndroidThermalState
ANDROID_THERMAL_STATE_SEVERE: AndroidThermalState
ANDROID_THERMAL_STATE_CRITICAL: AndroidThermalState
ANDROID_THERMAL_STATE_EMERGENCY: AndroidThermalState
ANDROID_THERMAL_STATE_SHUTDOWN: AndroidThermalState
APPLE_THERMAL_STATE_UNSPECIFIED: AppleThermalState
APPLE_THERMAL_STATE_NOMINAL: AppleThermalState
APPLE_THERMAL_STATE_FAIR: AppleThermalState
APPLE_THERMAL_STATE_SERIOUS: AppleThermalState
APPLE_THERMAL_STATE_CRITICAL: AppleThermalState

class CallState(_message.Message):
    __slots__ = ("participants", "started_at", "participant_count", "pins")
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINS_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[Participant]
    started_at: _timestamp_pb2.Timestamp
    participant_count: ParticipantCount
    pins: _containers.RepeatedCompositeFieldContainer[Pin]
    def __init__(self, participants: _Optional[_Iterable[_Union[Participant, _Mapping]]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., participant_count: _Optional[_Union[ParticipantCount, _Mapping]] = ..., pins: _Optional[_Iterable[_Union[Pin, _Mapping]]] = ...) -> None: ...

class ParticipantCount(_message.Message):
    __slots__ = ("total", "anonymous")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    total: int
    anonymous: int
    def __init__(self, total: _Optional[int] = ..., anonymous: _Optional[int] = ...) -> None: ...

class Pin(_message.Message):
    __slots__ = ("user_id", "session_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class Participant(_message.Message):
    __slots__ = ("user_id", "session_id", "published_tracks", "joined_at", "track_lookup_prefix", "connection_quality", "is_speaking", "is_dominant_speaker", "audio_level", "name", "image", "custom", "roles")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_TRACKS_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    TRACK_LOOKUP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_QUALITY_FIELD_NUMBER: _ClassVar[int]
    IS_SPEAKING_FIELD_NUMBER: _ClassVar[int]
    IS_DOMINANT_SPEAKER_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    published_tracks: _containers.RepeatedScalarFieldContainer[TrackType]
    joined_at: _timestamp_pb2.Timestamp
    track_lookup_prefix: str
    connection_quality: ConnectionQuality
    is_speaking: bool
    is_dominant_speaker: bool
    audio_level: float
    name: str
    image: str
    custom: _struct_pb2.Struct
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., published_tracks: _Optional[_Iterable[_Union[TrackType, str]]] = ..., joined_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., track_lookup_prefix: _Optional[str] = ..., connection_quality: _Optional[_Union[ConnectionQuality, str]] = ..., is_speaking: bool = ..., is_dominant_speaker: bool = ..., audio_level: _Optional[float] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., custom: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class StreamQuality(_message.Message):
    __slots__ = ("video_quality", "user_id")
    VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    video_quality: VideoQuality
    user_id: str
    def __init__(self, video_quality: _Optional[_Union[VideoQuality, str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class VideoDimension(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class VideoLayer(_message.Message):
    __slots__ = ("rid", "video_dimension", "bitrate", "fps", "quality")
    RID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    rid: str
    video_dimension: VideoDimension
    bitrate: int
    fps: int
    quality: VideoQuality
    def __init__(self, rid: _Optional[str] = ..., video_dimension: _Optional[_Union[VideoDimension, _Mapping]] = ..., bitrate: _Optional[int] = ..., fps: _Optional[int] = ..., quality: _Optional[_Union[VideoQuality, str]] = ...) -> None: ...

class Codec(_message.Message):
    __slots__ = ("payload_type", "name", "fmtp_line", "clock_rate", "encoding_parameters", "feedbacks")
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FMTP_LINE_FIELD_NUMBER: _ClassVar[int]
    CLOCK_RATE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FEEDBACKS_FIELD_NUMBER: _ClassVar[int]
    payload_type: int
    name: str
    fmtp_line: str
    clock_rate: int
    encoding_parameters: str
    feedbacks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, payload_type: _Optional[int] = ..., name: _Optional[str] = ..., fmtp_line: _Optional[str] = ..., clock_rate: _Optional[int] = ..., encoding_parameters: _Optional[str] = ..., feedbacks: _Optional[_Iterable[str]] = ...) -> None: ...

class ICETrickle(_message.Message):
    __slots__ = ("peer_type", "ice_candidate", "session_id")
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    peer_type: PeerType
    ice_candidate: str
    session_id: str
    def __init__(self, peer_type: _Optional[_Union[PeerType, str]] = ..., ice_candidate: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class TrackInfo(_message.Message):
    __slots__ = ("track_id", "track_type", "layers", "mid", "dtx", "stereo", "red", "muted")
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    DTX_FIELD_NUMBER: _ClassVar[int]
    STEREO_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    track_id: str
    track_type: TrackType
    layers: _containers.RepeatedCompositeFieldContainer[VideoLayer]
    mid: str
    dtx: bool
    stereo: bool
    red: bool
    muted: bool
    def __init__(self, track_id: _Optional[str] = ..., track_type: _Optional[_Union[TrackType, str]] = ..., layers: _Optional[_Iterable[_Union[VideoLayer, _Mapping]]] = ..., mid: _Optional[str] = ..., dtx: bool = ..., stereo: bool = ..., red: bool = ..., muted: bool = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message", "should_retry")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETRY_FIELD_NUMBER: _ClassVar[int]
    code: ErrorCode
    message: str
    should_retry: bool
    def __init__(self, code: _Optional[_Union[ErrorCode, str]] = ..., message: _Optional[str] = ..., should_retry: bool = ...) -> None: ...

class ClientDetails(_message.Message):
    __slots__ = ("sdk", "os", "browser", "device")
    SDK_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    BROWSER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    sdk: Sdk
    os: OS
    browser: Browser
    device: Device
    def __init__(self, sdk: _Optional[_Union[Sdk, _Mapping]] = ..., os: _Optional[_Union[OS, _Mapping]] = ..., browser: _Optional[_Union[Browser, _Mapping]] = ..., device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class Sdk(_message.Message):
    __slots__ = ("type", "major", "minor", "patch")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    type: SdkType
    major: str
    minor: str
    patch: str
    def __init__(self, type: _Optional[_Union[SdkType, str]] = ..., major: _Optional[str] = ..., minor: _Optional[str] = ..., patch: _Optional[str] = ...) -> None: ...

class OS(_message.Message):
    __slots__ = ("name", "version", "architecture")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    architecture: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., architecture: _Optional[str] = ...) -> None: ...

class Browser(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class Call(_message.Message):
    __slots__ = ("type", "id", "created_by_user_id", "host_user_id", "custom", "created_at", "updated_at")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    created_by_user_id: str
    host_user_id: str
    custom: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., host_user_id: _Optional[str] = ..., custom: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CallGrants(_message.Message):
    __slots__ = ("can_publish_audio", "can_publish_video", "can_screenshare")
    CAN_PUBLISH_AUDIO_FIELD_NUMBER: _ClassVar[int]
    CAN_PUBLISH_VIDEO_FIELD_NUMBER: _ClassVar[int]
    CAN_SCREENSHARE_FIELD_NUMBER: _ClassVar[int]
    can_publish_audio: bool
    can_publish_video: bool
    can_screenshare: bool
    def __init__(self, can_publish_audio: bool = ..., can_publish_video: bool = ..., can_screenshare: bool = ...) -> None: ...

class InputDevices(_message.Message):
    __slots__ = ("available_devices", "current_device", "is_permitted")
    AVAILABLE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    IS_PERMITTED_FIELD_NUMBER: _ClassVar[int]
    available_devices: _containers.RepeatedScalarFieldContainer[str]
    current_device: str
    is_permitted: bool
    def __init__(self, available_devices: _Optional[_Iterable[str]] = ..., current_device: _Optional[str] = ..., is_permitted: bool = ...) -> None: ...

class AndroidState(_message.Message):
    __slots__ = ("thermal_state", "is_power_saver_mode")
    THERMAL_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_POWER_SAVER_MODE_FIELD_NUMBER: _ClassVar[int]
    thermal_state: AndroidThermalState
    is_power_saver_mode: bool
    def __init__(self, thermal_state: _Optional[_Union[AndroidThermalState, str]] = ..., is_power_saver_mode: bool = ...) -> None: ...

class AppleState(_message.Message):
    __slots__ = ("thermal_state", "is_low_power_mode_enabled")
    THERMAL_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_POWER_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    thermal_state: AppleThermalState
    is_low_power_mode_enabled: bool
    def __init__(self, thermal_state: _Optional[_Union[AppleThermalState, str]] = ..., is_low_power_mode_enabled: bool = ...) -> None: ...
