# Cloudflare Calls

1. New RTCPeerConnection
2. Set Local Desription (After Creating Offer) 
3. Create New session (using above SDP) -> app/appsid/sessions/new
4. (iceconnectionstatechange) Wait for target.iceConnectionState to change to "connected"
5. AGAIN?? Set Local Description (After Creating Offer)
6. New Tracks -> sessions/{sessionId}/tracks/new (Using Local Track Objects and new SDP)
7. pc.ontrack => listen for remote tracks
8. New Tracks -> sessions/{sessionId}/tracks/new (Using Remote Track Objects and new SDP) (newRemoteTracksResult.requiresImmediateRenegotiation))
9. When new Remote Track has "offer" Type -> set remote description (using new SDP)
10. Set local Description with (create answer) -> sendAnswerSDP 

# GetStream
 
1. New RTCPeerConnection
2. Set Local Desription (After Creating Offer) 
3. sfuClient.setPublisher -> Combination of step 3 to 6 of Cloudflare Calls (step 4 is skipped altogether)
4. set remote description (no steps 7 to 10, newRemoteTracksResult.requiresImmediateRenegotiation from CloufFlare calls is -> onNegotiationNeeded in getstream calls)


# Backend Re-Implementation

To make even the simplest sample code work with GetStream, I would essentially end up re-implementing fundamental backend functionalities that are already deeply tied to Cloudflare’s Calls API. For instance, Cloudflare requires manual session management (new_session) and track handling (new_tracks), which GetStream abstracts with their sfuClient.setPublisher method. While GetStream automates much of the peer connection and track negotiation, we’d still need to rewrite large portions of our backend to accommodate it.

# Offer/Answer Negotiation Differences

In Cloudflare, we manage the offer/answer process step-by-step, waiting for the connection to establish, and then handling renegotiations manually. In contrast, GetStream’s negotiation is more abstracted, using an onNegotiationNeeded trigger instead of our explicit renegotiation step (renegotiate). This difference could become a blocker, as we may need to manually override parts of GetStream’s default behavior to match our current flow.

# Track Handling Complexities

In Cloudflare, we manually add and manage tracks through the new_tracks API, requiring fine-grained control over each track's lifecycle. GetStream abstracts much of this process, which seems simpler at first glance but introduces a potential mismatch with how we manage tracks and media streams. Aligning these would either require significant modification to our backend or risk running into unforeseen issues when the track management processes don’t align perfectly.

# Conclusion

The highlighted differences in offer/answer negotiation and track handling may turn into significant blockers. To get even a basic POC running, I would essentially need to rewrite key backend components, which I believe defeats the purpose of trying to integrate GetStream with minimal changes. This effort is likely to outweigh the potential benefits, especially when considering that we already have a working Cloudflare setup.
