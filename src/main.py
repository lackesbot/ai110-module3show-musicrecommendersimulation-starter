"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"favorite_genre": "pop",
                 "favorite_mood": "happy",
                 "favorite_energy": 0.8,
                 "likes_acoustic": False}
    


    high_energy_pop = {"favorite_genre": "pop",
                    "favorite_mood": "happy",
                    "favorite_energy": 0.9,
                    "likes_acoustic": False
    }

    chill_lofi = {"favorite_genre": "lofi",
                 "favorite_mood": "chill",
                 "favorite_energy": 0.3,
                 "likes_acoustic": False
    }

    deep_intense_rock = {"favorite_genre": "rock",
                 "favorite_mood": "intense",
                 "favorite_energy": 0.91,
                 "likes_acoustic": True
    }

    # --- Adversarial / edge-case profiles ---
    # Out-of-range energy: nothing clamps favorite_energy to [0, 1], so this can
    # make energyS negative and actually subtract from a song's score.
    out_of_range_energy = {"favorite_genre": "pop",
                 "favorite_mood": "happy",
                 "favorite_energy": 1.5,
                 "likes_acoustic": False
    }

    # Nonexistent genre: not present in songs.csv at all. Checks that scoring
    # degrades gracefully to energy/acoustic-only instead of erroring.
    nonexistent_genre = {"favorite_genre": "vaporwave",
                 "favorite_mood": "chill",
                 "favorite_energy": 0.5,
                 "likes_acoustic": False
    }

    # Missing key: no "favorite_mood" at all. score_song has no .get() default,
    # so this should raise KeyError - confirms that's the intended failure mode.
    missing_key_profile = {"favorite_genre": "pop",
                 "favorite_energy": 0.6,
                 "likes_acoustic": False
    }


    profiles = {
        "Starter profile": user_prefs,
        "High energy pop": high_energy_pop,
        "Chill lofi": chill_lofi,
        "Deep intense rock": deep_intense_rock,
        "Adversarial: out-of-range energy": out_of_range_energy,
        "Adversarial: nonexistent genre": nonexistent_genre,
        "Adversarial: missing key": missing_key_profile,
    }

    for label, profile in profiles.items():
        print("\n" + "=" * 40)
        print(f"TOP RECOMMENDATIONS - {label}")
        print("=" * 40)
        try:
            recommendations = recommend_songs(profile, songs, k=5)
        except KeyError as e:
            print(f"KeyError raised as expected: missing {e}")
            continue
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"\n{rank}. {song['title']}  (Score: {score:.2f})")
            for reason in explanation:
                print(f"     - {reason}")
    print("\n" + "=" * 40 + "\n")


if __name__ == "__main__":
    main()
