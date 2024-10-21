import axios, { type AxiosResponse } from "axios";
import type { CallsApiResponse, TrackObject } from "../types";

const BASE_URL = "http://localhost:5000";

export const createNewSession = async (
	offerSDP: string,
): Promise<CallsApiResponse> => {
	const response: AxiosResponse<CallsApiResponse> = await axios.post(
		`${BASE_URL}/new_session`,
		{ offer_sdp: offerSDP },
	);
	return response.data;
};

export const createNewTracks = async (
	trackObjects: TrackObject[],
	offerSDP?: string,
): Promise<CallsApiResponse> => {
	const response: AxiosResponse<CallsApiResponse> = await axios.post(
		`${BASE_URL}/new_tracks`,
		{ track_objects: trackObjects, offer_sdp: offerSDP },
	);
	return response.data;
};

export const sendAnswerSDP = async (answerSDP: string): Promise<void> => {
	await axios.put(`${BASE_URL}/send_answer`, { answer_sdp: answerSDP });
};
