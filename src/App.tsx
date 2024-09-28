// src/App.tsx

import React, { useEffect, useState } from "react";
import { useCallsContext } from "./context/CallsContext";
import {
  createNewSession,
  createNewTracks,
  sendAnswerSDP,
} from "./services/callsApi";
import VideoPlayer from "./components/VideoPlayer";
import { TrackObject } from "./types";

const App: React.FC = () => {
  const {
    localStream,
    remoteStream,
    setLocalStream,
    setRemoteStream,
    sessionId,
    setSessionId,
  } = useCallsContext();
  const [peerConnection, setPeerConnection] =
    useState<RTCPeerConnection | null>(null);

  useEffect(() => {
    // Initialize Peer Connection and local stream
    const initializeConnection = async () => {
      const pc = new RTCPeerConnection({
        iceServers: [{ urls: "stun:stun.cloudflare.com:3478" }],
      });
      setPeerConnection(pc);

      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });
      setLocalStream(stream);

      stream.getTracks().forEach((track) => {
        pc.addTrack(track, stream);
      });

      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);

      const newSession = await createNewSession(offer.sdp!);
      setSessionId(newSession.sessionId!);

      await pc.setRemoteDescription(
        new RTCSessionDescription({
          ...newSession.sessionDescription,
          type: newSession.sessionDescription.type as RTCSdpType, // Type assertion
        }),
      );

      pc.ontrack = (event) => {
        const remoteStream = new MediaStream();
        remoteStream.addTrack(event.track);
        setRemoteStream(remoteStream);
      };
    };

    initializeConnection();

    return () => {
      // Cleanup
      peerConnection?.close();
    };
  }, [setLocalStream, setRemoteStream, setSessionId]);

  useEffect(() => {
    if (peerConnection && sessionId) {
      // Manage additional tracks
      const handleNewTracks = async () => {
        const tracks: TrackObject[] =
          localStream?.getTracks().map((track) => ({
            location: "local",
            trackName: track.id,
          })) || [];

        const newTracks = await createNewTracks(tracks);
        if (newTracks.requiresImmediateRenegotiation) {
          await peerConnection.setRemoteDescription(
            new RTCSessionDescription({
              ...newTracks.sessionDescription,
              type: newTracks.sessionDescription.type as RTCSdpType, // Type assertion
            }),
          );

          const answer = await peerConnection.createAnswer();
          await peerConnection.setLocalDescription(answer);
          await sendAnswerSDP(answer.sdp!);
        }
      };

      handleNewTracks();
    }
  }, [peerConnection, sessionId, localStream]);

  return (
    <div className="grid">
      <h1>Calls Echo Demo</h1>
      <div>
        <h2>Local stream</h2>
        <VideoPlayer stream={localStream} muted />
      </div>
      <div>
        <h2>Remote echo stream</h2>
        <VideoPlayer stream={remoteStream} />
      </div>
    </div>
  );
};

export default App;
