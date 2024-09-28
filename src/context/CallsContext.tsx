import React, { createContext, useState, useContext, ReactNode } from 'react';
import { CallsApiResponse, SessionDescription, TrackObject } from '../types';

interface CallsContextProps {
  sessionId: string | null;
  localStream: MediaStream | null;
  remoteStream: MediaStream | null;
  createSession: (offerSDP: string) => Promise<CallsApiResponse>;
  createTracks: (trackObjects: TrackObject[], offerSDP?: string) => Promise<CallsApiResponse>;
  setSessionId: React.Dispatch<React.SetStateAction<string | null>>;
  setLocalStream: React.Dispatch<React.SetStateAction<MediaStream | null>>;
  setRemoteStream: React.Dispatch<React.SetStateAction<MediaStream | null>>;
}

const CallsContext = createContext<CallsContextProps | undefined>(undefined);

export const CallsProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [localStream, setLocalStream] = useState<MediaStream | null>(null);
  const [remoteStream, setRemoteStream] = useState<MediaStream | null>(null);

  // Add the necessary functions here for interacting with the API
  const createSession = async (offerSDP: string) => {
    // Function to create session
  };

  const createTracks = async (trackObjects: TrackObject[], offerSDP?: string) => {
    // Function to create tracks
  };

  return (
    <CallsContext.Provider
      value={{
        sessionId,
        localStream,
        remoteStream,
        createSession,
        createTracks,
        setSessionId,
        setLocalStream,
        setRemoteStream,
      }}
    >
      {children}
    </CallsContext.Provider>
  );
};

export const useCallsContext = () => {
  const context = useContext(CallsContext);
  if (!context) {
    throw new Error('useCallsContext must be used within a CallsProvider');
  }
  return context;
};
