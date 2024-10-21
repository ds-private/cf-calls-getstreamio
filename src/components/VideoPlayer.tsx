import type React from "react";
import { useEffect, useRef } from "react";

interface VideoPlayerProps {
	stream: MediaStream | null;
	muted?: boolean;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ stream, muted = false }) => {
	const videoRef = useRef<HTMLVideoElement | null>(null);

	useEffect(() => {
		if (videoRef.current && stream) {
			videoRef.current.srcObject = stream;
		}
	}, [stream]);

	return (
		<video ref={videoRef} autoPlay muted={muted} style={{ width: "100%" }} />
	);
};

export default VideoPlayer;
