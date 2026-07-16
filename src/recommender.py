from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


import csv
from csv import DictReader


GENRE_WEIGHT = 30
MOOD_WEIGHT = 10
ENERGY_WEIGHT = 15
ACOUSTIC_WEIGHT = 10

score = 0


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    favorite_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs.csv into a list of dicts with numeric fields converted to int/float."""
    
    songs = []
    print(f"Loading songs from {csv_path}...")
    with open (csv_path, 'r') as data:
        for line in csv.DictReader(data):
            line["id"] = int(line["id"])
            line["energy"] = float(line["energy"])
            line["tempo_bpm"] = float(line["tempo_bpm"])
            line["valence"] = float(line["valence"])
            line["danceability"] = float(line["danceability"])
            line["acousticness"] = float(line["acousticness"])
            songs.append(line) 
    
    return songs
   

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user_prefs on genre, mood, energy, and acousticness, returning (score, reasons)."""
    score = 0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += GENRE_WEIGHT 
        reasons.append(f"Genre matches (+{GENRE_WEIGHT})")

    if song["mood"] == user_prefs.get("favorite_mood"):
        score += MOOD_WEIGHT
        reasons.append(f"Mood matches (+{MOOD_WEIGHT})")

    if "favorite_energy" in user_prefs:
        energyS = 1 - abs(song["energy"] - user_prefs["favorite_energy"])
        score += ENERGY_WEIGHT * energyS

        if energyS > 0.3:
            reasons.append(f"Energy matches ({+ENERGY_WEIGHT})")

    acousticS = 1 - abs(song["acousticness"] - user_prefs["likes_acoustic"])
    score += ACOUSTIC_WEIGHT * acousticS

    if acousticS > 0.5:
        reasons.append(f"Acousticness matches (+{ACOUSTIC_WEIGHT})")

    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user_prefs and returns the top k, sorted by score descending."""
    rankedS = []
    
    for songF in songs:
       score, explanation = score_song(user_prefs, songF)
       rankedS.append((songF, score, explanation))
    
    #you have to specify which value you're comparing with in a tuple
    rankedS.sort(key=lambda item : item[1], reverse=True)

    finalRank = rankedS[:k]

    return finalRank