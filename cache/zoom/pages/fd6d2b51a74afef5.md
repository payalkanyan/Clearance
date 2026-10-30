# Granular scopes

Copy for LLM

[View as Markdown](https://developers.zoom.us/docs/integrations/oauth-scopes-granular.md)

On this page

This reference lists the available Zoom OAuth API endpoints and granular scopes.

## Zoom Meeting [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-meeting)

The following are the available **Zoom Meeting** APIs and their associated granular scopes.

### Archiving [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#archiving)

| API endpoint | granular scope |
| --- | --- |
| [Get a meeting's archived files](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getArchivedFiles) | `archiving:read:archived_files:admin``archiving:read:archived_files` |
| [Get archived file statistics](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getArchivedFileStatistics) | `archiving:read:archived_file_statistics:admin` |
| [Get a meeting's archive token for local archiving](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLocalArchivingArchiveToken) | `meeting:read:local_archiving_token:admin` |
| [List archived files](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listArchivedFiles) | `archiving:read:list_archived_files:admin``archiving:read:list_archived_files:master` |
| [List archived files](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/listArchivedFiles) | `archiving:read:list_archived_files:master` |
| [Update an archived file's auto-delete status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/updateArchivedFile) | `archiving:update:archived_file_auto_delete_status``archiving:update:archived_file_auto_delete_status:admin` |
| [Delete a meeting's archived files](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteArchivedFiles) | `archiving:delete:archived_files:admin` |

### Cloud Recording [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cloud-recording)

| API endpoint | granular scope |
| --- | --- |
| [Get a meeting or webinar recording's analytics details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/analytics_details) | `cloud_recording:read:recording_analytics_details``cloud_recording:read:recording_analytics_details:master``cloud_recording:read:recording_analytics_details:admin` |
| [Get a meeting or webinar recording's analytics details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/analytics_details) | `cloud_recording:read:recording_analytics_details:master` |
| [Recover meeting recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingStatusUpdate) | `cloud_recording:update:recover_meeting_recordings``cloud_recording:update:recover_meeting_recordings:master``cloud_recording:update:recover_meeting_recordings:admin` |
| [Recover meeting recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingStatusUpdate) | `cloud_recording:update:recover_meeting_recordings:master` |
| [Get meeting recording settings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingSettingUpdate) | `cloud_recording:read:recording_settings``cloud_recording:read:recording_settings:admin``cloud_recording:read:recording_settings:master` |
| [Get meeting recording settings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingSettingUpdate) | `cloud_recording:read:recording_settings:master` |
| [Get registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingRegistrantsQuestionsGet) | `cloud_recording:read:registration_questions``cloud_recording:read:registration_questions:master``cloud_recording:read:registration_questions:admin` |
| [Get registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingRegistrantsQuestionsGet) | `cloud_recording:read:registration_questions:master` |
| [Create a recording registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRecordingRegistrantCreate) | `cloud_recording:write:recording_registrant``cloud_recording:write:recording_registrant:master``cloud_recording:write:recording_registrant:admin` |
| [Create a recording registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRecordingRegistrantCreate) | `cloud_recording:write:recording_registrant:master` |
| [List an account's recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListRecordingsOfAnAccount) | `cloud_recording:read:list_account_recordings:master``cloud_recording:read:list_account_recordings:admin` |
| [Update a registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRecordingRegistrantStatus) | `cloud_recording:update:registrant_status``cloud_recording:update:registrant_status:master``cloud_recording:update:registrant_status:admin` |
| [Update a registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRecordingRegistrantStatus) | `cloud_recording:update:registrant_status:master` |
| [Get meeting recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingGet) | `cloud_recording:read:list_recording_files:admin``cloud_recording:read:list_recording_files``cloud_recording:read:list_recording_files:master` |
| [Get meeting recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingGet) | `cloud_recording:read:list_recording_files:master` |
| [Get a meeting or webinar recording's analytics summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/analytics_summary) | `cloud_recording:read:recording_analytics_summary``cloud_recording:read:recording_analytics_summary:master``cloud_recording:read:recording_analytics_summary:admin` |
| [Get a meeting or webinar recording's analytics summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/analytics_summary) | `cloud_recording:read:recording_analytics_summary:master` |
| [Recover a single recording](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingStatusUpdateOne) | `cloud_recording:update:recover_single_recording``cloud_recording:update:recover_single_recording:master``cloud_recording:update:recover_single_recording:admin` |
| [Recover a single recording](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingStatusUpdateOne) | `cloud_recording:update:recover_single_recording:master` |
| [List recording registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRecordingRegistrants) | `cloud_recording:read:list_recording_registrants``cloud_recording:read:list_recording_registrants:admin``cloud_recording:read:list_recording_registrants:master` |
| [List recording registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRecordingRegistrants) | `cloud_recording:read:list_recording_registrants:master` |
| [Delete a recording file for a meeting or webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingDeleteOne) | `cloud_recording:delete:recording_file``cloud_recording:delete:recording_file:admin``cloud_recording:delete:recording_file:master` |
| [Delete a recording file for a meeting or webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingDeleteOne) | `cloud_recording:delete:recording_file:master` |
| [Delete meeting or webinar recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingDelete) | `cloud_recording:delete:meeting_recording``cloud_recording:delete:meeting_recording:admin``cloud_recording:delete:meeting_recording:master` |
| [Delete meeting or webinar recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingDelete) | `cloud_recording:delete:meeting_recording:master` |
| [Update meeting recording settings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingSettingsUpdate) | `cloud_recording:update:recording_settings``cloud_recording:update:recording_settings:master``cloud_recording:update:recording_settings:admin` |
| [Update meeting recording settings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingSettingsUpdate) | `cloud_recording:update:recording_settings:master` |
| [List all recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingsList) | `cloud_recording:read:list_user_recordings``cloud_recording:read:list_user_recordings:master``cloud_recording:read:list_user_recordings:admin` |
| [List all recordings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingsList) | `cloud_recording:read:list_user_recordings:master` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/recordingRegistrantQuestionUpdate) | `cloud_recording:update:registration_questions:admin``cloud_recording:update:registration_questions``cloud_recording:update:registration_questions:master` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/recordingRegistrantQuestionUpdate) | `cloud_recording:update:registration_questions:master` |

### Devices [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#devices)

| API endpoint | granular scope |
| --- | --- |
| [Upgrade ZPA firmware or app](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/UpgradeZpas/app) | `device:write:zpa_os_app:admin``device:write:zpa_os_app:master` |
| [Get ZPA version info](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/GetZpaVersioninfo) | `device:read:list_zpa_versions:admin``device:read:list_zpa_versions:master` |
| [Assign a device to a user or commonarea](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Assigndevicetoauser/commonarea) | `device:write:zpa_device:admin``device:write:zpa_device:master` |
| [Delete ZPA device by vendor and mac address](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/DeleteZpaDeviceByVendorAndMacAddress) | `device:delete:zpa_device:admin``device:delete:zpa_device:master` |
| [Get ZDM group info](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Getzdmgroupinfo) | `device:read:list_groups:admin``device:read:list_groups:master` |
| [Assign a device to a group](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/assginGroup) | `device:write:group:admin``device:write:group:master` |
| [Get Zoom Phone Appliance settings by user ID](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/GetZpaDeviceListProfileSettingOfaUser) | `device:read:user_setting:admin``device:read:user_setting:master` |
| [Change device association](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/changeDeviceAssociation) | `device:update:zdm_device_assignment:admin` |

### H323 Devices [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#h323-devices)

| API endpoint | granular scope |
| --- | --- |
| [Create a H.323/SIP device](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deviceCreate) | `h323_device:write:device:admin` |
| [Delete a H.323/SIP device](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deviceDelete) | `h323_device:delete:device:admin` |
| [Update a H.323/SIP device](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deviceUpdate) | `h323_device:update:device:admin` |
| [List all H.323/SIP devices](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deviceList) | `h323_device:read:list_devices:admin` |

### In-Meeting Apps [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#in-meeting-apps)

| API endpoint | granular scope |
| --- | --- |
| [Add a meeting app](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingAppAdd) | `meeting:write:open_app``meeting:write:open_app:admin` |
| [Delete a meeting app](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingAppDelete) | `meeting:delete:open_app``meeting:delete:open_app:admin` |

### In-Meeting Features [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#in-meeting-features)

| API endpoint | granular scope |
| --- | --- |
| [Get a meeting's join token for local recording](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLocalRecordingJoinToken) | `meeting:read:local_recording_token``meeting:read:local_recording_token:admin` |
| [Get meeting's token](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingToken) | `meeting:read:token``meeting:read:token:admin` |
| [Get meeting's token](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingToken) | `meeting:read:token:master` |
| [Delete a live meeting message](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteMeetingChatMessageById) | `meeting:delete:live_meeting_chat_message``meeting:delete:live_meeting_chat_message:admin` |
| [In-meeting controls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/inMeetingControl) | `meeting:update:in_meeting_controls``meeting:update:in_meeting_controls:admin` |
| [In-meeting controls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/inMeetingControl) | `meeting:update:in_meeting_controls:master` |
| [Update a live meeting message](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/updateMeetingChatMessageById) | `meeting:update:live_meeting_chat_message``meeting:update:live_meeting_chat_message:admin` |

### Invitation & Registration [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#invitation--registration)

| API endpoint | granular scope |
| --- | --- |
| [Delete a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingregistrantdelete) | `meeting:delete:registrant``meeting:delete:registrant:admin` |
| [Delete a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingregistrantdelete) | `meeting:delete:registrant:master` |
| [Perform batch registration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/addBatchRegistrants) | `meeting:write:batch_registrants``meeting:write:batch_registrants:admin` |
| [Perform batch registration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/addBatchRegistrants) | `meeting:write:batch_registrants:master` |
| [Get meeting invitation](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingInvitation) | `meeting:read:invitation``meeting:read:invitation:admin` |
| [Get meeting invitation](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingInvitation) | `meeting:read:invitation:master` |
| [Add a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrantCreate) | `meeting:write:registrant``meeting:write:registrant:admin` |
| [Add a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRegistrantCreate) | `meeting:write:registrant:master` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrantQuestionUpdate) | `meeting:update:registration_question``meeting:update:registration_question:admin` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRegistrantQuestionUpdate) | `meeting:update:registration_question:master` |
| [Update registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrantStatus) | `meeting:update:registrant_status``meeting:update:registrant_status:admin` |
| [Update registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRegistrantStatus) | `meeting:update:registrant_status:master` |
| [Create a meeting's invite links](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingInviteLinksCreate) | `meeting:write:invite_links``meeting:write:invite_links:admin` |
| [Create a meeting's invite links](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingInviteLinksCreate) | `meeting:write:invite_links:master` |
| [List meeting registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrants) | `meeting:read:list_registrants``meeting:read:list_registrants:admin` |
| [List meeting registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRegistrants) | `meeting:read:list_registrants:master` |
| [List registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrantsQuestionsGet) | `meeting:read:list_registration_questions``meeting:read:list_registration_questions:admin` |
| [Get a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRegistrantGet) | `meeting:read:registrant``meeting:read:registrant:admin` |
| [Get a meeting registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingRegistrantGet) | `meeting:read:registrant:master` |

### Live streaming [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#live-streaming)

| API endpoint | granular scope |
| --- | --- |
| [Update a livestream](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLiveStreamUpdate) | `meeting:update:livestream``meeting:update:livestream:admin` |
| [Update a livestream](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingLiveStreamUpdate) | `meeting:update:livestream:master` |
| [Update livestream status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLiveStreamStatusUpdate) | `meeting:update:livestream_status``meeting:update:livestream_status:admin` |
| [Update livestream status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingLiveStreamStatusUpdate) | `meeting:update:livestream_status:master` |
| [Get livestream details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getMeetingLiveStreamDetails) | `meeting:read:livestream``meeting:read:livestream:admin` |
| [Get livestream details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getMeetingLiveStreamDetails) | `meeting:read:livestream:master` |
| [Get a meeting's join token for live streaming](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLiveStreamingJoinToken) | `meeting:read:live_streaming_token``meeting:read:live_streaming_token:admin` |

### Meeting Transcript [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#meeting-transcript)

| API endpoint | granular scope |
| --- | --- |
| [Get a meeting transcript](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/GetMeetingTranscript) | `cloud_recording:read:meeting_transcript``cloud_recording:read:meeting_transcript:admin` |
| [Delete a meeting or webinar transcript](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/DeleteMeetingTranscript) | `cloud_recording:delete:meeting_transcript``cloud_recording:delete:meeting_transcript:admin` |

### Meetings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#meetings)

| API endpoint | granular scope |
| --- | --- |
| [Get a meeting SIP URI with passcode](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getSipDialingWithPasscode) | `meeting:write:sip_dialing``meeting:write:sip_dialing:admin` |
| [Update meeting status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingStatus) | `meeting:update:status``meeting:update:status:admin` |
| [Update meeting status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingStatus) | `meeting:update:status:master` |
| [Get past meeting details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/pastMeetingDetails) | `meeting:read:past_meeting``meeting:read:past_meeting:admin` |
| [Get a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meeting) | `meeting:read:meeting``meeting:read:meeting:admin` |
| [Get a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meeting) | `meeting:read:meeting:master` |
| [Update a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingUpdate) | `meeting:update:meeting:admin``meeting:update:meeting` |
| [Update a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingUpdate) | `meeting:update:meeting:master` |
| [Delete a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingDelete) | `meeting:delete:meeting``meeting:delete:meeting:admin` |
| [Delete a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingDelete) | `meeting:delete:meeting:master` |
| [List meetings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetings) | `meeting:read:list_meetings``meeting:read:list_meetings:admin` |
| [List meetings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetings) | `meeting:read:list_meetings:master` |
| [Update participant Real-Time Media Streams (RTMS) app status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingRTMSStatusUpdate) | `meeting:update:participant_rtms_app_status``meeting:update:participant_rtms_app_status:admin` |
| [Get past meeting participants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/pastMeetingParticipants) | `meeting:read:list_past_participants``meeting:read:list_past_participants:admin` |
| [Create a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingCreate) | `meeting:write:meeting``meeting:write:meeting:admin` |
| [Create a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingCreate) | `meeting:write:meeting:master` |
| [List upcoming meetings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listUpcomingMeeting) | `meeting:read:list_upcoming_meetings``meeting:read:list_upcoming_meetings:admin` |
| [List past meetings' Q&A](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listPastMeetingQA) | `meeting:read:past_qa``meeting:read:past_qa:admin` |
| [List past meeting instances](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/pastMeetings) | `meeting:read:list_past_instances``meeting:read:list_past_instances:admin` |
| [List past meeting instances](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/pastMeetings) | `meeting:read:list_past_instances:master` |

### PAC [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#pac)

| API endpoint | granular scope |
| --- | --- |
| [List a user's PAC accounts](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userPACs) | `pac:read:list_pac_accounts``pac:read:list_pac_accounts:admin` |
| [List a user's PAC accounts](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userPACs) | `pac:read:list_pac_accounts:master` |

### Polls [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#polls)

| API endpoint | granular scope |
| --- | --- |
| [Delete a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingPollDelete) | `meeting:delete:poll``meeting:delete:poll:admin` |
| [Delete a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingPollDelete) | `meeting:delete:poll:master` |
| [List meeting polls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingPolls) | `meeting:read:list_polls``meeting:read:list_polls:admin` |
| [List meeting polls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingPolls) | `meeting:read:list_polls:master` |
| [List past meeting's poll results](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listPastMeetingPolls) | `meeting:read:list_poll_results``meeting:read:list_poll_results:admin` |
| [Perform batch poll creation](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/createBatchPolls) | `meeting:write:batch_polls``meeting:write:batch_polls:admin` |
| [Perform batch poll creation](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/createBatchPolls) | `meeting:write:batch_polls:master` |
| [Create a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingPollCreate) | `meeting:write:poll``meeting:write:poll:admin` |
| [Create a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingPollCreate) | `meeting:write:poll:master` |
| [Get a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingPollGet) | `meeting:read:poll``meeting:read:poll:admin` |
| [Get a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingPollGet) | `meeting:read:poll:master` |
| [Update a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingPollUpdate) | `meeting:update:poll``meeting:update:poll:admin` |
| [Update a meeting poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingPollUpdate) | `meeting:update:poll:master` |

### Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports)

| API endpoint | granular scope |
| --- | --- |
| [Get disclaimer report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Getdisclaimerreport) | `report:read:disclaimer:admin` |
| [Get disclaimer report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Getdisclaimerreport) | `report:read:disclaimer:master` |
| [Get a meeting activities report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingactivitylogs) | `report:read:meeting_activity_log:admin` |
| [Get a meeting activities report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingactivitylogs) | `report:read:meeting_activity_log:master` |
| [Get telephone reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportTelephone) | `report:read:telephone:admin` |
| [Get telephone reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportTelephone) | `report:read:telephone:master` |
| [Get meeting detail reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingDetails) | `report:read:meeting:admin` |
| [Get meeting detail reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingDetails) | `report:read:meeting:master` |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportOperationLogs) | `report:read:operation_logs:admin` |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportOperationLogs) | `report:read:operation_logs:master` |
| [Get meeting Q&A report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingQA) | `report:read:meeting_qna:admin` |
| [Get meeting Q&A report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingQA) | `report:read:meeting_qna:master` |
| [Get history meeting and webinar list](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Gethistorymeetingandwebinarlist) | `report:read:list_history_meetings:admin` |
| [Get history meeting and webinar list](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Gethistorymeetingandwebinarlist) | `report:read:list_history_meetings:master` |
| [Get remote support report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Getremotesupportreport) | `report:read:remote_support:admin` |
| [Get remote support report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Getremotesupportreport) | `report:read:remote_support:master` |
| [Get webinar poll reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportWebinarPolls) | `report:read:list_webinar_polls:admin` |
| [Get webinar poll reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportWebinarPolls) | `report:read:list_webinar_polls:master` |
| [Get webinar Q&A report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportWebinarQA) | `report:read:webinar_qna:admin` |
| [Get webinar Q&A report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportWebinarQA) | `report:read:webinar_qna:master` |
| [Get sign In / sign out activity report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportSignInSignOutActivities) | `report:read:user_activities:admin` |
| [Get sign In / sign out activity report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportSignInSignOutActivities) | `report:read:user_activities:master` |
| [Get meeting poll reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingPolls) | `report:read:list_meeting_polls:admin` |
| [Get meeting poll reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingPolls) | `report:read:list_meeting_polls:master` |
| [Get meeting reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetings) | `report:read:user:admin` |
| [Get meeting reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetings) | `report:read:user:master` |
| [Get active or inactive host reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportUsers) | `report:read:list_users:admin` |
| [Get active or inactive host reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportUsers) | `report:read:list_users:master` |
| [Get webinar participant reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportWebinarParticipants) | `report:read:list_webinar_participants:admin` |
| [Get webinar participant reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportWebinarParticipants) | `report:read:list_webinar_participants:master` |
| [Get upcoming events reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportUpcomingEvents) | `report:read:upcoming_meetings_webinars:admin` |
| [Get upcoming events reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportUpcomingEvents) | `report:read:upcoming_meetings_webinars:master` |
| [Get webinar survey report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportWebinarSurvey) | `report:read:webinar_survey:admin` |
| [Get webinar survey report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportWebinarSurvey) | `report:read:webinar_survey:master` |
| [Get meeting participant reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingParticipants) | `report:read:list_meeting_participants:admin` |
| [Get meeting participant reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingParticipants) | `report:read:list_meeting_participants:master` |
| [Get billing reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getBillingReport) | `report:read:billing:admin` |
| [Get billing reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getBillingReport) | `report:read:billing:master` |
| [Get webinar detail reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportWebinarDetails) | `report:read:webinar:admin` |
| [Get webinar detail reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportWebinarDetails) | `report:read:webinar:master` |
| [Get billing invoice reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getBillingInvoicesReports) | `report:read:billing_invoice:admin` |
| [Get billing invoice reports](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getBillingInvoicesReports) | `report:read:billing_invoice:master` |
| [Get meeting survey report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingSurvey) | `report:read:meeting_survey:admin` |
| [Get meeting survey report](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/reportMeetingSurvey) | `report:read:meeting_survey:master` |

### SIP Connected Audio [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sip-connected-audio)

| API endpoint | granular scope |
| --- | --- |
| [List internal call-out countries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListInternalCall-outCountries) | `sip_connected_audio:read:callout_countries:master``sip_connected_audio:read:callout_countries:admin` |
| [List internal numbers](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListInternalNumbers) | `sip_connected_audio:read:internal_numbers:master``sip_connected_audio:read:internal_numbers:admin` |
| [Add internal call-out countries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/AddInternalCall-outCountries) | `sip_connected_audio:write:callout_countries:admin``sip_connected_audio:write:callout_countries:master` |
| [Assign SIP trunk configuration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/AssignSIPTrunkConfiguration) | `sip_connected_audio:update:settings:master``sip_connected_audio:update:settings:admin` |
| [Add internal numbers](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/AddInternalNumbers) | `sip_connected_audio:write:internal_numbers:admin``sip_connected_audio:write:internal_numbers:master` |
| [Get SIP trunk configuration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/GetSIPTrunkConfiguration) | `sip_connected_audio:read:settings:master``sip_connected_audio:read:settings:admin` |
| [List SIP trunks](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListSIPTrunks) | `sip_connected_audio:read:trunks:master``sip_connected_audio:read:trunks:admin` |
| [Assign SIP trunks](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/AssignSIPTrunks) | `sip_connected_audio:write:trunks:master` |
| [Delete a SIP trunk](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/DeleteASIPTrunk) | `sip_connected_audio:delete:trunks:master` |
| [Delete all numbers](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/DeleteAllNumbers) | `sip_connected_audio:delete:numbers:master` |
| [Assign numbers](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/AssignNumbers) | `sip_connected_audio:write:numbers:master` |
| [Delete an internal number](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/DeleteAnInternalNumber) | `sip_connected_audio:delete:internal_numbers:admin``sip_connected_audio:delete:internal_numbers:master` |
| [List SIP trunk numbers](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/listSipTrunkNumbers) | `sip_connected_audio:read:numbers:master` |
| [Update an internal number](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/UpdateAnInternalNumber) | `sip_connected_audio:update:internal_numbers:master``sip_connected_audio:update:internal_numbers:admin` |
| [Delete internal call-out country](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/DeleteInternalCall-outCountry) | `sip_connected_audio:delete:callout_countries:master``sip_connected_audio:delete:callout_countries:admin` |

### SIP Phone [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sip-phone)

| API endpoint | granular scope |
| --- | --- |
| [Enable SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/EnableSIPPhonePhones) | `sip_phone:write:sip_phone:admin` |
| [Enable SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/EnableSIPPhonePhones) | `sip_phone:write:sip_phone:master` |
| [Update SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/UpdateSIPPhonePhones) | `sip_phone:update:sip_phone:admin` |
| [Update SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/UpdateSIPPhonePhones) | `sip_phone:update:sip_phone:master` |
| [List SIP phones](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/ListSIPPhonePhones) | `sip_phone:read:list_sip_phones:admin` |
| [List SIP phones](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListSIPPhonePhones) | `sip_phone:read:list_sip_phones:master` |
| [Delete SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteSIPPhonePhones) | `sip_phone:delete:sip_phone:admin` |
| [Delete SIP phone](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/deleteSIPPhonePhones) | `sip_phone:delete:sip_phone:master` |

### Summaries [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#summaries)

| API endpoint | granular scope |
| --- | --- |
| [List an account's meeting or webinar summaries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Listmeetingsummaries) | `meeting:read:list_summaries:admin` |
| [List an account's meeting or webinar summaries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Listmeetingsummaries) | `meeting:read:list_summaries:master` |
| [Delete a meeting or webinar summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Deletemeetingorwebinarsummary) | `meeting:delete:summary``meeting:delete:summary:admin` |
| [Delete a meeting or webinar summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Deletemeetingorwebinarsummary) | `meeting:delete:summary:master` |
| [Get a meeting or webinar summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/Getameetingsummary) | `meeting:read:summary``meeting:read:summary:admin` |
| [Get a meeting or webinar summary](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/Getameetingsummary) | `meeting:read:summary:master` |
| [List a user's meeting or webinar summaries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/ListUserMeetingSummaries) | `meeting:read:list_summaries``meeting:read:list_summaries:admin` |
| [List a user's meeting or webinar summaries](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/ListUserMeetingSummaries) | `meeting:read:list_summaries:master` |

### Surveys [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#surveys)

| API endpoint | granular scope |
| --- | --- |
| [Update a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingSurveyUpdate) | `meeting:update:survey``meeting:update:survey:admin` |
| [Update a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingSurveyUpdate) | `meeting:update:survey:master` |
| [Get a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingSurveyGet) | `meeting:read:survey``meeting:read:survey:admin` |
| [Get a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingSurveyGet) | `meeting:read:survey:master` |
| [Delete a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingSurveyDelete) | `meeting:delete:survey``meeting:delete:survey:admin` |
| [Delete a meeting survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingSurveyDelete) | `meeting:delete:survey:master` |

### TSP [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#tsp)

| API endpoint | granular scope |
| --- | --- |
| [Add a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userTSPCreate) | `tsp:write:tsp_account``tsp:write:tsp_account:admin` |
| [Add a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userTSPCreate) | `tsp:write:tsp_account:master` |
| [Get account's TSP information](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/tsp) | `tsp:read:tsp:admin` |
| [Get account's TSP information](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/tsp) | `tsp:read:tsp:master` |
| [Update a TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userTSPUpdate) | `tsp:update:tsp_account``tsp:update:tsp_account:admin` |
| [Update a TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userTSPUpdate) | `tsp:update:tsp_account:master` |
| [Delete a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userTSPDelete) | `tsp:delete:tsp_account``tsp:delete:tsp_account:admin` |
| [Delete a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userTSPDelete) | `tsp:delete:tsp_account:master` |
| [Set global dial-in URL for a TSP user](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/tspUrlUpdate) | `tsp:update:tsp_settings``tsp:update:tsp_settings:admin` |
| [Set global dial-in URL for a TSP user](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/tspUrlUpdate) | `tsp:update:tsp_settings:master` |
| [Get a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userTSP) | `tsp:read:tsp_account``tsp:read:tsp_account:admin` |
| [Get a user's TSP account](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userTSP) | `tsp:read:tsp_account:master` |
| [Update an account's TSP information](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/tspUpdate) | `tsp:update:tsp:admin` |
| [Update an account's TSP information](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/tspUpdate) | `tsp:update:tsp:master` |
| [List user's TSP accounts](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userTSPs) | `tsp:read:list_tsp_accounts``tsp:read:list_tsp_accounts:admin` |
| [List user's TSP accounts](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/userTSPs) | `tsp:read:list_tsp_accounts:master` |

### Templates [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#templates)

| API endpoint | granular scope |
| --- | --- |
| [List meeting templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listMeetingTemplates) | `meeting:read:list_templates``meeting:read:list_templates:admin` |
| [List meeting templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/listMeetingTemplates) | `meeting:read:list_templates:master` |
| [Create a meeting template from an existing meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingTemplateCreate) | `meeting:write:template``meeting:write:template:admin` |
| [Create a meeting template from an existing meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/meetingTemplateCreate) | `meeting:write:template:master` |

### Tracking Field [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#tracking-field)

| API endpoint | granular scope |
| --- | --- |
| [Get a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/trackingfieldGet) | `tracking_field:read:tracking_field:admin` |
| [Get a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/trackingfieldGet) | `tracking_field:read:tracking_field:master` |
| [Delete a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/trackingfieldDelete) | `tracking_field:delete:tracking_field:admin` |
| [Delete a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/trackingfieldDelete) | `tracking_field:delete:tracking_field:master` |
| [List tracking fields](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/trackingfieldList) | `tracking_field:read:list_tracking_fields:admin` |
| [List tracking fields](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/trackingfieldList) | `tracking_field:read:list_tracking_fields:master` |
| [Create a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/trackingfieldCreate) | `tracking_field:write:tracking_field:admin` |
| [Create a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/trackingfieldCreate) | `tracking_field:write:tracking_field:master` |
| [Update a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/trackingfieldUpdate) | `tracking_field:update:tracking_field:admin` |
| [Update a tracking field](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/trackingfieldUpdate) | `tracking_field:update:tracking_field:master` |

### Webinars [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#webinars)

| API endpoint | granular scope |
| --- | --- |
| [Delete a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarDelete) | `webinar:delete:webinar``webinar:delete:webinar:admin` |
| [Delete a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarDelete) | `webinar:delete:webinar:master` |
| [List registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantsQuestionsGet) | `webinar:read:list_registration_questions``webinar:read:list_registration_questions:admin` |
| [List registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrantsQuestionsGet) | `webinar:read:list_registration_questions:master` |
| [Get a webinar's join token for local recording](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarLocalRecordingJoinToken) | `webinar:read:local_recording_token``webinar:read:local_recording_token:admin` |
| [Create a webinar's poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPollCreate) | `webinar:write:poll``webinar:write:poll:admin` |
| [Create a webinar's poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPollCreate) | `webinar:write:poll:master` |
| [Upload a webinar's branding virtual background](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/uploadWebinarBrandingVB) | `webinar:write:branding_virtual_background``webinar:write:branding_virtual_background:admin` |
| [Upload a webinar's branding virtual background](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/uploadWebinarBrandingVB) | `webinar:write:branding_virtual_background:master` |
| [List a webinar's polls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPolls) | `webinar:read:list_polls``webinar:read:list_polls:admin` |
| [List a webinar's polls](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPolls) | `webinar:read:list_polls:master` |
| [Update registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantStatus) | `webinar:update:registrant_status``webinar:update:registrant_status:admin` |
| [Update registrant's status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrantStatus) | `webinar:update:registrant_status:master` |
| [Update a live stream](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarLiveStreamUpdate) | `webinar:update:livestream``webinar:update:livestream:admin` |
| [Update a live stream](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarLiveStreamUpdate) | `webinar:update:livestream:master` |
| [Remove all panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPanelistsDelete) | `webinar:delete:panelist``webinar:delete:panelist:admin` |
| [Remove all panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPanelistsDelete) | `webinar:delete:panelist:master` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantQuestionUpdate) | `webinar:update:registration_question``webinar:update:registration_question:admin` |
| [Update registration questions](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrantQuestionUpdate) | `webinar:update:registration_question:master` |
| [Delete a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarSurveyDelete) | `webinar:delete:survey``webinar:delete:survey:admin` |
| [Delete a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarSurveyDelete) | `webinar:delete:survey:master` |
| [Create a webinar template](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarTemplateCreate) | `webinar:write:template``webinar:write:template:admin` |
| [Create a webinar template](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarTemplateCreate) | `webinar:write:template:master` |
| [List webinar templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listWebinarTemplates) | `webinar:read:list_templates``webinar:read:list_templates:admin` |
| [List webinar templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/listWebinarTemplates) | `webinar:read:list_templates:master` |
| [Get a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinar) | `webinar:read:webinar``webinar:read:webinar:admin` |
| [Get a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinar) | `webinar:read:webinar:master` |
| [Get live stream details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getWebinarLiveStreamDetails) | `webinar:read:livestream``webinar:read:livestream:admin` |
| [Get live stream details](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getWebinarLiveStreamDetails) | `webinar:read:livestream:master` |
| [List past webinar instances](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/pastWebinars) | `webinar:read:list_past_instances``webinar:read:list_past_instances:admin` |
| [List past webinar instances](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/pastWebinars) | `webinar:read:list_past_instances:master` |
| [Upload a webinar's branding wallpaper](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/uploadWebinarBrandingWallpaper) | `webinar:write:branding_wallpaper``webinar:write:branding_wallpaper:admin` |
| [Upload a webinar's branding wallpaper](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/uploadWebinarBrandingWallpaper) | `webinar:write:branding_wallpaper:master` |
| [Get a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPollGet) | `webinar:read:poll``webinar:read:poll:admin` |
| [Get a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPollGet) | `webinar:read:poll:master` |
| [Get a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarSurveyGet) | `webinar:read:survey``webinar:read:survey:admin` |
| [Get a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarSurveyGet) | `webinar:read:survey:master` |
| [Update a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPollUpdate) | `webinar:update:poll``webinar:update:poll:admin` |
| [Update a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPollUpdate) | `webinar:update:poll:master` |
| [List past webinar poll results](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listPastWebinarPollResults) | `webinar:read:list_past_polls``webinar:read:list_past_polls:admin` |
| [Get a webinar's archive token for local archiving](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarLocalArchivingArchiveToken) | `webinar:read:local_archiving_token:admin` |
| [Create a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarCreate) | `webinar:write:webinar``webinar:write:webinar:admin` |
| [Create a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarCreate) | `webinar:write:webinar:master` |
| [List webinars](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinars) | `webinar:read:list_webinars``webinar:read:list_webinars:admin` |
| [List webinars](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinars) | `webinar:read:list_webinars:master` |
| [Set webinar's default branding virtual background](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/setWebinarBrandingVB) | `webinar:update:branding_virtual_background``webinar:update:branding_virtual_background:admin` |
| [Set webinar's default branding virtual background](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/setWebinarBrandingVB) | `webinar:update:branding_virtual_background:master` |
| [Get webinar's session branding](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getWebinarBranding) | `webinar:read:branding``webinar:read:branding:admin` |
| [Get webinar's session branding](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getWebinarBranding) | `webinar:read:branding:master` |
| [Get a webinar's join token for live streaming](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarLiveStreamingJoinToken) | `webinar:read:live_streaming_token``webinar:read:live_streaming_token:admin` |
| [Delete a webinar's branding wallpaper](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteWebinarBrandingWallpaper) | `webinar:delete:branding_wallpaper``webinar:delete:branding_wallpaper:admin` |
| [Delete a webinar's branding wallpaper](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/deleteWebinarBrandingWallpaper) | `webinar:delete:branding_wallpaper:master` |
| [Get a webinar SIP URI with passcode](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getWebinarSipDialingWithPasscode) | `webinar:write:sip_dialing``webinar:write:sip_dialing:admin` |
| [Perform batch registration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/addBatchWebinarRegistrants) | `webinar:write:batch_registrants``webinar:write:batch_registrants:admin` |
| [Perform batch registration](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/addBatchWebinarRegistrants) | `webinar:write:batch_registrants:master` |
| [Update a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarUpdate) | `webinar:update:webinar``webinar:update:webinar:admin` |
| [Update a webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarUpdate) | `webinar:update:webinar:master` |
| [Update webinar status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarStatus) | `webinar:update:status``webinar:update:status:admin` |
| [Update webinar status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarStatus) | `webinar:update:status:master` |
| [Delete a webinar's branding virtual backgrounds](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteWebinarBrandingVB) | `webinar:delete:branding_virtual_background``webinar:delete:branding_virtual_background:admin` |
| [Delete a webinar's branding virtual backgrounds](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/deleteWebinarBrandingVB) | `webinar:delete:branding_virtual_background:master` |
| [List panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPanelists) | `webinar:read:list_panelists``webinar:read:list_panelists:admin` |
| [List panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPanelists) | `webinar:read:list_panelists:master` |
| [Get webinar absentees](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarAbsentees) | `webinar:read:list_absentees``webinar:read:list_absentees:admin` |
| [Get webinar absentees](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarAbsentees) | `webinar:read:list_absentees:master` |
| [Get webinar tracking sources](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/getTrackingSources) | `webinar:read:list_tracking_sources``webinar:read:list_tracking_sources:admin` |
| [Get webinar tracking sources](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/getTrackingSources) | `webinar:read:list_tracking_sources:master` |
| [Delete a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPollDelete) | `webinar:delete:poll``webinar:delete:poll:admin` |
| [Delete a webinar poll](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPollDelete) | `webinar:delete:poll:master` |
| [Get webinar's token](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarToken) | `webinar:read:token``webinar:read:token:admin` |
| [Get webinar's token](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarToken) | `webinar:read:token:master` |
| [Remove a panelist](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPanelistDelete) | `webinar:delete:panelist``webinar:delete:panelist:admin` |
| [Remove a panelist](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPanelistDelete) | `webinar:delete:panelist:master` |
| [Delete a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteWebinarBrandingNameTag) | `webinar:delete:branding_name_tag``webinar:delete:branding_name_tag:admin` |
| [Delete a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/deleteWebinarBrandingNameTag) | `webinar:delete:branding_name_tag:master` |
| [Update a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/updateWebinarBrandingNameTag) | `webinar:update:branding_name_tag``webinar:update:branding_name_tag:admin` |
| [Update a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/updateWebinarBrandingNameTag) | `webinar:update:branding_name_tag:master` |
| [Get a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantGet) | `webinar:read:registrant``webinar:read:registrant:admin` |
| [Get a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrantGet) | `webinar:read:registrant:master` |
| [List Q&As of a past webinar](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listPastWebinarQA) | `webinar:read:past_qa``webinar:read:past_qa:admin` |
| [Add panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPanelistCreate) | `webinar:write:panelist``webinar:write:panelist:admin` |
| [Add panelists](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarPanelistCreate) | `webinar:write:panelist:master` |
| [Create webinar's invite links](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarInviteLinksCreate) | `webinar:write:invite_links``webinar:write:invite_links:admin` |
| [Create webinar's invite links](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarInviteLinksCreate) | `webinar:write:invite_links:master` |
| [Update live stream status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarLiveStreamStatusUpdate) | `webinar:update:livestream_status``webinar:update:livestream_status:admin` |
| [Update live stream status](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarLiveStreamStatusUpdate) | `webinar:update:livestream_status:master` |
| [Update a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarSurveyUpdate) | `webinar:update:survey``webinar:update:survey:admin` |
| [Update a webinar survey](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarSurveyUpdate) | `webinar:update:survey:master` |
| [Delete a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteWebinarRegistrant) | `webinar:delete:registrant``webinar:delete:registrant:admin` |
| [Delete a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/deleteWebinarRegistrant) | `webinar:delete:registrant:master` |
| [List webinar participants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listWebinarParticipants) | `webinar:read:list_past_participants:admin``webinar:read:list_past_participants` |
| [Create a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/createWebinarBrandingNameTag) | `webinar:write:branding_name_tag``webinar:write:branding_name_tag:admin` |
| [Create a webinar's branding name tag](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/createWebinarBrandingNameTag) | `webinar:write:branding_name_tag:master` |
| [List webinar registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrants) | `webinar:read:list_registrants``webinar:read:list_registrants:admin` |
| [List webinar registrants](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrants) | `webinar:read:list_registrants:master` |
| [Delete a live webinar message](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/deleteWebinarChatMessageById) | `webinar:delete:live_webinar_chat_message``webinar:delete:live_webinar_chat_message:admin` |
| [Add a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) | `webinar:write:registrant``webinar:write:registrant:admin` |
| [Add a webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma/#operation/webinarRegistrantCreate) | `webinar:write:registrant:master` |

## Zoom Mail [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-mail)

The following are the available **Zoom Mail** APIs and their associated granular scopes.

### Drafts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#drafts)

| API endpoint | granular scope |
| --- | --- |
| [Send out a draft email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/send_draft_email) | `email:write:send_draft``email:write:send_draft:admin` |
| [List emails from draft folder](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_draft_emails) | `email:read:list_drafts``email:read:list_drafts:admin` |
| [Get the specified draft email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_draft_email) | `email:read:draft``email:read:draft:admin` |
| [Create a new draft email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/create_draft_email) | `email:write:draft``email:write:draft:admin` |
| [Delete an existing draft email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/delete_draft_email) | `email:delete:draft``email:delete:draft:admin` |
| [Update the specified draft email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/update_draft_email) | `email:update:draft``email:update:draft:admin` |

### History [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#history)

| API endpoint | granular scope |
| --- | --- |
| [List history of events for mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_mailbox_history) | `email:read:history``email:read:history:admin` |

### Labels [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#labels)

| API endpoint | granular scope |
| --- | --- |
| [Get the specified label in mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_label_in_mailbox) | `email:read:label``email:read:label:admin` |
| [Update the specified label in mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/update_label_in_mailbox) | `email:update:label``email:update:label:admin` |
| [List labels in the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_labels_in_mailbox) | `email:read:list_labels``email:read:list_labels:admin` |
| [Create a new label in mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/create_label_in_mailbox) | `email:write:label``email:write:label:admin` |
| [Delete an existing label from mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/delete_label_from_mailbox) | `email:delete:label``email:delete:label:admin` |
| [Patch the specified label in mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/patch_label_in_mailbox) | `email:update:label``email:update:label:admin` |

### Mailbox [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#mailbox)

| API endpoint | granular scope |
| --- | --- |
| [Get the mailbox profile](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_mailbox_profile) | `email:read:profile``email:read:profile:admin` |

### Messages [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#messages)

| API endpoint | granular scope |
| --- | --- |
| [Batch delete the specified emails](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/batch_delete_emails) | `email:write:batch_delete_msgs``email:write:batch_delete_msgs:admin` |
| [Delete an existing email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/delete_email) | `email:delete:msg``email:delete:msg:admin` |
| [Move the specified email to TRASH folder](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/trash_email) | `email:write:trash_msg``email:write:trash_msg:admin` |
| [Update the specified email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/update_email) | `email:write:modify_msg``email:write:modify_msg:admin` |
| [Send out an email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/send_email) | `email:write:send_msg``email:write:send_msg:admin` |
| [List emails from the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_emails) | `email:read:list_msgs``email:read:list_msgs:admin` |
| [Move the specified email out of TRASH folder](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/untrash_email) | `email:write:untrash_msg``email:write:untrash_msg:admin` |
| [Create a new email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/create_email) | `email:write:msg``email:write:msg:admin` |
| [Batch modify the specified emails](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/batch_modify_emails) | `email:write:batch_modify_msgs``email:write:batch_modify_msgs:admin` |
| [Get the specified email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_email) | `email:read:msg``email:read:msg:admin` |

### Messages.Attachments [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#messagesattachments)

| API endpoint | granular scope |
| --- | --- |
| [Get the specified attachment for an email](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_email_attachment) | `email:read:attachment``email:read:attachment:admin` |

### Settings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settings)

| API endpoint | granular scope |
| --- | --- |
| [Update mailbox vacation response setting](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/update_mailbox_vacation_response_setting) | `email:update:setting_vacation``email:update:setting_vacation:admin` |
| [Get mailbox vacation response setting](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_mail_vacation_response_setting) | `email:read:setting_vacation``email:read:setting_vacation:admin` |

### Settings.Delegates [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settingsdelegates)

| API endpoint | granular scope |
| --- | --- |
| [Revoke an existing delegate access from the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/revoke_mailbox_delegate) | `email:delete:setting_delegate``email:delete:setting_delegate:admin` |
| [List delegates on the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_mailbox_delegates) | `email:read:list_setting_delegates``email:read:list_setting_delegates:admin` |
| [Grant a new delegate access on the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/grant_mailbox_delegate) | `email:write:setting_delegate``email:write:setting_delegate:admin` |
| [Get the specified delegate on the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_mailbox_delegate) | `email:read:setting_delegate``email:read:setting_delegate:admin` |

### Settings.Filters [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settingsfilters)

| API endpoint | granular scope |
| --- | --- |
| [Get the specified email filter](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_email_filter) | `email:read:setting_filter``email:read:setting_filter:admin` |
| [Delete the specified email filter](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/delete_email_filter) | `email:delete:setting_filter``email:delete:setting_filter:admin` |
| [List email filters](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_email_filters) | `email:read:list_setting_filters``email:read:list_setting_filters:admin` |
| [Create an email filter](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/create_email_filter) | `email:write:setting_filter``email:write:setting_filter:admin` |

### Threads [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#threads)

| API endpoint | granular scope |
| --- | --- |
| [Update the specified thread](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/update_email_thread) | `email:write:thread``email:write:thread:admin` |
| [Delete an existing email thread](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/delete_email_thread) | `email:delete:thread``email:delete:thread:admin` |
| [Move the specified thread out of TRASH folder](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/untrash_email_thread) | `email:write:untrash_thread``email:write:untrash_thread:admin` |
| [Move the specified thread to TRASH folder](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/trash_email_thread) | `email:write:trash_thread``email:write:trash_thread:admin` |
| [Get the specified email thread](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/get_email_thread) | `email:read:thread``email:read:thread:admin` |
| [List email threads from the mailbox](https://developers.zoom.us/docs/api/rest/reference/zoom-mail/methods/#operation/list_email_threads) | `email:read:list_threads``email:read:list_threads:admin` |

## Whiteboard [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#whiteboard)

The following are the available **Whiteboard** APIs and their associated granular scopes.

### Archiving [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#archiving-1)

| API endpoint | granular scope |
| --- | --- |
| [List whiteboards sessions](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Createwhiteboardsarchivefiles) | `whiteboard:read:list_sessions``whiteboard:read:list_sessions:admin` |
| [Download Whiteboards activity file](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Downloadwhiteboardsactivityfile) | `whiteboard:read:archived_file``whiteboard:read:archived_file:admin` |
| [List whiteboard sessions activities](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Listwhiteboardsessionsarchivedfiles) | `whiteboard:read:session``whiteboard:read:session:admin` |

### Classification Labels [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#classification-labels)

| API endpoint | granular scope |
| --- | --- |
| [Delete classification label](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/deleteClassificationLabel) | `whiteboard:delete:classification_labels:admin` |
| [Remove classification from whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/removeWhiteboardClassification) | `whiteboard:delete:whiteboard_classification``whiteboard:delete:whiteboard_classification:admin` |
| [Apply classification to whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Applyclassificationtowhiteboard) | `whiteboard:update:whiteboard_classification``whiteboard:update:whiteboard_classification:admin` |
| [Create a classification label](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/createClassificationLabel) | `whiteboard:write:classification_labels:admin` |
| [Update a classification label](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/updateClassificationLabel) | `whiteboard:update:classification_labels:admin` |
| [Get classification label](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/getClassificationLabel) | `whiteboard:read:classification_labels:admin` |
| [List classification labels](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/listClassificationLabels) | `whiteboard:read:list_classification_labels:admin``whiteboard:read:list_classification_labels` |

### Collaborator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#collaborator)

| API endpoint | granular scope |
| --- | --- |
| [Remove the collaborator from a whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/DeleteAWhiteboardCollaborator) | `whiteboard:delete:collaborator:admin``whiteboard:delete:collaborator` |
| [Get collaborators of a whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/GetAWhiteboardCollaborator) | `whiteboard:read:list_collaborators:admin``whiteboard:read:list_collaborators` |
| [Share a whiteboard to new users or team chat channels.](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/AddAWhiteboardCollaborator) | `whiteboard:write:collaborator:admin``whiteboard:write:collaborator` |
| [Update whiteboard collaborators](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/UpdateAWhiteboardCollaborator) | `whiteboard:update:collaborator:admin``whiteboard:update:collaborator` |

### Content [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#content)

| API endpoint | granular scope |
| --- | --- |
| [Delete Whiteboard Content](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/DeleteWhiteboardContent) | `whiteboard:delete:content` |
| [Get Whiteboard Content](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/GetWhiteboardContent) | `whiteboard:read:content` |
| [Save Whiteboard Content](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/SaveWhiteboardContent) | `whiteboard:write:content` |

### Document [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#document)

| API endpoint | granular scope |
| --- | --- |
| [Get a whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/GetAWhiteboard) | `whiteboard:read:whiteboard:admin``whiteboard:read:whiteboard` |
| [Update whiteboard basic information](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/UpdateAWhiteboardMetadata) | `whiteboard:update:whiteboard:admin` |
| [Create a new whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/newWhiteboardCreate) | `whiteboard:write:whiteboard` |
| [Delete a whiteboard](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/DeleteAWhiteboard) | `whiteboard:delete:whiteboard:admin``whiteboard:delete:whiteboard` |
| [List all whiteboards](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/ListWhiteboards) | `whiteboard:read:list_whiteboards:admin``whiteboard:read:list_whiteboards` |

### Export [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#export)

| API endpoint | granular scope |
| --- | --- |
| [Download whiteboard export](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Downloadwhiteboardexport) | `whiteboard:read:export``whiteboard:read:export:admin` |
| [Get whiteboard export generation status](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Getwhiteboardexportdatagenerationstatus) | `whiteboard:read:export``whiteboard:read:export:admin` |
| [Create whiteboard export](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Createwhiteboardsexport) | `whiteboard:write:export``whiteboard:write:export:admin` |

### File [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#file)

| API endpoint | granular scope |
| --- | --- |
| [Download Imported Whiteboard File](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Downloadembeddedwhiteboardfile) | `whiteboard:read:file``whiteboard:read:file:admin` |
| [Upload file for whiteboard import](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Uploadfileforwhiteboardimport) | `whiteboard:write:file``whiteboard:write:file:admin` |

### Import [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#import)

| API endpoint | granular scope |
| --- | --- |
| [Get whiteboard import status](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/GetWhiteboardimportstatus) | `whiteboard:read:import:admin``whiteboard:read:import` |
| [Create a new whiteboard by import](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/CreateWhiteboardImport) | `whiteboard:write:import``whiteboard:write:import:admin` |

### Project [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#project)

| API endpoint | granular scope |
| --- | --- |
| [Share a project to new users](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Shareaprojecttonewusers) | `whiteboard:write:project_collaborator``whiteboard:write:project_collaborator:admin` |
| [Move whiteboards to a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Movewhiteboardstoproject) | `whiteboard:write:project_whiteboard``whiteboard:write:project_whiteboard:admin` |
| [Remove whiteboards from a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Removewhiteboardsfromaproject) | `whiteboard:delete:project_whiteboard``whiteboard:delete:project_whiteboard:admin` |
| [Remove the collaborator from a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Removethecollaboratorfromaproject) | `whiteboard:delete:project_collaborator:admin``whiteboard:delete:project_collaborator` |
| [Delete a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Deleteproject) | `whiteboard:delete:project``whiteboard:delete:project:admin` |
| [Update project basic information](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Updateproject) | `whiteboard:update:project:admin``whiteboard:update:project` |
| [Get collaborators of a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Getcollaboratorsofaproject) | `whiteboard:read:project_collaborator``whiteboard:read:project_collaborator:admin` |
| [List subprojects](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/listSubProjects) | `whiteboard:read:subproject``whiteboard:read:subproject:admin` |
| [Get a project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Getaproject) | `whiteboard:read:project``whiteboard:read:project:admin` |
| [Update project collaborators](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Updateprojectcollaborators) | `whiteboard:update:project_collaborator``whiteboard:update:project_collaborator:admin` |
| [Create a new project](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Createproject) | `whiteboard:write:project``whiteboard:write:project:admin` |
| [List all projects](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/Listallprojects) | `whiteboard:read:list_projects:admin``whiteboard:read:list_projects` |
| [Create a subproject](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/createSubProject) | `whiteboard:write:subproject``whiteboard:write:subproject:admin` |

### Settings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settings-1)

| API endpoint | granular scope |
| --- | --- |
| [Update whiteboard share setting](https://developers.zoom.us/docs/api/rest/reference/Whiteboard/methods/#operation/UpdateAWhiteboardShareSetting) | `whiteboard:update:share_setting:admin``whiteboard:update:share_setting` |

## Zoom Clips [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-clips)

The following are the available **Zoom Clips** APIs and their associated granular scopes.

### Clips [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#clips)

| API endpoint | granular scope |
| --- | --- |
| [List all clips](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/GetUserClips) | `clips:read:list_user_clips``clips:read:list_user_clips:admin` |
| [List all clips](https://developers.zoom.us/docs/api/rest/reference/clips/ma/#operation/GetUserClips) | `clips:read:list_user_clips:master` |
| [Batch star clips](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Batchstarclips) | `clips:write:star_clips``clips:write:star_clips:admin` |

### Collaborator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#collaborator-1)

| API endpoint | granular scope |
| --- | --- |
| [Remove the collaborator from a clip](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/DeleteCollaborator) | `clips:delete:collaborators``clips:delete:collaborators:admin` |
| [Get collaborators of a clip](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/GetClipCollaborators) | `clips:read:list_collaborator``clips:read:list_collaborator:admin` |
| [Share a clip with new users](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/CreateCollaborator) | `clips:write:collaborators``clips:write:collaborators:admin` |

### Comment [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#comment)

| API endpoint | granular scope |
| --- | --- |
| [List clip comments](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Listclipcomments) | `clips:read:list_comments``clips:read:list_comments:admin` |
| [Delete a comment](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Deleteacomment) | `clips:delete:comment``clips:delete:comment:admin` |

### Download [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#download)

| API endpoint | granular scope |
| --- | --- |
| [Download a clip](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/downloadClip) | `clips:read:download_clip``clips:read:download_clip:admin` |

### Single [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#single)

| API endpoint | granular scope |
| --- | --- |
| [Delete a clip(soft delete)](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/DeleteClip) | `clips:delete:clip``clips:delete:clip:admin` |
| [Get Clip Chapters](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/GetClipChapters) | `clips:read:chapters``clips:read:chapters:admin` |
| [Create Clip Chapters](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/createClipChapters) | `clips:write:chapters``clips:write:chapters:admin` |
| [Duplicate Clips](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/DuplicateClips) | `clips:write:duplicate` |
| [Update a clip's basic info](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/UpdateClipById) | `clips:update:clip``clips:update:clip:admin` |
| [Get a clip](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/GetClipById) | `clips:read:clip``clips:read:clip:admin` |
| [Update clips share setting](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Updateclipssharesetting) | `clips:update:share_setting``clips:update:share_setting:admin` |

### Transfer [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#transfer)

| API endpoint | granular scope |
| --- | --- |
| [Transfer task status check](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Transfertaskstatuscheck) | `clips:read:transfer_task_status:admin` |
| [Transfer clips owner](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/Transferclipsowner) | `clips:write:transfer_owner:admin` |

### Upload [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#upload)

| API endpoint | granular scope |
| --- | --- |
| [Temporary file upload API for Clips](https://developers.zoom.us/docs/api/rest/reference/clips/methods/#operation/TemporaryfileuploadAPIforClips) | `clips:write:uploadTempFile``clips:write:uploadTempFile:admin` |

## Zoom Account [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-account)

The following are the available **Zoom Account** APIs and their associated granular scopes.

### Accounts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#accounts)

| API endpoint | granular scope |
| --- | --- |
| [Upload virtual background files](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/uploadVB) | `account:write:virtual_background_files:master``account:write:virtual_background_files:admin` |
| [Upload virtual background files](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/uploadVB) | `account:write:virtual_background_files:master` |
| [Update an account's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountSettingsRegistrationUpdate) | `account:update:registration_settings:master` |
| [Update an account's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountSettingsRegistrationUpdate) | `account:update:registration_settings:master` |
| [Get sub account details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/GetSubAccountDetails) | `account:read:sub_account:master``account:read:sub_account:admin` |
| [Update webinar Waiting Room branding](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/UpdatewebinarWaitingRoombranding) | `account:write:waiting_room_branding:master``account:write:waiting_room_branding:admin` |
| [Update webinar Waiting Room branding](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/UpdatewebinarWaitingRoombranding) | `account:write:waiting_room_branding:master` |
| [Update meeting Waiting Room branding](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountMeetingWaitingRoomBrandingUpdate) | `account:write:waiting_room_branding:admin``account:write:waiting_room_branding:master` |
| [Update meeting Waiting Room branding](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountMeetingWaitingRoomBrandingUpdate) | `account:write:waiting_room_branding:master` |
| [Delete virtual background files](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/delVB) | `account:delete:virtual_background_files:master``account:delete:virtual_background_files:admin` |
| [Delete virtual background files](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/delVB) | `account:delete:virtual_background_files:master` |
| [Update account settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountSettingsUpdate) | `account:update:settings:admin``account:update:settings:master` |
| [Update account settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountSettingsUpdate) | `account:update:settings:master` |
| [Update locked settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/UpdateLockedSettings) | `account:update:lock_settings:master``account:update:lock_settings:admin` |
| [Update locked settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/UpdateLockedSettings) | `account:update:lock_settings:master` |
| [Get an account's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountSettingsRegistration) | `account:read:registration_settings:master` |
| [Get an account's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountSettingsRegistration) | `account:read:registration_settings:master` |
| [Create a sub account](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountCreate) | `account:write:sub_account:master` |
| [Update the account owner](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/UpdateTheAccountOwner) | `account:update:owner:master``account:update:owner:admin` |
| [Update the account owner](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/UpdateTheAccountOwner) | `account:update:owner:master` |
| [Update options](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/UpdateOptions) | `account:update:options:master` |
| [Get locked settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getAccountLockSettings) | `account:read:lock_settings:master` |
| [Get locked settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getAccountLockSettings) | `account:read:lock_settings:master` |
| [Get account's managed domains](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountManagedDomain) | `account:read:managed_domains:master` |
| [Get account's managed domains](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountManagedDomain) | `account:read:managed_domains:master` |
| [Get account's trusted domains](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountTrustedDomain) | `account:read:trusted_domains:master` |
| [Get account's trusted domains](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountTrustedDomain) | `account:read:trusted_domains:master` |
| [Disassociate a sub account](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/DisassociateASubAccount) | `account:delete:sub_account:master` |
| [List sub accounts](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accounts) | `account:read:list_sub_accounts:master` |
| [Get account settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/accountSettings) | `account:read:settings:admin``account:read:settings:master` |
| [Get account settings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/accountSettings) | `account:read:settings:master` |

### Dashboards [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#dashboards)

| API endpoint | granular scope |
| --- | --- |
| [List meeting participants](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingParticipants) | `dashboard:read:list_meeting_participants:admin` |
| [List meeting participants](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingParticipants) | `dashboard:read:list_meeting_participants:master` |
| [Get top 25 issues of Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardZoomRoomIssue) | `dashboard:read:issues_zoomroom:admin` |
| [Get top 25 issues of Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardZoomRoomIssue) | `dashboard:read:issues_zoomroom:master` |
| [List client meeting satisfaction](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/listMeetingSatisfaction) | `dashboard:read:meeting_survey:admin` |
| [List client meeting satisfaction](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/listMeetingSatisfaction) | `dashboard:read:meeting_survey:master` |
| [Get webinar participants](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinarParticipants) | `dashboard:read:list_webinar_participants:admin` |
| [Get webinar participants](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinarParticipants) | `dashboard:read:list_webinar_participants:master` |
| [Get meeting participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingParticipantQOS) | `dashboard:read:meeting_participant_qos:admin` |
| [Get meeting participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingParticipantQOS) | `dashboard:read:meeting_participant_qos:master` |
| [Get issues of Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardIssueDetailZoomRoom) | `dashboard:read:issues_zoomroom:admin` |
| [Get issues of Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardIssueDetailZoomRoom) | `dashboard:read:issues_zoomroom:master` |
| [List webinars](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinars) | `dashboard:read:list_webinars:admin` |
| [List webinars](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinars) | `dashboard:read:list_webinars:master` |
| [Get webinar details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinarDetail) | `dashboard:read:webinar:admin` |
| [Get webinar details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinarDetail) | `dashboard:read:webinar:master` |
| [List webinar participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinarParticipantsQOS) | `dashboard:read:list_webinar_participants_qos:admin` |
| [List webinar participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinarParticipantsQOS) | `dashboard:read:list_webinar_participants_qos:master` |
| [Get zoom meetings client feedback](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardClientFeedbackDetail) | `dashboard:read:meeting_feedback:admin` |
| [Get zoom meetings client feedback](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardClientFeedbackDetail) | `dashboard:read:meeting_feedback:master` |
| [Get AI usage trend](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetAItrends) | `dashboard:read:ai_usage_trend:admin` |
| [Get AI usage trend](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/GetAItrends) | `dashboard:read:ai_usage_trend:master` |
| [Get Zoom Rooms details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardZoomRoom) | `dashboard:read:zoomroom:admin` |
| [Get Zoom Rooms details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardZoomRoom) | `dashboard:read:zoomroom:master` |
| [Get post meeting feedback](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/participantFeedback) | `dashboard:read:post_meeting_feedback:admin` |
| [Get post meeting feedback](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/participantFeedback) | `dashboard:read:post_meeting_feedback:master` |
| [Get AI adoption](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetAIAdoption) | `dashboard:read:ai_adoption:admin` |
| [Get AI adoption](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/GetAIAdoption) | `dashboard:read:ai_adoption:master` |
| [Get top 25 Zoom Rooms with issues](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardIssueZoomRoom) | `dashboard:read:list_zoomrooms:admin` |
| [Get top 25 Zoom Rooms with issues](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardIssueZoomRoom) | `dashboard:read:list_zoomrooms:master` |
| [Get AI usage details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetAIDetails) | `dashboard:read:ai_usage_details:admin` |
| [Get AI usage details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/GetAIDetails) | `dashboard:read:ai_usage_details:master` |
| [Get AI KPIs](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetAIROIKPIs) | `dashboard:read:ai_kpi:admin` |
| [Get AI KPIs](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/GetAIROIKPIs) | `dashboard:read:ai_kpi:master` |
| [List Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardZoomRooms) | `dashboard:read:list_zoomrooms:admin` |
| [List Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardZoomRooms) | `dashboard:read:list_zoomrooms:master` |
| [Get webinar participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinarParticipantQOS) | `dashboard:read:webinar_participant_qos:admin` |
| [Get webinar participant QoS](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinarParticipantQOS) | `dashboard:read:webinar_participant_qos:master` |
| [List meeting participants QoS](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingParticipantsQOS) | `dashboard:read:list_meeting_participants_qos:admin` |
| [List meeting participants QoS](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingParticipantsQOS) | `dashboard:read:list_meeting_participants_qos:master` |
| [Get AIC ROI KPIs](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getDashboardKpis) | `dashboard:read:aic_roi_kpi:admin` |
| [Get AIC ROI KPIs](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getDashboardKpis) | `dashboard:read:aic_roi_kpi:master` |
| [List Zoom meetings client feedback](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardClientFeedback) | `dashboard:read:list_meetings_feedback:admin` |
| [List Zoom meetings client feedback](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardClientFeedback) | `dashboard:read:list_meetings_feedback:master` |
| [Get post webinar feedback](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/participantWebinarFeedback) | `dashboard:read:post_webinar_feedback:admin` |
| [Get post webinar feedback](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/participantWebinarFeedback) | `dashboard:read:post_webinar_feedback:master` |
| [Get meeting quality scores](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardQuality) | `dashboard:read:meeting_quality_score:admin` |
| [Get meeting quality scores](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardQuality) | `dashboard:read:meeting_quality_score:master` |
| [Get CRC port usage](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardCRC) | `dashboard:read:crc_port_usage:admin` |
| [Get CRC port usage](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardCRC) | `dashboard:read:crc_port_usage:master` |
| [List the client versions](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getClientVersions) | `dashboard:read:client_versions:admin` |
| [List the client versions](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getClientVersions) | `dashboard:read:client_versions:master` |
| [List meetings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetings) | `dashboard:read:list_meetings:admin` |
| [List meetings](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetings) | `dashboard:read:list_meetings:master` |
| [Get meeting details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingDetail) | `dashboard:read:meeting:admin` |
| [Get meeting details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingDetail) | `dashboard:read:meeting:master` |
| [Get webinar sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardWebinarParticipantShare) | `dashboard:read:webinar_sharing:admin` |
| [Get webinar sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardWebinarParticipantShare) | `dashboard:read:webinar_sharing:master` |
| [Get chat metrics](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardChat) | `dashboard:read:chat:admin` |
| [Get chat metrics](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardChat) | `dashboard:read:chat:master` |
| [Get meeting sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingParticipantShare) | `dashboard:read:meeting_sharing:admin` |
| [Get meeting sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingParticipantShare) | `dashboard:read:meeting_sharing:master` |
| [Get AIC ROI meeting summary usage](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/dashboardMeetingSummaryUsage) | `dashboard:read:aic_roi_meeting_summary_usage:admin` |
| [Get AIC ROI meeting summary usage](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/dashboardMeetingSummaryUsage) | `dashboard:read:aic_roi_meeting_summary_usage:master` |

### Data Requests [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#data-requests)

| API endpoint | granular scope |
| --- | --- |
| [Get download link for data access request file](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/DownloadfilesfromDataRequest) | `data_request:read:download:admin` |
| [Cancel data deletion request](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/CancelDataRequest) | `data_request:delete:request:admin` |
| [List downloadable files for export data request](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetDownloadableFilesforDataRequest) | `data_request:read:download:admin` |
| [List data request history](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/GetDataRequestsHistory) | `data_request:read:history:admin` |
| [Create data (export/deletion) request](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/CreateDataAccessRequest) | `data_request:write:request:admin` |

### Information Barriers [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#information-barriers)

| API endpoint | granular scope |
| --- | --- |
| [Remove an Information Barrier policy](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/InformationBarriersDelete) | `information_barrier:delete:policy:admin` |
| [Remove an Information Barrier policy](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/InformationBarriersDelete) | `information_barrier:delete:policy:master` |
| [Update an Information Barriers policy](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/InformationBarriersUpdate) | `information_barrier:update:policy:admin` |
| [Update an Information Barriers policy](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/InformationBarriersUpdate) | `information_barrier:update:policy:master` |
| [Get an Information Barrier policy by ID](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/InformationBarriersGet) | `information_barrier:read:policy:admin` |
| [Get an Information Barrier policy by ID](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/InformationBarriersGet) | `information_barrier:read:policy:master` |
| [List information Barrier policies](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/InformationBarriersList) | `information_barrier:read:list_policies:admin` |
| [List information Barrier policies](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/InformationBarriersList) | `information_barrier:read:list_policies:master` |
| [Create an Information Barrier policy](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/InformationBarriersCreate) | `information_barrier:write:policy:admin` |
| [Create an Information Barrier policy](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/InformationBarriersCreate) | `information_barrier:write:policy:master` |

### Roles [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#roles)

| API endpoint | granular scope |
| --- | --- |
| [Unassign a role](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/roleMemberDelete) | `role:delete:member``role:delete:member:admin` |
| [Unassign a role](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/roleMemberDelete) | `role:delete:member:master` |
| [Create a role](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/createRole) | `role:write:role``role:write:role:admin` |
| [Create a role](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/createRole) | `role:write:role:master` |
| [List roles](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/roles) | `role:read:list_roles``role:read:list_roles:admin` |
| [List roles](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/roles) | `role:read:list_roles:master` |
| [Update role information](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateRole) | `role:update:role``role:update:role:admin` |
| [Update role information](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/updateRole) | `role:update:role:master` |
| [Delete a role](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/deleteRole) | `role:delete:role``role:delete:role:admin` |
| [Delete a role](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/deleteRole) | `role:delete:role:master` |
| [Get role information](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getRoleInformation) | `role:read:role``role:read:role:admin` |
| [Get role information](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getRoleInformation) | `role:read:role:master` |
| [List members in a role](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/roleMembers) | `role:read:list_members``role:read:list_members:admin` |
| [List members in a role](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/roleMembers) | `role:read:list_members:master` |
| [Assign a role](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/AddRoleMembers) | `role:write:member``role:write:member:admin` |
| [Assign a role](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/AddRoleMembers) | `role:write:member:master` |

### Single Sign-On [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#single-sign-on)

| API endpoint | granular scope |
| --- | --- |
| [Create an SP certificate](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/createSsoCertificate) | `sso:write:certificate:admin` |
| [Update SSO mapping](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoMappings) | `sso:update:mapping:admin` |
| [List SSO login logs](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/listSsoLoginLogs) | `sso:read:list_login_logs:admin` |
| [List SSO configurations](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/listSsoConfigurations) | `sso:read:config:admin` |
| [List SP certificates](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/listSsoCertificates) | `sso:read:certificate:admin` |
| [Enable or disable account SSO](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoStatus) | `sso:update:status:admin` |
| [Get SSO login log detail](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoLoginLog) | `sso:read:login_log:admin` |
| [Get account SSO capabilities](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoCapabilities) | `sso:read:capabilities:admin` |
| [Delete an SP certificate](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/deleteSsoCertificate) | `sso:delete:certificate:admin` |
| [Update account SSO settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoSettings) | `sso:update:settings:admin` |
| [Update an SP certificate](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoCertificate) | `sso:update:certificate:admin` |
| [Update an SSO configuration](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoConfiguration) | `sso:update:config:admin` |
| [Update an SSO configuration status](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/updateSsoConfigurationStatus) | `sso:update:config_status:admin` |
| [Get SSO mappings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoMappings) | `sso:read:mapping:admin` |
| [Delete an SSO configuration](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/deleteSsoConfiguration) | `sso:delete:config:admin` |
| [Get account SSO settings](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoSettings) | `sso:read:settings:admin` |
| [Get account SSO status](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoStatus) | `sso:read:status:admin` |
| [Create an SSO configuration](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/createSsoConfiguration) | `sso:write:config:admin` |
| [Get an SSO configuration](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSsoConfiguration) | `sso:read:config:admin` |

### Survey Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#survey-management)

| API endpoint | granular scope |
| --- | --- |
| [List channel survey instances](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/Getsurveyinstances) | `survey_management:read:list_survey_instances:admin` |
| [Get survey info](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSurveyInfo) | `survey_management:read:survey:admin` |
| [Get survey info](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getSurveyInfo) | `survey_management:read:survey:master` |
| [Get survey instances](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSurveyInstancesInfo) | `survey_management:read:list_survey_instances:admin` |
| [Get survey instances](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getSurveyInstancesInfo) | `survey_management:read:list_survey_instances:master` |
| [Get survey answers](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getSurveyAnswers) | `survey_management:read:list_survey_answers:admin` |
| [Get survey answers](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getSurveyAnswers) | `survey_management:read:list_survey_answers:master` |
| [Get surveys](https://developers.zoom.us/docs/api/rest/reference/account/methods/#operation/getAccountSurveys) | `survey_management:read:list_surveys:admin` |
| [Get surveys](https://developers.zoom.us/docs/api/rest/reference/account/ma/#operation/getAccountSurveys) | `survey_management:read:list_surveys:master` |

## Zoom Phone [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-phone)

The following are the available **Zoom Phone** APIs and their associated granular scopes.

### Accounts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#accounts-1)

| API endpoint | granular scope |
| --- | --- |
| [Delete phone numbers for an account's customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteOutboundCallerNumbers) | `phone:delete:customized_number:admin` |
| [Delete phone numbers for an account's customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteOutboundCallerNumbers) | `phone:delete:customized_number:master` |
| [Add phone numbers for an account's customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addOutboundCallerNumbers) | `phone:write:customized_number:admin` |
| [Add phone numbers for an account's customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addOutboundCallerNumbers) | `phone:write:customized_number:master` |
| [List an account's Zoom Phone settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listZoomPhoneAccountSettings) | `phone:read:list_account_settings:admin` |
| [List an account's Zoom Phone settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listZoomPhoneAccountSettings) | `phone:read:list_account_settings:master` |
| [List an account's customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCustomizeOutboundCallerNumbers) | `phone:read:list_customized_number:admin` |
| [List an account's customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCustomizeOutboundCallerNumbers) | `phone:read:list_customized_number:master` |

### Alerts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#alerts)

| API endpoint | granular scope |
| --- | --- |
| [Delete an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteAnAlertSetting) | `phone:delete:alert_setting:admin` |
| [Delete an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteAnAlertSetting) | `phone:delete:alert_setting:master` |
| [Get alert setting details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetAlertSettingDetails) | `phone:read:alert_setting:admin` |
| [Get alert setting details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetAlertSettingDetails) | `phone:read:alert_setting:master` |
| [List alert settings with paging query](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListAlertSettingsWithPagingQuery) | `phone:read:list_alert_settings:admin` |
| [List alert settings with paging query](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListAlertSettingsWithPagingQuery) | `phone:read:list_alert_settings:master` |
| [Add an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddAnAlertSetting) | `phone:write:alert_setting:admin` |
| [Add an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddAnAlertSetting) | `phone:write:alert_setting:master` |
| [Update an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAnAlertSetting) | `phone:patch:alert_setting:admin` |
| [Update an alert setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAnAlertSetting) | `phone:patch:alert_setting:master` |

### Audio Library [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#audio-library)

| API endpoint | granular scope |
| --- | --- |
| [Delete an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteAudioItem) | `phone:delete:audio``phone:delete:audio:admin` |
| [Delete an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteAudioItem) | `phone:delete:audio:master` |
| [Add audio items](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddAudioItem) | `phone:write:batch_audios``phone:write:batch_audios:admin` |
| [Add audio items](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddAudioItem) | `phone:write:batch_audios:master` |
| [Update an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAudioItem) | `phone:update:audio``phone:update:audio:admin` |
| [Update an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAudioItem) | `phone:update:audio:master` |
| [Add an audio item for text-to-speech conversion](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddAnAudio) | `phone:write:audio``phone:write:audio:admin` |
| [Add an audio item for text-to-speech conversion](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddAnAudio) | `phone:write:audio:master` |
| [Get an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetAudioItem) | `phone:read:audio``phone:read:audio:admin` |
| [Get an audio item](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetAudioItem) | `phone:read:audio:master` |
| [List audio items](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListAudioItems) | `phone:read:list_audios``phone:read:list_audios:admin` |
| [List audio items](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListAudioItems) | `phone:read:list_audios:master` |

### Auto Receptionists [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#auto-receptionists)

| API endpoint | granular scope |
| --- | --- |
| [Add auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addAutoReceptionistSetting) | `phone:write:auto_receptionist_setting:admin` |
| [Add auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addAutoReceptionistSetting) | `phone:write:auto_receptionist_setting:master` |
| [Update an auto receptionist policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAutoReceptionistPolicy) | `phone:update:auto_receptionist_policy:admin` |
| [Update an auto receptionist policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAutoReceptionistPolicy) | `phone:update:auto_receptionist_policy:master` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignAllPhoneNumsAutoReceptionist) | `phone:delete:auto_receptionist_number:admin` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignAllPhoneNumsAutoReceptionist) | `phone:delete:auto_receptionist_number:master` |
| [Get auto receptionist settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAutoReceptionistSettings) | `phone:read:auto_receptionist_setting:admin` |
| [Get auto receptionist settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAutoReceptionistSettings) | `phone:read:auto_receptionist_setting:master` |
| [Update auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAutoReceptionistSetting) | `phone:update:auto_receptionist_setting:admin` |
| [Update auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAutoReceptionistSetting) | `phone:update:auto_receptionist_setting:master` |
| [Update an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAutoReceptionist) | `phone:update:auto_receptionist:admin` |
| [Update an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAutoReceptionist) | `phone:update:auto_receptionist:master` |
| [Get auto receptionist call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAutoReceptionistCallHandlingSettings) | `phone:read:auto_receptionist_call_handling_setting:admin` |
| [Get auto receptionist call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAutoReceptionistCallHandlingSettings) | `phone:read:auto_receptionist_call_handling_setting:master` |
| [Add a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddPolicy) | `phone:write:auto_receptionist_policy:admin` |
| [Add a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddPolicy) | `phone:write:auto_receptionist_policy:master` |
| [Delete auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAutoReceptionistSetting) | `phone:delete:auto_receptionist_setting:admin` |
| [Delete auto receptionist setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAutoReceptionistSetting) | `phone:delete:auto_receptionist_setting:master` |
| [Update auto receptionist call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAutoReceptionistCallHandlingSettings) | `phone:update:auto_receptionist_call_handling_setting:admin` |
| [Update auto receptionist call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAutoReceptionistCallHandlingSettings) | `phone:update:auto_receptionist_call_handling_setting:master` |
| [Update a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updatePolicy) | `phone:update:auto_receptionist_policy:admin` |
| [Update a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updatePolicy) | `phone:update:auto_receptionist_policy:master` |
| [Delete a non-primary auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAutoReceptionist) | `phone:delete:auto_receptionist:admin` |
| [Delete a non-primary auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAutoReceptionist) | `phone:delete:auto_receptionist:master` |
| [Get an auto receptionist policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAutoReceptionistsPolicy) | `phone:read:auto_receptionist_policy:admin` |
| [Get an auto receptionist policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAutoReceptionistsPolicy) | `phone:read:auto_receptionist_policy:master` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignAPhoneNumAutoReceptionist) | `phone:delete:auto_receptionist_number:admin` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignAPhoneNumAutoReceptionist) | `phone:delete:auto_receptionist_number:master` |
| [Get an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAutoReceptionistDetail) | `phone:read:auto_receptionist:admin` |
| [Get an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAutoReceptionistDetail) | `phone:read:auto_receptionist:master` |
| [List auto receptionists](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAutoReceptionists) | `phone:read:list_auto_receptionists:admin` |
| [List auto receptionists](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAutoReceptionists) | `phone:read:list_auto_receptionists:master` |
| [Add an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addAutoReceptionist) | `phone:write:auto_receptionist:admin` |
| [Add an auto receptionist](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addAutoReceptionist) | `phone:write:auto_receptionist:master` |
| [Delete a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeletePolicy) | `phone:delete:auto_receptionist_policy:admin` |
| [Delete a policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeletePolicy) | `phone:delete:auto_receptionist_policy:master` |
| [Assign phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumbersAutoReceptionist) | `phone:write:auto_receptionist_number:admin` |
| [Assign phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumbersAutoReceptionist) | `phone:write:auto_receptionist_number:master` |

### Billing Account [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#billing-account)

| API endpoint | granular scope |
| --- | --- |
| [Get billing account details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetABillingAccount) | `phone:read:billing_account:admin` |
| [Get billing account details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetABillingAccount) | `phone:read:billing_account:master` |
| [List billing accounts](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listBillingAccount) | `phone:read:list_billing_accounts:admin` |
| [List billing accounts](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listBillingAccount) | `phone:read:list_billing_accounts:master` |

### Blocked List [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#blocked-list)

| API endpoint | granular scope |
| --- | --- |
| [Update a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateBlockedList) | `phone:update:blocked_list:admin` |
| [Update a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateBlockedList) | `phone:update:blocked_list:master` |
| [List blocked lists](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listBlockedList) | `phone:read:list_blocked_lists:admin` |
| [List blocked lists](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listBlockedList) | `phone:read:list_blocked_lists:master` |
| [Create a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addAnumberToBlockedList) | `phone:write:blocked_list:admin` |
| [Create a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addAnumberToBlockedList) | `phone:write:blocked_list:master` |
| [Get blocked list details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getABlockedList) | `phone:read:blocked_list:admin` |
| [Get blocked list details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getABlockedList) | `phone:read:blocked_list:master` |
| [Delete a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteABlockedList) | `phone:delete:blocked_list:admin` |
| [Delete a blocked list](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteABlockedList) | `phone:delete:blocked_list:master` |

### Call Handling [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-handling)

| API endpoint | granular scope |
| --- | --- |
| [Update a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallHandling) | `phone:update:call_handling_setting:admin` |
| [Update a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCallHandling) | `phone:update:call_handling_setting:master` |
| [Add a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addCallHandling) | `phone:write:call_handling_setting:admin` |
| [Add a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addCallHandling) | `phone:write:call_handling_setting:master` |
| [Get call handling settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallHandling) | `phone:read:list_call_handling_settings:admin` |
| [Get call handling settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallHandling) | `phone:read:list_call_handling_settings:master` |
| [Delete a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCallHandling) | `phone:delete:call_handling_setting:admin` |
| [Delete a call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCallHandling) | `phone:delete:call_handling_setting:master` |

### Call Logs [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-logs)

| API endpoint | granular scope |
| --- | --- |
| [Get call log details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallLogDetails) | `phone:read:call_log:admin` |
| [Get call log details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallLogDetails) | `phone:read:call_log:master` |
| [Add a client code to a call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addClientCodeToCallHistory) | `phone:update:call_log:admin` |
| [Add a client code to a call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addClientCodeToCallHistory) | `phone:update:call_log:master` |
| [Get call element](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallElement) | `phone:read:call_log:admin` |
| [Get call element](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallElement) | `phone:read:call_log:master` |
| [Get call history detail](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallHistoryDetail) | `phone:read:call_log:admin` |
| [Get call history detail](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallHistoryDetail) | `phone:read:call_log:master` |
| [Delete a user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserCallHistory) | `phone:delete:call_log``phone:delete:call_log:admin` |
| [Delete a user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserCallHistory) | `phone:delete:call_log:master` |
| [Delete a user's call log](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCallLog) | `phone:delete:call_log``phone:delete:call_log:admin` |
| [Delete a user's call log](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCallLog) | `phone:delete:call_log:master` |
| [Get User AI Call Summary Detail](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getUserAICallSummary) | `phone:read:ai_call_summary``phone:read:ai_call_summary:admin` |
| [Get User AI Call Summary Detail](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getUserAICallSummary) | `phone:read:ai_call_summary:master` |
| [Get user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUserCallHistory) | `phone:read:list_call_logs:admin``phone:read:list_call_logs` |
| [Get user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUserCallHistory) | `phone:read:list_call_logs:master` |
| [Get account's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/accountCallLogs) | `phone:read:list_call_logs:admin` |
| [Get account's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/accountCallLogs) | `phone:read:list_call_logs:master` |
| [Get account's call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/accountCallHistory) | `phone:read:list_call_logs:admin` |
| [Get account's call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/accountCallHistory) | `phone:read:list_call_logs:master` |
| [Get call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallPath) | `phone:read:call_log:admin` |
| [Get call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallPath) | `phone:read:call_log:master` |
| [Sync user's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/syncUserCallLogs) | `phone:read:list_call_logs``phone:read:list_call_logs:admin` |
| [Sync user's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/syncUserCallLogs) | `phone:read:list_call_logs:master` |
| [Get user's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUserCallLogs) | `phone:read:list_call_logs``phone:read:list_call_logs:admin` |
| [Get user's call logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUserCallLogs) | `phone:read:list_call_logs:master` |
| [Sync user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/syncUserCallHistory) | `phone:read:list_call_logs``phone:read:list_call_logs:admin` |
| [Sync user's call history](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/syncUserCallHistory) | `phone:read:list_call_logs:master` |
| [Add a client code to a call log](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addClientCodeToCallLog) | `phone:update:call_log:admin` |
| [Add a client code to a call log](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addClientCodeToCallLog) | `phone:update:call_log:master` |

### Call Queues [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-queues)

| API endpoint | granular scope |
| --- | --- |
| [Update call queue details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallQueue) | `phone:update:call_queue:admin` |
| [Update a call queue's policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCQPolicySubSetting) | `phone:update:call_queue_policy:admin` |
| [Update a call queue's policy subsetting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCQPolicySubSetting) | `phone:update:call_queue_policy:master` |
| [List call queues](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCallQueues) | `phone:read:list_call_queues:admin` |
| [List call queues](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCallQueues) | `phone:read:list_call_queues:master` |
| [Get call queue recordings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallQueueRecordings) | `phone:read:list_call_queue_recordings:admin` |
| [Get call queue recordings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallQueueRecordings) | `phone:read:list_call_queue_recordings:master` |
| [List call queue members](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCallQueueMembers) | `phone:read:list_call_queue_members:admin` |
| [List call queue members](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCallQueueMembers) | `phone:read:list_call_queue_members:master` |
| [Get call queue policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallQueuePolicy) | `phone:read:call_queue_policy:admin` |
| [Update call queue policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallQueuePolicy) | `phone:update:call_queue_policy:admin` |
| [Add members to a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Addmemberstoacustomgroup) | `phone:write:call_queue_custom_group_member:admin` |
| [Unassign all members](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignAllMembers) | `phone:delete:call_queue_member:admin` |
| [Unassign all members](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignAllMembers) | `phone:delete:call_queue_member:master` |
| [Get call queue custom group detail](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Getacustomgroup) | `phone:read:call_queue_custom_group:admin``phone:read:call_queue_custom_group:master` |
| [Get call queue details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getACallQueue) | `phone:read:call_queue:admin` |
| [Get call queue details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getACallQueue) | `phone:read:call_queue:master` |
| [Add a policy subsetting to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addCQPolicySubSetting) | `phone:write:call_queue_policy:admin` |
| [Add a policy subsetting to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addCQPolicySubSetting) | `phone:write:call_queue_policy:master` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unAssignPhoneNumCallQueue) | `phone:delete:call_queue_number:admin` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unAssignPhoneNumCallQueue) | `phone:delete:call_queue_number:master` |
| [Add call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addCallQueueSetting) | `phone:write:call_queue_setting:admin` |
| [Add call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addCallQueueSetting) | `phone:write:call_queue_setting:master` |
| [Remove a member from a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Removeamemberfromacustomgroup) | `phone:delete:call_queue_custom_group_member:admin` |
| [Remove a member from a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Removeamemberfromacustomgroup) | `phone:delete:call_queue_custom_group_member:master` |
| [Create a custom group in a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Createacustomgroupinacallqueue) | `phone:write:call_queue_custom_group:admin` |
| [Create a custom group in a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Createacustomgroupinacallqueue) | `phone:write:call_queue_custom_group:master` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignAPhoneNumCallQueue) | `phone:delete:call_queue_number:admin` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignAPhoneNumCallQueue) | `phone:delete:call_queue_number:master` |
| [Delete a CQ policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeCQPolicySubSetting) | `phone:delete:call_queue_policy:admin` |
| [Delete a CQ policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeCQPolicySubSetting) | `phone:delete:call_queue_policy:master` |
| [Create a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createCallQueue) | `phone:write:call_queue:admin` |
| [Create a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createCallQueue) | `phone:write:call_queue:master` |
| [Update call queue call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallQueueCallHandlingSetting) | `phone:update:call_queue_call_handling_setting:admin` |
| [Update call queue call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCallQueueCallHandlingSetting) | `phone:update:call_queue_call_handling_setting:master` |
| [Update call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallQueueSetting) | `phone:update:call_queue_setting:admin` |
| [Update call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCallQueueSetting) | `phone:update:call_queue_setting:master` |
| [Assign numbers to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneToCallQueue) | `phone:write:call_queue_number:admin` |
| [Assign numbers to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneToCallQueue) | `phone:write:call_queue_number:master` |
| [Get call queue settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallQueueSettings) | `phone:read:call_queue_setting:admin` |
| [Get call queue settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallQueueSettings) | `phone:read:call_queue_setting:master` |
| [Unassign a member](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignMemberFromCallQueue) | `phone:delete:call_queue_member:admin` |
| [Unassign a member](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignMemberFromCallQueue) | `phone:delete:call_queue_member:master` |
| [List call queue analytics](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/callqueueanalytics) | `phone:read:list_call_queues:admin` |
| [List call queue analytics](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/callqueueanalytics) | `phone:read:list_call_queues:master` |
| [Add members to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addMembersToCallQueue) | `phone:write:call_queue_member:admin` |
| [Add members to a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addMembersToCallQueue) | `phone:write:call_queue_member:master` |
| [Delete a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteACallQueue) | `phone:delete:call_queue:admin` |
| [Delete a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteACallQueue) | `phone:delete:call_queue:master` |
| [Update a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Updateacustomgroup) | `phone:update:call_queue_custom_group:admin` |
| [Update a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Updateacustomgroup) | `phone:update:call_queue_custom_group:master` |
| [Get call queue call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallQueueCallHandlingSetting) | `phone:read:call_queue_call_handling_setting:admin` |
| [Get call queue call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallQueueCallHandlingSetting) | `phone:read:call_queue_call_handling_setting:master` |
| [Delete call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCallQueueSetting) | `phone:delete:call_queue_setting:admin` |
| [Delete call queue setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCallQueueSetting) | `phone:delete:call_queue_setting:master` |
| [List custom groups of a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Listcustomgroupsofacallqueue) | `phone:read:call_queue_custom_group:admin` |
| [List custom groups of a call queue](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Listcustomgroupsofacallqueue) | `phone:read:call_queue_custom_group:master` |
| [Delete a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Deleteacustomgroup) | `phone:delete:call_queue_custom_group:admin``phone:delete:call_queue_custom_group:master` |
| [Delete a custom group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Deleteacustomgroup) | `phone:delete:call_queue_custom_group:master` |

### Carrier Reseller [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#carrier-reseller)

| API endpoint | granular scope |
| --- | --- |
| [List phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCRPhoneNumbers) | `phone:read:list_carrier_numbers:admin` |
| [List phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCRPhoneNumbers) | `phone:read:list_carrier_numbers:master` |
| [Activate phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/activeCRPhoneNumbers) | `phone:update:carrier_number:admin` |
| [Activate phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/activeCRPhoneNumbers) | `phone:update:carrier_number:master` |
| [Delete a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCRPhoneNumber) | `phone:delete:carrier_number:admin` |
| [Delete a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCRPhoneNumber) | `phone:delete:carrier_number:master` |
| [Create phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createCRPhoneNumbers) | `phone:write:carrier_number:admin` |
| [Create phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createCRPhoneNumbers) | `phone:write:carrier_number:master``phone:write:carrier_number:master` |

### Common Areas [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#common-areas)

| API endpoint | granular scope |
| --- | --- |
| [Get common area settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCommonAreaSettings) | `phone:read:list_common_area_settings:admin` |
| [Get common area settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCommonAreaSettings) | `phone:read:list_common_area_settings:master` |
| [Assign calling plans to a common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignCallingPlansToCommonArea) | `phone:write:common_area_calling_plan:admin` |
| [Assign calling plans to a common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignCallingPlansToCommonArea) | `phone:write:common_area_calling_plan:master` |
| [Add a common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addCommonArea) | `phone:write:common_area:admin` |
| [Add a common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addCommonArea) | `phone:write:common_area:master` |
| [Update common area call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCommonAreaCallHandlingSetting) | `phone:update:common_area_call_handling_setting:admin` |
| [Update common area call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCommonAreaCallHandlingSetting) | `phone:update:common_area_call_handling_setting:master` |
| [Update common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateCommonAreaSetting) | `phone:update:common_area_setting:admin` |
| [Update common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateCommonAreaSetting) | `phone:update:common_area_setting:master` |
| [Apply template to common areas](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ApplyTemplatetoCommonAreas) | `phone:write:apply_template_to_common_areas:admin` |
| [Apply template to common areas](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ApplyTemplatetoCommonAreas) | `phone:write:apply_template_to_common_areas:master` |
| [Delete a common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCommonArea) | `phone:delete:common_area:admin` |
| [Delete a common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCommonArea) | `phone:delete:common_area:master` |
| [Get common area details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getACommonArea) | `phone:read:common_area:admin` |
| [Get common area details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getACommonArea) | `phone:read:common_area:master` |
| [Delete common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCommonAreaSetting) | `phone:delete:common_area_setting:admin` |
| [Delete common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCommonAreaSetting) | `phone:delete:common_area_setting:master` |
| [Get common area call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCommonAreaCallHandlingSetting) | `phone:read:common_area_call_handling_setting:admin` |
| [Get common area call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCommonAreaCallHandlingSetting) | `phone:read:common_area_call_handling_setting:master` |
| [Add common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddCommonAreaSetting) | `phone:write:common_area_setting:admin` |
| [Add common area setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddCommonAreaSetting) | `phone:write:common_area_setting:master` |
| [Unassign a calling plan from the common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignCallingPlansFromCommonArea) | `phone:delete:common_area_calling_plan:admin` |
| [Unassign a calling plan from the common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignCallingPlansFromCommonArea) | `phone:delete:common_area_calling_plan:master` |
| [Assign phone numbers to a common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumbersToCommonArea) | `phone:write:common_area_number:admin` |
| [Assign phone numbers to a common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumbersToCommonArea) | `phone:write:common_area_number:master` |
| [Update common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCommonArea) | `phone:update:common_area:admin` |
| [Update common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCommonArea) | `phone:update:common_area:master` |
| [List activation codes](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listActivationCodes) | `phone:read:list_common_area_activation_codes:admin` |
| [List activation codes](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listActivationCodes) | `phone:read:list_common_area_activation_codes:master` |
| [List common areas](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCommonAreas) | `phone:read:common_area:admin` |
| [List common areas](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCommonAreas) | `phone:read:common_area:master` |
| [Generate activation codes for common areas](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Generateactivationcodesforcommonareas) | `phone:write:common_area:admin` |
| [Generate activation codes for common areas](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Generateactivationcodesforcommonareas) | `phone:write:common_area:master` |
| [Unassign phone numbers from common area](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignPhoneNumbersFromCommonArea) | `phone:delete:common_area_number:admin` |
| [Unassign phone numbers from common area](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignPhoneNumbersFromCommonArea) | `phone:delete:common_area_number:master` |
| [Update common area pin code](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateCommonAreaPinCode) | `phone:update:common_area:admin` |
| [Update common area pin code](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateCommonAreaPinCode) | `phone:update:common_area:master` |

### Dashboard [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#dashboard)

| API endpoint | granular scope |
| --- | --- |
| [List detectable personal location users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserDetectablePersonalLocation) | `phone:read:detectable_personal_location:admin` |
| [List detectable personal location users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserDetectablePersonalLocation) | `phone:read:detectable_personal_location:master` |
| [List real time location for users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserRealtimeLocation) | `phone:read:realtime_location_users:admin` |
| [List real time location for users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserRealtimeLocation) | `phone:read:realtime_location_users:master` |
| [List real time location for IP phones](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPhoneRealtimelocation) | `phone:read:realtime_location_devices:admin` |
| [List real time location for IP phones](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPhoneRealtimelocation) | `phone:read:realtime_location_devices:master` |
| [List default emergency address users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserDefaultEmergencyAddress) | `phone:read:default_emergency_address:admin` |
| [List default emergency address users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserDefaultEmergencyAddress) | `phone:read:default_emergency_address:master` |
| [List users permission for location sharing](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserLocationSharingPermission) | `phone:read:location_sharing_permission:admin` |
| [List users permission for location sharing](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserLocationSharingPermission) | `phone:read:location_sharing_permission:master` |
| [List nomadic emergency services users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserNomadicEmergencyServices) | `phone:read:nomadic_emergency_services:admin` |
| [List nomadic emergency services users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserNomadicEmergencyServices) | `phone:read:nomadic_emergency_services:master` |
| [Get call QoS](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallQoS) | `phone:read:call_qos:admin` |
| [Get call QoS](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallQoS) | `phone:read:call_qos:master` |
| [Get call details from call log](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getCallLogMetricsDetails) | `phone:read:call_log:admin` |
| [Get call details from call log](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getCallLogMetricsDetails) | `phone:read:call_log:master` |
| [List past call metrics](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPastCallMetrics) | `phone:read:list_call_logs:admin` |
| [List past call metrics](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPastCallMetrics) | `phone:read:list_call_logs:master` |
| [List call logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCallLogsMetrics) | `phone:read:list_call_logs:admin` |
| [List call logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCallLogsMetrics) | `phone:read:list_call_logs:master` |
| [List tracked locations](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listTrackedLocations) | `phone:read:list_tracked_locations:admin` |
| [List tracked locations](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listTrackedLocations) | `phone:read:list_tracked_locations:master` |

### Device Line Keys [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#device-line-keys)

| API endpoint | granular scope |
| --- | --- |
| [Get device line keys information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listDeviceLineKeySetting) | `phone:read:device_line_keys``phone:read:device_line_keys:admin` |
| [Get device line keys information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listDeviceLineKeySetting) | `phone:read:device_line_keys:master` |
| [Batch update device line key position](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/batchUpdateDeviceLineKeySetting) | `phone:update:device_line_keys``phone:update:device_line_keys:admin` |
| [Batch update device line key position](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/batchUpdateDeviceLineKeySetting) | `phone:update:device_line_keys:master` |

### Dial by Name Directory [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#dial-by-name-directory)

| API endpoint | granular scope |
| --- | --- |
| [Delete users from a directory](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteUsersFromDirectory) | `phone:delete:directory:admin` |
| [Delete users from a directory](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteUsersFromDirectory) | `phone:delete:directory:master` |
| [Delete users from a directory of a site](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteUsersFromDirectoryBySite) | `phone:delete:directory:admin` |
| [Delete users from a directory of a site](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteUsersFromDirectoryBySite) | `phone:delete:directory:master` |
| [List users in directory](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListUsersFromDirectory) | `phone:read:directory:admin` |
| [List users in directory](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListUsersFromDirectory) | `phone:read:directory:master` |
| [List users in a directory by site](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListUsersFromDirectoryBySite) | `phone:read:directory:admin` |
| [List users in a directory by site](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListUsersFromDirectoryBySite) | `phone:read:directory:master` |
| [Add users to a directory](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddUsersToDirectory) | `phone:write:directory:admin` |
| [Add users to a directory](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddUsersToDirectory) | `phone:write:directory:master` |
| [Add users to a directory of a site](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddUsersToDirectoryBySite) | `phone:write:directory:admin` |
| [Add users to a directory of a site](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddUsersToDirectoryBySite) | `phone:write:directory:master` |

### Emergency Addresses [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#emergency-addresses)

| API endpoint | granular scope |
| --- | --- |
| [Delete an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteEmergencyAddress) | `phone:delete:emergency_address:admin` |
| [Delete an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteEmergencyAddress) | `phone:delete:emergency_address:master` |
| [Get emergency address details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getEmergencyAddress) | `phone:read:emergency_address:admin` |
| [Get emergency address details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getEmergencyAddress) | `phone:read:emergency_address:master` |
| [Update an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateEmergencyAddress) | `phone:update:emergency_address:admin` |
| [Update an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateEmergencyAddress) | `phone:update:emergency_address:master` |
| [List emergency addresses](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listEmergencyAddresses) | `phone:read:list_emergency_addresses:admin` |
| [List emergency addresses](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listEmergencyAddresses) | `phone:read:list_emergency_addresses:master` |
| [Add an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addEmergencyAddress) | `phone:write:emergency_address:admin` |
| [Add an emergency address](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addEmergencyAddress) | `phone:write:emergency_address:master` |

### Emergency Service Locations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#emergency-service-locations)

| API endpoint | granular scope |
| --- | --- |
| [Delete an emergency location](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteLocation) | `phone:delete:emergency_location:admin` |
| [Delete an emergency location](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteLocation) | `phone:delete:emergency_location:master` |
| [Get emergency service location details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getLocation) | `phone:read:emergency_location:admin` |
| [Get emergency service location details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getLocation) | `phone:read:emergency_location:master` |
| [Update emergency service location](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateLocation) | `phone:update:emergency_location:admin` |
| [Update emergency service location](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateLocation) | `phone:update:emergency_location:master` |
| [List emergency service locations](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listLocations) | `phone:read:list_emergency_locations:admin` |
| [List emergency service locations](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listLocations) | `phone:read:list_emergency_locations:master` |
| [Add an emergency service location](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addLocation) | `phone:write:emergency_location:admin` |
| [Add an emergency service location](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addLocation) | `phone:write:emergency_location:master` |
| [Batch add emergency service locations](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/batchAddLocations) | `phone:write:batch_emergency_locations:admin` |
| [Batch add emergency service locations](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/batchAddLocations) | `phone:write:batch_emergency_locations:master` |

### Emergency Service Routing [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#emergency-service-routing)

| API endpoint | granular scope |
| --- | --- |
| [List an account's emergency routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountEmergencyRoutingRules) | `phone:read:list_emergency_services_routing_rules:admin` |
| [List an account's emergency routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountEmergencyRoutingRules) | `phone:read:list_emergency_services_routing_rules:master` |
| [List a site's emergency routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSiteEmergencyRoutingRules) | `phone:read:list_site_emergency_service_routing_rules:admin` |
| [List a site's emergency routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSiteEmergencyRoutingRules) | `phone:read:list_site_emergency_service_routing_rules:master` |
| [Add an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addAccountEmergencyRoutingRule) | `phone:write:emergency_services_routing_rule:admin` |
| [Add an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addAccountEmergencyRoutingRule) | `phone:write:emergency_services_routing_rule:master` |
| [Add a site's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSiteEmergencyRoutingRule) | `phone:write:site_emergency_service_routing_rule:admin` |
| [Add a site's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSiteEmergencyRoutingRule) | `phone:write:site_emergency_service_routing_rule:master` |
| [Delete an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAccountEmergencyRoutingRule) | `phone:delete:emergency_services_routing_rule:admin` |
| [Delete an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAccountEmergencyRoutingRule) | `phone:delete:emergency_services_routing_rule:master` |
| [Update a site emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSiteEmergencyRoutingRule) | `phone:update:site_emergency_service_routing_rule:admin` |
| [Update a site emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSiteEmergencyRoutingRule) | `phone:update:site_emergency_service_routing_rule:master` |
| [Update an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAccountEmergencyRoutingRule) | `phone:update:emergency_services_routing_rule:admin` |
| [Update an account's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAccountEmergencyRoutingRule) | `phone:update:emergency_services_routing_rule:master` |
| [Delete a site's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteSiteEmergencyRoutingRule) | `phone:delete:site_emergency_service_routing_rule:admin` |
| [Delete a site's emergency routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteSiteEmergencyRoutingRule) | `phone:delete:site_emergency_service_routing_rule:master` |

### Emergency Services [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#emergency-services)

| API endpoint | granular scope |
| --- | --- |
| [Update emergency service settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateEmergencyServiceSettings) | `phone:update:emergency_service_setting:admin` |
| [Update emergency service settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateEmergencyServiceSettings) | `phone:update:emergency_service_setting:master` |
| [Get emergency service settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getEmergencyServiceSettings) | `phone:read:emergency_service_setting:admin` |
| [Get emergency service settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getEmergencyServiceSettings) | `phone:read:emergency_service_setting:master` |

### External Contacts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#external-contacts)

| API endpoint | granular scope |
| --- | --- |
| [Update external contact](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateExternalContact) | `phone:update:external_contact:admin` |
| [Update external contact](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateExternalContact) | `phone:update:external_contact:master` |
| [List external contacts](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listExternalContacts) | `phone:read:list_external_contacts:admin` |
| [List external contacts](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listExternalContacts) | `phone:read:list_external_contacts:master` |
| [Delete an external contact](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAExternalContact) | `phone:delete:external_contact:admin` |
| [Delete an external contact](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAExternalContact) | `phone:delete:external_contact:master` |
| [Get external contact details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAExternalContact) | `phone:read:external_contact:admin` |
| [Get external contact details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAExternalContact) | `phone:read:external_contact:master` |
| [Add an external contact](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addExternalContact) | `phone:write:external_contact:admin` |
| [Add an external contact](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addExternalContact) | `phone:write:external_contact:master` |

### Fax [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#fax)

| API endpoint | granular scope |
| --- | --- |
| [Get fax log details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetFaxLogDetails) | `phone:read:list_fax_log:admin` |
| [Get fax log details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetFaxLogDetails) | `phone:read:list_fax_log:master` |
| [Download fax cover page preview image](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DownloadFaxCoverPreviewImage) | `phone:read:fax_cover_page``phone:read:fax_cover_page:admin` |
| [Download fax cover page preview image](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DownloadFaxCoverPreviewImage) | `phone:read:fax_cover_page:master` |
| [Download fax file](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Downloadfaxfile) | `phone:read:fax_log``phone:read:fax_log:admin` |
| [Download fax file](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Downloadfaxfile) | `phone:read:fax_log:master` |
| [Get account's fax logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetAccount'sFaxLogs) | `phone:read:list_fax_log:admin` |
| [Get account's fax logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetAccount'sFaxLogs) | `phone:read:list_fax_log:master` |
| [Delete fax log](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteFaxLog) | `phone:delete:fax_log``phone:delete:fax_log:admin` |
| [Upload fax file](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UploadFaxFiles) | `phone:write:send_fax``phone:write:send_fax:admin` |
| [Upload fax file](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UploadFaxFiles) | `phone:write:send_fax:master` |
| [Send fax](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/SendEFax) | `phone:write:send_fax``phone:write:send_fax:admin` |
| [Send fax](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/SendEFax) | `phone:write:send_fax:master` |
| [Get fax cover pages](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListFaxCovers) | `phone:read:fax_cover_page``phone:read:fax_cover_page:admin` |
| [Get fax cover pages](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListFaxCovers) | `phone:read:fax_cover_page:master` |
| [Get extension's fax logs](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Getuser'sfaxlogs) | `phone:read:list_fax_log``phone:read:list_fax_log:admin` |
| [Get extension's fax logs](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Getuser'sfaxlogs) | `phone:read:list_fax_log:master` |
| [Update fax log read status](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateFaxLogReadStatus) | `phone:read:fax_log:admin``phone:read:fax_log` |
| [Update fax log read status](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateFaxLogReadStatus) | `phone:read:fax_log:master` |

### Firmware Update Rules [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#firmware-update-rules)

| API endpoint | granular scope |
| --- | --- |
| [Get firmware update rule information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetFirmwareRuleDetail) | `phone:read:firmware_update_rule:admin` |
| [Get firmware update rule information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetFirmwareRuleDetail) | `phone:read:firmware_update_rule:master` |
| [Delete firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteFirmwareUpdateRule) | `phone:delete:firmware_update_rule:admin` |
| [Delete firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteFirmwareUpdateRule) | `phone:delete:firmware_update_rule:master` |
| [List firmware update rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListFirmwareRules) | `phone:read:list_firmware_update_rules:admin` |
| [List firmware update rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListFirmwareRules) | `phone:read:list_firmware_update_rules:master` |
| [Update firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateFirmwareRule) | `phone:update:firmware_update_rule:admin` |
| [Update firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateFirmwareRule) | `phone:update:firmware_update_rule:master` |
| [Add a firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddFirmwareRule) | `phone:write:firmware_update_rule:admin` |
| [Add a firmware update rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddFirmwareRule) | `phone:write:firmware_update_rule:master` |
| [List updatable firmwares](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListFirmwares) | `phone:read:list_firmwares:admin` |
| [List updatable firmwares](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListFirmwares) | `phone:read:list_firmwares:master` |

### Group Call Pickup [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#group-call-pickup)

| API endpoint | granular scope |
| --- | --- |
| [Update the group call pickup information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateGCP) | `phone:update:call_pickup_group:admin` |
| [Update the group call pickup information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateGCP) | `phone:update:call_pickup_group:master` |
| [List call pickup group members](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listGCPMembers) | `phone:read:call_pickup_group_member:admin` |
| [List call pickup group members](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listGCPMembers) | `phone:read:call_pickup_group_member:master` |
| [Add a group call pickup object](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addGCP) | `phone:write:call_pickup_group:admin` |
| [Add a group call pickup object](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addGCP) | `phone:write:call_pickup_group:master` |
| [Delete group call pickup objects](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteGCP) | `phone:delete:call_pickup_group:admin` |
| [Delete group call pickup objects](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteGCP) | `phone:delete:call_pickup_group:master` |
| [Get call pickup group by ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetGCP) | `phone:read:call_pickup_group:admin` |
| [Get call pickup group by ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetGCP) | `phone:read:call_pickup_group:master` |
| [List group call pickup objects](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listGCP) | `phone:read:list_call_pickup_groups:admin` |
| [List group call pickup objects](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listGCP) | `phone:read:list_call_pickup_groups:master` |
| [Add members to a call pickup group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addGCPMembers) | `phone:write:call_pickup_group_member:admin` |
| [Add members to a call pickup group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addGCPMembers) | `phone:write:call_pickup_group_member:master` |
| [Remove members from call pickup group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeGCPMembers) | `phone:delete:call_pickup_group_member:admin` |
| [Remove members from call pickup group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeGCPMembers) | `phone:delete:call_pickup_group_member:master` |

### Groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#groups)

| API endpoint | granular scope |
| --- | --- |
| [Get group phone settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getGroupPhoneSettings) | `phone:read:group_setting:admin` |
| [Get group phone settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getGroupPhoneSettings) | `phone:read:group_setting:master` |
| [Get group policy details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetGroupPolicyDetails) | `phone:read:group_policy:admin` |
| [Get group policy details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetGroupPolicyDetails) | `phone:read:group_policy:master` |
| [Update group policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateGroupPolicy) | `phone:update:group_policy:admin` |
| [Update group policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateGroupPolicy) | `phone:update:group_policy:master` |

### IVR [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#ivr)

| API endpoint | granular scope |
| --- | --- |
| [Update auto receptionist IVR](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAutoReceptionistIVR) | `phone:update:auto_receptionist_ivr:admin` |
| [Update auto receptionist IVR](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAutoReceptionistIVR) | `phone:update:auto_receptionist_ivr:master` |
| [Get auto receptionist IVR](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getAutoReceptionistIVR) | `phone:read:auto_receptionist_ivr:admin` |
| [Get auto receptionist IVR](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getAutoReceptionistIVR) | `phone:read:auto_receptionist_ivr:master` |

### Inbound Blocked List [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#inbound-blocked-list)

| API endpoint | granular scope |
| --- | --- |
| [Delete an extension's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteExtensiontLevelInboundBlockRules) | `phone:delete:extension_inbound_block_rule:admin``phone:delete:extension_inbound_block_rule` |
| [Delete an extension's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteExtensiontLevelInboundBlockRules) | `phone:delete:extension_inbound_block_rule:master` |
| [Delete an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteAccountLevelInboundBlockRules) | `phone:delete:inbound_block_rule:admin` |
| [Delete an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteAccountLevelInboundBlockRules) | `phone:delete:inbound_block_rule:master` |
| [Add an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddAccountLevelInboundBlockRules) | `phone:write:inbound_block_rule:admin` |
| [Add an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddAccountLevelInboundBlockRules) | `phone:write:inbound_block_rule:master` |
| [Mark a phone number as blocked for all extensions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/MarkPhoneNumberAsBlockedForAllExtensions) | `phone:update:inbound_blocked_for_all:admin` |
| [Mark a phone number as blocked for all extensions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/MarkPhoneNumberAsBlockedForAllExtensions) | `phone:update:inbound_blocked_for_all:master` |
| [Add an extension's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddExtensiontLevelInboundBlockRules) | `phone:write:extension_inbound_block_rule:admin``phone:write:extension_inbound_block_rule` |
| [Add an extension's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddExtensiontLevelInboundBlockRules) | `phone:write:extension_inbound_block_rule:master` |
| [Update an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAccountLevelInboundBlockRule) | `phone:update:inbound_block_rule:admin` |
| [Update an account's inbound block rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAccountLevelInboundBlockRule) | `phone:update:inbound_block_rule:master` |
| [List an account's inbound block rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListAccountLevelInboundBlockRules) | `phone:read:list_inbound_block_rules:admin` |
| [List an account's inbound block rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListAccountLevelInboundBlockRules) | `phone:read:list_inbound_block_rules:master` |
| [List an extension's inbound block rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListExtensionLevelInboundBlockRules) | `phone:read:list_extension_inbound_block_rules:admin``phone:read:list_extension_inbound_block_rules` |
| [List an extension's inbound block rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListExtensionLevelInboundBlockRules) | `phone:read:list_extension_inbound_block_rules:master` |
| [Delete an account's inbound blocked statistics](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteAccountLevelInboundBlockedStatistics) | `phone:delete:extension_inbound_block_rule_stat:admin` |
| [Delete an account's inbound blocked statistics](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteAccountLevelInboundBlockedStatistics) | `phone:delete:extension_inbound_block_rule_stat:master` |
| [List an account's inbound blocked statistics](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListAccountLevelInboundBlockedStatistics) | `phone:read:list_extension_inbound_block_rules_stat:admin` |
| [List an account's inbound blocked statistics](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListAccountLevelInboundBlockedStatistics) | `phone:read:list_extension_inbound_block_rules_stat:master` |

### Line Keys [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#line-keys)

| API endpoint | granular scope |
| --- | --- |
| [Get line key position and settings information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listLineKeySetting) | `phone:read:line_keys``phone:read:line_keys:admin` |
| [Get line key position and settings information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listLineKeySetting) | `phone:read:line_keys:master` |
| [Delete a line key setting.](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeleteLineKey) | `phone:delete:line_keys``phone:delete:line_keys:admin` |
| [Delete a line key setting.](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeleteLineKey) | `phone:delete:line_keys:master` |
| [Batch update line key position and settings information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/BatchUpdateLineKeySetting) | `phone:update:line_keys``phone:update:line_keys:admin` |
| [Batch update line key position and settings information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/BatchUpdateLineKeySetting) | `phone:update:line_keys:master` |

### Monitoring Groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#monitoring-groups)

| API endpoint | granular scope |
| --- | --- |
| [Remove all monitors or monitored members from a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeMembers) | `phone:delete:monitoring_group_member:admin` |
| [Remove all monitors or monitored members from a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeMembers) | `phone:delete:monitoring_group_member:master` |
| [Get a list of monitoring groups on an account](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listMonitoringGroup) | `phone:read:list_monitoring_groups:admin` |
| [Get a list of monitoring groups on an account](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listMonitoringGroup) | `phone:read:list_monitoring_groups:master` |
| [Get members of a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listMembers) | `phone:read:list_monitoring_group_members:admin` |
| [Get members of a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listMembers) | `phone:read:list_monitoring_group_members:master` |
| [Add members to a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addMembers) | `phone:write:monitoring_group_member:admin` |
| [Add members to a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addMembers) | `phone:write:monitoring_group_member:master` |
| [Delete a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteMonitoringGroup) | `phone:delete:monitoring_group:admin` |
| [Delete a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteMonitoringGroup) | `phone:delete:monitoring_group:master` |
| [Create a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createMonitoringGroup) | `phone:write:monitoring_group:admin` |
| [Create a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createMonitoringGroup) | `phone:write:monitoring_group:master` |
| [Remove a member from a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeMember) | `phone:delete:monitoring_group_member:admin` |
| [Remove a member from a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeMember) | `phone:delete:monitoring_group_member:master` |
| [Get monitoring group by ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getMonitoringGroupById) | `phone:read:monitoring_group:admin` |
| [Get monitoring group by ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getMonitoringGroupById) | `phone:read:monitoring_group:master` |
| [Update a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateMonitoringGroup) | `phone:update:monitoring_group:admin` |
| [Update a monitoring group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateMonitoringGroup) | `phone:update:monitoring_group:master` |

### Outbound Calling [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#outbound-calling)

| API endpoint | granular scope |
| --- | --- |
| [Add common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddCommonAreaOutboundCallingExceptionRule) | `phone:write:common_area_outbound_calling_rule:admin` |
| [Add common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddCommonAreaOutboundCallingExceptionRule) | `phone:write:common_area_outbound_calling_rule:master` |
| [Get site level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetSiteOutboundCallingCountriesAndRegions) | `phone:read:site_outbound_calling_rule:admin` |
| [Get site level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetSiteOutboundCallingCountriesAndRegions) | `phone:read:site_outbound_calling_rule:master` |
| [Get account level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetAccountOutboundCallingCountriesAndRegions) | `phone:read:list_outbound_calling_rules:admin` |
| [Get account level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetAccountOutboundCallingCountriesAndRegions) | `phone:read:list_outbound_calling_rules:master` |
| [Update user level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateUserOutboundCallingCountriesOrRegions) | `phone:update:user_outbound_calling_rule:admin` |
| [Update user level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateUserOutboundCallingCountriesOrRegions) | `phone:update:user_outbound_calling_rule:master` |
| [Add user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddUserOutboundCallingExceptionRule) | `phone:write:user_outbound_calling_rule:admin` |
| [Add user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddUserOutboundCallingExceptionRule) | `phone:write:user_outbound_calling_rule:master` |
| [Delete site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteSiteOutboundCallingExceptionRule) | `phone:delete:site_outbound_calling_rule:admin` |
| [Delete site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteSiteOutboundCallingExceptionRule) | `phone:delete:site_outbound_calling_rule:master` |
| [Update site level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateSiteOutboundCallingCountriesOrRegions) | `phone:update:site_outbound_calling_rule:admin` |
| [Update site level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateSiteOutboundCallingCountriesOrRegions) | `phone:update:site_outbound_calling_rule:master` |
| [Delete account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAccountOutboundCallingExceptionRule) | `phone:delete:outbound_calling_rule:admin` |
| [Delete account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAccountOutboundCallingExceptionRule) | `phone:delete:outbound_calling_rule:master` |
| [List site level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSiteOutboundCallingExceptionRule) | `phone:read:site_outbound_calling_rule:admin` |
| [List site level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSiteOutboundCallingExceptionRule) | `phone:read:site_outbound_calling_rule:master` |
| [Add site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddSiteOutboundCallingExceptionRule) | `phone:write:site_outbound_calling_rule:admin` |
| [Add site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddSiteOutboundCallingExceptionRule) | `phone:write:site_outbound_calling_rule:master` |
| [Update user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateUserOutboundCallingExceptionRule) | `phone:update:user_outbound_calling_rule:admin` |
| [Update user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateUserOutboundCallingExceptionRule) | `phone:update:user_outbound_calling_rule:master` |
| [Update common area level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateCommonAreaOutboundCallingCountriesOrRegions) | `phone:update:common_area_outbound_calling_rule:admin` |
| [Update common area level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateCommonAreaOutboundCallingCountriesOrRegions) | `phone:update:common_area_outbound_calling_rule:master` |
| [Update account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAccountOutboundCallingExceptionRule) | `phone:update:outbound_calling_rule:admin` |
| [Update account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAccountOutboundCallingExceptionRule) | `phone:update:outbound_calling_rule:master` |
| [Add account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddAccountOutboundCallingExceptionRule) | `phone:write:outbound_calling_rule:admin` |
| [Add account level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddAccountOutboundCallingExceptionRule) | `phone:write:outbound_calling_rule:master` |
| [Update account level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAccountOutboundCallingCountriesOrRegions) | `phone:update:outbound_calling_rule:admin` |
| [Update account level outbound calling countries or regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAccountOutboundCallingCountriesOrRegions) | `phone:update:outbound_calling_rule:master` |
| [Get user level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetUserOutboundCallingCountriesAndRegions) | `phone:read:user_outbound_calling_rule:admin` |
| [Get user level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetUserOutboundCallingCountriesAndRegions) | `phone:read:user_outbound_calling_rule:master` |
| [List account level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountOutboundCallingExceptionRule) | `phone:read:list_outbound_calling_rules:admin` |
| [List account level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountOutboundCallingExceptionRule) | `phone:read:list_outbound_calling_rules:master` |
| [Delete common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCommonAreaOutboundCallingExceptionRule) | `phone:delete:common_area_outbound_calling_rule:admin` |
| [Delete common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCommonAreaOutboundCallingExceptionRule) | `phone:delete:common_area_outbound_calling_rule:master` |
| [List common area level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCommonAreaOutboundCallingExceptionRule) | `phone:read:common_area_outbound_calling_rule:admin` |
| [List common area level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCommonAreaOutboundCallingExceptionRule) | `phone:read:common_area_outbound_calling_rule:master` |
| [Delete user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserOutboundCallingExceptionRule) | `phone:delete:user_outbound_calling_rule:admin` |
| [Delete user level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserOutboundCallingExceptionRule) | `phone:delete:user_outbound_calling_rule:master` |
| [Update common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateCommonAreaOutboundCallingExceptionRule) | `phone:update:common_area_outbound_calling_rule:admin` |
| [Update common area level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateCommonAreaOutboundCallingExceptionRule) | `phone:update:common_area_outbound_calling_rule:master` |
| [Get common area level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetCommonAreaOutboundCallingCountriesAndRegions) | `phone:read:common_area_outbound_calling_rule:admin` |
| [Get common area level outbound calling countries and regions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetCommonAreaOutboundCallingCountriesAndRegions) | `phone:read:common_area_outbound_calling_rule:master` |
| [Update site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateSiteOutboundCallingExceptionRule) | `phone:update:site_outbound_calling_rule:admin` |
| [Update site level outbound calling exception rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateSiteOutboundCallingExceptionRule) | `phone:update:site_outbound_calling_rule:master` |
| [List user level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserOutboundCallingExceptionRule) | `phone:read:user_outbound_calling_rule:admin` |
| [List user level outbound calling exception rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserOutboundCallingExceptionRule) | `phone:read:user_outbound_calling_rule:master` |

### Phone Devices [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-devices)

| API endpoint | granular scope |
| --- | --- |
| [Get device details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getADevice) | `phone:read:device:admin` |
| [Get device details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getADevice) | `phone:read:device:master` |
| [List Smartphones](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListSmartphones) | `phone:read:list_devices:admin` |
| [List Smartphones](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListSmartphones) | `phone:read:list_devices:master` |
| [Assign an entity to a device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addExtensionsToADevice) | `phone:write:device_extension:admin` |
| [Assign an entity to a device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addExtensionsToADevice) | `phone:write:device_extension:master` |
| [Reboot a desk phone](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/rebootPhoneDevice) | `phone:write:reboot_device:admin` |
| [Reboot a desk phone](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/rebootPhoneDevice) | `phone:write:reboot_device:master` |
| [Delete a device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteADevice) | `phone:delete:device:admin` |
| [Delete a device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteADevice) | `phone:delete:device:master` |
| [Update provision template of a device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateProvisionTemplateToDevice) | `phone:update:device_provision_template:admin` |
| [Update provision template of a device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateProvisionTemplateToDevice) | `phone:update:device_provision_template:master` |
| [Add a device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addPhoneDevice) | `phone:write:device:admin` |
| [Add a device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addPhoneDevice) | `phone:write:device:master` |
| [Sync deskphones](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/syncPhoneDevice) | `phone:write:sync_device:admin` |
| [Sync deskphones](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/syncPhoneDevice) | `phone:write:sync_device:master` |
| [Update a device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateADevice) | `phone:update:device:admin` |
| [Update a device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateADevice) | `phone:update:device:master` |
| [Unassign an entity from the device](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteExtensionFromADevice) | `phone:delete:device_extension:admin` |
| [Unassign an entity from the device](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteExtensionFromADevice) | `phone:delete:device_extension:master` |
| [List devices](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPhoneDevices) | `phone:read:list_devices:admin` |
| [List devices](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPhoneDevices) | `phone:read:list_devices:master` |

### Phone Numbers [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-numbers)

| API endpoint | granular scope |
| --- | --- |
| [List site emergency number pool phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSiteEmergencyNumberPoolNumbers) | `phone:read:list_sites_emergency_numbers:admin` |
| [List site emergency number pool phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSiteEmergencyNumberPoolNumbers) | `phone:read:list_sites_emergency_numbers:master` |
| [Unassign phone numbers from the emergency number pool](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignPhoneNumberFromEmergencyNumberPool) | `phone:delete:emergency_number:admin` |
| [Unassign phone numbers from the emergency number pool](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignPhoneNumberFromEmergencyNumberPool) | `phone:delete:emergency_number:master` |
| [Update a site's unassigned phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSiteForUnassignedPhoneNumbers) | `phone:update:site_number:admin` |
| [Update a site's unassigned phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSiteForUnassignedPhoneNumbers) | `phone:update:site_number:master` |
| [Assign a phone number to a user](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumber) | `phone:write:user_number``phone:write:user_number:admin` |
| [Assign a phone number to a user](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumber) | `phone:write:user_number:master` |
| [Delete unassigned phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUnassignedPhoneNumbers) | `phone:delete:number:admin` |
| [Delete unassigned phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUnassignedPhoneNumbers) | `phone:delete:number:master` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UnassignPhoneNumber) | `phone:delete:user_number``phone:delete:user_number:admin` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UnassignPhoneNumber) | `phone:delete:user_number:master` |
| [Update a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updatePhoneNumberDetails) | `phone:update:number:admin` |
| [Update a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updatePhoneNumberDetails) | `phone:update:number:master` |
| [List account emergency number pool phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountEmergencyNumberPoolNumbers) | `phone:read:emergency_number:admin` |
| [List account emergency number pool phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountEmergencyNumberPoolNumbers) | `phone:read:emergency_number:master` |
| [Add BYOC phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addBYOCNumber) | `phone:write:byo_carrier_number:admin` |
| [Add BYOC phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addBYOCNumber) | `phone:write:byo_carrier_number:master` |
| [Assign phone numbers to the emergency number pool](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumberToEmergencyNumberPool) | `phone:write:emergency_number:admin` |
| [Assign phone numbers to the emergency number pool](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumberToEmergencyNumberPool) | `phone:write:emergency_number:master` |
| [Get a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPhoneNumberDetails) | `phone:read:numbers:admin` |
| [Get a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPhoneNumberDetails) | `phone:read:numbers:master` |
| [List phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountPhoneNumbers) | `phone:read:list_numbers:admin` |
| [List phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountPhoneNumbers) | `phone:read:list_numbers:master` |

### Phone Plans [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-plans)

| API endpoint | granular scope |
| --- | --- |
| [List plan information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPhonePlans) | `phone:read:list_calling_plans:admin` |
| [List plan information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPhonePlans) | `phone:read:list_calling_plans:master` |
| [List calling plans](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCallingPlans) | `phone:read:list_calling_plans:admin` |
| [List calling plans](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCallingPlans) | `phone:read:list_calling_plans:master` |

### Phone Roles [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-roles)

| API endpoint | granular scope |
| --- | --- |
| [Update a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdatePhoneRole) | `phone:update:role:admin` |
| [Update a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdatePhoneRole) | `phone:update:role:master` |
| [List phone roles](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListPhoneRoles) | `phone:read:list_roles:admin` |
| [List phone roles](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListPhoneRoles) | `phone:read:list_roles:master` |
| [Add members to roles](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddRoleMembers) | `phone:write:role_member:admin` |
| [Add members to roles](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddRoleMembers) | `phone:write:role_member:master` |
| [List phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListPhoneRoleTargets) | `phone:read:list_roles:admin` |
| [List phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListPhoneRoleTargets) | `phone:read:list_roles:master` |
| [Delete a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeletePhoneRole) | `phone:delete:role:admin` |
| [Delete a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeletePhoneRole) | `phone:delete:role:master` |
| [Duplicate a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DuplicatePhoneRole) | `phone:write:role:admin` |
| [Duplicate a phone role](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DuplicatePhoneRole) | `phone:write:role:master` |
| [Delete phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DeletePhoneRoleTargets) | `phone:delete:role:admin` |
| [Delete phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DeletePhoneRoleTargets) | `phone:delete:role:master` |
| [Delete members in a role](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/DelRoleMembers) | `phone:delete:role_member:admin` |
| [Delete members in a role](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/DelRoleMembers) | `phone:delete:role_member:master` |
| [List members in a role](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/ListRoleMembers) | `phone:read:role_member:admin` |
| [List members in a role](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/ListRoleMembers) | `phone:read:role_member:master` |
| [Add phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/AddPhoneRoleTargets) | `phone:write:role:admin` |
| [Add phone role targets](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/AddPhoneRoleTargets) | `phone:write:role:master` |
| [Get role information](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getRoleInformation) | `phone:read:role:admin` |
| [Get role information](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getRoleInformation) | `phone:read:role:master` |

### Private Directory [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#private-directory)

| API endpoint | granular scope |
| --- | --- |
| [Remove a member from a private directory](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeAMemberFromAPrivateDirectory) | `phone:delete:private_directory_member:admin` |
| [Remove a member from a private directory](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeAMemberFromAPrivateDirectory) | `phone:delete:private_directory_member:master` |
| [Add members to a private directory](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addMembersToAPrivateDirectory) | `phone:write:private_directory_member:admin` |
| [Add members to a private directory](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addMembersToAPrivateDirectory) | `phone:write:private_directory_member:master` |
| [Update a private directory member](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAPrivateDirectoryMember) | `phone:update:private_directory_member:admin` |
| [Update a private directory member](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAPrivateDirectoryMember) | `phone:update:private_directory_member:master` |
| [List private directory members](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPrivateDirectoryMembers) | `phone:read:list_private_directory_members:admin` |
| [List private directory members](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPrivateDirectoryMembers) | `phone:read:list_private_directory_members:master` |

### Provider Exchange [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#provider-exchange)

| API endpoint | granular scope |
| --- | --- |
| [List carrier peering phone numbers.](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listCarrierPeeringPhoneNumbers) | `phone:read:list_peering_numbers:admin` |
| [List carrier peering phone numbers.](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listCarrierPeeringPhoneNumbers) | `phone:read:list_peering_numbers:master` |
| [Update peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updatePeeringPhoneNumbers) | `phone:update:peering_number:admin` |
| [Update peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updatePeeringPhoneNumbers) | `phone:update:peering_number:master` |
| [Add peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addPeeringPhoneNumbers) | `phone:write:peering_number:admin` |
| [Add peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addPeeringPhoneNumbers) | `phone:write:peering_number:master` |
| [List peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPeeringPhoneNumbers) | `phone:read:list_peering_numbers:admin` |
| [List peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPeeringPhoneNumbers) | `phone:read:list_peering_numbers:master` |
| [Remove peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deletePeeringPhoneNumbers) | `phone:delete:peering_number:admin` |
| [Remove peering phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deletePeeringPhoneNumbers) | `phone:delete:peering_number:master` |

### Provision Templates [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#provision-templates)

| API endpoint | granular scope |
| --- | --- |
| [List provision templates](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountProvisionTemplate) | `phone:read:list_provision_templates:admin` |
| [List provision templates](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountProvisionTemplate) | `phone:read:list_provision_templates:master` |
| [Delete a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteProvisionTemplate) | `phone:delete:provision_template:admin` |
| [Delete a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteProvisionTemplate) | `phone:delete:provision_template:master` |
| [Update a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateProvisionTemplate) | `phone:update:provision_template:admin` |
| [Update a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateProvisionTemplate) | `phone:update:provision_template:master` |
| [Get a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetProvisionTemplate) | `phone:read:provision_template:admin` |
| [Get a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetProvisionTemplate) | `phone:read:provision_template:master` |
| [Add a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addProvisionTemplate) | `phone:write:provision_template:admin` |
| [Add a provision template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addProvisionTemplate) | `phone:write:provision_template:master` |

### Push To Talk [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#push-to-talk)

| API endpoint | granular scope |
| --- | --- |
| [List push to talk channels](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPushToTalkChannels) | `phone:read:list_push_to_talk_channels:admin` |
| [List push to talk channels](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPushToTalkChannels) | `phone:read:list_push_to_talk_channels:master` |
| [List push to talk channel members](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPushToTalkChannelMembers) | `phone:read:list_push_to_talk_channel_members:admin` |
| [List push to talk channel members](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPushToTalkChannelMembers) | `phone:read:list_push_to_talk_channel_members:master` |
| [Remove a member from a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeAMemberFromAPushToTalkChannel) | `phone:delete:push_to_talk_channel_member:admin` |
| [Remove a member from a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeAMemberFromAPushToTalkChannel) | `phone:delete:push_to_talk_channel_member:master` |
| [Add members to a push to talk (PTT) channel](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addMembersToAPushToTalkChannel) | `phone:write:push_to_talk_channel_member:admin` |
| [Add members to a push to talk (PTT) channel](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addMembersToAPushToTalkChannel) | `phone:write:push_to_talk_channel_member:master` |
| [Create a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createAPushToTalkChannel) | `phone:write:push_to_talk_channel:admin` |
| [Create a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createAPushToTalkChannel) | `phone:write:push_to_talk_channel:master` |
| [Get push to talk channel details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPushToTalkChannelDetails) | `phone:read:push_to_talk_channel:admin` |
| [Get push to talk channel details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPushToTalkChannelDetails) | `phone:read:push_to_talk_channel:master` |
| [Remove a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeAPushToTalkChannel) | `phone:delete:push_to_talk_channel:admin` |
| [Remove a push to talk channel](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeAPushToTalkChannel) | `phone:delete:push_to_talk_channel:master` |
| [Update push to talk channel details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updatePushToTalkChannelDetails) | `phone:update:push_to_talk_channel:admin` |
| [Update push to talk channel details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updatePushToTalkChannelDetails) | `phone:update:push_to_talk_channel:master` |

### Recordings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#recordings)

| API endpoint | granular scope |
| --- | --- |
| [Get recording by call ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPhoneRecordingsByCallIdOrCallLogId) | `phone:read:call_recording``phone:read:call_recording:admin` |
| [Get recording by call ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPhoneRecordingsByCallIdOrCallLogId) | `phone:read:call_recording:master` |
| [Update Auto Delete Field](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateAutoDeleteField) | `phone:update:call_recording``phone:update:call_recording:admin` |
| [Update Auto Delete Field](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateAutoDeleteField) | `phone:update:call_recording:master` |
| [Update Recording Status](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UpdateRecordingStatus) | `phone:update:call_recording``phone:update:call_recording:admin` |
| [Update Recording Status](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UpdateRecordingStatus) | `phone:update:call_recording:master` |
| [Delete a call recording](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteCallRecording) | `phone:delete:call_recording``phone:delete:call_recording:admin` |
| [Delete a call recording](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteCallRecording) | `phone:delete:call_recording:master` |
| [Get user's recordings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUserRecordings) | `phone:read:list_recordings``phone:read:list_recordings:admin` |
| [Get user's recordings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUserRecordings) | `phone:read:list_recordings:master` |
| [Download a phone recording transcript](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneDownloadRecordingTranscript) | `phone:read:recording_transcript``phone:read:recording_transcript:admin` |
| [Download a phone recording transcript](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneDownloadRecordingTranscript) | `phone:read:recording_transcript:master` |
| [Download a phone recording](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneDownloadRecordingFile) | `phone:read:call_recording``phone:read:call_recording:admin` |
| [Download a phone recording](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneDownloadRecordingFile) | `phone:read:call_recording:master` |
| [Get a recording by call element ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPhoneRecordingByCallElementId) | `phone:read:call_recording``phone:read:call_recording:admin` |
| [Get a recording by call element ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPhoneRecordingByCallElementId) | `phone:read:call_recording:master` |
| [Get call recordings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPhoneRecordings) | `phone:read:list_call_recordings:admin` |
| [Get call recordings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPhoneRecordings) | `phone:read:list_call_recordings:master` |

### Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-1)

| API endpoint | granular scope |
| --- | --- |
| [Get fax charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Getfaxchargesusagereport) | `phone:read:fax_charges:admin` |
| [Get fax charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/Getfaxchargesusagereport) | `phone:read:fax_charges:master` |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPSOperationLogs) | `phone:read:operation_logs:admin` |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPSOperationLogs) | `phone:read:operation_logs:master` |
| [Get call charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetCallChargesUsageReport) | `phone:read:call_charges:admin` |
| [Get call charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetCallChargesUsageReport) | `phone:read:call_charges:master` |
| [Get SMS/MMS charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetSMSChargesUsageReport) | `phone:read:sms_charges:admin` |
| [Get SMS/MMS charges usage report](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetSMSChargesUsageReport) | `phone:read:sms_charges:master` |

### Routing Rules [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#routing-rules)

| API endpoint | granular scope |
| --- | --- |
| [Update directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateRoutingRule) | `phone:update:routing_rule:admin` |
| [Update directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateRoutingRule) | `phone:update:routing_rule:master` |
| [List directory backup routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listRoutingRule) | `phone:read:list_routing_rules:admin` |
| [List directory backup routing rules](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listRoutingRule) | `phone:read:list_routing_rules:master` |
| [Add directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addRoutingRule) | `phone:write:routing_rule:admin` |
| [Add directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addRoutingRule) | `phone:write:routing_rule:master` |
| [Get directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getRoutingRule) | `phone:read:routing_rule:admin` |
| [Get directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getRoutingRule) | `phone:read:routing_rule:master` |
| [Delete directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteRoutingRule) | `phone:delete:routing_rule:admin` |
| [Delete directory backup routing rule](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteRoutingRule) | `phone:delete:routing_rule:master` |

### SMS [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms)

| API endpoint | granular scope |
| --- | --- |
| [Get user's SMS sessions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/userSmsSession) | `phone:read:list_sms_sessions``phone:read:list_sms_sessions:admin` |
| [Get user's SMS sessions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/userSmsSession) | `phone:read:list_sms_sessions:master` |
| [Sync SMS by session ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/smsSessionSync) | `phone:read:sms_session``phone:read:sms_session:admin` |
| [Sync SMS by session ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/smsSessionSync) | `phone:read:sms_session:master` |
| [List user's SMS sessions in descending order](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetSmsSessions) | `phone:read:sms_session``phone:read:sms_session:admin` |
| [List user's SMS sessions in descending order](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetSmsSessions) | `phone:read:sms_session:master` |
| [Get SMS session details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/smsSessionDetails) | `phone:read:sms_session``phone:read:sms_session:admin` |
| [Get SMS session details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/smsSessionDetails) | `phone:read:sms_session:master` |
| [Get account's SMS sessions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/accountSmsSession) | `phone:read:list_sms_sessions``phone:read:list_sms_sessions:admin` |
| [Get account's SMS sessions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/accountSmsSession) | `phone:read:list_sms_sessions:master` |
| [Get SMS by message ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/smsByMessageId) | `phone:read:sms_message``phone:read:sms_message:admin` |
| [Get SMS by message ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/smsByMessageId) | `phone:read:sms_message:master` |
| [Post SMS message](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/postSmsMessage) | `phone:read:sms_message``phone:read:sms_message:admin` |

### SMS Campaign [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms-campaign)

| API endpoint | granular scope |
| --- | --- |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignCampaignPhoneNumber) | `phone:delete:sms_campaign_number:admin` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignCampaignPhoneNumber) | `phone:delete:sms_campaign_number:master` |
| [List user's opt statuses of phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getUserNumberCampaignOptStatus) | `phone:read:sms_campaign_number_opt_status``phone:read:sms_campaign_number_opt_status:admin` |
| [List user's opt statuses of phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getUserNumberCampaignOptStatus) | `phone:read:sms_campaign_number_opt_status:master` |
| [List opt statuses of phone numbers assigned to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getNumberCampaignOptStatus) | `phone:read:sms_campaign_number_opt_status:admin` |
| [List opt statuses of phone numbers assigned to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getNumberCampaignOptStatus) | `phone:read:sms_campaign_number_opt_status:master` |
| [Assign a phone number to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignCampaignPhoneNumbers) | `phone:write:sms_campaign_number:admin` |
| [Assign a phone number to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignCampaignPhoneNumbers) | `phone:write:sms_campaign_number:master` |
| [List SMS campaigns](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listAccountSMSCampaigns) | `phone:read:list_sms_campaigns:admin` |
| [List SMS campaigns](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listAccountSMSCampaigns) | `phone:read:list_sms_campaigns:master` |
| [Update opt statuses of phone numbers assigned to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateNumberCampaignOptStatus) | `phone:update:sms_campaign_number_opt_status:admin` |
| [Update opt statuses of phone numbers assigned to SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateNumberCampaignOptStatus) | `phone:update:sms_campaign_number_opt_status:master` |
| [Get an SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetSMSCampaign) | `phone:read:sms_campaign:admin` |
| [Get an SMS campaign](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetSMSCampaign) | `phone:read:sms_campaign:master` |

### SMS Consent [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms-consent)

| API endpoint | granular scope |
| --- | --- |
| [List opt statuses of phone numbers assigned to SMS consent](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getNumberConsentOptStatus) | `phone:read:sms_consent_number_opt_status:admin` |
| [List opt statuses of phone numbers assigned to SMS consent](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getNumberConsentOptStatus) | `phone:read:sms_consent_number_opt_status:master` |

### Setting Templates [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#setting-templates)

| API endpoint | granular scope |
| --- | --- |
| [List setting templates](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSettingTemplates) | `phone:read:list_setting_templates:admin` |
| [List setting templates](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSettingTemplates) | `phone:read:list_setting_templates:master` |
| [Add a setting template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSettingTemplate) | `phone:write:setting_template:admin` |
| [Add a setting template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSettingTemplate) | `phone:write:setting_template:master` |
| [Get setting template details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getSettingTemplate) | `phone:read:setting_template:admin` |
| [Get setting template details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getSettingTemplate) | `phone:read:setting_template:master` |
| [Update a setting template](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSettingTemplate) | `phone:update:setting_template:admin` |
| [Update a setting template](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSettingTemplate) | `phone:update:setting_template:master` |

### Settings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settings-2)

| API endpoint | granular scope |
| --- | --- |
| [List ported numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPortedNumbers) | `phone:read:list_ported_numbers:admin` |
| [List ported numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPortedNumbers) | `phone:read:list_ported_numbers:master` |
| [Update account policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateAccountPolicy) | `phone:update:policy:admin` |
| [Update account policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateAccountPolicy) | `phone:update:policy:master` |
| [List SIP groups](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSipGroups) | `phone:read:list_sip_groups:admin` |
| [List SIP groups](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSipGroups) | `phone:read:list_sip_groups:master` |
| [Get ported numbers details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getPortedNumbersDetails) | `phone:read:ported_number:admin` |
| [Get ported numbers details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getPortedNumbersDetails) | `phone:read:ported_number:master` |
| [List BYOC SIP trunks](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listBYOCSIPTrunk) | `phone:read:list_sip_trunks:admin` |
| [List BYOC SIP trunks](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listBYOCSIPTrunk) | `phone:read:list_sip_trunks:master` |
| [Get account policy details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetAccountPolicyDetails) | `phone:read:policy:admin` |
| [Get account policy details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetAccountPolicyDetails) | `phone:read:policy:master` |
| [Get phone account settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneSetting) | `phone:read:settings:admin` |
| [Get phone account settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneSetting) | `phone:read:settings:master` |
| [Update phone account settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updatePhoneSettings) | `phone:update:settings:admin` |
| [Update phone account settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updatePhoneSettings) | `phone:update:settings:master` |

### Shared Line Appearance [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#shared-line-appearance)

| API endpoint | granular scope |
| --- | --- |
| [List shared line appearances](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSharedLineAppearances) | `phone:read:list_shared_line_appearances:admin` |
| [List shared line appearances](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSharedLineAppearances) | `phone:read:list_shared_line_appearances:master` |

### Shared Line Group [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#shared-line-group)

| API endpoint | granular scope |
| --- | --- |
| [Update a shared line group policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSharedLineGroupPolicy) | `phone:update:shared_line_group_policy:admin` |
| [Update a shared line group policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSharedLineGroupPolicy) | `phone:update:shared_line_group_policy:master` |
| [Unassign a member from a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAMemberSLG) | `phone:delete:shared_line_member:admin` |
| [Unassign a member from a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAMemberSLG) | `phone:delete:shared_line_member:master` |
| [Get a shared line group policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getSharedLineGroupPolicy) | `phone:read:shared_line_group_policy:admin` |
| [Get a shared line group policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getSharedLineGroupPolicy) | `phone:read:shared_line_group_policy:master` |
| [Update shared line group call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSharedLineGroupCallHandlingSetting) | `phone:update:shared_line_group_call_handling_setting:admin` |
| [Update shared line group call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSharedLineGroupCallHandlingSetting) | `phone:update:shared_line_group_call_handling_setting:master` |
| [Unassign members from a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteMembersOfSLG) | `phone:delete:shared_line_member:admin` |
| [Unassign members from a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteMembersOfSLG) | `phone:delete:shared_line_member:master` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deletePhoneNumbersSLG) | `phone:delete:shared_line_group_number:admin` |
| [Unassign all phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deletePhoneNumbersSLG) | `phone:delete:shared_line_group_number:master` |
| [Update an SLG policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSLGPolicySubSetting) | `phone:update:shared_line_group_policy:admin` |
| [Update an SLG policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSLGPolicySubSetting) | `phone:update:shared_line_group_policy:master` |
| [Update shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSharedLineGroupSetting) | `phone:update:shared_line_group_setting:admin` |
| [Update shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSharedLineGroupSetting) | `phone:update:shared_line_group_setting:master` |
| [Assign phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumbersSLG) | `phone:write:shared_line_group_number:admin` |
| [Assign phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumbersSLG) | `phone:write:shared_line_group_number:master` |
| [Get shared line group settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getSharedLineGroupSettings) | `phone:read:shared_line_group_setting:admin` |
| [Get shared line group settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getSharedLineGroupSettings) | `phone:read:shared_line_group_setting:master` |
| [Add members to a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addMembersToSharedLineGroup) | `phone:write:shared_line_member:admin` |
| [Add members to a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addMembersToSharedLineGroup) | `phone:write:shared_line_member:master` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteAPhoneNumberSLG) | `phone:delete:shared_line_group_number:admin` |
| [Unassign a phone number](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteAPhoneNumberSLG) | `phone:delete:shared_line_group_number:master` |
| [Create a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createASharedLineGroup) | `phone:write:shared_line_group:admin` |
| [Create a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createASharedLineGroup) | `phone:write:shared_line_group:master` |
| [Update a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateASharedLineGroup) | `phone:update:shared_line_group:admin` |
| [Update a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateASharedLineGroup) | `phone:update:shared_line_group:master` |
| [Add a policy setting to a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSLGPolicySubSetting) | `phone:write:shared_line_group_policy:admin` |
| [Add a policy setting to a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSLGPolicySubSetting) | `phone:write:shared_line_group_policy:master` |
| [Delete a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteASharedLineGroup) | `phone:delete:shared_line_group:admin` |
| [Delete a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteASharedLineGroup) | `phone:delete:shared_line_group:master` |
| [List shared line groups](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSharedLineGroups) | `phone:read:list_shared_line_groups:admin` |
| [List shared line groups](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSharedLineGroups) | `phone:read:list_shared_line_groups:master` |
| [Get a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getASharedLineGroup) | `phone:read:shared_line_group:admin` |
| [Get a shared line group](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getASharedLineGroup) | `phone:read:shared_line_group:master` |
| [Delete shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteSharedLineGroupSetting) | `phone:delete:shared_line_group_setting:admin` |
| [Delete shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteSharedLineGroupSetting) | `phone:delete:shared_line_group_setting:master` |
| [Add shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSharedLineGroupSetting) | `phone:write:shared_line_group_setting:admin` |
| [Add shared line group setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSharedLineGroupSetting) | `phone:write:shared_line_group_setting:master` |
| [Delete an SLG policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/removeSLGPolicySubSetting) | `phone:delete:shared_line_group_policy:admin` |
| [Delete an SLG policy setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/removeSLGPolicySubSetting) | `phone:delete:shared_line_group_policy:master` |
| [Get shared line group call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getSharedLineGroupCallHandlingSetting) | `phone:read:shared_line_group_call_handling_setting:admin` |
| [Get shared line group call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getSharedLineGroupCallHandlingSetting) | `phone:read:shared_line_group_call_handling_setting:master` |

### Sites [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sites)

| API endpoint | granular scope |
| --- | --- |
| [Get a phone site setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getSiteSettingForType) | `phone:read:site_setting:admin` |
| [Get a phone site setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getSiteSettingForType) | `phone:read:site_setting:master` |
| [Update the site setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSiteSetting) | `phone:update:site_setting:admin` |
| [Update the site setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSiteSetting) | `phone:update:site_setting:master` |
| [Add a site setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSiteSetting) | `phone:write:site_setting:admin` |
| [Add a site setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSiteSetting) | `phone:write:site_setting:master` |
| [Delete a phone site](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deletePhoneSite) | `phone:delete:site:admin` |
| [Delete a phone site](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deletePhoneSite) | `phone:delete:site:master` |
| [Get phone site details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getASite) | `phone:read:site:admin` |
| [Get phone site details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getASite) | `phone:read:site:master` |
| [Create a phone site](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/createPhoneSite) | `phone:write:site:admin` |
| [Create a phone site](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/createPhoneSite) | `phone:write:site:master` |
| [Add customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addSiteOutboundCallerNumbers) | `phone:write:site_customized_number:admin` |
| [Add customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addSiteOutboundCallerNumbers) | `phone:write:site_customized_number:master` |
| [Remove customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteSiteOutboundCallerNumbers) | `phone:delete:site_customized_number:admin` |
| [Remove customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteSiteOutboundCallerNumbers) | `phone:delete:site_customized_number:master` |
| [Delete a site setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteSiteSetting) | `phone:delete:site_setting:admin` |
| [Delete a site setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteSiteSetting) | `phone:delete:site_setting:master` |
| [List customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listSiteCustomizeOutboundCallerNumbers) | `phone:read:list_site_customized_number:admin` |
| [List customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listSiteCustomizeOutboundCallerNumbers) | `phone:read:list_site_customized_number:master` |
| [Update phone site details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateSiteDetails) | `phone:update:site:admin` |
| [Update phone site details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateSiteDetails) | `phone:update:site:master` |
| [List phone sites](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPhoneSites) | `phone:read:list_sites:admin` |
| [List phone sites](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPhoneSites) | `phone:read:list_sites:master` |

### Users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users)

| API endpoint | granular scope |
| --- | --- |
| [Get a user's profile](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUser) | `phone:read:user``phone:read:user:admin` |
| [Get a user's profile](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUser) | `phone:read:user:master` |
| [Unassign user's calling plan](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignCallingPlan) | `phone:delete:users_calling_plan``phone:delete:users_calling_plan:admin` |
| [Unassign user's calling plan](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignCallingPlan) | `phone:delete:users_calling_plan:master` |
| [Delete a user's profile setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserProfileSetting) | `phone:delete:user_setting``phone:delete:user_setting:admin` |
| [Delete a user's profile setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserProfileSetting) | `phone:delete:user_setting:master` |
| [List phone users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listPhoneUsers) | `phone:read:list_users:admin` |
| [List phone users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listPhoneUsers) | `phone:read:list_users:master` |
| [Update user's calling plan](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateCallingPlan) | `phone:update:calling_plan``phone:update:calling_plan:admin` |
| [Update user's calling plan](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateCallingPlan) | `phone:update:calling_plan:master` |
| [Update multiple users' properties in batch](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUsersPropertiesInBatch) | `phone:update:batch_users:admin` |
| [Update multiple users' properties in batch](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUsersPropertiesInBatch) | `phone:update:batch_users:master` |
| [Assign calling plan to a user](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignCallingPlan) | `phone:write:calling_plan``phone:write:calling_plan:admin` |
| [Assign calling plan to a user](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignCallingPlan) | `phone:write:calling_plan:master` |
| [Get user policy details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/GetUserPolicyDetails) | `phone:read:user_policy:admin` |
| [Get user policy details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/GetUserPolicyDetails) | `phone:read:user_policy:master` |
| [List users' phone numbers for a customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUserCustomizeOutboundCallerNumbers) | `phone:read:list_user_customized_number``phone:read:list_user_customized_number:admin` |
| [List users' phone numbers for a customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUserCustomizeOutboundCallerNumbers) | `phone:read:list_user_customized_number:master` |
| [Update user policy](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUserPolicy) | `phone:update:user_policy:admin` |
| [Update user policy](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUserPolicy) | `phone:update:user_policy:master` |
| [Remove users' customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserOutboundCallerNumbers) | `phone:delete:user_customized_number``phone:delete:user_customized_number:admin` |
| [Remove users' customized outbound caller ID phone numbers](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserOutboundCallerNumbers) | `phone:delete:user_customized_number:master` |
| [Update a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUserSetting) | `phone:update:shared_setting``phone:update:shared_setting:admin` |
| [Update a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUserSetting) | `phone:update:shared_setting:master` |
| [Update user call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUserCallHandlingSetting) | `phone:update:user_call_handling_setting:admin``phone:update:user_call_handling_setting` |
| [Update user call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUserCallHandlingSetting) | `phone:update:user_call_handling_setting:master` |
| [Add user call forward setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addUserCallForwardSetting) | `phone:write:user_call_handling_setting``phone:write:user_call_handling_setting:admin` |
| [Add user call forward setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addUserCallForwardSetting) | `phone:write:user_call_handling_setting:master` |
| [Get a user's profile settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUserSettings) | `phone:read:user_setting:admin``phone:read:user_setting` |
| [Get a user's profile settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUserSettings) | `phone:read:user_setting:master` |
| [Add a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addUserSetting) | `phone:write:shared_setting``phone:write:shared_setting:admin` |
| [Add a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addUserSetting) | `phone:write:shared_setting:master` |
| [Batch add users](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/batchAddUsers) | `phone:write:batch_users:admin` |
| [Batch add users](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/batchAddUsers) | `phone:write:batch_users:master` |
| [Delete user call forward setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserCallForwardSetting) | `phone:delete:user_call_handling_setting``phone:delete:user_call_handling_setting:admin` |
| [Delete user call forward setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserCallForwardSetting) | `phone:delete:user_call_handling_setting:master` |
| [Add a user's profile setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addUserProfileSetting) | `phone:write:user_setting:admin``phone:write:user_setting` |
| [Add a user's profile setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addUserProfileSetting) | `phone:write:user_setting:master` |
| [Delete a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteUserSetting) | `phone:delete:shared_setting``phone:delete:shared_setting:admin` |
| [Delete a user's shared access setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteUserSetting) | `phone:delete:shared_setting:master` |
| [Get user call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getUserCallHandlingSetting) | `phone:read:user_call_handling_setting:admin``phone:read:user_call_handling_setting` |
| [Get user call handling setting](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getUserCallHandlingSetting) | `phone:read:user_call_handling_setting:master` |
| [Update a user's profile settings](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUserSettings) | `phone:update:user_setting``phone:update:user_setting:admin` |
| [Update a user's profile settings](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUserSettings) | `phone:update:user_setting:master` |
| [Add phone numbers for users' customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addUserOutboundCallerNumbers) | `phone:write:user_customized_number``phone:write:user_customized_number:admin` |
| [Add phone numbers for users' customized outbound caller ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addUserOutboundCallerNumbers) | `phone:write:user_customized_number:master` |
| [Update a user's profile](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateUserProfile) | `phone:update:user``phone:update:user:admin` |
| [Update a user's profile](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateUserProfile) | `phone:update:user:master` |

### Voicemails [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#voicemails)

| API endpoint | granular scope |
| --- | --- |
| [Get user's voicemails](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneUserVoiceMails) | `phone:read:list_voicemails``phone:read:list_voicemails:admin` |
| [Get user's voicemails](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneUserVoiceMails) | `phone:read:list_voicemails:master` |
| [Update Voicemail Read Status](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateVoicemailReadStatus) | `phone:update:voicemail``phone:update:voicemail:admin` |
| [Update Voicemail Read Status](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateVoicemailReadStatus) | `phone:update:voicemail:master` |
| [Get account voicemails](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/accountVoiceMails) | `phone:read:list_voicemails:admin` |
| [Get account voicemails](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/accountVoiceMails) | `phone:read:list_voicemails:master` |
| [Get voicemail details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getVoicemailDetails) | `phone:read:voicemail``phone:read:voicemail:admin` |
| [Get voicemail details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getVoicemailDetails) | `phone:read:voicemail:master` |
| [Download a phone voicemail](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/phoneDownloadVoicemailFile) | `phone:read:voicemail:admin``phone:read:voicemail` |
| [Download a phone voicemail](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/phoneDownloadVoicemailFile) | `phone:read:voicemail:master` |
| [Get user voicemail details from a call log](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getVoicemailDetailsByCallIdOrCallLogId) | `phone:read:voicemail``phone:read:voicemail:admin` |
| [Get user voicemail details from a call log](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getVoicemailDetailsByCallIdOrCallLogId) | `phone:read:voicemail:master` |
| [Delete a voicemail](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/deleteVoicemail) | `phone:delete:voicemail``phone:delete:voicemail:admin` |
| [Delete a voicemail](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/deleteVoicemail) | `phone:delete:voicemail:master` |
| [Get a voicemail by call element ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getVoicemailDetailsByCallElementId) | `phone:read:voicemail``phone:read:voicemail:admin` |
| [Get a voicemail by call element ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getVoicemailDetailsByCallElementId) | `phone:read:voicemail:master` |

### WhatsApp Messages [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#whatsapp-messages)

| API endpoint | granular scope |
| --- | --- |
| [Get user's WhatsApp sessions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/userWhatsappSession) | `phone:read:list_whatsapp_sessions``phone:read:list_whatsapp_sessions:admin` |
| [Get user's WhatsApp sessions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/userWhatsappSession) | `phone:read:list_whatsapp_sessions:master` |
| [Get WhatsApp session details](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/whatsappSessionDetails) | `phone:read:whatsapp_session``phone:read:whatsapp_session:admin` |
| [Get WhatsApp session details](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/whatsappSessionDetails) | `phone:read:whatsapp_session:master` |
| [Send WhatsApp message](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/postWhatsAppMessage) | `phone:write:whatsapp_message``phone:write:whatsapp_message:admin` |
| [Send WhatsApp message](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/postWhatsAppMessage) | `phone:write:whatsapp_message:master` |
| [Get WhatsApp message by message ID](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/whatsappByMessageId) | `phone:read:whatsapp_message``phone:read:whatsapp_message:admin` |
| [Get WhatsApp message by message ID](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/whatsappByMessageId) | `phone:read:whatsapp_message:master` |
| [Get account's WhatsApp sessions](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listWhatsAppSessions) | `phone:read:list_whatsapp_sessions``phone:read:list_whatsapp_sessions:admin` |
| [Get account's WhatsApp sessions](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listWhatsAppSessions) | `phone:read:list_whatsapp_sessions:master` |

### Zoom Rooms [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms)

| API endpoint | granular scope |
| --- | --- |
| [Remove a phone number from a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/UnassignPhoneNumberFromZoomRoom) | `phone:delete:room_phone_number:admin` |
| [Remove a phone number from a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/UnassignPhoneNumberFromZoomRoom) | `phone:delete:room_phone_number:master` |
| [Assign calling plans to a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignCallingPlanToRoom) | `phone:write:room_calling_plan:admin` |
| [Assign calling plans to a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignCallingPlanToRoom) | `phone:write:room_calling_plan:master` |
| [Add a Zoom Room to a Zoom Phone](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/addZoomRoom) | `phone:write:room:admin` |
| [Add a Zoom Room to a Zoom Phone](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/addZoomRoom) | `phone:write:room:master` |
| [Update a Zoom Room under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/updateZoomRoom) | `phone:update:room:admin` |
| [Update a Zoom Room under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/updateZoomRoom) | `phone:update:room:master` |
| [Assign phone numbers to a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/assignPhoneNumberToZoomRoom) | `phone:write:room_phone_number:admin` |
| [Assign phone numbers to a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/assignPhoneNumberToZoomRoom) | `phone:write:room_phone_number:master` |
| [Remove a calling plan from a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/unassignCallingPlanFromRoom) | `phone:delete:room_calling_plan:admin` |
| [Remove a calling plan from a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/unassignCallingPlanFromRoom) | `phone:delete:room_calling_plan:master` |
| [List Zoom Rooms without Zoom Phone assignment](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listUnassignedZoomRooms) | `phone:read:list_rooms:admin` |
| [List Zoom Rooms without Zoom Phone assignment](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listUnassignedZoomRooms) | `phone:read:list_rooms:master` |
| [Remove a Zoom Room from a ZP account](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/RemoveZoomRoom) | `phone:delete:room:admin` |
| [Remove a Zoom Room from a ZP account](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/RemoveZoomRoom) | `phone:delete:room:master` |
| [Get a Zoom Room under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/getZoomRoom) | `phone:read:room:admin` |
| [Get a Zoom Room under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/getZoomRoom) | `phone:read:room:master` |
| [List Zoom Rooms under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/listZoomRooms) | `phone:read:list_rooms:admin` |
| [List Zoom Rooms under Zoom Phone license](https://developers.zoom.us/docs/api/rest/reference/phone/ma/#operation/listZoomRooms) | `phone:read:list_rooms:master` |

## Tasks [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#tasks)

The following are the available **Tasks** APIs and their associated granular scopes.

### Assignee [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#assignee)

| API endpoint | granular scope |
| --- | --- |
| [Add assignees to a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/addTasksAssignees) | `tasks:write:assignees``tasks:write:assignees:admin` |
| [Get assignees of a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/GetAssigneesOfATask) | `tasks:read:assignees``tasks:read:assignees:admin` |
| [Remove Assignee from task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/removeTaskAssignee) | `tasks:delete:assignees``tasks:delete:assignees:admin` |

### Collaborator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#collaborator-2)

| API endpoint | granular scope |
| --- | --- |
| [Add collaborators to a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/addTasksCollaborators) | `tasks:write:collaborators``tasks:write:collaborators:admin` |
| [Remove collaborator from task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/removeTaskCollaborator) | `tasks:delete:collaborator:admin``tasks:delete:collaborator` |
| [Get collaborators of a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/Getcollaboratorsofatask) | `tasks:read:list_collaborators``tasks:read:list_collaborators:admin` |

### Comment [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#comment-1)

| API endpoint | granular scope |
| --- | --- |
| [Add a comment to a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/addComment) | `tasks:write:comment:admin``tasks:write:comment` |
| [Get a task's comments](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/GetAV1TasksComment) | `tasks:read:comments``tasks:read:comments:admin` |
| [Delete a task's comment](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/DeleteTaskComment) | `tasks:delete:comment:admin``tasks:delete:comment` |

### File [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#file-1)

| API endpoint | granular scope |
| --- | --- |
| [Upload a file in tasks](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/Uploadfilefortasksimport) | `tasks:write:file``tasks:write:file:admin` |

### Import [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#import-1)

| API endpoint | granular scope |
| --- | --- |
| [Submit a task import job](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/submitTasksImportJob) | `tasks:write:import``tasks:write:import:admin` |
| [Get import job status](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/getTasksImportJob) | `tasks:read:import``tasks:read:import:admin` |

### Tasks [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#tasks-1)

| API endpoint | granular scope |
| --- | --- |
| [Update task fields](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/updateTask) | `tasks:update:task``tasks:update:task:admin` |
| [Delete a task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/deleteTask) | `tasks:delete:task:admin``tasks:delete:task` |
| [Create a new task](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/createTask) | `tasks:write:task` |
| [Get task details](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/getTaskDetail) | `tasks:read:task``tasks:read:task:admin` |
| [List tasks](https://developers.zoom.us/docs/api/rest/reference/Tasks/methods/#operation/getMyTasks) | `tasks:read:list_tasks:admin``tasks:read:list_tasks` |

## Zoom Chat [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-chat)

The following are the available **Zoom Chat** APIs and their associated granular scopes.

### Chat Channel Mention Group [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-channel-mention-group)

| API endpoint | granular scope |
| --- | --- |
| [List the members of a mention group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listTheMembersOfMentionGroup) | `team_chat:read:mention_group``team_chat:read:mention_group:admin` |
| [Add channel members to a mention group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/addAChannelMembersToMentionGroup) | `team_chat:update:mention_group``team_chat:update:mention_group:admin` |
| [List channel mention groups](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChannelMentionGroup) | `team_chat:read:mention_group``team_chat:read:mention_group:admin` |
| [Remove channel mention group members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/removeChannelMentionGroupMembers) | `team_chat:update:mention_group``team_chat:update:mention_group:admin` |
| [Update a channel mention group information](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateChannelMentionGroup) | `team_chat:update:mention_group``team_chat:update:mention_group:admin` |
| [Create a channel mention group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/createChannelMentionGroup) | `team_chat:write:mention_group:admin``team_chat:write:mention_group` |
| [Delete a channel mention group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteAChannelMentionGroup) | `team_chat:delete:mention_group``team_chat:delete:mention_group:admin` |

### Chat Channels [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-channels)

| API endpoint | granular scope |
| --- | --- |
| [List channel members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listUserLevelChannelMembers) | `team_chat:read:list_members``team_chat:read:list_members:admin` |
| [List channel members (Groups)](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listChannelMembersGroups) | `team_chat:read:list_groups:admin` |
| [Remove a member (group)](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/removeAMemberGroup) | `team_chat:delete:group:admin` |
| [Remove a member](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/removeAUserLevelChannelMember) | `team_chat:delete:member``team_chat:delete:member:admin` |
| [List channel activity logs](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listAllChannelActivityLogs) | `team_chat:read:list_channel_activity_logs:admin` |
| [Leave a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/leaveChannel) | `team_chat:delete:member``team_chat:delete:member:admin` |
| [Update a chat session content tab](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_session_content_tab_update) | `zoom_chat:update:chat_tab` |
| [Perform operations on channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/PerformOperationsOnChannels) | `team_chat:update:archive_channels``team_chat:update:archive_channels:admin` |
| [List user's channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChannels) | `team_chat:read:list_user_channels``team_chat:read:list_user_channels:admin` |
| [Invite channel members (Groups)](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/inviteChannelMembersGroups) | `team_chat:write:groups:admin` |
| [Join a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/joinChannel) | `team_chat:write:member` |
| [Remove a chat session content tab](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_session_content_tab_delete) | `zoom_chat:delete:chat_tab` |
| [Invite channel members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/InviteUserLevelChannelMembers) | `team_chat:write:members``team_chat:write:members:admin` |
| [Get a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getUserLevelChannel) | `team_chat:read:channel``team_chat:read:channel:admin` |
| [Delete a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteUserLevelChannel) | `team_chat:delete:channel``team_chat:delete:channel:admin` |
| [Create a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/createChannel) | `team_chat:write:user_channel``team_chat:write:user_channel:admin` |
| [Batch remove members from a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/batchRemoveChannelMembers) | `team_chat:delete:batch_members``team_chat:delete:batch_members:admin` |
| [Update a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateUserLevelChannel) | `team_chat:update:channel``team_chat:update:channel:admin` |
| [Add a chat session content tab](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_session_content_tab_create) | `zoom_chat:write:chat_tab` |

### Chat Channels (Account-level) [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-channels-account-level)

| API endpoint | granular scope |
| --- | --- |
| [List channel administrators](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listChannelAdministrators) | `team_chat:read:list_administrators:admin` |
| [Get a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChannel) | `team_chat:read:user_channel``team_chat:read:user_channel:admin` |
| [Invite channel members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/inviteChannelMembers) | `team_chat:write:members``team_chat:write:members:admin` |
| [Batch demote channel administrators](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/batchDemoteChannelAdministrators) | `team_chat:delete:batch_administrators:admin` |
| [Search user's or account's channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/searchChannels) | `team_chat:write:search_channels``team_chat:write:search_channels:admin` |
| [Promote channel members to administrators](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/promoteChannelMembersAsAdmin) | `team_chat:write:administrator:admin` |
| [Remove a member](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/removeAChannelMember) | `team_chat:delete:member:admin` |
| [Batch delete channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/batchDeleteChannelsAccountLevel) | `team_chat:delete:channels``team_chat:delete:channels:admin` |
| [List channel members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listChannelMembers) | `team_chat:read:list_members``team_chat:read:list_members:admin` |
| [Delete a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteChannel) | `team_chat:delete:user_channel``team_chat:delete:user_channel:admin` |
| [Update retention policy of a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateChannelRetention) | `team_chat:update:retention:admin` |
| [Get retention policy of a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChannelRetention) | `team_chat:read:retention:admin` |
| [List channel activity logs](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listChannelActivityLogs) | `team_chat:read:list_channel_activity_logs:admin` |
| [List account's public channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getAccountChannels) | `team_chat:read:list_channels:admin` |
| [Update a channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateChannel) | `team_chat:update:user_channel``team_chat:update:user_channel:admin` |
| [Assign a new channel owner](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/reassignChannelOwner) | `team_chat:update:channel_owner:admin` |
| [Batch remove members from a user's channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/batchRemoveUserChannelMembers) | `team_chat:delete:member:admin` |

### Chat Emoji [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-emoji)

| API endpoint | granular scope |
| --- | --- |
| [Add a custom emoji](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/addACustomEmoji) | `team_chat:write:custom_emoji``team_chat:write:custom_emoji:admin` |
| [Delete a custom emoji](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/DeleteCustomEmoji) | `team_chat:delete:custom_emoji``team_chat:delete:custom_emoji:admin` |
| [List custom emojis](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listCustomEmojis) | `team_chat:read:list_custom_emojis``team_chat:read:list_custom_emojis:admin` |

### Chat External Connections [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-external-connections)

| API endpoint | granular scope |
| --- | --- |
| [External connections: view direct chats for one external user.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_internal_users_in_direct_chats_with_external_user_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view direct chats for one internal user.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_external_users_in_direct_chats_with_internal_user_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view external accounts connected to your account.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_external_accounts_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view direct chats for one external account.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_external_users_in_direct_chats_for_external_account_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view channels for one external account.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_channels_for_external_account_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view external users who collaborate with your account.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_external_users_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view channels for one internal user.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_channels_for_internal_user_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view internal users who collaborate with external users.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_internal_users_with_external_activity_list) | `zoom_chat:read:list_external_connections:admin` |
| [External connections: view channels for one external user.](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/zoom_chat_connected_channels_for_external_user_list) | `zoom_chat:read:list_external_connections:admin` |

### Chat Files [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-files)

| API endpoint | granular scope |
| --- | --- |
| [Send a chat file](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/sendChatFile) | `team_chat:write:message_files``team_chat:write:message_files:admin` |
| [Get file info](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getFileInfo) | `team_chat:read:file``team_chat:read:file:admin` |
| [Upload a chat file](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/uploadAChatFile) | `team_chat:write:files``team_chat:write:files:admin` |
| [Delete a chat file](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteChatFile) | `team_chat:delete:file``team_chat:delete:file:admin` |

### Chat Messages [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-messages)

| API endpoint | granular scope |
| --- | --- |
| [Delete a scheduled message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteScheduleMessage) | `team_chat:delete:scheduled_message` |
| [List user's chat messages](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChatMessages) | `team_chat:read:list_user_messages``team_chat:read:list_user_messages:admin` |
| [React to a chat message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/reactMessage) | `team_chat:update:message_emoji``team_chat:update:message_emoji:admin` |
| [Delete a message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteChatMessage) | `team_chat:delete:user_message``team_chat:delete:user_message:admin` |
| [Perform operations on the message of channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/PerformMessageOfChannel) | `team_chat:update:pin_message` |
| [Update a message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/editMessage) | `team_chat:update:user_message``team_chat:update:user_message:admin` |
| [Get a forwarded message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getForwardedMessage) | `team_chat:read:user_message``team_chat:read:user_message:admin` |
| [Add or remove a bookmark](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/addOrRemoveABookmark) | `team_chat:update:bookmark` |
| [List scheduled messages](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listScheduledMessages) | `team_chat:read:list_scheduled_messages` |
| [Send a chat message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/sendaChatMessage) | `team_chat:write:user_message``team_chat:write:user_message:admin` |
| [Retrieve a thread](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/retrieveThread) | `team_chat:read:thread_message``team_chat:read:thread_message:admin` |
| [Get a message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChatMessage) | `team_chat:read:user_message``team_chat:read:user_message:admin` |
| [List bookmarks](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/fetchBookmarks) | `team_chat:read:list_bookmarks` |
| [Mark message read or unread](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/markMessage) | `team_chat:update:message_status``team_chat:update:message_status:admin` |
| [List pinned history messages of channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listChannelPinnedMessages) | `team_chat:read:list_pinned_messages` |

### Chat Migration [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-migration)

| API endpoint | granular scope |
| --- | --- |
| [Get migrated Zoom channel IDs](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getMigrationChannelsMapping) | `team_chat:read:migrated_channels:admin` |
| [Migrate channel members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateChannelMembers) | `team_chat:write:migrate_channel_members:admin` |
| [Delete a channel tab](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/Deleteachanneltab) | `team_chat:delete:channel_tab:admin` |
| [Get migrated Zoom user IDs](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getMigrationUsersMapping) | `team_chat:read:migrated_users:admin` |
| [Migrate chat messages](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateChatMessages) | `team_chat:write:migrate_chat_messages:admin` |
| [Migrate a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateASharedSpace) | `team_chat:write:migrate_shared_spaces:admin` |
| [Migrate a channel tab](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateAChannelTab) | `team_chat:write:migrate_channel_tab:admin` |
| [Migrate a chat channel](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateAChatChannel) | `team_chat:write:migrate_a_chat_channel:admin` |
| [Migrate chat message reactions](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/MigrateChatMessageReactions) | `team_chat:write:migrate_chat_message_reactions:admin` |

### Chat Reminder [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-reminder)

| API endpoint | granular scope |
| --- | --- |
| [List reminders](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listReminders) | `team_chat:read:list_reminders` |
| [Create a reminder message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/createReminderForMessage) | `team_chat:write:reminder` |
| [Delete a reminder for a message](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteReminderForMessage) | `team_chat:delete:reminder` |

### Chat Sessions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#chat-sessions)

| API endpoint | granular scope |
| --- | --- |
| [Star or unstar a channel or contact user](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/starUnstarChannelContact) | `team_chat:update:chat_control``team_chat:update:chat_control:admin` |
| [List a user's chat sessions](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getChatSessions) | `team_chat:read:list_user_sessions``team_chat:read:list_user_sessions:admin` |

### Contacts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#contacts)

| API endpoint | granular scope |
| --- | --- |
| [Update a user-managed contact](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/contacts_personal_contact_update) | `zoom_chat:update:personal_contact``zoom_chat:update:personal_contact:admin` |
| [Search company contacts](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/searchCompanyContacts) | `contact:read:list_contacts``contact:read:list_contacts:admin` |
| [Get user's contact details](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getUserContact) | `team_chat:read:contact` |
| [Create a user-managed contact](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/Createauser-managedcontact) | `zoom_chat:write:personal_contact``zoom_chat:write:personal_contact:admin` |
| [Delete a user-managed contact](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/Deleteauser-managedcontact) | `zoom_chat:delete:personal_contact``zoom_chat:delete:personal_contact:admin` |
| [List user's contacts](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getUserContacts) | `team_chat:read:list_contacts` |

### IM Groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#im-groups)

| API endpoint | granular scope |
| --- | --- |
| [Update an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupUpdate) | `contact_group:update:group:admin` |
| [Update an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupUpdate) | `contact_group:update:group:master` |
| [Add IM directory group members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupMembersCreate) | `contact_group:write:member:admin` |
| [Add IM directory group members](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupMembersCreate) | `contact_group:write:member:master` |
| [List IM directory groups](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroups) | `contact_group:read:list_groups:admin` |
| [List IM directory groups](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroups) | `contact_group:read:list_groups:master` |
| [Delete an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupDelete) | `contact_group:delete:group:admin` |
| [Delete an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupDelete) | `contact_group:delete:group:master` |
| [Retrieve an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroup) | `contact_group:read:group:admin` |
| [Retrieve an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroup) | `contact_group:read:group:master` |
| [Delete IM directory group member](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupMembersDelete) | `contact_group:delete:member:admin` |
| [Delete IM directory group member](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupMembersDelete) | `contact_group:delete:member:master` |
| [Create an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupCreate) | `contact_group:write:group:admin` |
| [Create an IM directory group](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupCreate) | `contact_group:write:group:master` |
| [List IM directory group members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/imGroupMembers) | `contact_group:read:list_members:admin` |
| [List IM directory group members](https://developers.zoom.us/docs/api/rest/reference/chat/ma/#operation/imGroupMembers) | `contact_group:read:list_members:master` |

### Invitations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#invitations)

| API endpoint | granular scope |
| --- | --- |
| [Send new contact invitation](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/sendNewContactInvitation) | `team_chat:write:contact_information:admin``team_chat:write:contact_information` |

### Legal Hold [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#legal-hold)

| API endpoint | granular scope |
| --- | --- |
| [Add a legal hold matter](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/addLegalHoldMatter) | `team_chat:write:legal_hold_matter:admin` |
| [Download legal hold files for given matter](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/downloadLegalHoldFiles) | `team_chat:read:legal_hold_matter_file:admin` |
| [List legal hold files by given matter](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listLegalHoldFiles) | `team_chat:read:list_legal_hold_matter_files:admin` |
| [Update legal hold matter](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateLegalHoldMatter) | `team_chat:update:legal_hold_matter:admin` |
| [List legal hold matters](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listLegalHoldMatters) | `team_chat:read:list_legal_hold_matters:admin` |
| [Delete legal hold matters](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteLegalHoldMatters) | `team_chat:delete:legal_hold_matter:admin` |

### Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-2)

| API endpoint | granular scope |
| --- | --- |
| [Get chat message reports](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/reportChatMessages) | `report:read:chat_session:admin` |
| [Get chat sessions reports](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/reportChatSessions) | `report:read:list_chat_sessions:admin` |

### Shared Spaces [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#shared-spaces)

| API endpoint | granular scope |
| --- | --- |
| [Remove members from a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteSpaceMembers) | `team_chat:delete:shared_space_members``team_chat:delete:shared_space_members:admin` |
| [List shared spaces](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listSharedSpaces) | `team_chat:read:list_shared_spaces``team_chat:read:list_shared_spaces:admin` |
| [List shared space members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listSharedSpaceMembers) | `team_chat:read:list_shared_space_members``team_chat:read:list_shared_space_members:admin` |
| [Delete a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/deleteSpace) | `team_chat:delete:shared_space``team_chat:delete:shared_space:admin` |
| [Get a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/getASharedSpace) | `team_chat:read:shared_space``team_chat:read:shared_space:admin` |
| [Update shared space settings](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateSharedSpaceSettings) | `team_chat:update:shared_space``team_chat:update:shared_space:admin` |
| [Promote shared space members to administrators](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/promoteSpaceMembers) | `team_chat:write:shared_space_administrators``team_chat:write:shared_space_administrators:admin` |
| [List shared space channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/listSharedSpaceChannels) | `team_chat:read:list_shared_space_channels``team_chat:read:list_shared_space_channels:admin` |
| [Add members to a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/addSpaceMembers) | `team_chat:write:shared_space_members``team_chat:write:shared_space_members:admin` |
| [Demote shared space administrators to members](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/demoteSpaceAdmins) | `team_chat:delete:shared_space_administrators``team_chat:delete:shared_space_administrators:admin` |
| [Create a shared space](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/createSpace) | `team_chat:write:shared_space``team_chat:write:shared_space:admin` |
| [Move shared space channels](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/updateSharedSpaceChannels) | `team_chat:update:shared_space_channels` |
| [Transfer shared space ownership](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/transferSpaceOwner) | `team_chat:update:shared_space_owner``team_chat:update:shared_space_owner:admin` |

## Workforce Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#workforce-management)

The following are the available **Workforce Management** APIs and their associated granular scopes.

### Filter groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#filter-groups)

| API endpoint | granular scope |
| --- | --- |
| \[List filter groups\](/docs/api/rest/reference/Workforce Management/methods/#operation/Listfiltergroups) | `workforce_management:read:list_filter_groups:admin` |

### Forecasts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#forecasts)

| API endpoint | granular scope |
| --- | --- |
| \[Get a forecast for a scheduling group\](/docs/api/rest/reference/Workforce Management/methods/#operation/Getforecastofschedulinggroup) | `workforce_management:read:forecasts:admin` |
| \[List forecasts\](/docs/api/rest/reference/Workforce Management/methods/#operation/Listforecasts) | `workforce_management:read:forecasts:admin` |

### Imports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#imports)

| API endpoint | granular scope |
| --- | --- |
| \[Upload historical queue metrics\](/docs/api/rest/reference/Workforce Management/methods/#operation/Uploadhistoricalqueuemetrics) | `workforce_management:write:queue_metrics:admin` |
| \[Delete historical agent status\](/docs/api/rest/reference/Workforce Management/methods/#operation/deleteHistoricalAgentStatus) | `workforce_management:delete:agent_status:admin` |
| \[Upload forecast staffing\](/docs/api/rest/reference/Workforce Management/methods/#operation/UploadStaffing) | `workforce_management:write:staffing:admin` |
| \[Upload forecast\](/docs/api/rest/reference/Workforce Management/methods/#operation/Uploadforecast) | `workforce_management:write:import_forecast:admin` |
| \[Get historical queue metrics import metadata\](/docs/api/rest/reference/Workforce Management/methods/#operation/Viewhistoricalqueuemetricimoprtmeta) | `workforce_management:read:queue_metrics:admin` |
| \[ Upload historical agent status \](/docs/api/rest/reference/Workforce Management/methods/#operation/uploadHistoricalAgentStatus) | `workforce_management:write:agent_status:admin` |

### Organizational Groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#organizational-groups)

| API endpoint | granular scope |
| --- | --- |
| \[Get multiple organizational groups\](/docs/api/rest/reference/Workforce Management/methods/#operation/getMultipleOrganizationalGroups) | `workforce_management:read:organizational_groups:admin` |
| \[Update an organizational group\](/docs/api/rest/reference/Workforce Management/methods/#operation/updateOrganizationalGroup) | `workforce_management:update:organizational_groups:admin` |
| \[Create an organizational group\](/docs/api/rest/reference/Workforce Management/methods/#operation/createOrganizationalGroup) | `workforce_management:write:organizational_groups:admin` |
| \[Get a single organizational group\](/docs/api/rest/reference/Workforce Management/methods/#operation/getOrganizationalGroup) | `workforce_management:read:organizational_groups:admin` |
| \[Delete organizational group\](/docs/api/rest/reference/Workforce Management/methods/#operation/deleteOrganizationalGroup) | `workforce_management:delete:organizational_groups:admin` |

### Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-3)

| API endpoint | granular scope |
| --- | --- |
| \[List all schedule agents\](/docs/api/rest/reference/Workforce Management/methods/#operation/listScheduleAgents) | `workforce_management:read:list_schedule_agents:admin` |
| \[List agents' adherence data\](/docs/api/rest/reference/Workforce Management/methods/#operation/listAdherenceAgents) | `workforce_management:read:list_adherence_agents:admin` |

### Schedules [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#schedules)

| API endpoint | granular scope |
| --- | --- |
| \[List all schedule agents\](/docs/api/rest/reference/Workforce Management/methods/#operation/listSchedules) | `workforce_management:read:list_schedule_agents:admin` |

### Scheduling groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#scheduling-groups)

| API endpoint | granular scope |
| --- | --- |
| \[List scheduling groups\](/docs/api/rest/reference/Workforce Management/methods/#operation/Listschedulinggroups) | `workforce_management:read:list_scheduling_groups:admin` |

### Users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users-1)

| API endpoint | granular scope |
| --- | --- |
| \[List users\](/docs/api/rest/reference/Workforce Management/methods/#operation/Listallusers) | `workforce_management:read:list_users:admin` |

## Zoom User [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-user)

The following are the available **Zoom User** APIs and their associated granular scopes.

### Divisions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#divisions)

| API endpoint | granular scope |
| --- | --- |
| [Create a division](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/Createadivision) | `division:write:division:admin` |
| [Get a division](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/Getdivision) | `division:read:division:admin` |
| [List divisions](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/listDivisions) | `division:read:list_divisions:admin` |
| [List division members](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/listDivisionMembers) | `division:read:member:admin` |
| [Delete a division](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/Deletedivision) | `division:delete:division:admin` |
| [Update a division](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/Updateadivision) | `division:update:division:admin` |
| [Assign a division](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/assigndivisionMember) | `division:write:member:admin` |

### Groups [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#groups-1)

| API endpoint | granular scope |
| --- | --- |
| [Delete Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/delGroupVB) | `group:delete:virtual_background_files:admin` |
| [Delete Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/delGroupVB) | `group:delete:virtual_background_files:master` |
| [Upload Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/uploadGroupVB) | `group:write:virtual_background_files:admin` |
| [Upload Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/uploadGroupVB) | `group:write:virtual_background_files:master` |
| [List group channels](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupChannels) | `group:read:list_channels:admin` |
| [List group channels](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupChannels) | `group:read:list_channels:master` |
| [Delete a group admin](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupAdminsDelete) | `group:delete:administrator:admin` |
| [Delete a group admin](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupAdminsDelete) | `group:delete:administrator:master` |
| [Update a group](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupUpdate) | `group:update:group:admin` |
| [Update a group](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupUpdate) | `group:update:group:master` |
| [Create a group](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupCreate) | `group:write:group:admin` |
| [Create a group](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupCreate) | `group:write:group:master` |
| [Get a group's settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/getGroupSettings) | `group:read:settings:admin` |
| [Get a group's settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/getGroupSettings) | `group:read:settings:master` |
| [Update a group's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupSettingsRegistrationUpdate) | `group:update:registration_settings:admin` |
| [Update a group's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupSettingsRegistrationUpdate) | `group:update:registration_settings:master` |
| \[Update meeting Waiting Room branding\](/docs/api/rest/reference/user/methods/#operation/Update meeting Waiting Room branding-copy-1post) | `group:write:waiting_room_branding:admin` |
| \[Update meeting Waiting Room branding\](/docs/api/rest/reference/user/ma/#operation/Update meeting Waiting Room branding-copy-1post) | `group:write:waiting_room_branding:master` |
| [List group admins](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupAdmins) | `group:read:administrator:admin` |
| [List group admins](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupAdmins) | `group:read:administrator:master` |
| [Delete a group member](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupMembersDelete) | `group:delete:member:admin` |
| [Delete a group member](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupMembersDelete) | `group:delete:member:master` |
| [Add group members](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupMembersCreate) | `group:write:member:admin` |
| [Add group members](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupMembersCreate) | `group:write:member:master` |
| [Update locked settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupLockedSettings) | `group:update:lock_settings:admin` |
| [Update locked settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupLockedSettings) | `group:update:lock_settings:master` |
| [Update a group's settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/updateGroupSettings) | `group:update:settings:admin` |
| [Update a group's settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/updateGroupSettings) | `group:update:settings:master` |
| [List groups](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groups) | `group:read:list_groups:admin` |
| [List groups](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groups) | `group:read:list_groups:master` |
| \[Update webinar Waiting Room branding\](/docs/api/rest/reference/user/methods/#operation/Update webinar Waiting Room branding-copy-1post) | `group:write:waiting_room_branding:admin` |
| \[Update webinar Waiting Room branding\](/docs/api/rest/reference/user/ma/#operation/Update webinar Waiting Room branding-copy-1post) | `group:write:waiting_room_branding:master` |
| [Get a group](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/group) | `group:read:group:admin` |
| [Get a group](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/group) | `group:read:group:master` |
| [Get locked settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/getGroupLockSettings) | `group:read:lock_settings:admin` |
| [Get locked settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/getGroupLockSettings) | `group:read:lock_settings:master` |
| [Add group admins](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupAdminsCreate) | `group:write:administrator:admin` |
| [List group members](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupMembers) | `group:read:list_members:admin` |
| [List group members](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupMembers) | `group:read:list_members:master` |
| [Update a group member](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/updateAGroupMember) | `group:update:member:admin` |
| [Update a group member](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/updateAGroupMember) | `group:update:member:master` |
| [Delete a group](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupDelete) | `group:delete:group:admin` |
| [Delete a group](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupDelete) | `group:delete:group:master` |
| [Get a group's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/groupSettingsRegistration) | `group:read:registration_settings:admin` |
| [Get a group's webinar registration settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/groupSettingsRegistration) | `group:read:registration_settings:master` |

### Users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users-2)

| API endpoint | granular scope |
| --- | --- |
| [List a user's collaboration devices](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/listCollaborationDevices) | `user:read:list_collaboration_devices``user:read:list_collaboration_devices:admin` |
| [Get user permissions](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userPermission) | `user:read:list_permissions``user:read:list_permissions:admin` |
| [Get user permissions](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userPermission) | `user:read:list_permissions:master` |
| [Delete a scheduler](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSchedulerDelete) | `user:delete:scheduler``user:delete:scheduler:admin` |
| [Delete a scheduler](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSchedulerDelete) | `user:delete:scheduler:master` |
| [Create users](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userCreate) | `user:write:user:admin` |
| [Create users](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userCreate) | `user:write:user:master` |
| [Add assistants](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userAssistantCreate) | `user:write:assistant``user:write:assistant:admin` |
| [Add assistants](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userAssistantCreate) | `user:write:assistant:master` |
| [Update a user's presence status](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/updatePresenceStatus) | `user:update:presence_status``user:update:presence_status:admin` |
| [Get a user](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/user) | `user:read:user``user:read:user:admin` |
| [Get a user](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/user) | `user:read:user:master` |
| \[Update webinar Waiting Room branding\](/docs/api/rest/reference/user/methods/#operation/Update webinar Waiting Room branding-copy-0post) | `user:write:waiting_room_branding``user:write:waiting_room_branding:admin` |
| \[Update webinar Waiting Room branding\](/docs/api/rest/reference/user/ma/#operation/Update webinar Waiting Room branding-copy-0post) | `user:write:waiting_room_branding:master` |
| [Update user settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSettingsUpdate) | `user:update:settings``user:update:settings:admin` |
| [Update user settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSettingsUpdate) | `user:update:settings:master` |
| [Upload a user's profile picture](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userPicture) | `user:write:profile_picture``user:write:profile_picture:admin` |
| [Upload a user's profile picture](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userPicture) | `user:write:profile_picture:master` |
| [Get user summary](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSummary) | `user:read:summary:admin` |
| [Get user summary](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSummary) | `user:read:summary:master` |
| [Delete user schedulers](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSchedulersDelete) | `user:delete:scheduler``user:delete:scheduler:admin` |
| [Delete user schedulers](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSchedulersDelete) | `user:delete:scheduler:master` |
| [Get meeting summary templates](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/Getmeetingsummarytemplates) | `user:read:settings``user:read:settings:admin` |
| [Get a user presence status](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/getUserPresenceStatus) | `user:read:presence_status``user:read:presence_status:admin` |
| [Update a user](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userUpdate) | `user:update:user``user:update:user:admin` |
| [Update a user](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userUpdate) | `user:update:user:master` |
| [List users](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/users) | `user:read:list_users:admin` |
| [List users](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/users) | `user:read:list_users:master` |
| [List user schedulers](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSchedulers) | `user:read:list_schedulers``user:read:list_schedulers:admin` |
| [List user schedulers](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSchedulers) | `user:read:list_schedulers:master` |
| [Delete a user assistant](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userAssistantDelete) | `user:delete:assistant``user:delete:assistant:admin` |
| [Delete a user assistant](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userAssistantDelete) | `user:delete:assistant:master` |
| [Delete a user](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userDelete) | `user:delete:user``user:delete:user:admin` |
| [Delete a user](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userDelete) | `user:delete:user:master` |
| [Delete user assistants](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userAssistantsDelete) | `user:delete:assistant``user:delete:assistant:admin` |
| [Delete user assistants](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userAssistantsDelete) | `user:delete:assistant:master` |
| [List user assistants](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userAssistants) | `user:read:list_assistants``user:read:list_assistants:admin` |
| [List user assistants](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userAssistants) | `user:read:list_assistants:master` |
| [Update user status](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userStatus) | `user:update:status``user:update:status:admin` |
| [Update user status](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userStatus) | `user:update:status:master` |
| [Get the user's ZAK](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userZak) | `user:read:zak``user:read:zak:admin` |
| [Update a user's email](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userEmailUpdate) | `user:update:email``user:update:email:admin` |
| [Update a user's email](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userEmailUpdate) | `user:update:email:master` |
| [Revoke a user's SSO token](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSSOTokenDelete) | `user:delete:token``user:delete:token:admin` |
| [Revoke a user's SSO token](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSSOTokenDelete) | `user:delete:token:master` |
| [Delete Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/delUserVB) | `user:delete:virtual_background_files``user:delete:virtual_background_files:admin` |
| [Delete Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/delUserVB) | `user:delete:virtual_background_files:master` |
| [Upload Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/uploadVBuser) | `user:write:virtual_background_files``user:write:virtual_background_files:admin` |
| [Upload Virtual Background files](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/uploadVBuser) | `user:write:virtual_background_files:master` |
| [Get a user's token](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userToken) | `user:read:token``user:read:token:admin` |
| [Get a user's token](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userToken) | `user:read:token:master` |
| [Bulk update features for users](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/bulkUpdateFeature) | `user:write:feature:admin` |
| [Bulk update features for users](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/bulkUpdateFeature) | `user:write:feature:master` |
| [Get user settings](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSettings) | `user:read:settings``user:read:settings:admin` |
| [Get user settings](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userSettings) | `user:read:settings:master` |
| [Get collaboration device detail](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/getCollaborationDevice) | `user:read:collaboration_device``user:read:collaboration_device:admin` |
| [Check a user's PM room](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userVanityName) | `user:read:pm_room``user:read:pm_room:admin` |
| [Update a user's password](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userPassword) | `user:update:password``user:update:password:admin` |
| [Update a user's password](https://developers.zoom.us/docs/api/rest/reference/user/ma/#operation/userPassword) | `user:update:password:master` |
| [Check a user email](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userEmail) | `user:read:email``user:read:email:admin` |
| \[Update meeting Waiting Room branding\](/docs/api/rest/reference/user/methods/#operation/Update meeting Waiting Room branding-copy-0post) | `user:write:waiting_room_branding:admin``user:write:waiting_room_branding` |
| \[Update meeting Waiting Room branding\](/docs/api/rest/reference/user/ma/#operation/Update meeting Waiting Room branding-copy-0post) | `user:write:waiting_room_branding:master` |

## Zoom Billing [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-billing)

The following are the available **Zoom Billing** APIs and their associated granular scopes.

### Billing [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#billing)

| API endpoint | granular scope |
| --- | --- |
| [Cancel a base plan](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/CancelABasePlan) | `billing:update:cancel_plan:master` |
| [Get AI credits limit](https://developers.zoom.us/docs/api/rest/reference/billing/methods/#operation/GetAiCreditsLimits) | `billing:read:billing_information``billing:read:billing_information:admin``billing:read:billing_information:master` |
| [Download subaccounts' billing invoice reports](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/downloadBillingInvoiceReport) | `billing:read:download_invoice_reports:master` |
| [Download an invoice file](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/downloadInvoicePDF) | `billing:read:download_invoice_file:master` |
| [Get account subscriptions information](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetAccountMsqPlanInformation) | `billing:read:plan_information:admin``billing:read:plan_information:master` |
| [Update billing information](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/UpdateBillingInformation) | `billing:update:billing_information:master` |
| [Get AI credits balance](https://developers.zoom.us/docs/api/rest/reference/billing/methods/#operation/GetAiCreditsBalance) | `billing:read:billing_information``billing:read:billing_information:admin``billing:read:billing_information:master` |
| [List upcoming renewal accounts](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/Getupcomingrenewalaccounts) | `billing:read:list_upcoming_renewal_accounts:master` |
| [Update a base plan](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/UpdateABasePlan) | `billing:update:plan:master` |
| [Get plan usage](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetPlanUsage) | `billing:read:plan_usage:master``billing:read:plan_usage:admin` |
| [Get invoice details](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetInvoiceDetails) | `billing:read:invoice_details:master``billing:read:invoice_details:admin` |
| [Update an account's additional plan](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/UpdateAnAccount'sAdditionalPlan) | `billing:update:additional_plans:master` |
| [Get account plan information](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetAccountPlanInformation) | `billing:read:plan_information:master``billing:read:plan_information:admin` |
| [Get billing information](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetBillingInformation) | `billing:read:billing_information:master``billing:read:billing_information:admin` |
| [List billing invoices](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/ListBillingInvoices) | `billing:read:list_invoices:master``billing:read:list_invoices:admin` |
| [Update AI credits limit](https://developers.zoom.us/docs/api/rest/reference/billing/methods/#operation/UpdateAiCreditsLimits) | `billing:update:billing_information``billing:update:billing_information:admin``billing:update:billing_information:master` |
| [Subscribe subaccount to an additional plan](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/SubscribeAccountToAnAdditionalPlan) | `billing:write:subscribe_additional_plans:master` |
| [Get AI credits usage](https://developers.zoom.us/docs/api/rest/reference/billing/methods/#operation/GetAiCreditsUsage) | `billing:read:billing_information``billing:read:billing_information:admin``billing:read:billing_information:master` |
| [Get account subscriptions usage](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/GetMsqPlanUsage) | `billing:read:plan_usage:admin``billing:read:plan_usage:master` |
| [Cancel additional plans](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/CancelAdditionalPlans) | `billing:update:cancel_additional_plans:master` |
| [Download an invoice file (v2)](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/downloadInvoicePDFFile) | `billing:read:download_invoice_file:master` |
| [Delete subaccounts' billing invoice report](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/deleteBillingInvoiceReport) | `billing:delete:invoice_report:master` |
| [Subscribe an account to a plan](https://developers.zoom.us/docs/api/rest/reference/billing/ma/#operation/SubscribeAccountToAPlan) | `billing:write:subscribe_plan:master` |

## Zoom Scheduler [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-scheduler)

The following are the available **Zoom Scheduler** APIs and their associated granular scopes.

### Routing Forms [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#routing-forms)

| API endpoint | granular scope |
| --- | --- |
| [get routing response](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Getroutingresponse) | `scheduler:read:routing``scheduler:read:routing:admin` |
| [list account routing response](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/list_account_routing_response) | `scheduler:read:routing``scheduler:read:routing:admin` |

### analytics [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#analytics)

| API endpoint | granular scope |
| --- | --- |
| [Report analytics](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/report_analytics) | `scheduler:read:analytics``scheduler:read:analytics:admin` |

### availability [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#availability)

| API endpoint | granular scope |
| --- | --- |
| [Get availability](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/get_availability) | `scheduler:read:availability``scheduler:read:availability:admin` |
| [Patch availability](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/patch_availability) | `scheduler:update:availability``scheduler:update:availability:admin` |
| [Insert availability](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/insert_availability) | `scheduler:write:availability``scheduler:write:availability:admin` |
| [Delete availability](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/delete_availability) | `scheduler:delete:availability``scheduler:delete:availability:admin` |
| [List availability](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/list_availability) | `scheduler:read:list_availability``scheduler:read:list_availability:admin` |

### scheduled events [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#scheduled-events)

| API endpoint | granular scope |
| --- | --- |
| [Patch scheduled events](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/patch_scheduled_events) | `scheduler:update:scheduled_event``scheduler:update:scheduled_event:admin` |
| [Create a booking for a schedule slot](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/create_booking) | `scheduler:write:scheduled_event``scheduler:write:scheduled_event:admin` |
| [List scheduled events](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/list_scheduled_events) | `scheduler:read:list_scheduled_events``scheduler:read:list_scheduled_events:admin` |
| [Get scheduled event attendee](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/get_scheduled_event_attendee) | `scheduler:read:scheduled_event_attendee``scheduler:read:scheduled_event_attendee:admin` |
| [Get scheduled events](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/get_scheduled_events) | `scheduler:read:scheduled_event``scheduler:read:scheduled_event:admin` |
| [Delete scheduled events](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/delete_scheduled_events) | `scheduler:delete:scheduled_event``scheduler:delete:scheduled_event:admin` |

### schedules [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#schedules-1)

| API endpoint | granular scope |
| --- | --- |
| [List schedules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/list_schedules) | `scheduler:read:list_schedule``scheduler:read:list_schedule:admin` |
| [Patch schedules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/patch_schedule) | `scheduler:update:patch_schedule``scheduler:update:patch_schedule:admin` |
| [Insert schedules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/insert_schedule) | `scheduler:write:insert_schedule``scheduler:write:insert_schedule:admin` |
| [Get schedules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/get_schedule) | `scheduler:read:get_schedule``scheduler:read:get_schedule:admin` |
| [Delete schedules](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/delete_schedules) | `scheduler:delete:delete_schedule``scheduler:delete:delete_schedule:admin` |
| [List schedule available times](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/list_available_time) | `scheduler:read:get_schedule``scheduler:read:get_schedule:admin` |

### scheduling links [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#scheduling-links)

| API endpoint | granular scope |
| --- | --- |
| [Single use link](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/single_use_link) | `scheduler:write:single_use_link``scheduler:write:single_use_link:admin` |

### shares [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#shares)

| API endpoint | granular scope |
| --- | --- |
| [Create shares](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/create_shares) | `scheduler:write:share``scheduler:write:share:admin` |

### team [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#team)

| API endpoint | granular scope |
| --- | --- |
| [List team](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/Listteam) | `scheduler:read:get_schedule``scheduler:read:get_schedule:admin` |

### users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users-3)

| API endpoint | granular scope |
| --- | --- |
| [Get user](https://developers.zoom.us/docs/api/rest/reference/phone/methods/#operation/get_user) | `scheduler:read:user``scheduler:read:user:admin` |

## Video SDK [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#video-sdk)

The following are the available **Video SDK** APIs and their associated granular scopes.

### Byos Storage [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#byos-storage)

| API endpoint | granular scope |
| --- | --- |
| [Change storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStorageDetailPatch) | `video_sdk:update:storage_location_detail:admin` |
| [Change storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStorageDetailPatch) | `video_sdk:update:storage_location_detail:master` |
| [Add storage location](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStoragePost) | `video_sdk:write:storage_location:admin` |
| [Add storage location](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStoragePost) | `video_sdk:write:storage_location:master` |
| [Update Bring Your Own Storage settings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStorageSwitchPatch) | `video_sdk:update:storage_location_settings:admin` |
| [Update Bring Your Own Storage settings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStorageSwitchPatch) | `video_sdk:update:storage_location_settings:master` |
| [Delete storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStorageDetailDelete) | `video_sdk:delete:storage_location_detail:admin` |
| [Delete storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStorageDetailDelete) | `video_sdk:delete:storage_location_detail:master` |
| [Storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStorageDetailGet) | `video_sdk:read:storage_location_detail:admin` |
| [Storage location detail](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStorageDetailGet) | `video_sdk:read:storage_location_detail:master` |
| [List storage location](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/byosStorageGet) | `video_sdk:read:storage_location:admin` |
| [List storage location](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/byosStorageGet) | `video_sdk:read:storage_location:master` |

### Cloud Recording [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cloud-recording-1)

| API endpoint | granular scope |
| --- | --- |
| [Recover a single recording](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingStatusUpdateOne) | `video_sdk:update:recover_recording_file:admin` |
| [Recover a single recording](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingStatusUpdateOne) | `video_sdk:update:recover_recording_file:master` |
| [Delete session's recording file](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingDeleteOne) | `video_sdk:delete:recording_file:admin` |
| [Delete session's recording file](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingDeleteOne) | `video_sdk:delete:recording_file:master` |
| [Delete session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingDelete) | `video_sdk:delete:session_recordings:admin` |
| [Delete session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingDelete) | `video_sdk:delete:session_recordings:master` |
| [List recordings of an account](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingsList) | `video_sdk:read:list_account_recordings:admin` |
| [List recordings of an account](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingsList) | `video_sdk:read:list_account_recordings:master` |
| [List session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingGet) | `video_sdk:read:list_session_recordings:admin` |
| [List session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingGet) | `video_sdk:read:list_session_recordings:master` |
| [Recover session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/recordingStatusUpdate) | `video_sdk:update:recover_session_recordings:admin` |
| [Recover session's recordings](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/recordingStatusUpdate) | `video_sdk:update:recover_session_recordings:master` |

### Sessions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sessions)

| API endpoint | granular scope |
| --- | --- |
| [Get a session SIP URI with passcode](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/GetASessionSIPURIWithPasscode) | `video_sdk:write:session_sip_dialing:admin` |
| [Get session user QoS](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionUserQOS) | `video_sdk:read:seesion_user_qos:admin` |
| [Get session user QoS](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionUserQOS) | `video_sdk:read:seesion_user_qos:master` |
| [List sessions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessions) | `video_sdk:read:session_list:admin` |
| [List sessions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessions) | `video_sdk:read:session_list:master` |
| [List session users](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionUsers) | `video_sdk:read:session_users:admin` |
| [List session users](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionUsers) | `video_sdk:read:session_users:master` |
| [Update session status](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionStatus) | `video_sdk:update:session_status:admin` |
| [Update session status](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionStatus) | `video_sdk:update:session_status:master` |
| [Update a session live stream](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionLiveStreamUpdate) | `video_sdk:update:session_livestream:admin` |
| [Update a session live stream](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionLiveStreamUpdate) | `video_sdk:update:session_livestream:master` |
| [Get a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Getastreamingestion) | `video_sdk:read:stream_ingestion:admin` |
| [Get a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Getastreamingestion) | `video_sdk:read:stream_ingestion:master` |
| [Update session livestream status](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionLiveStreamStatusUpdate) | `video_sdk:update:session_livestream_status:admin` |
| [Update session livestream status](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionLiveStreamStatusUpdate) | `video_sdk:update:session_livestream_status:master` |
| [List stream ingestions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Liststreamingestions) | `video_sdk:read:list_stream_ingestions:admin` |
| [List stream ingestions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Liststreamingestions) | `video_sdk:read:list_stream_ingestions:master` |
| [Get session details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionDetail) | `video_sdk:read:session_detail:admin` |
| [Get session details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionDetail) | `video_sdk:read:session_detail:master` |
| [Get sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionParticipantShare) | `video_sdk:read:session_user_sharing:admin` |
| [Get sharing/recording details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionParticipantShare) | `video_sdk:read:session_user_sharing:master` |
| [List session streaming ingestions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Listsessionstreamingingestions) | `video_sdk:read:list_session_stream_ingestions:admin` |
| [List session streaming ingestions](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Listsessionstreamingingestions) | `video_sdk:read:list_session_stream_ingestions:master` |
| [Create a session](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Createasession) | `video_sdk:write:session:admin` |
| [Create a session](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Createasession) | `video_sdk:write:session:master` |
| [Delete a session](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionDelete) | `video_sdk:delete:session:admin` |
| [Delete a session](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionDelete) | `video_sdk:delete:session:master` |
| [Use in-session events controls](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/inSessionEventsControl) | `video_sdk:update:in_session_controls:admin` |
| [Use in-session events controls](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/inSessionEventsControl) | `video_sdk:update:in_session_controls:master` |
| [List session users QoS](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/sessionUsersQOS) | `video_sdk:read:session_users_qos:admin` |
| [List session users QoS](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/sessionUsersQOS) | `video_sdk:read:session_users_qos:master` |
| [Delete a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Deleteastreamingestion) | `video_sdk:delete:stream_ingestion:admin` |
| [Delete a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Deleteastreamingestion) | `video_sdk:delete:stream_ingestion:master` |
| [Create a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Createastreamingestion) | `video_sdk:write:stream_ingestion:admin` |
| [Create a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Createastreamingestion) | `video_sdk:write:stream_ingestion:master` |
| [Get session live stream details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/getLiveStreamDetails) | `video_sdk:read:session_livestream:admin` |
| [Get session live stream details](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/getLiveStreamDetails) | `video_sdk:read:session_livestream:master` |
| [Update Realtime Media Streams (RTMS) app status](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/updateSessionRtmsAppStatus) | `video_sdk:update:session_rtms_app_status:admin` |
| [Update a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/Updateastreamingestion) | `video_sdk:update:stream_ingestion:admin` |
| [Update a stream ingestion](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/Updateastreamingestion) | `video_sdk:update:stream_ingestion:master` |

### Video SDK Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#video-sdk-reports)

| API endpoint | granular scope |
| --- | --- |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/vsdkReportOperationLogs) | `video_sdk:read:operation_log:admin` |
| [Get operation logs report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/vsdkReportOperationLogs) | `video_sdk:read:operation_log:master` |
| [Get telephone report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/vsdkReportTelephone) | `video_sdk:read:telephone:admin` |
| [Get telephone report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/vsdkReportTelephone) | `video_sdk:read:telephone:master` |
| [Get daily usage report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/methods/#operation/vsdkReportDaily) | `video_sdk:read:daily_report:admin` |
| [Get daily usage report](https://developers.zoom.us/docs/api/rest/reference/video-sdk/ma/#operation/vsdkReportDaily) | `video_sdk:read:daily_report:master` |

## Workflow [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#workflow)

The following are the available **Workflow** APIs and their associated granular scopes.

### ai [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#ai)

| API endpoint | granular scope |
| --- | --- |
| [Start an ad-hoc agentic workflow asynchronously](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/executeAgenticWorkflowAsync) | `workflow:write:definition``workflow:write:definition:admin` |
| [List user-owned agentic workflows](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/listAgenticWorkflows) | `workflow:read:definition``workflow:read:definition:admin` |
| [Get an agentic workflow definition](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/getAgenticWorkflowDefinition) | `workflow:read:definition:admin``workflow:read:definition` |
| [Undeploy an agentic workflow](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/undeployAgenticWorkflow) | `workflow:write:definition``workflow:write:definition:admin` |
| [Get an agentic workflow execution](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/getAgenticWorkflowExecution) | `workflow:read:definition``workflow:read:definition:admin` |
| [Describe an agentic workflow node](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/describeAgenticWorkflowNode) | `workflow:read:definition``workflow:read:definition:admin` |
| [Resume an agentic workflow waiting for human input](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/resumeAgenticWorkflowExecution) | `workflow:write:definition``workflow:write:definition:admin` |
| [Create or update and deploy an agentic workflow](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/deployAgenticWorkflow) | `workflow:write:definition``workflow:write:definition:admin` |
| [List activities for a published agentic workflow](https://developers.zoom.us/docs/api/rest/reference/Workflow/methods/#operation/listAgenticWorkflowActivities) | `workflow:read:list_definitions``workflow:read:list_definitions:admin` |

## AI Companion [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#ai-companion)

The following are the available **AI Companion** APIs and their associated granular scopes.

### Archived [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#archived)

| API endpoint | granular scope |
| --- | --- |
| \[Get AI Companion conversation archives\](/docs/api/rest/reference/AI Companion/methods/#operation/GetAICconversationarchives) | `aic:read:conversation_archives:admin` |

## Zoom Quality Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-quality-management)

The following are the available **Zoom Quality Management** APIs and their associated granular scopes.

### Calibrations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#calibrations)

| API endpoint | granular scope |
| --- | --- |
| \[List calibrations\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/ListCalibrations) | `zoom_quality_management:read:calibrations``zoom_quality_management:read:calibrations:admin` |
| \[Get calibration detail\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/GetCalibrationDetail) | `zoom_quality_management:read:calibrations``zoom_quality_management:read:calibrations:admin` |

### Cases [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cases)

| API endpoint | granular scope |
| --- | --- |
| \[Get case details\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/getCaseDetails) | `zoom_quality_management:read:cases``zoom_quality_management:read:cases:admin` |
| \[List cases\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/listCases) | `zoom_quality_management:read:cases``zoom_quality_management:read:cases:admin` |

### Evaluations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#evaluations)

| API endpoint | granular scope |
| --- | --- |
| \[List automated evaluations\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/ListAutomatedEvaluations) | `zoom_quality_management:read:evaluations:admin``zoom_quality_management:read:evaluations` |
| \[View evaluation detail\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/EvaluationDetail) | `zoom_quality_management:read:evaluations``zoom_quality_management:read:evaluations:admin` |
| \[List evaluations\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/Listevaluations) | `zoom_quality_management:read:evaluations``zoom_quality_management:read:evaluations:admin` |

### Interactions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#interactions)

| API endpoint | granular scope |
| --- | --- |
| \[View interaction detail\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/InteractionDetail) | `zoom_quality_management:read:interactions``zoom_quality_management:read:interactions:admin` |
| \[Add an interaction\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/Addinteraction) | `zoom_quality_management:write:interactions``zoom_quality_management:write:interactions:admin` |
| \[List interactions\](/docs/api/rest/reference/Zoom Quality Management/methods/#operation/ListInteractions) | `zoom_quality_management:read:interactions``zoom_quality_management:read:interactions:admin` |

## Zoom Revenue Accelerator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-revenue-accelerator)

The following are the available **Zoom Revenue Accelerator** APIs and their associated granular scopes.

### Accounts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#accounts-2)

| API endpoint | granular scope |
| --- | --- |
| [Get indicators settings \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/accountSettingsIndicatorsDeprecated) | `zra:read:indicator``zra:read:indicator:admin` |
| [Get indicators settings](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/accountIndicatorsSettings) | `zra:read:indicator``zra:read:indicator:admin` |

### Conversations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#conversations)

| API endpoint | granular scope |
| --- | --- |
| [Upload iq multipart file.](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UploadZraMultipartFile.) | `zra:write:file``zra:write:file:admin` |
| [Get conversation comments \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationCommentsDeprecated) | `zra:read:list_conversation_comments``zra:read:list_conversation_comments:admin` |
| [Delete conversation's comment \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/deleteConversationCommentDeprecated) | `zra:delete:conversation_comment``zra:delete:conversation_comment:admin` |
| [Add new comments to the conversation \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/addConversationCommentDeprecated) | `zra:write:conversation_comment``zra:write:conversation_comment:admin` |
| [Add new comments to the conversation](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/addConversationComments) | `zra:read:list_conversation_comments``zra:read:list_conversation_comments:admin` |
| [Get conversation content analysis \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationContentAnalysisDeprecated) | `zra:read:conversation_analysis``zra:read:conversation_analysis:admin` |
| [Get a user's playlist \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getUserPlaylistDeprecated) | `zra:read:list_conversation_playlists``zra:read:list_conversation_playlists` |
| [Get conversation comments](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationCommentsById) | `zra:read:list_conversation_comments``zra:read:list_conversation_comments:admin` |
| [List conversations \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/listConversationsDeprecated) | `zra:read:list_conversations``zra:read:list_conversations:admin` |
| [Update conversation host id to new host id by conversation id \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UpdateconversationhostidtonewhostidbyconversationidDeprecated) | `zra:update:conversation_host``zra:update:conversation_host:admin` |
| [Delete conversation by conversation ID \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/deleteConversationDeprecated) | `zra:delete:conversations``zra:delete:conversations:admin` |
| [Get conversation content analysis](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationContentAnalysisById) | `zra:read:conversation_analysis``zra:read:conversation_analysis:admin` |
| [Update conversation host id to new host id by conversation id](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UpdateConversationhostid2NewHostidByConversationId) | `zra:update:conversation_host``zra:update:conversation_host:admin` |
| [Delete conversation's comment](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/deleteConversationCommentById) | `zra:delete:conversation_comment``zra:delete:conversation_comment:admin` |
| [Upload iq multipart file. \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UploadIqMultipartFileDeprecated) | `zra:write:file``zra:write:file:admin` |
| [Get conversation information \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationInfoDeprecated) | `zra:read:conversations:admin``zra:read:conversations` |
| [Add conversation by meeting record url or meeting UUID.](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/addConversationByRecord) | `zra:write:conversation``zra:write:conversation:admin` |
| [Upload IQ file](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UploadZraFile) | `zra:write:file``zra:write:file:admin` |
| [Add conversation by file id or download url.](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AddConversationByFileIdOrDownloadUrl) | `zra:write:conversation``zra:write:conversation:admin` |
| [Add conversation by file id or download url. \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AddConversationByFileIdOrDownloadUrlDeprecated) | `zra:write:conversation``zra:write:conversation:admin` |
| [Edit conversation comment \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/editConversationCommentDeprecated) | `zra:update:conversation_comment``zra:update:conversation_comment:admin` |
| [Get conversation information](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationDetail) | `zra:read:conversations:admin``zra:read:conversations` |
| [Get conversation scorecards \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationScorecardsDeprecated) | `zra:read:conversation_scorecards``zra:read:conversation_scorecards:admin` |
| [Upload IQ file \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UploadIQFileDeprecated) | `zra:write:file``zra:write:file:admin` |
| [Initiate and complete a multipart upload.](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/InitiateAndCompleteAMultipartUpload) | `zra:write:file``zra:write:file:admin` |
| \[Initiate and complete a multipart upload. \[Deprecated\]\](/docs/api/rest/reference/iq/methods/#operation/InitiateAndCompleteAMultipartUpload. \[Deprecated\]) | `zra:write:file``zra:write:file:admin` |
| [Get a user's playlist](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getUserPlaylists) | `zra:read:list_conversation_playlists``zra:read:list_conversation_playlists` |
| [List conversations](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/listAllConversations) | `zra:read:list_conversations``zra:read:list_conversations:admin` |
| [Get conversation interactions](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationInteraction) | `zra:read:conversation_participants``zra:read:conversation_participants:admin` |
| [Edit conversation comment](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/editConversationCommentById) | `zra:update:conversation_comment``zra:update:conversation_comment:admin` |
| [Delete conversation by conversation ID](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/deleteConversationById) | `zra:delete:conversations``zra:delete:conversations:admin` |
| [Get conversation scorecards](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationScorecardsById) | `zra:read:conversation_scorecards``zra:read:conversation_scorecards:admin` |
| [Get conversation interactions \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getConversationInteractionsDeprecated) | `zra:read:conversation_participants``zra:read:conversation_participants:admin` |
| [Add conversation by meeting record url or meeting UUID. \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/addConversationDeprecated) | `zra:write:conversation``zra:write:conversation:admin` |

### Custom CRM [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#custom-crm)

| API endpoint | granular scope |
| --- | --- |
| [Unregister CRM API connection](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/unregisterCrm) | `zra:delete:crm_registration:admin` |
| [Get imported CRM leads](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getCrmLeads) | `zra:read:crm_lead:admin` |
| [Bulk import CRM leads](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/bulkImportLeads) | `zra:write:crm_lead:admin` |
| [Get imported CRM contacts](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getCrmContacts) | `zra:read:crm_contact:admin` |
| [Get current CRM API registration](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getCrmRegistration) | `zra:read:crm_registration:admin` |
| [Get imported CRM deals](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getCrmDeals) | `zra:read:crm_deal:admin` |
| [Register CRM API connection](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/registerCrm) | `zra:write:crm_registration:admin` |
| [Get imported CRM accounts](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getCrmAccounts) | `zra:read:crm_account:admin` |
| [Bulk import CRM accounts](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/bulkImportAccounts) | `zra:write:crm_accounts:admin` |
| [Bulk import CRM contacts](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/bulkImportContacts) | `zra:write:crm_contact:admin` |
| [Bulk import CRM deals](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/bulkImportDeals) | `zra:write:crm_deal:admin` |
| [Poll async task result](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getAsyncTask) | `zra:read:crm_task:admin` |

### Deals [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#deals)

| API endpoint | granular scope |
| --- | --- |
| [Delete activity from the deal](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/DeleteActivityFromDeal) | `zra:delete:deal_activity``zra:delete:deal_activity:admin` |
| [Get deal information \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getDealInfoDeprecated) | `zra:read:deal``zra:read:deal:admin` |
| [List deals](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/listAllDeals) | `zra:read:list_deals``zra:read:list_deals:admin` |
| [Get deal activities \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getDealActivitiesDeprecated) | `zra:read:list_deal_activities``zra:read:list_deal_activities:admin` |
| [Get deal information](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getDealDetail) | `zra:read:deal``zra:read:deal:admin` |
| [Get deal activities](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/geAllActivitiesFromDeal) | `zra:read:list_deal_activities``zra:read:list_deal_activities:admin` |
| [List deals \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/listDealsDeprecated) | `zra:read:list_deals``zra:read:list_deals:admin` |
| [Delete activity from the deal \[Deprecated\]](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/DeleteActivityFromTheDealDeprecated) | `zra:delete:deal_activity``zra:delete:deal_activity:admin` |

### ScheduleMeetings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#schedulemeetings)

| API endpoint | granular scope |
| --- | --- |
| [List scheduled meetings](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/Listallscheduledmeetings) | `zra:read:list_conversations``zra:read:list_conversations:admin` |

### Teams [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#teams)

| API endpoint | granular scope |
| --- | --- |
| [Delete Team](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/DeleteTeam) | `zra:delete:team:admin` |
| [Get Team Detail](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/GetTeamDetail) | `zra:read:team:admin` |
| [Assign Team Managers](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AssignTeamManagers) | `zra:write:team_manages:admin` |
| [Assign Team Members](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AssignTeamMembers) | `zra:write:team_members:admin` |
| [List Account Teams](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/ListTeams) | `zra:read:team_list:admin``zra:read:team_list` |
| [List Unassigned Team Users](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/ListUnassignedTeamUsers) | `zra:read:unassigned_team_users:admin` |
| [List Team Managers](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/ListTeamManagers) | `zra:read:team_managers:admin``zra:read:team_managers` |
| [Move team to new parent](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/MoveTeam) | `zra:update:team:admin` |
| [List Team Members](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/ListTeamMembers) | `zra:read:team_members:admin``zra:read:team_members` |
| [Remove additional access from current team](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/DeleteSharedFromTeams) | `zra:delete:team:admin` |
| [Update Team name](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UpdateTeam) | `zra:update:team:admin` |
| [Unassign Team Members](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UnassignTeamMembers) | `zra:delete:team_members:admin` |
| [Create Team](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/CreateTeam) | `zra:write:team:admin` |
| [Grant additional access to current team](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AddSharedFromTeams) | `zra:write:team:admin` |
| [Remove additional access from target teams](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/DeleteSharedToTeams) | `zra:delete:team:admin` |
| [Unassign Team Managers](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/UnassignTeamManagers) | `zra:delete:team_managers:admin` |
| [Grant additional access to target teams](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/AddSharedToTeams) | `zra:write:team:admin` |

### Users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users-4)

| API endpoint | granular scope |
| --- | --- |
| [Get User info](https://developers.zoom.us/docs/api/rest/reference/iq/methods/#operation/getUserInfo) | `zra:read:user``zra:read:user:admin` |

## Cobrowse SDK [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cobrowse-sdk)

The following are the available **Cobrowse SDK** APIs and their associated granular scopes.

### Sessions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sessions-1)

| API endpoint | granular scope |
| --- | --- |
| \[List past sessions\](/docs/api/rest/reference/Cobrowse SDK/methods/#operation/Listpastsession) | `cobrowse_sdk:read:list_past_sessions:admin` |
| \[Get session details\](/docs/api/rest/reference/Cobrowse SDK/methods/#operation/Getasession) | `cobrowse_sdk:read:session_details:admin` |
| \[List session users\](/docs/api/rest/reference/Cobrowse SDK/methods/#operation/Listsessionusers) | `cobrowse_sdk:read:list_session_users:admin` |
| \[List live sessions\](/docs/api/rest/reference/Cobrowse SDK/methods/#operation/Listlivesessions) | `cobrowse_sdk:read:list_live_sessions:admin` |

## Integration Healthcare [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#integration-healthcare)

The following are the available **Integration Healthcare** APIs and their associated granular scopes.

### clinicalnotes [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#clinicalnotes)

| API endpoint | granular scope |
| --- | --- |
| \[List clinical notes\](/docs/api/rest/reference/Integration Healthcare/methods/#operation/GetClinicalNote) | `healthcare:read:list_clinical_notes:admin``healthcare:read:list_clinical_notes:master` |
| \[Get a Clinical Note\](/docs/api/rest/reference/Integration Healthcare/methods/#operation/GetaClinicalNote) | `healthcare:read:clinical_notes:admin``healthcare:read:clinical_notes:master` |
| \[Update a Clinical Note\](/docs/api/rest/reference/Integration Healthcare/methods/#operation/UpdateClinicalNote) | `healthcare:update:clinical_notes:admin``healthcare:update:clinical_notes:master` |

## Zoom Rooms [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-1)

The following are the available **Zoom Rooms** APIs and their associated granular scopes.

### Room Apps [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#room-apps)

| API endpoint | granular scope |
| --- | --- |
| [Config Zoom Room Controller Apps](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ConfigZoomRoomControllerApps) | `zoom_rooms:write:zoom_apps:admin` |

### Visitor Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#visitor-management)

| API endpoint | granular scope |
| --- | --- |
| [Get a list of visitors by location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/invitationList) | `visitor_management:read:list_invitations``visitor_management:read:list_invitations:admin` |
| [Invitation details by invitationID](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getInvitation) | `visitor_management:read:invitation_details``visitor_management:read:invitation_details:admin` |
| [Update an invitation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateInvitation) | `visitor_management:update:invitation``visitor_management:update:invitation:admin` |
| [Send an invitation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/createInvitation) | `visitor_management:write:invitation``visitor_management:write:invitation:admin` |
| [Check in a visitor](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/checkinVisitor) | `visitor_management:write:check_in``visitor_management:write:check_in:admin` |
| [Delete an Invitation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteInvitation) | `visitor_management:delete:invitation``visitor_management:delete:invitation:admin` |

### Workspaces [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#workspaces)

| API endpoint | granular scope |
| --- | --- |
| [Add a workspace photo](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddaWorkspacephoto) | `workspace:write:workspace:admin` |
| [Get a floor's reservations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getafloor'sreservations) | `workspace:read:list_floor_workspace_reservations:admin``workspace:read:list_floor_workspace_reservations:master` |
| [Create a reservation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/createReservation) | `workspace:write:reservation``workspace:write:reservation:admin` |
| [Get a workspace's reservations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listReservations) | `workspace:read:list_reservations``workspace:read:list_reservations:admin` |
| [Delete workspace photos](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteaWorkspacephoto) | `workspace:delete:photo:admin` |
| [Get a workspace](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getWorkspace) | `workspace:read:list_workspaces``workspace:read:list_workspaces:admin` |
| [Get a neighborhood](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetNeighborhood) | `workspace:read:neighborhood:admin` |
| [Update a reservation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateReservation) | `workspace:update:reservation``workspace:update:reservation:admin` |
| [Edit a workspace asset](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/PatchWorkspaceasset) | `workspace:update:asset:admin` |
| [Delete Workspace floor map](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteWorkspaceFloorMap) | `workspace:write:location``workspace:write:location:admin` |
| [Create a workspace](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/createWorkspace) | `workspace:write:workspace:admin` |
| [List workspace reservation questionnaires](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Listworkspacereservationquestionnaires) | `workspace:read:reservation:admin``workspace:read:reservation:master` |
| [List workspace additional information with time range](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getaworkspaceadditionalenhancements) | `workspace:read:list_workspaces``workspace:read:list_workspaces:admin` |
| [List released workspaces by timeout](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getWorksapceReservationReleaseInof) | `zoom_rooms:read:list_release_infos:admin` |
| [Check in/out of a reservation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/reservationEvent) | `workspace:write:events``workspace:write:events:admin` |
| [Get all workspace assets](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getallworkspaceassets) | `workspace:read:asset:admin` |
| [Create a workspace asset](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddaWorkspaceasset) | `workspace:write:asset:admin` |
| [List workspace reservations by locations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getworkspacereservationsinlocations) | `workspace:read:list_reservations:admin``workspace:read:list_reservations:master` |
| [Get a workspace reservation by reservationId](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GETGetaworkspacereservationbyreservationID) | `workspace:read:reservation``workspace:read:reservation:admin` |
| [Get Workspace Calendar Free/Busy Event](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetWorkspaceCalendarFree/BusyEvent) | `workspace:read:workspace:admin` |
| [List workspaces](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listWorkspaces) | `workspace:read:list_workspaces``workspace:read:list_workspaces:admin` |
| [Delete a workspace](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteWorkspace) | `workspace:delete:workspace:admin` |
| [Get workspace settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getWorkspaceSettings) | `workspace:read:settings:admin` |
| [List neighborhoods](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListNeighborhoods) | `workspace:read:neighborhood:admin` |
| [Get a workspace QR code](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getWorkspaceQRCode) | `workspace:read:qr:admin` |
| [Update workspace settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateWorkspaceSettings) | `workspace:update:setting:admin``workspace:update:setting:master` |
| [Update a workspace](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateWorkspace) | `workspace:update:workspace:admin` |
| [Delete a reservation](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteReservation) | `workspace:delete:reservation``workspace:delete:reservation:admin` |
| [Delete neighborhoods](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteNeighborhoods) | `workspace:delete:neighborhood:admin` |
| [Get a workspace location floor map](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getlocationfloormap) | `workspace:read:location``workspace:read:location:admin` |
| [Get questionnaire answer summary](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getworkspacequestionnaireresponses) | `workspace:read:workspace_reservation_questionnaire_response:admin``workspace:read:workspace_reservation_questionnaire_response:master` |
| [Get a location's hot desk usage](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getHotDeskUsage) | `workspace:read:usage``workspace:read:usage:admin` |
| [Add or Update a Workspace floor map](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddOrUpdateAWorkspaceFloorMap) | `workspace:write:location``workspace:write:location:admin` |
| [Get a user's workspace's reservations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/userListReservations) | `workspace:read:list_reservations:admin` |
| [Get a workspace asset](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/get_workspace_asset) | `workspace:read:asset:admin` |
| [Set Workspace Calendar Free/Busy Event](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/SetCalendarFree/BusyEvent) | `workspace:write:workspace:admin` |
| [Delete a workspace asset](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteaWorkspaceasset) | `workspace:delete:asset:admin` |
| [Set a desk assignment](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/setADeskAssignment) | `workspace:write:assignment:admin` |
| [Get a desk assignment](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getadeskassignment) | `workspace:read:assignment``workspace:read:assignment:admin` |
| [Delete a desk assignment](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Deleteadeskassignment) | `workspace:delete:assignment:admin` |

### Zoom Rooms [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-2)

| API endpoint | granular scope |
| --- | --- |
| [Get device information](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getRoomDevices) | `zoom_rooms:read:device_profile:admin` |
| [List Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listZoomRooms) | `zoom_rooms:read:list_rooms:admin` |
| [List Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/listZoomRooms) | `zoom_rooms:read:list_rooms:master` |
| [Delete a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteRoomProfile) | `zoom_rooms:delete:device_profile:admin` |
| [Delete a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/deleteRoomProfile) | `zoom_rooms:delete:device_profile:master` |
| [Apply configuration profile for Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ApplyconfigurationprofileforZoomRoom) | `zoom_rooms:update:room_settings:admin` |
| [Apply configuration profile for Zoom Rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/ApplyconfigurationprofileforZoomRoom) | `zoom_rooms:update:room_settings:master` |
| [Use Zoom Room controls](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ZoomRoomsControls) | `zoom_rooms:update:room_control:admin` |
| [Use Zoom Room controls](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/ZoomRoomsControls) | `zoom_rooms:update:room_control:master` |
| [Update E911 digital signage](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/manageE911signage) | `zoom_rooms:update:room_controls:admin` |
| [Update E911 digital signage](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/manageE911signage) | `zoom_rooms:update:room_controls:master` |
| [Create a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/createRoomDeviceProfile) | `zoom_rooms:write:device_profile:admin` |
| [Create a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/createRoomDeviceProfile) | `zoom_rooms:write:device_profile:master` |
| [Update Zoom Room settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZRSettings) | `zoom_rooms:update:room_settings:admin` |
| [Update Zoom Room settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZRSettings) | `zoom_rooms:update:room_settings:master` |
| [List Zoom Room devices](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listZRDevices) | `zoom_rooms:read:list_devices:admin` |
| [List Zoom Room devices](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/listZRDevices) | `zoom_rooms:read:list_devices:master` |
| [Get Zoom Room profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRProfile) | `zoom_rooms:read:room:admin` |
| [Get Zoom Room profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRProfile) | `zoom_rooms:read:room:master` |
| [Delete a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteAZoomRoom) | `zoom_rooms:delete:room:admin` |
| [Delete a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/deleteAZoomRoom) | `zoom_rooms:delete:room:master` |
| [Get Zoom Rooms virtual controller URL](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getWebzrcUrl) | `zoom_rooms:read:virtual_controller:admin` |
| [Get Zoom Rooms virtual controller URL](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getWebzrcUrl) | `zoom_rooms:read:virtual_controller:admin` |
| [Update a Zoom Room profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateRoomProfile) | `zoom_rooms:update:room:admin` |
| [Update a Zoom Room profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateRoomProfile) | `zoom_rooms:update:room:master` |
| [Change a Zoom Room's location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/changeZRLocation) | `zoom_rooms:update:room_location:admin` |
| [Change a Zoom Room's location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/changeZRLocation) | `zoom_rooms:update:room_location:master` |
| [List device profiles](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getRoomProfiles) | `zoom_rooms:read:list_device_profiles:admin` |
| [List device profiles](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getRoomProfiles) | `zoom_rooms:read:list_device_profiles:master` |
| [Get Zoom Room settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRSettings) | `zoom_rooms:read:room_settings:admin` |
| [Get Zoom Room settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRSettings) | `zoom_rooms:read:room_settings:master` |
| [Add a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/addARoom) | `zoom_rooms:write:room:admin` |
| [Add a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/addARoom) | `zoom_rooms:write:room:master` |
| [Get Zoom Room sensor data](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRSensorData) | `zoom_rooms:read:sensor_data:admin` |
| [Update a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateDeviceProfile) | `zoom_rooms:update:device_profile:admin` |
| [Update a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateDeviceProfile) | `zoom_rooms:update:device_profile:master` |
| [Get a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getRoomProfile) | `zoom_rooms:read:device_profile:admin` |
| [Get a device profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getRoomProfile) | `zoom_rooms:read:device_profile:master` |

### Zoom Rooms Account [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-account)

| API endpoint | granular scope |
| --- | --- |
| [Get Zoom Room account profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRAccountProfile) | `zoom_rooms:read:account_profile:admin` |
| [Get Zoom Room account profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRAccountProfile) | `zoom_rooms:read:account_profile:master` |
| [Update Zoom Room account profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZRAccProfile) | `zoom_rooms:update:account_profile:admin` |
| [Update Zoom Room account profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZRAccProfile) | `zoom_rooms:update:account_profile:master` |
| [Get Zoom Room account settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRAccountSettings) | `zoom_rooms:read:account_settings:admin` |
| [Get Zoom Room account settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRAccountSettings) | `zoom_rooms:read:account_settings:master` |
| [Update Zoom Room account settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZoomRoomAccSettings) | `zoom_rooms:update:account_settings:admin` |
| [Update Zoom Room account settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZoomRoomAccSettings) | `zoom_rooms:update:account_settings:master` |

### Zoom Rooms Calendar [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-calendar)

| API endpoint | granular scope |
| --- | --- |
| [Start calendar service sync process](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/syncACalendarService) | `zoom_rooms:update:calendar_service:admin` |
| [List calendar services](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getCalendarServices) | `zoom_rooms:read:list_calendar_services:admin` |
| [List calendar resources by calendar service](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getCalendarResourcesByServiceId) | `zoom_rooms:read:list_calendar_resources:admin` |
| [Add a calendar resource to a calendar service](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/addACalendarResourceToCalendarService) | `zoom_rooms:write:calendar_resource:admin` |
| [Delete a calendar resource](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteACalendarResource) | `zoom_rooms:delete:calendar_resource:admin` |
| [Get a calendar resource by ID](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getCalendarResourceById) | `zoom_rooms:read:calendar_resource:admin` |
| [Delete a calendar service](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteACalendarService) | `zoom_rooms:delete:calendar_service:admin` |

### Zoom Rooms Content [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-content)

| API endpoint | granular scope |
| --- | --- |
| [List Digital Signage library playlist published rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListDigitalSignagelibraryplaylistpublishedrooms) | `zoom_rooms:read:digital_signage_library_playlists:admin` |
| [List Digital Signage library playlist published rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/ListDigitalSignagelibraryplaylistpublishedrooms) | `zoom_rooms:read:digital_signage_library_playlists:master` |
| [Add Zoom Rooms background image library content](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddZoomRoomsBackgroundImageLibraryContent) | `zoom_rooms:write:background_library_content:admin` |
| [Update Zoom Rooms Background Image Library Folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/UpdateaZoomRoomsBackgroundLibraryFolderName) | `zoom_rooms:update:background_library_folder:admin` |
| [List default Zoom Rooms background image library contents](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListDefaultZoomRoomsBackgroundImageLibrarycontents) | `zoom_rooms:read:background_library_content:admin` |
| [Add a digital signage URL](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddadigitalsignageURL) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Add a digital signage URL](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/AddadigitalsignageURL) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Update Digital Signage library playlist published rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/UpdateDigitalSignagelibraryplaylistpublishedrooms) | `zoom_rooms:write:digital_signage_library_playlists:admin` |
| [Update Digital Signage library playlist published rooms](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/UpdateDigitalSignagelibraryplaylistpublishedrooms) | `zoom_rooms:write:digital_signage_library_playlists:master` |
| [Add Zoom Rooms Background Image Library Folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddZoomRoomsBackgroundLibraryFolder) | `zoom_rooms:write:background_library_folder:admin` |
| [Delete Zoom Rooms Background Image Library Folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteZoomRoomsBackgroundLibraryFolder) | `zoom_rooms:delete:background_library_folder:admin` |
| [Add a Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AddaDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:admin` |
| [Add a Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/AddaDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:master` |
| [Delete Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:admin` |
| [Delete Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/DeleteDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:master` |
| [Update Digital Signage library playlist content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/UpdateDigitalSignagelibraryplaylistcontentitems) | `zoom_rooms:write:digital_signage_library_playlists:admin` |
| [Update Digital Signage library playlist content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/UpdateDigitalSignagelibraryplaylistcontentitems) | `zoom_rooms:write:digital_signage_library_playlists:master` |
| [Get Zoom Rooms Background Image Library Folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetZoomRoomsBackgroundLibraryFolder) | `zoom_rooms:read:background_library_folder:admin` |
| [List Zoom Rooms Background Image Library Folders](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListZoomRoomsBackgroundLibraryFolders) | `zoom_rooms:read:background_library_folder:admin` |
| [List Digital Signage library playlists](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListDigitalSignagelibraryplaylists) | `zoom_rooms:read:digital_signage_library_playlists:admin` |
| [List Digital Signage library playlists](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/ListDigitalSignagelibraryplaylists) | `zoom_rooms:read:digital_signage_library_playlists:master` |
| [Update a digital signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Updateadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Update a digital signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Updateadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Add a digital signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Addadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Add a digital signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Addadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Get Digital Signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getdigitalsignagecontentfolderdetails) | `zoom_rooms:read:digital_signage_library_contents:admin` |
| [Get Digital Signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Getdigitalsignagecontentfolderdetails) | `zoom_rooms:read:digital_signage_library_contents:master` |
| [Update a Digital Signage content item attributes](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Updateadigitalsignagecontentitemattributes) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Update a Digital Signage content item attributes](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Updateadigitalsignagecontentitemattributes) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Get Digital Signage library playlist content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetDigitalSignagelibraryplaylistcontentitems) | `zoom_rooms:read:digital_signage_library_playlists:admin` |
| [Get Digital Signage library playlist content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/GetDigitalSignagelibraryplaylistcontentitems) | `zoom_rooms:read:digital_signage_library_playlists:master` |
| [Get Digital Signage content item](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Getdigitalsignagecontentitem) | `zoom_rooms:read:digital_signage_library_contents:admin` |
| [Get Digital Signage content item](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Getdigitalsignagecontentitem) | `zoom_rooms:read:digital_signage_library_contents:master` |
| [Get Zoom Rooms background image library content](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetZoomRoomsBackgroundImageLibraryContent) | `zoom_rooms:read:background_library_content:admin` |
| [List Zoom Rooms background image library contents](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/ListZoomRoomsbackgroundimagelibrarycontents) | `zoom_rooms:read:background_library_content:admin` |
| [Get Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GetDigitalSignagelibraryplaylist) | `zoom_rooms:read:digital_signage_library_playlists:admin` |
| [Get Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/GetDigitalSignagelibraryplaylist) | `zoom_rooms:read:digital_signage_library_playlists:master` |
| [Delete a Digital Signage content item](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Deleteadigitalsignagecontentitem) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Delete a Digital Signage content item](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Deleteadigitalsignagecontentitem) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Add a digital signage image or video](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Adddigitalsignageimageorvideo) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Add a digital signage image or video](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Adddigitalsignageimageorvideo) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Delete a Digital Signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Deleteadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Delete a Digital Signage content folder](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Deleteadigitalsignagecontentfolder) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Update Zoom Rooms background image library content](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/UpdateZoomRoomsBackgroundImageLibraryContent) | `zoom_rooms:update:background_library_content:admin` |
| [List Digital Signage content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/GETListdigitalsignagecontentitems) | `zoom_rooms:read:digital_signage_library_contents:admin` |
| [List Digital Signage content items](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/GETListdigitalsignagecontentitems) | `zoom_rooms:read:digital_signage_library_contents:master` |
| [Update a Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/UpdateaDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:admin` |
| [Update a Digital Signage library playlist](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/UpdateaDigitalSignagelibraryplaylist) | `zoom_rooms:write:digital_signage_library_playlists:master` |
| [Update a Digital Signage image or video file](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/Updateadigitalsignageimageorvideofile) | `zoom_rooms:write:digital_signage_library_contents:admin` |
| [Update a Digital Signage image or video file](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/Updateadigitalsignageimageorvideofile) | `zoom_rooms:write:digital_signage_library_contents:master` |
| [Delete Zoom Rooms Background Image Library Content](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/DeleteZoomRoomsBackgroundImageLibraryContent) | `zoom_rooms:delete:background_library_content:admin` |

### Zoom Rooms Devices [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-devices)

| API endpoint | granular scope |
| --- | --- |
| [Change Zoom Rooms app version](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/changeZoomRoomsAppVersion) | `zoom_rooms:update:device_app_version:admin` |
| [Change Zoom Rooms app version](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/changeZoomRoomsAppVersion) | `zoom_rooms:update:device_app_version:master` |
| [Delete a Zoom Room user device](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteDevice) | `zoom_rooms:delete:device:admin` |

### Zoom Rooms Location [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-location)

| API endpoint | granular scope |
| --- | --- |
| [Add a location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/addAZRLocation) | `zoom_rooms:write:location:admin` |
| [Add a location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/addAZRLocation) | `zoom_rooms:write:location:master` |
| [Get Zoom Room location structure](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRLocationStructure) | `zoom_rooms:read:location_hierarchy:admin` |
| [Get Zoom Room location structure](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRLocationStructure) | `zoom_rooms:read:location_hierarchy:master` |
| [Update Zoom Rooms location structure](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZoomRoomsLocationStructure) | `zoom_rooms:update:location_hierarchy:admin` |
| [Update Zoom Rooms location structure](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZoomRoomsLocationStructure) | `zoom_rooms:update:location_hierarchy:master` |
| [Delete a location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteAZRLocation) | `zoom_rooms:write:location:admin` |
| [Delete a location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/deleteAZRLocation) | `zoom_rooms:write:location:master` |
| [Change the assigned parent location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/changeParentLocation) | `zoom_rooms:update:location:admin` |
| [Change the assigned parent location](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/changeParentLocation) | `zoom_rooms:update:location:master` |
| [List Zoom Room locations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listZRLocations) | `zoom_rooms:read:list_locations:admin` |
| [List Zoom Room locations](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/listZRLocations) | `zoom_rooms:read:list_locations:master` |
| [Update location settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZRLocationSettings) | `zoom_rooms:update:location_settings:admin` |
| [Update location settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZRLocationSettings) | `zoom_rooms:update:location_settings:master` |
| [Get location settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRLocationSettings) | `zoom_rooms:read:location_settings:admin` |
| [Get location settings](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRLocationSettings) | `zoom_rooms:read:location_settings:master` |
| [Update Zoom Room location profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/updateZRLocationProfile) | `zoom_rooms:update:location:admin` |
| [Update Zoom Room location profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/updateZRLocationProfile) | `zoom_rooms:update:location:master` |
| [Get Zoom Room location profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/getZRLocationProfile) | `zoom_rooms:read:location:admin` |
| [Get Zoom Room location profile](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/ma/#operation/getZRLocationProfile) | `zoom_rooms:read:location:master` |

### Zoom Rooms Tags [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-rooms-tags)

| API endpoint | granular scope |
| --- | --- |
| [Assign Tags to Zoom Rooms By Location ID](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AssignTagsToZoomRoomsByLocationID) | `zoom_rooms:update:room_tag:admin` |
| [List all Zoom Room Tags](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/listZoomRoomTags) | `zoom_rooms:read:list_tags:admin` |
| [Assign Tags to a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/AssignTagsToAZoomRoom) | `zoom_rooms:update:room_tag:admin` |
| [Create a new Zoom Rooms Tag](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/createZoomRoomTag) | `zoom_rooms:write:tag:admin` |
| [Delete Tag](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/deleteZoomRoomTag) | `zoom_rooms:delete:tag:admin` |
| [Un-assign Tags from a Zoom Room](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/unassignZoomRoomTag) | `zoom_rooms:delete:room_tag:admin` |
| [Edit Tag](https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/#operation/editZoomRoomTag) | `zoom_rooms:update:tag:admin` |

## QSS [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#qss)

The following are the available **QSS** APIs and their associated granular scopes.

### Dashboards [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#dashboards-1)

| API endpoint | granular scope |
| --- | --- |
| [List meeting participants QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/methods/#operation/dashboardMeetingParticipantsQOSSummary) | `dashboard:read:list_meeting_participants_qos:admin` |
| [List meeting participants QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/ma/#operation/dashboardMeetingParticipantsQOSSummary) | `dashboard:read:list_meeting_participants_qos:master` |
| [List webinar participants QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/methods/#operation/dashboardWebinarParticipantsQOSSummary) | `dashboard:read:list_webinar_participants_qos:admin` |
| [List webinar participants QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/ma/#operation/dashboardWebinarParticipantsQOSSummary) | `dashboard:read:list_webinar_participants_qos:master` |

### Video SDK Sessions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#video-sdk-sessions)

| API endpoint | granular scope |
| --- | --- |
| [List session users QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/methods/#operation/sessionUsersQOSSummary) | `qss:read:session_users_summary:admin` |
| [List session users QoS Summary](https://developers.zoom.us/docs/api/rest/reference/qss/ma/#operation/sessionUsersQOSSummary) | `qss:read:session_users_summary:master` |

## Conference Room Connector (CRC) [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#conference-room-connector-crc)

The following are the available **Conference Room Connector (CRC)** APIs and their associated granular scopes.

### Account [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#account)

| API endpoint | granular scope |
| --- | --- |
| [Get Cisco/Polycom Room Account Setting](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/getCiscoPolycomRoomAccountSetting) | `crc:read:rooms_account_settings:admin` |
| [Get Cisco/Polycom Room Account Setting](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/getCiscoPolycomRoomAccountSetting) | `crc:read:rooms_account_settings:master` |
| [Update Cisco/Polycom Room Account Setting](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/UpdateCiscoPolycomRoomAccountSetting) | `crc:update:rooms_account_settings:admin` |
| [Update Cisco/Polycom Room Account Setting](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/UpdateCiscoPolycomRoomAccountSetting) | `crc:update:rooms_account_settings:master` |

### Api Connector [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#api-connector)

| API endpoint | granular scope |
| --- | --- |
| [Get an API Connector's private key](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/GetanAPIConnector'sprivatekey) | `crc:read:apiconnector_private_key:admin` |
| [Get an API Connector's private key](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/GetanAPIConnector'sprivatekey) | `crc:read:apiconnector_private_key:master` |
| [Get an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/GetAPIConnector) | `crc:read:apiconnector:admin` |
| [Get an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/GetAPIConnector) | `crc:read:apiconnector:master` |
| [List API Connectors](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/GetListAPIConnectors) | `crc:read:list_apiconnectors:admin` |
| [List API Connectors](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/GetListAPIConnectors) | `crc:read:list_apiconnectors:master` |
| [Delete an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/DeleteAPIConnector) | `crc:delete:apiconnector:admin` |
| [Delete an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/DeleteAPIConnector) | `crc:delete:apiconnector:master` |
| [Create an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/CreateAPIConnector) | `crc:write:apiconnector:admin` |
| [Create an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/CreateAPIConnector) | `crc:write:apiconnector:master` |
| [Update an API Connector's private key](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/UpdateAPIConnectorPrivateKey) | `crc:update:apiconnector_private_key:admin` |
| [Update an API Connector's private key](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/UpdateAPIConnectorPrivateKey) | `crc:update:apiconnector_private_key:master` |
| [Update an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/UpdateAPIConnector) | `crc:update:apiconnector:admin` |
| [Update an API Connector](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/UpdateAPIConnector) | `crc:update:apiconnector:master` |

### Cisco/Polycom Rooms [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#ciscopolycom-rooms)

| API endpoint | granular scope |
| --- | --- |
| [Get a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/GetaManagedRoom) | `crc:read:room:admin` |
| [Get a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/GetaManagedRoom) | `crc:read:room:master` |
| [Delete a managed room](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/Deleteamanagedroom) | `crc:delete:room:admin` |
| [Delete a managed room](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/Deleteamanagedroom) | `crc:delete:room:master` |
| [List Managed Rooms](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/ListManagedRooms) | `crc:read:list_rooms:admin` |
| [List Managed Rooms](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/ListManagedRooms) | `crc:read:list_rooms:master` |
| [Update a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/UpdateaManagedRoom) | `crc:update:room:admin` |
| [Update a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/UpdateaManagedRoom) | `crc:update:room:master` |
| [Create a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/CreateaManagedRoom) | `crc:write:room:admin` |
| [Create a Managed Room](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/CreateaManagedRoom) | `crc:write:room:master` |

### Participant [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#participant)

| API endpoint | granular scope |
| --- | --- |
| [Get participant identifier code](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/get_participant_identifier_code) | `crc:read:participant_identifier_code:admin``crc:read:participant_identifier_code:master` |

### Room Template [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#room-template)

| API endpoint | granular scope |
| --- | --- |
| [Delete a room template](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/Deletearoomtemplate) | `crc:delete:rooms_template:admin` |
| [Delete a room template](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/Deletearoomtemplate) | `crc:delete:rooms_template:master` |
| [List Room Templates](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/ListRoomTemplates) | `crc:read:list_rooms_templates:admin` |
| [List Room Templates](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/ListRoomTemplates) | `crc:read:list_rooms_templates:master` |
| [Get a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/GetaRoomTemplate) | `crc:read:rooms_template:admin` |
| [Get a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/GetaRoomTemplate) | `crc:read:rooms_template:master` |
| [Create a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/CreateaRoomTemplate) | `crc:write:rooms_template:admin` |
| [Create a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/CreateaRoomTemplate) | `crc:write:rooms_template:master` |
| [Update a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/methods/#operation/UpdateaRoomTemplate) | `crc:update:rooms_template:admin` |
| [Update a Room Template](https://developers.zoom.us/docs/api/rest/reference/crc/ma/#operation/UpdateaRoomTemplate) | `crc:update:rooms_template:master` |

## Contact Center [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#contact-center)

The following are the available **Contact Center** APIs and their associated granular scopes.

### Accounts [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#accounts-3)

| API endpoint | granular scope |
| --- | --- |
| [List storage locations](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListStorageLocations) | `contact_center:read:account_storage_location:admin` |

### Address Books [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#address-books)

| API endpoint | granular scope |
| --- | --- |
| [List address book contacts](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listContacts) | `contact_center:read:list_address_book_contacts:admin` |
| [Batch create address book contacts](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchCreateContact) | `contact_center:write:address_book_contact:admin` |
| [Update an address book contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateContact) | `contact_center:update:address_book_contact:admin` |
| [List an address book's custom fields](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listaddressbookcustomfields) | `contact_center:read:address_book_custom_field:admin` |
| [Update an address book unit](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateUnit) | `contact_center:update:address_book_unit:admin` |
| [Batch update address book contacts](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchUpdateContact) | `contact_center:update:address_book_contact:admin` |
| [Delete an address book custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteancustomfield) | `contact_center:delete:address_book_custom_field:admin` |
| [List address books](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAddressBooks) | `contact_center:read:list_address_books:admin` |
| [Update an address book](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateAddressBook) | `contact_center:update:address_book:admin` |
| [Update an address book custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateacustomfield) | `contact_center:update:address_book_custom_field:admin` |
| [Delete an address book unit](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteUnit) | `contact_center:delete:address_book_unit:admin` |
| [Create an address book custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Createacustomfield) | `contact_center:write:address_book_custom_field:admin` |
| [Get an address book](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAddressBook) | `contact_center:read:address_book:admin` |
| [Batch delete address book contacts](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchDeletecontact) | `contact_center:delete:address_book_contact:admin` |
| [Get an address book's custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Getaaddressbookcustomfield) | `contact_center:read:address_book_custom_field:admin` |
| [Get an address book unit](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getUnit) | `contact_center:read:address_book_unit:admin` |
| [List address book units](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listUnits) | `contact_center:read:list_address_book_units:admin` |
| [Create an address book unit](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createUnit) | `contact_center:write:address_book_unit:admin` |
| [Get an address book contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getContact) | `contact_center:read:address_book_contact:admin` |
| [Delete an address book](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteAddressBook) | `contact_center:delete:address_book:admin` |
| [List an address book contact's custom fields](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListContactCustomFields) | `contact_center:read:address_book_custom_field:admin` |
| [Delete an address book contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/contactDelete) | `contact_center:delete:address_book_contact:admin` |
| [Create an address book contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createContact) | `contact_center:write:address_book_contact:admin` |
| [Create an address book](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createAddressBook) | `contact_center:write:address_book:admin` |

### Agent Statuses [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#agent-statuses)

| API endpoint | granular scope |
| --- | --- |
| [Get a system status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAStatus) | `contact_center:read:system_status:admin` |
| [Delete a system status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteSystemStatus) | `contact_center:delete:system_status:admin` |
| [List system statuses](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSystemStatus) | `contact_center:read:list_system_statues:admin` |
| [Update a system status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateSystemStatus) | `contact_center:update:system_status:admin` |
| [Create a system status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createSystemStatus) | `contact_center:write:system_status:admin` |

### Asset Library [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#asset-library)

| API endpoint | granular scope |
| --- | --- |
| [List assets](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAssets) | `contact_center:read:asset_library:admin` |
| [Delete an asset category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteAnAssetCategory) | `contact_center:delete:asset_library:admin` |
| [Create an asset category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createAnAssetCategory) | `contact_center:write:asset_library:admin` |
| [Update an asset](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateAnAsset) | `contact_center:write:asset_library:admin` |
| [Duplicate an asset](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/duplicateAnAsset) | `contact_center:write:asset_library:admin` |
| [Create an asset](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createAnAsset) | `contact_center:write:asset_library:admin` |
| [Get an asset category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAnAssetCategory) | `contact_center:read:asset_library:admin` |
| [Delete asset items](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteassetitems) | `contact_center:write:asset_library:admin` |
| [Batch update asset items](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/BatchUpdateAssetItems) | `contact_center:update:asset_library:admin` |
| [List asset categories](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAssetCategories) | `contact_center:read:asset_library:admin` |
| [Update an asset category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateAnAssetCategory) | `contact_center:write:asset_library:admin` |
| [Get an asset](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAnAsset) | `contact_center:read:asset_library:admin` |
| [Delete an asset](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteAnAsset) | `contact_center:delete:asset_library:admin` |

### Block List Rules [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#block-list-rules)

| API endpoint | granular scope |
| --- | --- |
| [Get a block list rule of IP addresses](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getBlockListRuleIpAddress) | `contact_center:read:block_list_rules:admin` |
| [Get a block list rule of phone numbers](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getBlockListRulePhoneNumber) | `contact_center:read:block_list_rules:admin` |
| [Delete phone numbers' block list rules](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteBlockListRulePhoneNumbers) | `contact_center:delete:block_list_rules:admin` |
| [List block list rules of phone numbers](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listBlockListRulesPhoneNumbers) | `contact_center:read:block_list_rules:admin` |
| [Delete IP addresses' block list rules](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteBlockListRuleIpAddresses) | `contact_center:delete:block_list_rules:admin` |
| [List block list rules for IP addresses](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listBlockListRulesIpAddresses) | `contact_center:read:block_list_rules:admin` |
| [Create block list rules for IP addresses](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createBlockListRulesIpAddresses) | `contact_center:write:block_list_rules:admin` |
| [Create block list rules for phone numbers](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createBlockListRulesPhoneNumbers) | `contact_center:write:block_list_rules:admin` |

### Call Control [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-control)

| API endpoint | granular scope |
| --- | --- |
| [Control an engagement's recording](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementRecordingControl) | `contact_center:update:engagement_recording_control:admin` |
| [List user's devices](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listuserdevices) | `contact_center:read:user_device:admin` |
| [Command control of a user](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/userControl) | `contact_center:write:user_control:admin` |

### Campaigns [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#campaigns)

| API endpoint | granular scope |
| --- | --- |
| [Delete an outbound campaign](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteOutboundCampaign) | `contact_center:delete:outbound_campaign:admin` |
| [Get a campaign contact list's contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getCampaignContactListContact) | `contact_center:read:outbound_campaign_contacts:admin` |
| [Remove a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteCampaignContactList) | `contact_center:delete:outbound_campaign_contactlist:admin` |
| [List a campaign contact's custom fields](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listCampaignContactCustomFields) | `contact_center:read:outbound_campaign_contactlist:admin` |
| [Update a campaign contact list's custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateACampaignCustomField) | `contact_center:update:outbound_campaign_contactlist:admin` |
| [Insert a batch of contacts into a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Insertabatchofcontactstoacampaigncontactlist) | `contact_center:write:outbound_campaign_contacts:admin` |
| [Batch create a campaign DNC list's phones](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchCreateCampaignDncListPhones) | `contact_center:write:outbound_campaign_dnc_list_phones:admin` |
| [Remove campaign contact list's contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteCampaigncontactListContact) | `contact_center:delete:outbound_campaign_contacts:admin` |
| [List campaign contact lists' custom fields](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listCampaignCustomFields) | `contact_center:read:outbound_campaign_contactlist:admin` |
| [Get a campaign contact list's custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getACampaignContactCustomField) | `contact_center:read:outbound_campaign_contactlist:admin` |
| [Get a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getCampaignContactList) | `contact_center:read:outbound_campaign_contactlist:admin` |
| [Update an outbound campaign status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateanoutboundcampaignstatus) | `contact_center:update:outbound_campaign:admin` |
| [Update contact on a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateCampaignContactListContact) | `contact_center:update:outbound_campaign_contacts:admin` |
| [Update a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateCampaignContactList) | `contact_center:update:outbound_campaign_contactlist:admin` |
| [Batch delete a campaign DNC list's phones](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchDeleteCampaignDncListPhone) | `contact_center:delete:outbound_campaign_dnc_list_phones:admin` |
| [Create an outbound campaign](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createOutboundCampaign) | `contact_center:write:outbound_campaign:admin` |
| [Delete a campaign contact list's custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteACampaignCustomField) | `contact_center:delete:outbound_campaign_contactlist:admin` |
| [Get an outbound campaign](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getOutboundCampaign) | `contact_center:read:outbound_campaign:admin` |
| [List outbound campaigns](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listOutboundCampaigns) | `contact_center:read:outbound_campaign:admin` |
| [Batch update campaign contact lists](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Batchupdatecampaigncontactlists) | `contact_center:update:outbound_campaign_contactlist:admin` |
| [Create a campaign contact list's custom field](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createACampaignContactCustomField) | `contact_center:write:outbound_campaign_contactlist:admin` |
| [Create a campaign contact list's contact](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createCampaignContactListContact) | `contact_center:write:outbound_campaign_contacts:admin` |
| [Update an outbound campaign](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateOutboundCampaign) | `contact_center:update:outbound_campaign:admin` |
| [Update outbound campaign contact lists](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateOutboundCampaignContactLists) | `contact_center:update:outbound_campaign:admin` |
| [List a campaign contact list's contacts](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listCampaignContactListContacts) | `contact_center:read:outbound_campaign_contacts:admin` |
| [Create a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createCampaignContactList) | `contact_center:write:outbound_campaign_contactlist:admin` |
| [List campaign DNC phone numbers](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listCampaignDncListPhones) | `contact_center:read:outbound_campaign_dnc_list_phones:admin` |
| [List campaign contact lists](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listCampaignContactLists) | `contact_center:read:outbound_campaign_contactlist:admin` |
| [Update a batch of contacts on a campaign contact list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateabatchofcontactsonacampaigncontactlist) | `contact_center:update:outbound_campaign_contacts:admin` |

### Dispositions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#dispositions)

| API endpoint | granular scope |
| --- | --- |
| [Create a disposition set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createSet) | `contact_center:write:disposition_set:admin` |
| [Delete a disposition](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteDisposition) | `contact_center:delete:disposition:admin` |
| [Get a disposition](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getDisposition) | `contact_center:read:disposition:admin` |
| [Delete a disposition set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteSet) | `contact_center:delete:disposition_set:admin` |
| [Update a disposition set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateSet) | `contact_center:update:disposition_set:admin` |
| [Create a disposition](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createDisposition) | `contact_center:write:disposition:admin` |
| [List dispositions](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listDispositions) | `contact_center:read:list_dispositions:admin` |
| [Update a disposition](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateDisposition) | `contact_center:update:disposition:admin` |
| [Get a disposition set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getSet) | `contact_center:read:disposition_set:admin` |
| [List disposition sets](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSets) | `contact_center:read:list_disposition_sets:admin` |

### Engagements [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#engagements)

| API endpoint | granular scope |
| --- | --- |
| [Poll an engagement recording's status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/EngagementRecordingStatus) | `contact_center:read:engagement_recording_status:admin` |
| [Get an engagement's available transfer flows](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/GetAvailableTransferFlows) | `contact_center:read:flow:admin` |
| [Get a historical engagement](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getEngagement) | `contact_center:read:engagement:admin` |
| [Update an engagement](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateEngagement) | `contact_center:update:engagement:admin` |
| [Get an engagement's attachments](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListAttachments) | `contact_center:read:attachment:admin` |
| \[List open engagements\](/docs/api/rest/reference/contact-center/methods/#operation/list open engagements) | `contact_center:read:list_engagements:admin` |
| [Get an engagement's survey](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getEngagementSurvey) | `contact_center:read:engagement:admin` |
| [Get an engagement's available transfer queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/GetAvailableTransferQueues) | `contact_center:read:list_queues:admin` |
| [Get an engagement's available transfer users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/GetAvailableTransferUsers) | `contact_center:read:list_users:admin` |
| [List historical engagements](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listEngagements) | `contact_center:read:list_engagements:admin` |
| [Start an engagement](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Startworkitemengagement) | `contact_center:write:engagement:admin` |
| [Get an engagement's events](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getEngagementEvents) | `contact_center:read:engagement:admin` |

### Files [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#files)

| API endpoint | granular scope |
| --- | --- |
| [Upload a file](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/uploadAFile) | `contact_center:write:files:admin` |

### Flows [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#flows)

| API endpoint | granular scope |
| --- | --- |
| [Export a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ExportFlow) | `contact_center:read:flow:admin` |
| [Add flow entry points](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/AddFlowEntryPoints) | `contact_center:write:flow:admin` |
| [Delete a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/DeleteFlow) | `contact_center:delete:flow:admin` |
| [Get a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAFlow) | `contact_center:read:flow:admin` |
| [Import a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ImportFlow) | `contact_center:write:flow:admin` |
| [List entry points](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListentryPoints) | `contact_center:read:flow:admin` |
| [List flows](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listFlows) | `contact_center:read:list_flows:admin` |
| [Edit a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/EditFlow) | `contact_center:update:flow:admin` |
| [Publish a flow](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/PublishFlow) | `contact_center:update:flow:admin` |
| [List the flow's entry points](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListFlowEntryPoints) | `contact_center:read:flow:admin` |
| [Remove flow entry points](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/RemoveFlowEntryPoints) | `contact_center:delete:flow:admin` |

### Follow-up Tasks [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#follow-up-tasks)

| API endpoint | granular scope |
| --- | --- |
| [List engagement follow-up tasks](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementFollowUpTasksBatchList) | `contact_center:read:list_follow_up_tasks:admin` |
| [Update a follow-up task](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementFollowUpTaskPatch) | `contact_center:update:follow_up_task` |
| [Get a follow-up task](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementFollowUpTaskGet) | `contact_center:read:follow_up_task:admin` |

### Inboxes [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#inboxes)

| API endpoint | granular scope |
| --- | --- |
| [Update an inbox's email notification setting](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateaninboxemailnotification) | `contact_center:update:inbox:admin` |
| [Delete an inbox message](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxMessageDelete) | `contact_center:delete:inbox_message:admin` |
| [Get an inbox email notification list](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Getinboxemailnotificationlist) | `contact_center:read:inbox:admin` |
| [Assign queues to an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignInboxQueues) | `contact_center:write:inbox_queue:admin` |
| [Create an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxCreate) | `contact_center:write:inbox:admin` |
| [List inbox users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listInboxUsers) | `contact_center:read:inbox_user:admin` |
| [Delete inbox messages](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxesMessagesDelete) | `contact_center:delete:inbox_messages:admin` |
| [Unassign queues from an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/unassignInboxQueues) | `contact_center:delete:inbox_queue:admin` |
| [Assign inbox access users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignInboxUsers) | `contact_center:write:inbox_user:admin` |
| [Get an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getInbox) | `contact_center:read:inbox:admin` |
| [List an account's inbox messages](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listInboxesMessages) | `contact_center:read:inbox_messages:admin` |
| [List an inbox's messages](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listInboxMessages) | `contact_center:read:inbox_messages:admin` |
| [Unassign inbox access users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/unassignInboxUsers) | `contact_center:delete:inbox_user:admin` |
| [Update an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxUpdate) | `contact_center:update:inbox:admin` |
| [Delete an inbox's messages](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxMessagesDelete) | `contact_center:delete:inbox_messages:admin` |
| [List inboxes](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listInbox) | `contact_center:read:list_inboxes:admin` |
| [Delete inboxes](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/inboxesDelete) | `contact_center:delete:inbox:admin` |
| [List queues assigned to an inbox](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listInboxQueues) | `contact_center:read:list_inbox_queues:admin` |

### Logs [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#logs)

| API endpoint | granular scope |
| --- | --- |
| [List voice call logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listVoiceCall) | `contact_center:read:voice_call_log:admin` |
| [List voice call logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/ma/#operation/listVoiceCall) | `contact_center:read:voice_call_log:master` |
| [List email message history](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getEmailMessageHistory) | `contact_center:read:engagement_log:admin` |
| [List SMS logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSMS) | `contact_center:read:sms_log:admin` |
| [List SMS logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/ma/#operation/listSMS) | `contact_center:read:sms_log:master` |
| [List operation logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listOperationLogs) | `contact_center:read:operation_logs:admin` |
| [List work item message history](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getWorkItemMessageHistory) | `contact_center:read:engagement_log:admin` |
| [List message history](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getMessageHistory) | `contact_center:read:messaging:admin` |

### Messaging [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#messaging)

| API endpoint | granular scope |
| --- | --- |
| [Send a message](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/SendaMessage) | `contact_center:write:messaging:admin` |

### Notes [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#notes)

| API endpoint | granular scope |
| --- | --- |
| [List engagement notes](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementNotes) | `contact_center:read:list_notes:admin` |
| [List notes](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/notes) | `contact_center:read:list_notes:admin` |
| [Get a note](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getNote) | `contact_center:read:note:admin` |
| [Update a note](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/noteUpdate) | `contact_center:update:note` |

### Operating Hours [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#operating-hours)

| API endpoint | granular scope |
| --- | --- |
| [Delete business hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/businessHourDelete) | `contact_center:delete:business_hour:admin` |
| [Get a closure set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAClosureSet) | `contact_center:read:closure_hour:admin` |
| [List the business hours' flows](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listBusinessHourFlows) | `contact_center:read:business_hours_flow:admin` |
| [List the business hours' queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listBusinessHourQueues) | `contact_center:read:business_hours_queue:admin` |
| [Delete a closure set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/closureSetDelete) | `contact_center:delete:closure_hour:admin` |
| [Get business hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getABusinessHour) | `contact_center:read:business_hour:admin` |
| [Update business hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/businessHourUpdate) | `contact_center:update:business_hour:admin` |
| [List the closures' flows](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listClosureSetFlows) | `contact_center:read:clousre_hour_flow:admin` |
| [List business hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listBusinessHours) | `contact_center:read:list_business_hours:admin` |
| [Create a closure set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/closuresSetCreate) | `contact_center:write:closure_hour:admin` |
| [Create business hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/businessHourCreate) | `contact_center:write:business_hour:admin` |
| [List closures](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listClosures) | `contact_center:read:list_closure_hours:admin` |
| [Update a closure set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/closureSetUpdate) | `contact_center:update:closure_hour:admin` |
| [List the closures' queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listClosureSetQueues) | `contact_center:read:closure_hour_queue:admin` |

### Queue Waiting Experiences [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#queue-waiting-experiences)

| API endpoint | granular scope |
| --- | --- |
| [Delete a queue waiting experience interrupt menu strategy](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueWaitingExperienceInterruptMenuStrategy) | `contact_center:delete:queue:admin` |
| [Assign a queue waiting experience interrupt menu strategy](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueWaitingExperienceInterruptMenu) | `contact_center:update:queue:admin` |

### Queues [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#queues)

| API endpoint | granular scope |
| --- | --- |
| [Assign queue disposition sets](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueDispositionSets) | `contact_center:write:queue_disposition_set:admin` |
| [List queue scheduled callback variables](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listScheduledCallbackVariables) | `contact_center:read:queue:admin` |
| [Get a queue's interrupt settings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueInterruptSettings) | `contact_center:read:queue:admin` |
| [Delete queue recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueRecordings) | `contact_center:delete:recording:admin` |
| [Batch create queues with a template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Batchcreatequeueswithatemplate) | `contact_center:write:queue:admin` |
| [Update a queue agent's opt-in/opt-out status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateQueueAgent) | `contact_center:update:queue_agent:admin` |
| [Update a queue template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateQueueTemplate) | `contact_center:update:queue:admin` |
| [Unassign a queue disposition set](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueDispositionSet) | `contact_center:delete:queue_disposition_set:admin` |
| [Assign queue agents](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueAgents) | `contact_center:write:queue_agent:admin` |
| [Delete a queue's interrupt menu configuration](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueInterruptMenu) | `contact_center:update:queue:admin` |
| [Update a queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/queueUpdate) | `contact_center:update:queue:admin` |
| [List queue disposition sets](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueDispositionSets) | `contact_center:read:list_disposition_sets:admin` |
| [Get a queue's operating hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAQueueOperatingHours) | `contact_center:read:queue_operating_hours:admin` |
| [Delete an attendee from a scheduled callback event](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteascheduledcallbackforanattendee) | `contact_center:write:queue:admin` |
| [Unassign a queue agent](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueAgent) | `contact_center:delete:queue_agent:admin` |
| [List queue dispositions](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueDispositions) | `contact_center:read:list_dispositions:admin` |
| [List queue recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listQueueRecordings) | `contact_center:read:list_recordings:admin``contact_center:read:list_recordings` |
| [Assign queue dispositions](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueDispositions) | `contact_center:write:queue disposition:admin` |
| [Update a queue's operating hours](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/QueueOperatingHoursUpdate) | `contact_center:patch:queue_operating_hours:admin` |
| [List a queue's scheduled callbacks availability](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listqueuescheduledcallbacksavailability) | `contact_center:read:queue:admin` |
| [Schedule a callback on a queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Scheduleacallbackonaqueue) | `contact_center:write:queue:admin` |
| [Unassign queue teams](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchDeleteQueueTeams) | `contact_center:delete:queue_team:admin` |
| [Unassign a queue supervisor](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueSupervisor) | `contact_center:delete:queue_supervisor:admin` |
| [List queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listQueues) | `contact_center:read:list_queues:admin` |
| [List queue supervisors](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueSupervisors) | `contact_center:delete:queue_supervisor:admin` |
| [Create a queue template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createQueueTemplate) | `contact_center:write:queue:admin` |
| [List queue templates](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listqueuetemplates) | `contact_center:read:queue:admin` |
| [Assign queue teams](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueTeams) | `contact_center:write:queue_team:admin` |
| [Create a queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/queueCreate) | `contact_center:write:queue:admin` |
| [Unassign a queue disposition](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueDisposition) | `contact_center:delete:queue_disposition:admin` |
| [Delete a queue template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueTemplate) | `contact_center:delete:queue:admin` |
| [Delete a queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/queueDelete) | `contact_center:delete:queue:admin` |
| [List queue agents](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueAgents) | `contact_center:read:list_queue_agents:admin` |
| [Unassign a queue team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueTeam) | `contact_center:delete:queue_team:admin` |
| [Get a queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAQueue) | `contact_center:read:queue:admin` |
| [Update a queue's interrupt settings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateQueueInterrupts) | `contact_center:update:queue:admin` |
| [Assign a queue menu based interrupt](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueMenuBasedInterrupt) | `contact_center:update:queue:admin` |
| [Batch delete queue templates](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteQueueTemplates) | `contact_center:delete:queue:admin` |
| [Get a queue template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getQueueTemplate) | `contact_center:read:queue:admin` |
| [Assign queue supervisors](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignQueueSupervisors) | `contact_center:delete:queue_supervisor:admin` |
| [Batch delete queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Batchdeletequeues) | `contact_center:delete:queue:admin` |

### RTMS [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#rtms)

| API endpoint | granular scope |
| --- | --- |
| [Update engagement Real-Time Media Streams (RTMS) app status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/engagementRTMSStatusUpdate) | `contact_center:update:engagement_rtms_app_status``contact_center:update:engagement_rtms_app_status:admin` |

### Recordings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#recordings-1)

| API endpoint | granular scope |
| --- | --- |
| [List engagement recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listEngagementRecordings) | `contact_center:read:list_recordings:admin` |
| [Delete a recording](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteRecording) | `contact_center:delete:recording:admin` |
| [Delete engagement recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteEngagementRecordings) | `contact_center:delete:recording:admin` |
| [List recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listRecordings) | `contact_center:read:list_recordings:admin` |

### Regions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#regions)

| API endpoint | granular scope |
| --- | --- |
| [Create a region](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/CreateARegion) | `contact_center:write:region:admin` |
| [List regions](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListRegions) | `contact_center:read:list_regions:admin` |
| [Delete a region](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/DeleteARegion) | `contact_center:delete:region:admin` |
| [Get a region](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/GetARegion) | `contact_center:read:region:admin` |
| [Assign users to a region](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/AssignUsersToARegion) | `contact_center:write:region_user:admin` |
| [List a region's users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListRegion'sUsers) | `contact_center:read:list_region_users:admin` |
| [Update a region](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/UpdateARegion) | `contact_center:udpate:region:admin` |

### Reports V1 (Legacy) [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-v1-legacy)

| API endpoint | granular scope |
| --- | --- |
| [List historical agent reports by queue](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listQueueAgentsMetrics) | `contact_center:read:agent_report:admin` |
| [List historical queue's agents reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listQueueAgentMetric) | `contact_center:read:agent_report:admin` |
| [List historical queue reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listHistoricalQueueMetric) | `contact_center:read:queue_report:admin` |
| [List historical detail reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listHistoricalDetailMetric) | `contact_center:read:engagement_report:admin` |
| [List agent's status history reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAgentStatusHistory) | `contact_center:read:agent_status_report:admin` |
| [List agent's time sheet reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAgentTimeSheet) | `contact_center:read:agent_report:admin` |
| [List agent leg reports](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listAgentLegMetric) | `contact_center:read:agent_report:admin` |

### Reports V2 (CX Analytics) [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-v2-cx-analytics)

| API endpoint | granular scope |
| --- | --- |
| [List historical queue performance dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalqueueperformancedatasetdata) | `contact_center:read:dataset_queue_performance:admin` |
| [Get historical custom report tabular schema](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getHistoricalCustomReportTabularSchema) | `contact_center:read:custom_report:admin` |
| [List historical Zoom Phone to Contact Center call journey data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListhistoricalZoomphonetozcccalljourneydata) | `contact_center:read:call_journey_log:admin` |
| [List historical custom report tabular data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalcustomreporttabulardata) | `contact_center:read:custom_report:admin` |
| [List historical agent performance dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalagentperformancedatasetdata) | `contact_center:read:dataset_agent_performance:admin` |
| [List historical engagement log data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalengagementlogs) | `contact_center:read:engagement_log:admin` |
| [List historical engagement timelines](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listHistoricalEngagementTimelines) | `contact_center:read:engagement_timeline:admin` |
| [List historical agent timecard dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalagenttimecarddatasetdata) | `contact_center:read:dataset_agent_timecard:admin` |
| [List historical expert assist dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listexpertassistdatasetdata) | `contact_center:read:dataset_expert_assist:admin` |
| [List historical engagement dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listengagementdatasetdata) | `contact_center:read:dataset_engagement:admin` |
| [List historical flow performance dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalflowperformancedatasetdata) | `contact_center:read:dataset_flow_performance:admin` |
| [List historical agent work session logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalagentworksessionlogs) | `contact_center:read:list_agent_work_session_logs:admin` |
| [List historical agent compliance logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalagentcompliancelog) | `contact_center:read:list_agent_compliance_logs:admin` |
| [List historical routing log performance dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalroutinglogperformancedatasetdata) | `contact_center:read:dataset_routing_log:admin` |
| [List historical disposition dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricaldispositiondatasetdata) | `contact_center:read:dataset_disposition:admin` |
| [List historical agent opt in or out logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricalagentoptlogs) | `contact_center:read:list_agent_opt_logs:admin` |
| [List historical outbound dialer performance dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listhistoricaloutbounddialerperformancedatasetdata) | `contact_center:read:dataset_outbound_dialer_performance:admin` |
| [List historical agent load dataset data](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listagentloaddatasetdata) | `contact_center:read:dataset_agent_load:admin` |

### Roles [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#roles-1)

| API endpoint | granular scope |
| --- | --- |
| [Delete a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteRole) | `contact_center:delete:role:admin` |
| [Update a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateRole) | `contact_center:update:role:admin` |
| [Delete role privileges](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteroleprivileges) | `contact_center:delete:role:admin` |
| [Get a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getRole) | `contact_center:read:role:admin` |
| [List users of a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getRoleUsers) | `contact_center:read:list_role_users:admin` |
| [Duplicate a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Duplicatearole) | `contact_center:write:role:admin` |
| [Unassign a user from a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteRoleUser) | `contact_center:delete:role_user:admin` |
| [Assign a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignRoleUsers) | `contact_center:write:role_user:admin` |
| [Create a role](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createRole) | `contact_center:write:role:admin` |
| [List roles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listRoles) | `contact_center:read:list_roles:admin` |

### Routing Profiles [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#routing-profiles)

| API endpoint | granular scope |
| --- | --- |
| [Update an agent routing profile's details](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateanagentroutingprofile'sdetails) | `contact_center:update:agent_routing_profile:admin` |
| [Get an agent routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAgentRoutingProfile) | `contact_center:read:agent_routing_profile:admin` |
| [Get a consumer routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Getaconsumerroutingprofile) | `contact_center:read:consumer_routing_profile:admin` |
| [Delete an agent routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteanagentroutingprofile) | `contact_center:delete:agent_routing_profile:admin` |
| [List agent routing profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listagentroutingprofiles) | `contact_center:read:agent_routing_profile:admin` |
| [List consumer routing profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Listconsumerroutingprofiles) | `contact_center:read:consumer_routing_profile:admin` |
| [Create an agent routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Createanagentroutingprofile) | `contact_center:write:agent_routing_profile:admin` |
| [Create a consumer routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Createaconsumerroutingprofile) | `contact_center:write:consumer_routing_profile:admin` |
| [Delete a consumer routing profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Deleteaconsumerroutingprofile) | `contact_center:delete:consumer_routing_profile:admin` |
| [Update a consumer routing profile's details](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateaconsumerroutingprofile'sdetails) | `contact_center:update:consumer_routing_profile:admin` |

### SMS [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms-1)

| API endpoint | granular scope |
| --- | --- |
| [Send an SMS](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/contactCenterSMS) | `contact_center:write:sms:admin` |

### Skills [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#skills)

| API endpoint | granular scope |
| --- | --- |
| [Delete a skill category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/SkillCategoryDelete) | `contact_center:delete:skill_category:admin` |
| [Update a skill category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/SkillCategoryUpdate) | `contact_center:update:skill_category:admin` |
| [List skills](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSkills) | `contact_center:read:list_skills:admin` |
| [Create a skill](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/skillCreate) | `contact_center:write:skill:admin` |
| [Create a skill category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/SkillCategoryCreate) | `contact_center:write:skill_category:admin` |
| [List skill categories](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSkillCategory) | `contact_center:read:list_skill_categories:admin` |
| [List skill users](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listSkillUsers) | `contact_center:read:list_skill_users:admin` |
| [Get a skill category](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getSkillCategory) | `contact_center:read:skill_category:admin` |
| [Update a skill](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/skillNameUpdate) | `contact_center:update:skill:admin` |
| [Get a skill](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getSkill) | `contact_center:read:skill:admin` |
| [Delete a skill](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/skillDelete) | `contact_center:delete:skill:admin` |

### Teams [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#teams-1)

| API endpoint | granular scope |
| --- | --- |
| [Assign team supervisors](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignTeamSupervisors) | `contact_center:write:team:admin` |
| [List team supervisors](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listTeamSupervisors) | `contact_center:read:team:admin` |
| [Move a team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/moveTeam) | `contact_center:update:team:admin` |
| [List a team's child teams](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getTeamChildTeams) | `contact_center:read:team:admin` |
| [Unassign team supervisors](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/unassignTeamSupervisors) | `contact_center:delete:team:admin` |
| [Delete a team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteTeam) | `contact_center:delete:team:admin` |
| [Assign team agents](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignTeamAgents) | `contact_center:write:team:admin` |
| [Create a team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/CreateTeam) | `contact_center:write:team:admin` |
| [List team's parent teams](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getTeamParentTeams) | `contact_center:read:team:admin` |
| [Get a team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getTeamDetail) | `contact_center:read:team:admin` |
| [Update a team](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateateam) | `contact_center:update:team:admin` |
| [List team agents](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listTeamAgents) | `contact_center:read:team:admin` |
| [List teams](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listTeams) | `contact_center:read:team:admin` |
| [Unassign team agents](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/unassignTeamAgents) | `contact_center:delete:team:admin` |

### Users [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#users-5)

| API endpoint | granular scope |
| --- | --- |
| [Update a user's profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateUser) | `contact_center:update:user:admin` |
| [Create a user's profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createUser) | `contact_center:write:user:admin` |
| [Opt-in or opt-out a user's queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/BatchOptInOrOutUserQueues) | `contact_center:update:queue_agent:admin` |
| [Update a user template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateAUserTemplate) | `contact_center:update:user_templates:admin` |
| [List a user's skills](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListAUserSkills) | `contact_center:read:list_user_skills:admin` |
| [Batch create user profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/BatchCreateUsers) | `contact_center:write:batch_users:admin` |
| [List user profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/users) | `contact_center:read:list_users:admin` |
| [List user templates](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/ListUserTemplates) | `contact_center:read:user_templates:admin` |
| [Delete a user template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteAUserTemplate) | `contact_center:delete:user_templates:admin` |
| [Delete a user's recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteUserRecordings) | `contact_center:delete:recording:admin` |
| [Get a user template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Getanusertemplate) | `contact_center:read:user_templates:admin` |
| [Batch delete user profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/batchDeleteUsers) | `contact_center:delete:batch_users:admin` |
| [Update a user's status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Updateauser'sstatus) | `contact_center:update:user:admin` |
| [List a user's queues](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listUserQueues) | `contact_center:read:list_user_queues:admin` |
| [Assign a user's skills](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/assignSkills) | `contact_center:write:user_skill:admin` |
| [List a user's recordings](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listUserRecordings) | `contact_center:read:list_recordings:admin``contact_center:read:list_recordings` |
| [Unassign a user's skill](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteASkill) | `contact_center:delete:user_skill:admin` |
| [Delete a user's profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/userDelete) | `contact_center:delete:user:admin` |
| [Get a user's profile](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getUser) | `contact_center:read:user:admin` |
| [Create a user template](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createAUserTemplate) | `contact_center:write:user_templates:admin` |
| [Batch update user profiles](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/BatchUpdateUsers) | `contact_center:update:batch_users:admin` |
| [Batch update user status](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/Batchupdateuserstatus) | `contact_center:update:batch_users:admin` |

### Variables [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#variables)

| API endpoint | granular scope |
| --- | --- |
| [Update a variable](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/variableUpdate) | `contact_center:update:variable:admin` |
| [Get a variable](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/variableGet) | `contact_center:read:variable:admin` |
| [Create a variable](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createVariable) | `contact_center:write:variable:admin` |
| [List variable groups](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listVariableGroups) | `contact_center:read:list_variable_groups:admin` |
| [Get a variable log](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getVariableLog) | `contact_center:read:variable_log:admin` |
| [Delete a variable group](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/DeleteGroup) | `contact_center:delete:variable_group:admin` |
| [Delete a variable](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/variableDelete) | `contact_center:delete:variable:admin` |
| [Get a variable group](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/getAVariableGroup) | `contact_center:read:variable_group:admin` |
| [Update a variable group](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/updateVariableGroup) | `contact_center:update:variable_group:admin` |
| [List variables](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/variables) | `contact_center:read:list_variables:admin` |
| [List variable logs](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/listVariableLogs) | `contact_center:read:list_variable_logs:admin` |
| [Delete a variable log](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/deleteVariableLog) | `contact_center:delete:variable_log:admin` |
| [Create a variable group](https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/#operation/createVariableGroup) | `contact_center:write:variable_group:admin` |

## Zoom Calendar [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-calendar)

The following are the available **Zoom Calendar** APIs and their associated granular scopes.

### acl [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#acl)

| API endpoint | granular scope |
| --- | --- |
| [Create a new ACL rule](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Insertacl) | `calendar:write:acl``calendar:write:acl:admin` |
| [Delete an existing ACL rule](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Deleteacl) | `calendar:delete:acl``calendar:delete:acl:admin` |
| [Update the specified ACL rule](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Patchacl) | `calendar:update:acl``calendar:update:acl:admin` |
| [List ACL rules of specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Listacl) | `calendar:read:list_acl``calendar:read:list_acl:admin` |
| [Get the specified ACL rule](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Getacl) | `calendar:read:acl``calendar:read:acl:admin` |

### calendar list [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#calendar-list)

| API endpoint | granular scope |
| --- | --- |
| [Insert an existing calendar to the user's own calendarList](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/InsertcalendarList) | `calendar:write:calendar_list` |
| [Delete an existing calendar from the user's own calendarList](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/DeletecalendarList) | `calendar:delete:calendar_list` |
| [List the calendars in the user's own calendarList](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/ListcalendarList) | `calendar:read:list_calendar_lists` |
| [Update an existing calendar in the user's own calendarList](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/PatchcalendarList) | `calendar:update:calendar_list` |
| [Get a specified calendar from the user's own calendarList](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/GetcalendarList) | `calendar:read:calendar_list` |

### calendars [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#calendars)

| API endpoint | granular scope |
| --- | --- |
| [Get the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Getcalendar) | `calendar:read:calendar``calendar:read:calendar:admin` |
| [Delete a calendar owned by a user](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Deletecalendar) | `calendar:delete:calendar``calendar:delete:calendar:admin` |
| [Create a new secondary calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Insertcalendar) | `calendar:write:calendar``calendar:write:calendar:admin` |
| [Update the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Patchcalendar) | `calendar:update:calendar``calendar:update:calendar:admin` |

### colors [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#colors)

| API endpoint | granular scope |
| --- | --- |
| [Get the color definitions for calendars and events](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Getcolor) | `calendar:read:color``calendar:read:color:admin` |

### events [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#events)

| API endpoint | granular scope |
| --- | --- |
| [Quick add an event to the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Quickaddevent) | `calendar:write:quick_add_event``calendar:write:quick_add_event:admin` |
| [Move the specified event from a calendar to another specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Moveevent) | `calendar:write:move_event``calendar:write:move_event:admin` |
| [Get the specified event on the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Getevent) | `calendar:read:event``calendar:read:event:admin` |
| [Update the specified event on the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Patchevent) | `calendar:update:event``calendar:update:event:admin` |
| [Import event to the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Importevent) | `calendar:write:import_event``calendar:write:import_event:admin` |
| [List events on the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Listevent) | `calendar:read:list_events``calendar:read:list_events:admin` |
| [Insert a new event to the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Insertevent) | `calendar:write:event``calendar:write:event:admin` |
| [List all instances of the specified recurring event](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Instanceevent) | `calendar:read:instance_event``calendar:read:instance_event:admin` |
| [Delete an existing event from the specified calendar](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Deleteevent) | `calendar:delete:event``calendar:delete:event:admin` |

### freebusy [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#freebusy)

| API endpoint | granular scope |
| --- | --- |
| [Query freebusy information for a set of calendars](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Queryfreebusy) | `calendar:read:list_events``calendar:read:list_events:admin` |

### settings [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#settings-3)

| API endpoint | granular scope |
| --- | --- |
| [Get the specified user calendar settings of the authenticated user](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Getsetting) | `calendar:read:setting` |
| [List all user calendar settings of the authenticated user](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Listsettings) | `calendar:read:list_settings` |
| [Patch the specified user calendar settings of the authenticated user](https://developers.zoom.us/docs/api/rest/reference/zoom-calendar/methods/#operation/Patchsetting) | `calendar:update:setting``calendar:update:setting:admin` |

## Hub [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#hub)

The following are the available **Hub** APIs and their associated granular scopes.

### Export [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#export-1)

| API endpoint | granular scope |
| --- | --- |
| [Get file content](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/Gethubcontent) | `hub:read:content` |

### File Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#file-management)

| API endpoint | granular scope |
| --- | --- |
| [Duplicate a file](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/Duplicatefile) | `hub:write:content` |
| [Get file duplicate task status](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/GetDuplicateFileTaskStatus) | `hub:read:file_duplicate_task` |
| [Move a file](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/MoveFile) | `hub:write:move``hub:write:move:admin` |

### Import [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#import-2)

| API endpoint | granular scope |
| --- | --- |
| [Create a new file from content](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/createNewFileWithContent) | `hub:write:content` |

### Shared folder [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#shared-folder)

| API endpoint | granular scope |
| --- | --- |
| [Delete a shared folder](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/deleteASharedFolder) | `hub:delete:shared_folder``hub:delete:shared_folder:admin` |
| [List shared folders](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/listSharedFolders) | `hub:read:shared_folder``hub:read:shared_folder:admin` |
| [Get metadata of a shared folder](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/getSharedFolderMetadata) | `hub:read:shared_folder``hub:read:shared_folder:admin` |
| [Modify metadata of a shared folder](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/ModifySharedFolderMetadata) | `hub:update:shared_folder` |
| [Create a shared folder](https://developers.zoom.us/docs/api/rest/reference/Hub/methods/#operation/createASharedFolder) | `hub:write:shared_folder` |

## Zoom Virtual Agent [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-virtual-agent)

The following are the available **Zoom Virtual Agent** APIs and their associated granular scopes.

### Knowledge Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#knowledge-management)

| API endpoint | granular scope |
| --- | --- |
| [Get articles](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetArticles) | `zva:read:list_km_articles``zva:read:list_km_articles:admin` |
| [Get sync](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetSync) | `zva:read:km_kb:admin` |
| [Get article](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetArticle) | `zva:read:km_article``zva:read:km_article:admin` |
| [Delete article](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/DeleteArticle) | `zva:delete:km_article``zva:delete:km_article:admin` |
| [Create sync request](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/CreateSyncRequest) | `zva:update:km_kb:admin` |
| [Update article](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/UpdateArticle) | `zva:update:km_article``zva:update:km_article:admin` |
| [Create article](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/CreateArticle) | `zva:write:km_article``zva:write:km_article:admin` |

### Logs [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#logs-1)

| API endpoint | granular scope |
| --- | --- |
| [List AI Management operation logs](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/ListAIManagementOperationLogs) | `zva:read:list_operation_logs:admin` |

### Report [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#report)

| API endpoint | granular scope |
| --- | --- |
| [Get Zoom Virtual Agent engagements](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetZVAEngagements) | `zva:read:list_engagements:admin` |
| [Get ZVA variable details](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetZVAengagementvariabledetails) | `zva:read:list_variables:admin` |
| [Get ZVA query details](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetZVAQueryDetails) | `zva:read:list_queries:admin` |
| [Get ZVA Surveys](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetZVASurveys) | `zva:read:list_surveys:admin` |
| [Get ZVA transcripts](https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/#operation/GetZVATranscripts) | `zva:read:list_transcripts:admin` |

## Number Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#number-management)

The following are the available **Number Management** APIs and their associated granular scopes.

### Cloud Peering Provider Exchange [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cloud-peering-provider-exchange)

| API endpoint | granular scope |
| --- | --- |
| \[Remove peering phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/deletePeeringPhoneNumbers) | `number_management:delete:peering_number:admin` |
| \[Remove peering phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/deletePeeringPhoneNumbers) | `number_management:delete:peering_number:master` |
| \[List peering phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/listPeeringPhoneNumbers) | `number_management:read:list_peering_numbers:admin` |
| \[List peering phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/listPeeringPhoneNumbers) | `number_management:read:list_peering_numbers:master` |
| \[Update peering phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/updatePeeringPhoneNumbers) | `number_management:update:peering_number:admin` |
| \[Update peering phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/updatePeeringPhoneNumbers) | `number_management:update:peering_number:master` |
| \[List peering phone numbers for provider\](/docs/api/rest/reference/Number Management/methods/#operation/Listpeeringphonenumbersforprovider) | `number_management:read:list_carrier_peering_numbers:admin` |
| \[List peering phone numbers for provider\](/docs/api/rest/reference/Number Management/ma/#operation/Listpeeringphonenumbersforprovider) | `number_management:read:list_carrier_peering_numbers:master` |
| \[Add peering phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/addPeeringPhoneNumbers) | `number_management:write:peering_number:admin` |
| \[Add peering phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/addPeeringPhoneNumbers) | `number_management:write:peering_number:master` |

### Phone Numbers [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-numbers-1)

| API endpoint | granular scope |
| --- | --- |
| \[Add BYOC phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/AddBYOCPhoneNumber) | `number_management:write:byoc_numbers:admin` |
| \[Add BYOC phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/AddBYOCPhoneNumber) | `number_management:write:byoc_numbers:master` |
| \[Delete phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/DeleteNumbers) | `number_management:delete:numbers:admin` |
| \[Delete phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/DeleteNumbers) | `number_management:delete:numbers:master` |
| \[Move Operator Connect Number Microsoft tenant\](/docs/api/rest/reference/Number Management/methods/#operation/MoveOperatorConnectNumbertenant) | `number_management:update:move_number_ms_tenant:admin` |
| \[Move Operator Connect Number Microsoft tenant\](/docs/api/rest/reference/Number Management/ma/#operation/MoveOperatorConnectNumbertenant) | `number_management:update:move_number_ms_tenant:master` |
| \[Get a phone number\](/docs/api/rest/reference/Number Management/methods/#operation/getPhoneNumber) | `number_management:read:numbers:admin` |
| \[Get a phone number\](/docs/api/rest/reference/Number Management/ma/#operation/getPhoneNumber) | `number_management:read:numbers:master` |
| \[Update a phone number\](/docs/api/rest/reference/Number Management/methods/#operation/updatePhoneNumberDetail) | `number_management:update:numbers:admin` |
| \[Update a phone number\](/docs/api/rest/reference/Number Management/ma/#operation/updatePhoneNumberDetail) | `number_management:update:numbers:master` |
| \[List phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/listPhoneNumbers) | `number_management:read:list_numbers:admin` |
| \[List phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/listPhoneNumbers) | `number_management:read:list_numbers:master` |
| \[Allocate/Unallocate phone numbers\](/docs/api/rest/reference/Number Management/methods/#operation/AllocateNumber) | `number_management:write:numbers:admin` |
| \[Allocate/Unallocate phone numbers\](/docs/api/rest/reference/Number Management/ma/#operation/AllocateNumber) | `number_management:write:numbers:master` |

### Phone Plan [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#phone-plan)

| API endpoint | granular scope |
| --- | --- |
| \[List phone number plan information\](/docs/api/rest/reference/Number Management/methods/#operation/Listphonenumberplaninformation) | `number_management:read:numbers_plan:admin` |
| \[List phone number plan information\](/docs/api/rest/reference/Number Management/ma/#operation/Listphonenumberplaninformation) | `number_management:read:numbers_plan:master` |

### SMS Campaigns [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms-campaigns)

| API endpoint | granular scope |
| --- | --- |
| \[List SMS campaigns\](/docs/api/rest/reference/Number Management/methods/#operation/listAccountSMSCampaigns) | `number_management:read:list_sms_campaigns:admin` |
| \[List SMS campaigns\](/docs/api/rest/reference/Number Management/ma/#operation/listAccountSMSCampaigns) | `number_management:read:list_sms_campaigns:master` |
| \[Get an SMS campaign\](/docs/api/rest/reference/Number Management/methods/#operation/GetSMSCampaign) | `number_management:read:sms_campaign:admin` |
| \[Get an SMS campaign\](/docs/api/rest/reference/Number Management/ma/#operation/GetSMSCampaign) | `number_management:read:sms_campaign:master` |
| \[Assign a phone number to SMS campaign\](/docs/api/rest/reference/Number Management/methods/#operation/assignCampaignPhoneNumbers) | `number_management:update:numbers:admin` |
| \[Assign a phone number to SMS campaign\](/docs/api/rest/reference/Number Management/ma/#operation/assignCampaignPhoneNumbers) | `number_management:update:numbers:master` |
| \[Unassign phone number from SMS campaign\](/docs/api/rest/reference/Number Management/methods/#operation/unassignCampaignPhoneNumber) | `number_management:update:numbers:admin` |
| \[Unassign phone number from SMS campaign\](/docs/api/rest/reference/Number Management/ma/#operation/unassignCampaignPhoneNumber) | `number_management:update:numbers:master` |

### SMS Consent [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sms-consent-1)

| API endpoint | granular scope |
| --- | --- |
| \[Update an SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/UpdateSMSConsent) | `number_management:update:sms_consent:admin` |
| \[Update an SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/UpdateSMSConsent) | `number_management:update:sms_consent:master` |
| \[Create an SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/CreateSMSConsent) | `number_management:write:sms_consent:admin` |
| \[Create an SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/CreateSMSConsent) | `number_management:write:sms_consent:master` |
| \[Delete SMS consent policies\](/docs/api/rest/reference/Number Management/methods/#operation/DeleteSMSConsents) | `number_management:delete:sms_consent:admin` |
| \[Delete SMS consent policies\](/docs/api/rest/reference/Number Management/ma/#operation/DeleteSMSConsents) | `number_management:delete:sms_consent:master` |
| \[Unassign phone numbers from SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/UnassignPhoneNumbersFromConsent) | `number_management:delete:numbers:admin` |
| \[Unassign phone numbers from SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/UnassignPhoneNumbersFromConsent) | `number_management:delete:numbers:master` |
| \[Assign phone numbers to SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/AssignPhoneNumbersToConsent) | `number_management:write:numbers:admin` |
| \[Assign phone numbers to SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/AssignPhoneNumbersToConsent) | `number_management:write:numbers:master` |
| \[Get an SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/GetSMSConsent) | `number_management:read:sms_consent:admin` |
| \[Get an SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/GetSMSConsent) | `number_management:read:sms_consent:master` |
| \[List SMS consent policies\](/docs/api/rest/reference/Number Management/methods/#operation/ListSMSConsents) | `number_management:read:sms_consent:admin` |
| \[List SMS consent policies\](/docs/api/rest/reference/Number Management/ma/#operation/ListSMSConsents) | `number_management:read:sms_consent:master` |
| \[List phone numbers assigned to SMS consent policy\](/docs/api/rest/reference/Number Management/methods/#operation/ListConsentPhoneNumbers) | `number_management:read:sms_consent:admin` |
| \[List phone numbers assigned to SMS consent policy\](/docs/api/rest/reference/Number Management/ma/#operation/ListConsentPhoneNumbers) | `number_management:read:sms_consent:master` |

### Setting [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#setting)

| API endpoint | granular scope |
| --- | --- |
| \[List ported numbers\](/docs/api/rest/reference/Number Management/methods/#operation/Listportednumbers) | `number_management:read:list_ported_numbers:admin` |
| \[List ported numbers\](/docs/api/rest/reference/Number Management/ma/#operation/Listportednumbers) | `number_management:read:list_ported_numbers:master` |
| \[List BYOC SIP trunks\](/docs/api/rest/reference/Number Management/methods/#operation/ListBYOCSIPtrunks) | `number_management:read:list_sip_trunks:admin` |
| \[List BYOC SIP trunks\](/docs/api/rest/reference/Number Management/ma/#operation/ListBYOCSIPtrunks) | `number_management:read:list_sip_trunks:master` |
| \[Get ported numbers details\](/docs/api/rest/reference/Number Management/methods/#operation/Getportednumbersdetails) | `number_management:read:ported_number:admin` |
| \[Get ported numbers details\](/docs/api/rest/reference/Number Management/ma/#operation/Getportednumbersdetails) | `number_management:read:ported_number:master` |
| \[List SIP groups\](/docs/api/rest/reference/Number Management/methods/#operation/ListSIPgroups) | `number_management:read:list_sip_groups:admin` |
| \[List SIP groups\](/docs/api/rest/reference/Number Management/ma/#operation/ListSIPgroups) | `number_management:read:list_sip_groups:master` |

## Zoom Commerce [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-commerce)

The following are the available **Zoom Commerce** APIs and their associated granular scopes.

### Account Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#account-management)

| API endpoint | granular scope |
| --- | --- |
| [Get the account details for a Zoom Partner/Subreseller/End Customer](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAccountDetails) | `zoom_commerce:read:account:admin` |
| [Create an end customer account](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createAccount) | `zoom_commerce:write:sub_account:admin` |
| [Get the list of all accounts associated with a Zoom Partner/Sub-Reseller, by the account type](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllAccounts) | `zoom_commerce:read:account:admin` |
| [Add contacts to an existing end customer or your own account.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/addAccountContact) | `zoom_commerce:update:account:admin` |

### Billing [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#billing-1)

| API endpoint | granular scope |
| --- | --- |
| [Gets the PDF document for the billing document ID](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/downloadBillingDoc) | `zoom_commerce:read:billing_documents:admin` |
| [Gets all billing documents for a distributor or a reseller](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllBillingDocs) | `zoom_commerce:read:billing_documents:admin` |
| [Get detailed information about a specific invoice for a distributor or a reseller](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getInvoiceDetail) | `zoom_commerce:read:billing_documents:admin` |

### Deal Registration [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#deal-registration)

| API endpoint | granular scope |
| --- | --- |
| [Get details of a deal registration by registration number](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getDealRegDetails) | `zoom_commerce:read:deal_registration:admin` |
| [Retrieves all valid Zoom Campaigns which a deal registration can be associated with.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getCampaigns) | `zoom_commerce:read:deal_registration:admin` |
| [Gets all valid Deal Registrations for a partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllDealRegs) | `zoom_commerce:read:deal_registration:admin` |
| [Creates a new deal registration for a partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createDealReg) | `zoom_commerce:write:deal_registration:admin` |
| [Updates an existing deal registration](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/Updatesanexistingdealregistration) | `zoom_commerce:write:deal_registration:admin` |

### Order [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#order)

| API endpoint | granular scope |
| --- | --- |
| [Gets all orders for a Zoom partner.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllOrders) | `zoom_commerce:read:order:admin` |
| [Get order details by order reference ID](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getOrderDetails) | `zoom_commerce:read:order:admin` |
| [Create a subscription order for a Zoom partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createOrder) | `zoom_commerce:write:order:admin` |
| [Preview delta order metrics and subscriptions in an order](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createOrderPreview) | `zoom_commerce:write:order:admin` |

### Platform [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#platform)

| API endpoint | granular scope |
| --- | --- |
| [Gets details of all files associated with a quote or deal registration](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/allFileDetails) | `zoom_commerce:read:file:admin` |
| [Download a file associated with a quote or deal registration.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/downloadFile.) | `zoom_commerce:read:file:admin` |
| [Upload an attachment pdf file in context of a deal registration or quote](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/uploadFile) | `zoom_commerce:write:file:admin` |

### Product Catalog [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#product-catalog)

| API endpoint | granular scope |
| --- | --- |
| [Validate offer compatibility and dependencies](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/validateOffers) | `zoom_commerce:read:product_catalog:admin` |
| [Gets the pricebook in a downloadable file](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/downloadPricebook) | `zoom_commerce:read:product_catalog:admin` |
| [Gets Zoom Product Catalog for a Zoom Partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getOffers) | `zoom_commerce:read:product_catalog:admin` |
| [Gets the details for a Zoom product or offer.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getOfferDetail) | `zoom_commerce:read:product_catalog:admin` |

### Quote [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#quote)

| API endpoint | granular scope |
| --- | --- |
| [Gets all quotes for a Zoom partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllQuotes) | `zoom_commerce:read:quote:admin` |
| [Submits a subscription quote for provisioning](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/provisionQuote) | `zoom_commerce:write:quote:admin` |
| [Get quote details by quote reference ID](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getQuoteDetails) | `zoom_commerce:read:quote:admin` |
| [Preview delta quote metrics and subscriptions in a quote](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createQuotePreview) | `zoom_commerce:write:quote:admin` |
| [Update a subscription quote for a Zoom Partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/updateQuote) | `zoom_commerce:write:quote:admin` |
| [Create a subscription quote for a Zoom Partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/createQuote) | `zoom_commerce:write:quote:admin` |

### Subscription [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#subscription)

| API endpoint | granular scope |
| --- | --- |
| [Gets paid subscriptions for a Zoom partner.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllSubscriptions) | `zoom_commerce:read:subscription:admin` |
| [Get trial details for an end customer by their Zoom account number or the trial ID](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getTrialDetails) | `zoom_commerce:read:subscription:admin` |
| [Get trial subscriptions for a Zoom partner](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getAllTrialSubscriptions) | `zoom_commerce:read:subscription:admin` |
| [Gets subscription changes/versions for a given subscription number.](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getSubscriptionVersions) | `zoom_commerce:read:subscription:admin` |
| [Gets subscription details for a given subscription number](https://developers.zoom.us/docs/api/rest/reference/commerce/methods/#operation/getSubscriptionDetails) | `zoom_commerce:read:subscription:admin` |

## Sheets [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sheets)

The following are the available **Sheets** APIs and their associated granular scopes.

### Cell [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#cell)

| API endpoint | granular scope |
| --- | --- |
| [Edit cells on a sheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/editCell) | `sheets:write:content` |
| [Read cell values from a sheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/readCell) | `sheets:read:content` |

### Sheet [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sheet)

| API endpoint | granular scope |
| --- | --- |
| [Add a sheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/addSheets) | `sheets:write:content` |
| [Rename a sheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/renameSheet) | `sheets:update:content` |
| [Delete a sheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/deleteSheets) | `sheets:delete:content` |

### Spreadsheet [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#spreadsheet)

| API endpoint | granular scope |
| --- | --- |
| [Create a spreadsheet](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/createSpreadsheet) | `sheets:write:content` |
| [Get spreadsheet metadata and sample data](https://developers.zoom.us/docs/api/rest/reference/Sheets/methods/#operation/getSpreadsheet) | `sheets:read:content` |

## Canvas [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#canvas)

The following are the available **Canvas** APIs and their associated granular scopes.

### Archiving [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#archiving-2)

| API endpoint | granular scope |
| --- | --- |
| [Download archive attachments](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/BatchGetArchiveAttachmentDownloadUrl) | `docs:read:archive:admin` |
| [List doc archive data](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Listdocarchive) | `docs:read:archive:admin` |

### Collaborator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#collaborator-3)

| API endpoint | granular scope |
| --- | --- |
| [Modify a collaborator’s role on a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ModifyCollaboratorRole) | `docs:update:collaborator``docs:update:collaborator:admin` |
| [Remove a collaborator from a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/RemoveACollaborator) | `docs:delete:collaborator``docs:delete:collaborator:admin` |
| [Add collaborators for a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/AddCollaborators) | `docs:write:collaborator``docs:write:collaborator:admin` |
| [List collaborators of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ListCollaborators) | `docs:read:list_file_collaborators``docs:read:list_file_collaborators:admin` |

### Comment [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#comment-2)

| API endpoint | granular scope |
| --- | --- |
| [Update a comment](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/UpdateComment) | `canvas:update:comment` |
| [List comments](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ListComments) | `canvas:read:comment` |
| [Create a comment](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/CreateComment) | `canvas:write:comment` |
| [Get a comment](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/GetComment) | `canvas:read:comment` |
| [Delete a comment](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/DeleteComment) | `canvas:delete:comment` |

### DataTable Content [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#datatable-content)

| API endpoint | granular scope |
| --- | --- |
| [List columns](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Listdatatablecolumns) | `canvas:read:data_table` |
| [Update rows](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Updaterows) | `canvas:update:data_table` |
| [Search rows](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Searchrows) | `canvas:read:data_table` |
| [Update table metadata](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Updateembeddeddatatablename) | `canvas:update:data_table` |
| [Create a column](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Createacolumn) | `canvas:write:data_table` |
| [List data tables in a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Listdatatablesinfile) | `canvas:read:data_table` |
| [Delete a column](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Deleteacolumn) | `canvas:delete:data_table` |
| [Create table rows](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Createdatatablerows) | `canvas:write:data_table` |
| [Update a column](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Updateacolumn) | `canvas:update:data_table` |
| [Delete rows](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Deleterows) | `canvas:delete:data_table` |
| [Create data table](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Createanembeddeddatatable) | `canvas:write:data_table` |

### Doc Content [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#doc-content)

| API endpoint | granular scope |
| --- | --- |
| [Insert blocks into a document](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Insertblocksintoadocument) | `docs:write:content` |
| [Delete a specific block](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/DeleteBlock) | `docs:delete:content` |
| [Replace a range of blocks](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Replacearangeofblocks) | `docs:update:content` |
| [Update a specific block](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/UpdateBlock) | `docs:update:content` |

### Export [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#export-2)

| API endpoint | granular scope |
| --- | --- |
| [Get file content](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Getfilecontent) | `docs:read:export` |
| [Get file export status](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Getfileexportstatus) | `docs:read:export``docs:read:export:admin` |
| [Create a file export](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Createafileexport) | `docs:write:export``docs:write:export:admin` |

### File Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#file-management-1)

| API endpoint | granular scope |
| --- | --- |
| [Get user My docs info](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/GetUserMyDocsID) | `docs:read:file:admin` |
| [Get metadata of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/QueryFileMetadata) | `docs:read:file``docs:read:file:admin` |
| [Modify metadata of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ModifyMetadata) | `docs:update:file``docs:update:file:admin` |
| [Create a new file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/CreateDoc) | `docs:write:file``docs:write:file:admin` |
| [List all children of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ListAllChildren) | `docs:read:list_children``docs:read:list_children:admin` |
| [Transfer ownership of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/TransferOwnershipOfAFile) | `docs:update:file_owner``docs:update:file_owner:admin` |
| [Delete a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/DeleteFile) | `docs:delete:file``docs:delete:file:admin` |

### File Uploads [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#file-uploads)

| API endpoint | granular scope |
| --- | --- |
| [Create file upload for docs import or attachments](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Uploadfilefordocsimportorattachments) | `docs:write:file_uploads``docs:write:file_uploads:admin` |

### General Access [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#general-access)

| API endpoint | granular scope |
| --- | --- |
| [Get the general access setting of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/GetFileGeneralAccess) | `docs:read:general_access``docs:read:general_access:admin` |
| [Modify the general access setting of a file](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/ModifyFileGeneralAccess) | `docs:update:general_access``docs:update:general_access:admin` |

### Import [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#import-3)

| API endpoint | granular scope |
| --- | --- |
| [Create a new file from content](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/createNewFileWithMarkdown) | `docs:write:import` |
| [Create a new file by import](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Createanewfilebyimport) | `docs:write:import``docs:write:import:admin` |
| [Get file import status](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Getdocsfileimportstatus) | `docs:read:import``docs:read:import:admin` |

### Report [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#report-1)

| API endpoint | granular scope |
| --- | --- |
| [Get activity report](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/GetActivityReport) | `docs:read:activity_report:admin` |

### Search [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#search)

| API endpoint | granular scope |
| --- | --- |
| [Search files](https://developers.zoom.us/docs/api/rest/reference/Canvas/methods/#operation/Search) | `canvas:write:file_search` |

## My Notes [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#my-notes)

The following are the available **My Notes** APIs and their associated granular scopes.

### My Notes Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#my-notes-management)

| API endpoint | granular scope |
| --- | --- |
| \[Get My Notes content and transcript\](/docs/api/rest/reference/My Notes/methods/#operation/DocBridgeInternalOpenAPIService\_InternalOpenAPIGetMyNotes) | `my_notes:read:content` |
| \[List my notes\](/docs/api/rest/reference/My Notes/methods/#operation/ListMyNotesByMeetingId) | `my_notes:read:note` |

## Zoom Video Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-video-management)

The following are the available **Zoom Video Management** APIs and their associated granular scopes.

### Channels [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#channels)

| API endpoint | granular scope |
| --- | --- |
| [List channels](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/listVideoChannels) | `video_mgmt:read:list_channels``video_mgmt:read:list_channels:admin` |
| [Update channel](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/UpdateVideoChannel) | `video_mgmt:update:channel``video_mgmt:update:channel:admin` |
| [Channel actions](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/channelActions) | `video_mgmt:update:channel``video_mgmt:update:channel:admin` |
| [Get channel details](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/getChannelDetail) | `video_mgmt:read:channel``video_mgmt:read:channel:admin` |
| [Delete channel](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeleteChannel) | `video_mgmt:delete:channel``video_mgmt:delete:channel:admin` |
| [Create a channel](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/createChannel) | `video_mgmt:write:channel``video_mgmt:write:channel:admin` |

### Permissions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#permissions)

| API endpoint | granular scope |
| --- | --- |
| [List channel permissions](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/listChannelPermissions) | `video_mgmt:read:list_permissions``video_mgmt:read:list_permissions:admin` |
| [Update channel permissions](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/updateChannelPermissions) | `video_mgmt:update:permissions``video_mgmt:update:permissions:admin` |
| [Create channel permissions](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/createChannelPermissions) | `video_mgmt:write:permissions``video_mgmt:write:permissions:admin` |
| [Delete channel permissions](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeleteChannelPermissions) | `video_mgmt:delete:permissions``video_mgmt:delete:permissions:admin` |

### Playlists [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#playlists)

| API endpoint | granular scope |
| --- | --- |
| [Update playlist](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/UpdatePlaylist) | `video_mgmt:update:playlist``video_mgmt:update:playlist:admin` |
| [Delete playlist](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeletePlaylist) | `video_mgmt:delete:playlist``video_mgmt:delete:playlist:admin` |
| [List playlists](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/ListPlaylists) | `video_mgmt:read:list_playlists``video_mgmt:read:list_playlists:admin` |
| [Add channel playlists](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/AddChannelPlaylists) | `video_mgmt:write:channel_playlists``video_mgmt:write:channel_playlists:admin` |
| [List channel playlists](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/ListChannelPlaylists) | `video_mgmt:read:list_channel_playlists``video_mgmt:read:list_channel_playlists:admin` |
| [Create a playlist](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/createPlaylist) | `video_mgmt:write:playlist``video_mgmt:write:playlist:admin` |
| [Delete channel playlists](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeleteChannelPlaylists) | `video_mgmt:delete:channel_playlists``video_mgmt:delete:channel_playlists:admin` |

### Videos [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#videos)

| API endpoint | granular scope |
| --- | --- |
| [Update metadata for a specific video.](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/updateVideoMetadata) | `video_mgmt:update:video_metadata``video_mgmt:update:video_metadata:admin` |
| [List playlist videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/ListPlaylistVideos) | `video_mgmt:read:list_playlist_videos``video_mgmt:read:list_playlist_videos:admin` |
| [Add playlist videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/AddPlaylistVideos) | `video_mgmt:write:playlist_videos``video_mgmt:write:playlist_videos:admin` |
| [Delete playlist videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeletePlaylistVideos) | `video_mgmt:delete:playlist_videos``video_mgmt:delete:playlist_videos:admin` |
| [Delete channel videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/DeleteChannelVideos) | `video_mgmt:delete:channel_videos``video_mgmt:delete:channel_videos:admin` |
| [Add channel videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/AddChannelVideos) | `video_mgmt:write:channel_videos``video_mgmt:write:channel_videos:admin` |
| [List all videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/ListAllVideos) | `video_mgmt:read:list_videos``video_mgmt:read:list_videos:admin` |
| [List channel videos](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/ListChannelVideos) | `video_mgmt:read:list_channel_videos``video_mgmt:read:list_channel_videos:admin` |
| [Get metadata for a specific video](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/getVideoMetadata) | `video_mgmt:read:video_metadata``video_mgmt:read:video_metadata:admin` |

### files [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#files-1)

| API endpoint | granular scope |
| --- | --- |
| [Upload file for video management](https://developers.zoom.us/docs/api/rest/reference/video-management/methods/#operation/uploadFileToVideoMgmt) | `video_mgmt:write:file``video_mgmt:write:file:admin` |

## Zoom Events [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-events)

The following are the available **Zoom Events** APIs and their associated granular scopes.

### Attendee Actions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#attendee-actions)

| API endpoint | granular scope |
| --- | --- |
| [Update event attendee actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/UpdateEventAttendeeActions) | `zoom_events:update:batch_attendee_actions``zoom_events:update:batch_attendee_actions:admin` |
| [List event attendee actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListEventAttendeeActions) | `zoom_events:read:list_attendee_actions``zoom_events:read:list_attendee_actions:admin` |
| [List session attendee actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListSessionAttendeeActions) | `zoom_events:read:list_session_attendee_actions``zoom_events:read:list_session_attendee_actions:admin` |
| [Update session attendee actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/UpdateSessionAttendeeActions) | `zoom_events:update:batch_session_attendee_actions``zoom_events:update:batch_session_attendee_actions:admin` |

### Co Editors [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#co-editors)

| API endpoint | granular scope |
| --- | --- |
| [Add or remove event co-editors](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/coeditoractions) | `zoom_events:write:coeditor``zoom_events:write:coeditor:admin` |
| [List coeditors](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getCoEditors) | `zoom_events:read:list_coeditors``zoom_events:read:list_coeditors:admin` |

### Emails [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#emails)

| API endpoint | granular scope |
| --- | --- |
| [List event emails sent status](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/listEmailSentStatuses) | `zoom_events:read:list_emails_status``zoom_events:read:list_emails_status:admin` |
| [List event email types](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/listEmailTypes) | `zoom_events:read:list_email_types``zoom_events:read:list_email_types:admin` |

### Event Access [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#event-access)

| API endpoint | granular scope |
| --- | --- |
| [List event access links](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEventAccessLinks) | `zoom_events:read:list_access_links``zoom_events:read:list_access_links:admin` |
| [Get event access link](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/GetEventAccessLink) | `zoom_events:read:access_links``zoom_events:read:access_links:admin` |
| [Update event access](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateEventAccess) | `zoom_events:update:access_links``zoom_events:update:access_links:admin` |
| [Delete event access link](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteEventAccessLink) | `zoom_events:delete:access_links``zoom_events:delete:access_links:admin` |
| [Create event access link](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createEventAccessLink) | `zoom_events:write:access_links``zoom_events:write:access_links:admin` |

### Events [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#events-1)

| API endpoint | granular scope |
| --- | --- |
| [List events](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEvents) | `zoom_events:read:list_events``zoom_events:read:list_events:admin` |
| [Delete an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteEvent) | `zoom_events:delete:event``zoom_events:delete:event:admin` |
| [Event actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/EventActions) | `zoom_events:write:event``zoom_events:write:event:admin` |
| [Update an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateEvent) | `zoom_events:update:event``zoom_events:update:event:admin` |
| [Get an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEventInfo) | `zoom_events:read:event``zoom_events:read:event:admin` |
| [Create an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createEvent) | `zoom_events:write:event``zoom_events:write:event:admin` |

### Exhibitors [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#exhibitors)

| API endpoint | granular scope |
| --- | --- |
| [Create an exhibitor](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createExhibitor) | `zoom_events:write:exhibitor``zoom_events:write:exhibitor:admin` |
| [List exhibitors](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getExhibitors) | `zoom_events:read:list_exhibitors``zoom_events:read:list_exhibitors:admin` |
| [Update exhibitor for an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateExhibitor) | `zoom_events:update:exhibitor``zoom_events:update:exhibitor:admin` |
| [Delete an exhibitor](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteExhibitor) | `zoom_events:delete:exhibitor``zoom_events:delete:exhibitor:admin` |
| [List sponsor tiers](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListSponsorTiers) | `zoom_events:read:list_sponsor_tiers``zoom_events:read:list_sponsor_tiers:admin` |
| [Get an exhibitor](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getExhibitorInfo) | `zoom_events:read:exhibitor``zoom_events:read:exhibitor:admin` |

### Files [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#files-2)

| API endpoint | granular scope |
| --- | --- |
| [Upload events multipart files](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/uploadMultipartEventFile) | `zoom_events:write:file_upload``zoom_events:write:file_upload:admin` |
| [Initiate and complete the multipart file upload](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/initiateAndCompleteAEventMultipartUpload.) | `zoom_events:write:file_upload``zoom_events:write:file_upload:admin` |
| [Upload events file](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/uploadEventFile) | `zoom_events:write:file_upload``zoom_events:write:file_upload:admin` |

### Hubs [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#hubs)

| API endpoint | granular scope |
| --- | --- |
| [Creates a new hub host](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createHubHost) | `zoom_events:write:hub_host``zoom_events:write:hub_host:admin` |
| [List hub Hosts](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/gethubhostList) | `zoom_events:read:list_hub_hosts``zoom_events:read:list_hub_hosts:admin` |
| [List hub videos](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListHubVideos) | `zoom_events:read:list_hub_videos``zoom_events:read:list_hub_videos:admin` |
| [List hubs](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getHubList) | `zoom_events:read:list_hubs``zoom_events:read:list_hubs:admin` |
| [Remove hub host](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteHubHost) | `zoom_events:delete:hub_host``zoom_events:delete:hub_host:admin` |

### Insights [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#insights)

| API endpoint | granular scope |
| --- | --- |
| [Get attendee engagement data](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getAttendeeEngagement) | `zoom_events:read:attendee_engagement``zoom_events:read:attendee_engagement:admin` |

### Registrants [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#registrants)

| API endpoint | granular scope |
| --- | --- |
| [List registrants](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getRegistrants) | `zoom_events:read:list_registrants``zoom_events:read:list_registrants:admin` |
| [List session attendees](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSessionAttendeeList) | `zoom_events:read:list_session_attendees``zoom_events:read:list_session_attendees:admin` |

### Reports [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#reports-4)

| API endpoint | granular scope |
| --- | --- |
| [Get VOD channel registration report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/VodChannelReigistration) | `zoom_events:read:vod_registrations``zoom_events:read:vod_registrations:admin` |
| [Get event survey report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/EventSurveyReportApi) | `zoom_events:read:list_session_surveys``zoom_events:read:list_session_surveys:admin` |
| [Get session attendance report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/SessionAttendanceReport) | `zoom_events:read:session_attendance``zoom_events:read:session_attendance:admin` |
| [Get chat transcripts report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ChatTranscriptsReport) | `zoom_events:read:chat_transcripts``zoom_events:read:chat_transcripts:admin` |
| [Get custom report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getCustomEventReport) | `zoom_events:read:custom_report``zoom_events:read:custom_report:admin` |
| [Get event registrations report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/EventRegistrationsReport) | `zoom_events:read:event_registration``zoom_events:read:event_registration:admin` |
| [Get event attendance (Live or Lobby) report](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/EventAttendanceReport) | `zoom_events:read:event_attendance``zoom_events:read:event_attendance:admin` |

### Sessions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#sessions-2)

| API endpoint | granular scope |
| --- | --- |
| [List sessions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEventSessionList) | `zoom_events:read:list_sessions``zoom_events:read:list_sessions:admin` |
| [List session reservations](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListSessionReservations) | `zoom_events:read:list_session_reservations``zoom_events:read:list_session_reservations:admin` |
| [Add session reservations](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/AddSessionReservations) | `zoom_events:write:session_reservations``zoom_events:write:session_reservations:admin` |
| [Update a session](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateEventSession) | `zoom_events:update:session``zoom_events:update:session:admin` |
| [Get the session information](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEventSessionInfo) | `zoom_events:read:session``zoom_events:read:session:admin` |
| [Create a session](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createEventSession) | `zoom_events:write:session``zoom_events:write:session:admin` |
| [Get session livestream configuration](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSessionLivestreamConfiguration) | `zoom_events:read:session_livestream_config``zoom_events:read:session_livestream_config:admin` |
| [Delete session reservations](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/DeleteSessionReservations) | `zoom_events:delete:session_reservations``zoom_events:delete:session_reservations:admin` |
| [Update session livestream configuration](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/UpdateSessionLivestreamConfiguration) | `zoom_events:update:session_livestream_config``zoom_events:update:session_livestream_config:admin` |
| [List session interpreters](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSessionInterpreterList) | `zoom_events:read:list_session_interpreters``zoom_events:read:list_session_interpreters:admin` |
| [Delete a session](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteEventSession) | `zoom_events:delete:session``zoom_events:delete:session:admin` |
| [Create or update session polls](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateSessionPolls) | `zoom_events:update:session_poll``zoom_events:update:session_poll:admin` |
| [List session polls](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSessionPolls) | `zoom_events:read:list_session_polls``zoom_events:read:list_session_polls:admin` |
| [Get ticket session join token by Event ID and Session ID](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSessionJoinToken) | `zoom_events:read:session_token``zoom_events:read:session_token:admin` |
| [Create or update session interpreters](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateSessionInterpreters) | `zoom_events:update:session_interpreter``zoom_events:update:session_interpreter:admin` |

### Speakers [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#speakers)

| API endpoint | granular scope |
| --- | --- |
| [List speakers](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSpeakers) | `zoom_events:read:list_speakers``zoom_events:read:list_speakers:admin` |
| [Get a speaker](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getSpeaker) | `zoom_events:read:speaker``zoom_events:read:speaker:admin` |
| [Create a speaker](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createSpeaker) | `zoom_events:write:speaker``zoom_events:write:speaker:admin` |
| [Delete a speaker](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteSpeaker) | `zoom_events:delete:speaker``zoom_events:delete:speaker:admin` |
| [Update a speaker](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateSpeaker) | `zoom_events:update:speaker``zoom_events:update:speaker:admin` |

### Ticket Types [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#ticket-types)

| API endpoint | granular scope |
| --- | --- |
| [List ticket types](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getEventTicketTypes) | `zoom_events:read:list_ticket_types``zoom_events:read:list_ticket_types:admin` |
| [Update registration questions for ticket type](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateRegistrationQuestionsForTicketType) | `zoom_events:update:registraion_question``zoom_events:update:registraion_question:admin` |
| [Delete a ticket type](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteEventTicketType) | `zoom_events:delete:ticket_type``zoom_events:delete:ticket_type:admin` |
| [Update ticket type for an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateTicketType) | `zoom_events:update:ticket_type``zoom_events:update:ticket_type:admin` |
| [List registration questions for ticket type](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getRegistrationQuestionsForTicketType) | `zoom_events:read:list_registration_questions``zoom_events:read:list_registration_questions:admin` |
| [Create an event ticket type](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createTicketType) | `zoom_events:write:ticket_type``zoom_events:write:ticket_type:admin` |
| [Update registration questions for an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateRegistrationQuestionsForEvent) | `zoom_events:update:registraion_question``zoom_events:update:registraion_question:admin` |
| [List registration questions for an event](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getRegistrationQuestionsForEvent) | `zoom_events:read:list_registration_questions``zoom_events:read:list_registration_questions:admin` |

### Tickets [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#tickets)

| API endpoint | granular scope |
| --- | --- |
| [Get a ticket](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getTicketDetails) | `zoom_events:read:ticket``zoom_events:read:ticket:admin` |
| [Create tickets](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createTickets) | `zoom_events:write:ticket``zoom_events:write:ticket:admin` |
| [Delete a ticket](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/deleteTicket) | `zoom_events:delete:ticket``zoom_events:delete:ticket:admin` |
| [Update ticket](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/Updateticket) | `zoom_events:write:ticket``zoom_events:write:ticket:admin` |
| [List tickets](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getTickets) | `zoom_events:read:list_tickets``zoom_events:read:list_tickets:admin` |

### Video On-Demand [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#video-on-demand)

| API endpoint | granular scope |
| --- | --- |
| [VOD channel actions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/vodChannelActions) | `zoom_events:update:vod_channel``zoom_events:update:vod_channel:admin` |
| [List VOD channel videos](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListVODChannelVideos) | `zoom_events:read:list_vod_channel_videos``zoom_events:read:list_vod_channel_videos:admin` |
| [Delete VOD Channel](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/DeleteVODChannel) | `zoom_events:delete:vod_channel``zoom_events:delete:vod_channel:admin` |
| [Create VOD channel](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/createVodChannel) | `zoom_events:write:vod_channel``zoom_events:write:vod_channel:admin` |
| [Delete VOD channel video](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/DeleteVODChannelVideo) | `zoom_events:delete:vod_channel_videos``zoom_events:delete:vod_channel_videos:admin` |
| [Update VOD channel](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/UpdateVideoChannel) | `zoom_events:update:vod_channel``zoom_events:update:vod_channel:admin` |
| [Get VOD channel details](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getVODChannelDetail) | `zoom_events:read:vod_channel``zoom_events:read:vod_channel:admin` |
| [List channels](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getVODChannels) | `zoom_events:read:list_all_vod_channels``zoom_events:read:list_all_vod_channels:admin` |
| [Add VOD channel videos](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/AddVODChannelVideos) | `zoom_events:write:vod_channel_videos``zoom_events:write:vod_channel_videos:admin` |

### Video On-Demand Registrations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#video-on-demand-registrations)

| API endpoint | granular scope |
| --- | --- |
| [List VOD Registration](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/ListVODRegistration) | `zoom_events:read:vod_registrations``zoom_events:read:vod_registrations:admin` |
| [Get VOD Registration Questions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getRegistrationQuestionsForVODChannel) | `zoom_events:read:vod_registration_questions``zoom_events:read:vod_registration_questions:admin` |
| [update VOD channel registration questions](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateRegistrationQuestionsForVODchannel) | `zoom_events:update:vod_registration_questions``zoom_events:update:vod_registration_questions:admin` |
| [VOD channel registration](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/VODTicketRegistration) | `zoom_events:write:vod_registration``zoom_events:write:vod_registration:admin` |

### Videos [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#videos-1)

| API endpoint | granular scope |
| --- | --- |
| [Get metadata for a specific video](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/getVideoMetadata) | `zoom_events:read:video_metadata``zoom_events:read:video_metadata:admin` |
| [Update metadata for a specific video](https://developers.zoom.us/docs/api/rest/reference/event/methods/#operation/updateVideoMetadata) | `zoom_events:update:video_metadata``zoom_events:update:video_metadata:admin` |

## Zoom Mesh [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-mesh)

The following are the available **Zoom Mesh** APIs and their associated granular scopes.

### Locations [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#locations)

| API endpoint | granular scope |
| --- | --- |
| [List Mesh locations](https://developers.zoom.us/docs/api/rest/reference/zoom-mesh/methods/#operation/ListMeshLocation) | `zoom_mesh:read:list_locations:admin` |
| [Create a Mesh location](https://developers.zoom.us/docs/api/rest/reference/zoom-mesh/methods/#operation/CreateMeshLocation) | `zoom_mesh:write:location:admin` |
| [Get a Mesh location](https://developers.zoom.us/docs/api/rest/reference/zoom-mesh/methods/#operation/GetMeshLocation) | `zoom_mesh:read:location:admin` |
| [Delete a Mesh location](https://developers.zoom.us/docs/api/rest/reference/zoom-mesh/methods/#operation/DeleteMeshLocation) | `zoom_mesh:delete:location:admin` |
| [Update a Mesh location](https://developers.zoom.us/docs/api/rest/reference/zoom-mesh/methods/#operation/UpdateMeshLocation) | `zoom_mesh:update:location:admin` |

## Marketplace [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#marketplace)

The following are the available **Marketplace** APIs and their associated granular scopes.

### App [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#app)

| API endpoint | granular scope |
| --- | --- |
| [List apps](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/ListApps) | `marketplace:read:list_apps:admin` |
| [Get an app's user requests](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getAppUserRequests) | `marketplace:read:app_request:admin` |
| [Update app's request status](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/updateAppRequestStatus) | `marketplace:update:app_request:admin` |
| [Update app pre approval setting](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/Updateapppreapprovalsetting) | `marketplace:write:app_pre_approve:admin` |
| [Generate Zoom App Deeplink](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/GenerateZoomAppDeeplink) | `marketplace:write:app_deeplink:admin` |
| [Get user's custom field values](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getCustomFieldValues) | `marketplace:read:custom_fields:admin``marketplace:read:custom_fields` |
| [Get API call logs](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/Getapicalllogs) | `marketplace:read:list_api_logs:admin` |
| [Send app notifications](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/Sendappnotifications) | `marketplace:write:notifications` |
| [Create apps](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/CreateApps) | `marketplace:write:app``marketplace:write:app:admin` |
| [Create apps](https://developers.zoom.us/docs/api/rest/reference/marketplace/ma/#operation/CreateApps) | `marketplace:write:app:master` |
| [Get app user entitlements](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getAppUserEntitlementRequests) | `marketplace:read:list_user_entitlements``marketplace:read:list_user_entitlements:admin` |
| [Get a user's entitlements](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getUserEntitlementRequests) | `marketplace:read:list_user_entitlements``marketplace:read:list_user_entitlements:admin` |
| [Get information about an app](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getAppInfo) | `marketplace:read:app``marketplace:read:app:admin` |
| [Add app allow requests for users](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/AddAppAllowRequestsForUsers) | `marketplace:write:app_request:admin` |
| [Rotate client secret](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/RotateClientSecret) | `marketplace:update:client_secret` |
| [Get a user's app requests](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getUserAppRequests) | `marketplace:read:list_user_app_requests:admin``marketplace:read:list_user_app_requests` |
| [Enable or disable user app subscription](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/Enable/Disableuserappsubscription) | `marketplace:write:app:admin` |
| [Deletes an app](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/deleteApp) | `marketplace:write:app``marketplace:write:app:admin` |

### Manifest [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#manifest)

| API endpoint | granular scope |
| --- | --- |
| [Export an app manifest from an existing app](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/getAppManifest) | `marketplace:read:app``marketplace:read:app:admin` |
| [Update an app by manifest](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/updateAppByManifest) | `marketplace:write:app``marketplace:write:app:admin` |
| [Validate an app manifest](https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/#operation/validatingManifest) | `marketplace:read:app``marketplace:read:app:admin` |

## SCIM [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#scim)

The following are the available **SCIM** APIs and their associated granular scopes.

### Group [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#group)

| API endpoint | granular scope |
| --- | --- |
| [Create a group](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupScim2Create) | `scim2:admin` |
| [List groups](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupSCIM2List) | `scim2:admin` |
| [Delete a group](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupSCIM2Delete) | `scim2:admin` |
| [Get a group](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupSCIM2Get) | `scim2:admin` |
| [Update a group](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupSCIM2Update) | `scim2:admin` |

### User [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#user)

| API endpoint | granular scope |
| --- | --- |
| [Get a user](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userSCIM2Get) | `scim2:admin` |
| [Delete a user](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userSCIM2Delete) | `scim2:admin` |
| [Update a user](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userSCIM2Update) | `scim2:admin` |
| [List users](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userSCIM2List) | `scim2:admin` |
| [Deactivate a user](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userADSCIM2Deactivate) | `scim2:admin` |
| [Create a user](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/userScim2Create) | `scim2:admin` |

## Zoom Auto Dialer [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#zoom-auto-dialer)

The following are the available **Zoom Auto Dialer** APIs and their associated granular scopes.

### Call History & Reporting [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-history--reporting)

| API endpoint | granular scope |
| --- | --- |
| \[Get Seller Productivity Report\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetSellerProductivityReport) | `zoom_auto_dialer:read:user_seller_productivity:admin` |
| \[Get call history by ID\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetCallDetailsbyCallID) | `zoom_auto_dialer:read:call_history:admin` |
| \[Get Report Call History\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetReportCallHistory) | `zoom_auto_dialer:read:list_seller_productivity:admin` |
| \[Get Call History\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetCallHistory) | `zoom_auto_dialer:read:call_history:admin` |

### Call List Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#call-list-management)

| API endpoint | granular scope |
| --- | --- |
| \[Create Call List\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/CreateCallList) | `zoom_auto_dialer:write:call_lists:admin` |
| \[Update Call List\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/UpdateCallList) | `zoom_auto_dialer:update:call_lists:admin` |
| \[List Call Lists\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/ListCallLists) | `zoom_auto_dialer:read:call_lists:admin` |
| \[Get Call List by ID\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetCallListbyID) | `zoom_auto_dialer:read:call_lists:admin` |
| \[Delete Call List\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/DeleteCallList) | `zoom_auto_dialer:delete:call_lists:admin` |

### Prospect Management [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#prospect-management)

| API endpoint | granular scope |
| --- | --- |
| \[Delete Prospect\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/DeleteProspect) | `zoom_auto_dialer:delete:prospects:admin` |
| \[Get Prospect by ID\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/GetProspectbyID) | `zoom_auto_dialer:read:prospects:admin` |
| \[Create Prospect\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/CreateProspect) | `zoom_auto_dialer:write:prospects:admin` |
| \[Update Prospect\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/UpdateProspect) | `zoom_auto_dialer:update:prospects:admin` |
| \[List All Prospects in Call List\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/ListAllProspectsInCallList) | `zoom_auto_dialer:read:prospects:admin` |
| \[Create Prospects batch\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/CreateProspects) | `zoom_auto_dialer:write:prospects:admin` |
| \[Update Prospects batch\](/docs/api/rest/reference/Zoom Auto Dialer/methods/#operation/UpdateProspects) | `zoom_auto_dialer:update:prospects:admin` |

## AIAGW\_SDK [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#aiagw_sdk)

The following are the available **AIAGW\_SDK** APIs and their associated granular scopes.

### Decisions [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#decisions)

| API endpoint | granular scope |
| --- | --- |
| [Evaluate decision questions](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/decideDecisions) | `aiservices:write:decide:admin` |

### Scribe [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#scribe)

| API endpoint | granular scope |
| --- | --- |
| [Get Batch Job Status](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchJobStatus) | `aiservices:read:scribe_batch_job:admin` |
| [Live Scribe WebSocket](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/liveTranscribe) | `aiservices:write:live_transcribe:admin` |
| [Get Batch Scribe Job File](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchScribeJobFile) | `aiservices:read:scribe_batch_job_file:admin` |
| [List Batch Jobs](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchJobs) | `aiservices:read:list_scribe_batch_jobs:admin` |
| [Submit Batch Scribe Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/submitBatchAsr) | `aiservices:write:scribe_batch_job:admin` |
| [Scribe (Synchronous)](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/createFastAsr) | `aiservices:write:transcribe:admin` |
| [Cancel Batch Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/cancelBatchJob) | `aiservices:delete:scribe_batch_job:admin` |
| [List Batch Job Files](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchJobFiles) | `aiservices:read:list_scribe_batch_job_files:admin` |

### Speech Summarization [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#speech-summarization)

| API endpoint | granular scope |
| --- | --- |
| [Summarize (Synchronous)​](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/transcribeAndSummarizeStream) | `aiservices:write:transcribe-summarize:admin` |

### Summarizer [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#summarizer)

| API endpoint | granular scope |
| --- | --- |
| [List Batch Summarizer Jobs](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchSummarizerJobs) | `aiservices:read:list_summarizer_batch_jobs:admin` |
| [List Batch Summarizer Job Files](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchSummarizerJobFiles) | `aiservices:read:list_summarizer_batch_job_files:admin` |
| [Get Batch Summarizer Job File](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchSummarizerJobFile) | `aiservices:read:summarizer_batch_job_file:admin` |
| [Get Batch Summarizer Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchSummarizerJob) | `aiservices:read:summarizer_batch_job:admin` |
| [Submit Batch Summarizer Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/submitBatchSummarizer) | `aiservices:write:summarizer_batch_job:admin` |
| [Cancel Batch Summarizer Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/cancelBatchSummarizerJob) | `aiservices:delete:summarizer_batch_job:admin` |
| [Summarize (Synchronous)](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/summarize) | `aiservices:write:summarize:admin` |

### Translator [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#translator)

| API endpoint | granular scope |
| --- | --- |
| [Get Batch Translator Job File](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchTranslatorJobFile) | `aiservices:read:translator_batch_job_file:admin` |
| [Translate (Synchronous)](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/translate) | `aiservices:write:translate:admin` |
| [List Batch Translator Jobs](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchTranslatorJobs) | `aiservices:read:list_translator_batch_jobs:admin` |
| [Submit Batch Translator Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/submitBatchTranslator) | `aiservices:write:translator_batch_job:admin` |
| [List Batch Translator Job Files](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/listBatchTranslatorJobFiles) | `aiservices:read:list_translator_batch_job_files:admin` |
| [Get Batch Translator Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/getBatchTranslatorJob) | `aiservices:read:translator_batch_job:admin` |
| [Cancel Batch Translator Job](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/cancelBatchTranslatorJob) | `aiservices:delete:translator_batch_job:admin` |

### VoiceAgent [\#](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/\#voiceagent)

| API endpoint | granular scope |
| --- | --- |
| [Live Voice Agent WebSocket](https://developers.zoom.us/docs/api/rest/reference/AIAGW_SDK/methods/#operation/liveVoiceAgent) | `aiservices:read:voice-agent:admin` |