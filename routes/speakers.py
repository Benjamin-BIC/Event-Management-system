from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.speaker import Speaker, SpeakerCreate
from services.speaker_service import speaker_service

router = APIRouter()


@router.post("/", response_model=Speaker, status_code=status.HTTP_201_CREATED)
async def create_speaker(speaker: SpeakerCreate):
    return speaker_service.create_speaker(speaker)


@router.get("/", response_model=List[Speaker])
async def read_speakers():
    return speaker_service.get_speakers()


@router.get("/{speaker_id}", response_model=Speaker)
async def read_speaker(speaker_id: int):
    speaker = speaker_service.get_speaker(speaker_id)
    if speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker


@router.put("/{speaker_id}", response_model=Speaker)
async def update_speaker(speaker_id: int, speaker: SpeakerCreate):
    updated_speaker = speaker_service.update_speaker(speaker_id, speaker)
    if updated_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return updated_speaker


@router.delete("/{speaker_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_speaker(speaker_id: int):
    if not speaker_service.delete_speaker(speaker_id):
        raise HTTPException(status_code=404, detail="Speaker not found")
    return
