from typing import List, Optional
from schemas.speaker import Speaker, SpeakerCreate


class SpeakerService:
    def __init__(self):
        self.speakers_db = []
        self.next_id = 1

    def create_speaker(self, speaker: SpeakerCreate) -> Speaker:
        db_speaker = Speaker(id=self.next_id, **speaker.model_dump())
        self.speakers_db.append(db_speaker)
        self.next_id += 1
        return db_speaker

    def get_speaker(self, speaker_id: int) -> Optional[Speaker]:
        for speaker in self.speakers_db:
            if speaker.id == speaker_id:
                return speaker
        return None

    def get_speakers(self) -> List[Speaker]:
        return self.speakers_db

    def update_speaker(self, speaker_id: int, speaker: SpeakerCreate) -> Optional[Speaker]:
        for i, speaker in enumerate(self.speakers_db):
            if speaker.id == speaker_id:
                updated_speaker = speaker.model_copy(
                    update=speaker.model_dump())
                self.speakers_db[i] = updated_speaker
                return updated_speaker
        return None

    def delete_speaker(self, speaker_id: int) -> bool:
        initial_len = len(self.speakers_db)
        self.speakers_db = [
            speaker for speaker in self.speakers_db if speaker.id != speaker_id]
        return len(self.speakers_db) != initial_len


speaker_service = SpeakerService()
