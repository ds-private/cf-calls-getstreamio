from cfcalls.protocols import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartNoiseCancellationRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class StartNoiseCancellationResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class StopNoiseCancellationRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class StopNoiseCancellationResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class SendStatsRequest(_message.Message):
    __slots__ = ("session_id", "subscriber_stats", "publisher_stats", "webrtc_version", "sdk", "sdk_version", "audio_devices", "video_devices", "android", "apple")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_STATS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_STATS_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_VERSION_FIELD_NUMBER: _ClassVar[int]
    SDK_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DEVICES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DEVICES_FIELD_NUMBER: _ClassVar[int]
    ANDROID_FIELD_NUMBER: _ClassVar[int]
    APPLE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    subscriber_stats: str
    publisher_stats: str
    webrtc_version: str
    sdk: str
    sdk_version: str
    audio_devices: _models_pb2.InputDevices
    video_devices: _models_pb2.InputDevices
    android: _models_pb2.AndroidState
    apple: _models_pb2.AppleState
    def __init__(self, session_id: _Optional[str] = ..., subscriber_stats: _Optional[str] = ..., publisher_stats: _Optional[str] = ..., webrtc_version: _Optional[str] = ..., sdk: _Optional[str] = ..., sdk_version: _Optional[str] = ..., audio_devices: _Optional[_Union[_models_pb2.InputDevices, _Mapping]] = ..., video_devices: _Optional[_Union[_models_pb2.InputDevices, _Mapping]] = ..., android: _Optional[_Union[_models_pb2.AndroidState, _Mapping]] = ..., apple: _Optional[_Union[_models_pb2.AppleState, _Mapping]] = ...) -> None: ...

class SendStatsResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class ICERestartRequest(_message.Message):
    __slots__ = ("session_id", "peer_type")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    peer_type: _models_pb2.PeerType
    def __init__(self, session_id: _Optional[str] = ..., peer_type: _Optional[_Union[_models_pb2.PeerType, str]] = ...) -> None: ...

class ICERestartResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class UpdateMuteStatesRequest(_message.Message):
    __slots__ = ("session_id", "mute_states")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MUTE_STATES_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    mute_states: _containers.RepeatedCompositeFieldContainer[TrackMuteState]
    def __init__(self, session_id: _Optional[str] = ..., mute_states: _Optional[_Iterable[_Union[TrackMuteState, _Mapping]]] = ...) -> None: ...

class UpdateMuteStatesResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class TrackMuteState(_message.Message):
    __slots__ = ("track_type", "muted")
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    track_type: _models_pb2.TrackType
    muted: bool
    def __init__(self, track_type: _Optional[_Union[_models_pb2.TrackType, str]] = ..., muted: bool = ...) -> None: ...

class AudioMuteChanged(_message.Message):
    __slots__ = ("muted",)
    MUTED_FIELD_NUMBER: _ClassVar[int]
    muted: bool
    def __init__(self, muted: bool = ...) -> None: ...

class VideoMuteChanged(_message.Message):
    __slots__ = ("muted",)
    MUTED_FIELD_NUMBER: _ClassVar[int]
    muted: bool
    def __init__(self, muted: bool = ...) -> None: ...

class UpdateSubscriptionsRequest(_message.Message):
    __slots__ = ("session_id", "tracks")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    tracks: _containers.RepeatedCompositeFieldContainer[TrackSubscriptionDetails]
    def __init__(self, session_id: _Optional[str] = ..., tracks: _Optional[_Iterable[_Union[TrackSubscriptionDetails, _Mapping]]] = ...) -> None: ...

class UpdateSubscriptionsResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class TrackSubscriptionDetails(_message.Message):
    __slots__ = ("user_id", "session_id", "track_type", "dimension")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    track_type: _models_pb2.TrackType
    dimension: _models_pb2.VideoDimension
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., track_type: _Optional[_Union[_models_pb2.TrackType, str]] = ..., dimension: _Optional[_Union[_models_pb2.VideoDimension, _Mapping]] = ...) -> None: ...

class SendAnswerRequest(_message.Message):
    __slots__ = ("peer_type", "sdp", "session_id")
    PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    peer_type: _models_pb2.PeerType
    sdp: str
    session_id: str
    def __init__(self, peer_type: _Optional[_Union[_models_pb2.PeerType, str]] = ..., sdp: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class SendAnswerResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class ICETrickleResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _models_pb2.Error
    def __init__(self, error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...

class SetPublisherRequest(_message.Message):
    __slots__ = ("sdp", "session_id", "tracks")
    SDP_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    session_id: str
    tracks: _containers.RepeatedCompositeFieldContainer[_models_pb2.TrackInfo]
    def __init__(self, sdp: _Optional[str] = ..., session_id: _Optional[str] = ..., tracks: _Optional[_Iterable[_Union[_models_pb2.TrackInfo, _Mapping]]] = ...) -> None: ...

class SetPublisherResponse(_message.Message):
    __slots__ = ("sdp", "session_id", "ice_restart", "error")
    SDP_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ICE_RESTART_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    session_id: str
    ice_restart: bool
    error: _models_pb2.Error
    def __init__(self, sdp: _Optional[str] = ..., session_id: _Optional[str] = ..., ice_restart: bool = ..., error: _Optional[_Union[_models_pb2.Error, _Mapping]] = ...) -> None: ...
