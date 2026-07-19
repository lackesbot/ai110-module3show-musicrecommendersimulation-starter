# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

musicRecommender02

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate. 
It generates music recommndation based on your  preferences such as the genre, mood, acousticness, valence etc. 
- What assumptions does it make about the user. 
It assumes that what the user has put is what you want the output of. 
- Is this for real users or classroom exploration. 
For classroom, because I feel like right now at this stage there is so much we can add to make it better 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  : 
energy, mood, genre, acouisticness, tempo, valence, danceability 
- What user preferences are considered : 
energy, mood, genre, acouisticness
- How does the model turn those into a score: 
it compares the song and see if it matches the user preferences then does calculation to add it with points. 
- What changes did you make from the starter logic: 
genre match is weighted heavily that the rest and instead of having the same weight each preference has a different weight
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog 
19
- What genres or moods are represented  
pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, classical, metal, folk, r&b, electronic, country, and reggae.
- Did you add or remove data
I added about 5 additional songs  
- Are there parts of musical taste missing in the dataset  
It is missing many common parts of taste like more subgenres, different eras, multilingual music, live/acoustic versions, instrumental-heavy tracks rtc.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results
it works ecxtremely well with the pop genre

- Cases where the recommendations matched your intuition  
when matching the mood of the song to the user preferences, I found that majority of it was really to the point.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Genre distribution is skewed, but GENRE_WEIGHT (30) doesn't account for it. A user who loves classical or country can never get more than one +30 genre bonus in their entire top-5 — the other 4 slots are filled by songs that don't match their genre at all, ranked only on energy/mood/acoustic. A lofi or pop fan gets multiple genre-boosted songs to choose from. Net effect: niche-genre users' "recommendations" are mostly filler from whatever's energy-adjacent, while pop/lofi fans get a richer genuinely-matching list. The system structurally favors the two most-represented genres.

likes_acoustic is boolean, but acousticness in the data is continuous (0.03–0.95). Anyone whose actual taste is "somewhat acoustic" (like the r&b track at 0.40 or country at 0.60) has no way to express it — they're mapped to whichever extreme is closer, distorting scores for every song in between.


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested:
I tested mood and energy
- What you looked for in the recommendations.
I looked ton see if the recommndations wouldnchange hevily if had removed one or the other.
- What surprised you.
What suprised me was that the only thing that changed drasticlly was the points and maybe one song but the rest of the songs matched with the one that wasn't altered.
- Any simple tests or comparisons you ran.
I ran The before/after comparison for the pop/0.8 energy/non-acoustic



---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences: 
For the future, I want to have a variety of user preferences so that the recommendations are not widely skewed. Also I want to have widely range of songs with differentt genres so that we can get a more accurate recommendation.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

I truly enjoyed working on this project. It forced me to think about ways I can make the system better which I feel has really pushed my python skills further. Soemthing that I have learned about recommendation systems is that for you to hve an accurate measure lots of data is needed that cover a whole range of inputs. Something unexpected that I discovered was how much python skills goes intop data analysis and really was an eye opener to keep improving my python skills. 