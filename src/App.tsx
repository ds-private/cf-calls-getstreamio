import { StreamVideoClient, type User } from "@stream-io/video-client";
import type React from "react";
import { useEffect, useRef } from "react";
import CallsApp from "./CallsApp";

const App: React.FC = () => {
	const localVideoElement = useRef<HTMLVideoElement | null>(null);
	const remoteVideoElement = useRef<HTMLVideoElement | null>(null);
	async function stream_init() {
		const apiKey = "mmhfdzb5evj2";
		const token =
			"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3Byb250by5nZXRzdHJlYW0uaW8iLCJzdWIiOiJ1c2VyL0JvYmFfRmV0dCIsInVzZXJfaWQiOiJCb2JhX0ZldHQiLCJ2YWxpZGl0eV9pbl9zZWNvbmRzIjo2MDQ4MDAsImlhdCI6MTcyOTAyOTE2NSwiZXhwIjoxNzI5NjMzOTY1fQ.jrjg3gOOslK5s9HJ7yUd9bg9Ew5Tf7qQ0aFgeEfoaAc";
		const user: User = { id: "Boba_Fett" };

		const client = new StreamVideoClient({
			apiKey,
			token,
			user,
			options: { baseURL: "http://localhost:5000" },
		});

		const call = client.call("default", "lsAVy6CSeqdF");
		call.join({ create: true }).then(async () => {
			call.camera.enable();
			call.microphone.enable();
		});
	}
	async function raw_init() {
		// Use Cloudflare's STUN server
		const pc = new RTCPeerConnection({
			iceServers: [
				{
					urls: "stun:stun.cloudflare.com:3478",
				},
			],
			bundlePolicy: "max-bundle",
		});

		// In order to successfully establish a peer connection, we need at least one track to publish.
		// In this case, we create two: video & audio
		const localStream = await navigator.mediaDevices.getUserMedia({
			video: true,
			audio: true,
		});

		// Get the local video element in the HTML and set the source to show local stream
		// const localVideoElement = document.getElementById("local-video");
		// Ensure localVideoElement is not null or undefined before assigning
		if (localVideoElement?.current) {
			localVideoElement.current.srcObject = localStream;
		}

		// Add sendonly trancievers to the PeerConnection
		const transceivers = localStream.getTracks().map((track) =>
			pc.addTransceiver(track, {
				direction: "sendonly",
			}),
		);

		// Create a instance of CallsApp (defined below). Please note that this is not an official SDK but just a demo showing the HTML API.
		const app = new CallsApp();

		// Send the first offer and create a session. The returned sessionId is required to retrieve any track published by this peer
		await pc.setLocalDescription(await pc.createOffer());
		const newSessionResult = await app.newSession(
			pc.localDescription?.sdp || "PC SDP NOT SET 50",
		);
		await pc.setRemoteDescription(
			new RTCSessionDescription(newSessionResult.sessionDescription),
		);

		// Make the peer connection was established
		await new Promise<void>((resolve, reject) => {
			pc.addEventListener("iceconnectionstatechange", (ev) => {
				const target = ev.target as RTCPeerConnection; // Cast ev.target to RTCPeerConnection
				if (target.iceConnectionState === "connected") {
					resolve();
				}
				setTimeout(reject, 5000, "connect timeout");
			});
		});

		// We associate a trackName to a transceiver identified by a mid (media ID). This way the track
		// is remotely reachable by the tuple (sessionId, trackName)
		const trackObjects = transceivers.map((transceiver) => {
			return {
				location: "local",
				mid: transceiver.mid,
				trackName: transceiver?.sender?.track?.id,
			};
		});

		// Get local description, create a new track, set remote description with the response
		await pc.setLocalDescription(await pc.createOffer());
		const newLocalTracksResult = await app.newTracks(
			trackObjects,
			pc?.localDescription?.sdp,
		);
		await pc.setRemoteDescription(
			new RTCSessionDescription(newLocalTracksResult.sessionDescription),
		);

		const remoteTrackObjects = trackObjects.map((trackObject) => {
			return {
				location: "remote",
				sessionId: app.sessionId,
				trackName: trackObject.trackName,
			};
		});

		// Prepare to receive the tracks before asking for them
		const remoteTracksPromise: Promise<MediaStreamTrack[]> = new Promise(
			(resolve) => {
				const tracks: MediaStreamTrack[] = [];
				pc.ontrack = (event) => {
					tracks.push(event.track);
					console.debug(`Got track mid=${event.track}`);
					if (tracks.length >= 2) {
						// remote video & audio are ready
						resolve(tracks);
					} else {
						console.log("No Tracks found! SDKJ32");
					}
				};
			},
		);

		// Calls API request to ask for the tracks
		const newRemoteTracksResult = await app.newTracks(remoteTrackObjects);
		if (newRemoteTracksResult.requiresImmediateRenegotiation) {
			switch (newRemoteTracksResult.sessionDescription.type) {
				case "offer":
					// We let Cloudflare know we're ready to receive the tracks
					await pc.setRemoteDescription(
						new RTCSessionDescription(newRemoteTracksResult.sessionDescription),
					);
					await pc.setLocalDescription(await pc.createAnswer());
					await app.sendAnswerSDP(pc.localDescription?.sdp || "");
					break;
				case "answer":
					throw new Error("An offer SDP was expected");
			}
		}

		// Once started receiving the tracks (video & audio) send the data to the video tag
		const remoteTracks = await remoteTracksPromise;
		// const remoteVideoElement = document.getElementById("remote-video");
		const remoteStream = new MediaStream();
		remoteStream.addTrack(remoteTracks[0]);
		remoteStream.addTrack(remoteTracks[1]);
		if (remoteVideoElement?.current) {
			remoteVideoElement.current.srcObject = remoteStream;
		}
	}

	useEffect(() => {
		// raw_init();
		stream_init();
	}, []);

	return (
		<div className="grid">
			<h1>Calls Echo Demo</h1>
			<div>
				<h2>Local stream</h2>
				<video ref={localVideoElement} autoPlay muted />
			</div>
			<div>
				<h2>Remote echo stream</h2>
				<video ref={remoteVideoElement} autoPlay />
			</div>
		</div>
	);
};

export default App;
