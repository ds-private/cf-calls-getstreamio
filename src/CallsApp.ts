import {
  createNewSession,
  createNewTracks,
  sendAnswerSDP,
} from "./services/callsApi";

export default class CallsApp {
  private prefixPath: string;
  sessionId?: string;

  constructor(
    private basePath: string = "http://localhost:5000",
    // private basePath: string = "https://eo7t07xifmum2qz.m.pipedream.net"
  ) {
    this.prefixPath = `${basePath}/calls`;
  }

  // Method to send a request, with body and method as optional
  async sendRequest(
    url: string,
    body: object,
    method: string = "POST",
  ): Promise<any> {
    const request: RequestInit = {
      method: method,
      mode: "cors",
      body: JSON.stringify(body),
      headers: {
        "content-type": "application/json",
      },
    };
    const response = await fetch(url, request);
    const result = await response.json();
    return result;
  }

  // Check for errors in the result
  checkErrors(result: any, tracksCount: number = 0): void {
    if (result.errorCode) {
      throw new Error(result.errorDescription);
    }
    for (let i = 0; i < tracksCount; i++) {
      if (result.tracks[i]?.errorCode) {
        throw new Error(`tracks[${i}]: ${result.tracks[i].errorDescription}`);
      }
    }
  }

  // Sends the initial offer and creates a session
  async newSession(offerSDP: string): Promise<any> {
    const url = `${this.prefixPath}/sessions/new`;
    const body = {
      sessionDescription: {
        type: "offer",
        sdp: offerSDP,
      },
    };
    const result = await this.sendRequest(url, body);
    this.checkErrors(result);
    this.sessionId = result.sessionId;
    return result;
  }

  // Shares local tracks or gets tracks
  async newTracks(
    trackObjects: any[],
    offerSDP: string | null = null,
  ): Promise<any> {
    if (!this.sessionId) {
      throw new Error("Session ID is not set. Please create a session first.");
    }

    const url = `${this.prefixPath}/sessions/${this.sessionId}/tracks/new`;
    const body: any = {
      sessionDescription: {
        type: "offer",
        sdp: offerSDP,
      },
      tracks: trackObjects,
    };
    if (!offerSDP) {
      delete body.sessionDescription;
    }
    const result = await this.sendRequest(url, body);
    this.checkErrors(result, trackObjects.length);
    return result;
  }

  // Sends an answer SDP if renegotiation is required
  async sendAnswerSDP(answer: string): Promise<void> {
    if (!this.sessionId) {
      throw new Error("Session ID is not set. Please create a session first.");
    }

    const url = `${this.prefixPath}/sessions/${this.sessionId}/renegotiate`;
    const body = {
      sessionDescription: {
        type: "answer",
        sdp: answer,
      },
    };
    const result = await this.sendRequest(url, body, "PUT");
    this.checkErrors(result);
  }
}
