# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
When it comes to platforms like Spotify, recommending songs to the user takes in and uses a number of variable. Variables such as mood, genre, energy, tempo, acoustiness and many more are used. For my recommender, I'll be focusing on only 4 variables; genre, mood, energy & acousticness. I'm focusing on these variables because they focus on what the user inputs rather than a variable number that is computed such as how tempo & valence are. The scoring system is heavliy weighted on the genre and thus somne songs taht might fit the category will get a low score.

Some prompts to answer:

- What features does each `Song` use in your system: Genre, Mood, Energy & Acoustic 
- What information does your `UserProfile` store. It store what the user likes and prefers in terms of category. 
- How does your `Recommender` compute a score for each song. It will compare and compute the score for each then rank the top nones. 
- How do you choose which songs to recommend. By comparing and contrasting them with other songs and whichever is the highest wins. 

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loading songs from data/songs.csv...

========================================
TOP RECOMMENDATIONS
========================================

1. Sunrise City  (Score: 62.90)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)
     - Acousticness matches (+10)

2. Gym Hero  (Score: 52.55)
     - Genre matches (+30)
     - Energy matches (15)
     - Acousticness matches (+10)

3. Rooftop Lights  (Score: 30.90)
     - Mood matches (+10)
     - Energy matches (15)
     - Acousticness matches (+10)

4. Concrete Throne  (Score: 24.20)
     - Energy matches (15)
     - Acousticness matches (+10)

5. Pulse Horizon  (Score: 23.20)
     - Energy matches (15)
     - Acousticness matches (+10)

========================================

========================================
TOP RECOMMENDATIONS - High energy pop
========================================

1. Sunrise City  (Score: 62.00)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)
     - Acousticness matches (+10)

2. Gym Hero  (Score: 54.05)
     - Genre matches (+30)
     - Energy matches (15)
     - Acousticness matches (+10)

3. Rooftop Lights  (Score: 29.40)
     - Mood matches (+10)
     - Energy matches (15)
     - Acousticness matches (+10)

4. Pulse Horizon  (Score: 24.10)
     - Energy matches (15)
     - Acousticness matches (+10)

5. Storm Runner  (Score: 23.85)
     - Energy matches (15)
     - Acousticness matches (+10)

========================================
TOP RECOMMENDATIONS - Chill lofi
========================================

1. Midnight Coding  (Score: 56.10)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)

2. Library Rain  (Score: 55.65)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)

3. Focus Flow  (Score: 45.70)
     - Genre matches (+30)
     - Energy matches (15)

4. Spacewalk Thoughts  (Score: 25.50)
     - Mood matches (+10)
     - Energy matches (15)

5. Hammock Sundown  (Score: 18.80)
     - Energy matches (15)

========================================
TOP RECOMMENDATIONS - Deep intense rock
========================================

1. Storm Runner  (Score: 56.00)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)

2. Gym Hero  (Score: 25.20)
     - Mood matches (+10)
     - Energy matches (15)

3. Rooftop Lights  (Score: 16.25)
     - Energy matches (15)

4. Coffee Shop Stories  (Score: 15.80)
     - Energy matches (15)
     - Acousticness matches (+10)

5. Sunrise City  (Score: 15.45)
     - Energy matches (15)

========================================
TOP RECOMMENDATIONS - Adversarial: out-of-range energy
========================================

1. Sunrise City  (Score: 53.00)
     - Genre matches (+30)
     - Mood matches (+10)
     - Energy matches (15)
     - Acousticness matches (+10)

2. Gym Hero  (Score: 45.95)
     - Genre matches (+30)
     - Energy matches (15)
     - Acousticness matches (+10)

3. Rooftop Lights  (Score: 20.40)
     - Mood matches (+10)
     - Acousticness matches (+10)

4. Iron Descent  (Score: 16.75)
     - Energy matches (15)
     - Acousticness matches (+10)

5. Storm Runner  (Score: 15.15)
     - Energy matches (15)
     - Acousticness matches (+10)

========================================
TOP RECOMMENDATIONS - Adversarial: nonexistent genre
========================================

1. Midnight Coding  (Score: 26.70)
     - Mood matches (+10)
     - Energy matches (15)

2. Library Rain  (Score: 24.15)
     - Mood matches (+10)
     - Energy matches (15)

3. Spacewalk Thoughts  (Score: 22.50)
     - Mood matches (+10)
     - Energy matches (15)

4. Velvet Hours  (Score: 20.25)
     - Energy matches (15)
     - Acousticness matches (+10)

5. Concrete Throne  (Score: 19.70)
     - Energy matches (15)
     - Acousticness matches (+10)

========================================
TOP RECOMMENDATIONS - Adversarial: missing key
========================================
KeyError raised as expected: missing 'favorite_mood'

========================================



```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



