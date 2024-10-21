import { useEffect, useRef, useCallback } from "react";
import { StreamVideoClient, type User } from "@stream-io/video-client";
import { cleanupParticipant, renderParticipant } from "./participant";

const App: React.FC = () => {
	const participantsEl = useRef<HTMLDivElement | null>(null);

	const stream_init = useCallback(() => {
		const apiKey = "mmhfdzb5evj2";
		const callId = "FpDUjzLCEg4b";
		const token =
			"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3Byb250by5nZXRzdHJlYW0uaW8iLCJzdWIiOiJ1c2VyL0JvYmFfRmV0dCIsInVzZXJfaWQiOiJCb2JhX0ZldHQiLCJ2YWxpZGl0eV9pbl9zZWNvbmRzIjo2MDQ4MDAsImlhdCI6MTcyOTAyOTE2NSwiZXhwIjoxNzI5NjMzOTY1fQ.jrjg3gOOslK5s9HJ7yUd9bg9Ew5Tf7qQ0aFgeEfoaAc";
		const user: User = { id: "Boba_Fett" };

		const client = new StreamVideoClient({
			apiKey,
			token,
			user,
			options: {
				logLevel: "info",
				// baseURL: "http://localhost:5000"
			},
		});

		const call = client.call("default", callId);

		call.screenShare.enableScreenShareAudio();
		call.screenShare.setSettings({
			maxFramerate: 10,
			maxBitrate: 1500000,
		});
		call.join({ create: true }).then(() => {
			call.camera.enable();
			call.microphone.enable();
		});

		window.addEventListener("beforeunload", () => {
			call.leave();
		});

		if (participantsEl?.current) {
			call.setViewport(participantsEl?.current);
		}

		call.state.participants$.subscribe((participants) => {
			// render / update existing participants
			participants.forEach((participant) => {
				if (participantsEl?.current) {
					renderParticipant(call, participant, participantsEl?.current);
				}
			});

			// Remove stale elements for stale participants
			if (participantsEl?.current) {
				participantsEl?.current
					.querySelectorAll<HTMLMediaElement>("video, audio")
					.forEach((el) => {
						const sessionId = el.dataset.sessionId!;
						const participant = participants.find(
							(p) => p.sessionId === sessionId,
						);
						if (!participant) {
							cleanupParticipant(sessionId);
							el.remove();
						}
					});
			}
		});
	}, []);

	useEffect(() => {
		stream_init();
	}, [stream_init]);

	return <div ref={participantsEl}></div>;
};

export default App;
