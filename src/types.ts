export interface SessionDescription {
  type: string;
  sdp: string;
}

export interface TrackObject {
  location: 'local' | 'remote';
  mid?: string;
  sessionId?: string;
  trackName: string;
}

export interface CallsApiResponse {
  sessionId?: string;
  sessionDescription: SessionDescription;
  tracks?: TrackObject[];
  errorCode?: string;
  errorDescription?: string;
  requiresImmediateRenegotiation?: boolean;
}

