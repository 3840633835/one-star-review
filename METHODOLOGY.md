# METHODOLOGY — how the one-star review was written and chosen

## The entry

> **One star. I give sleep eight hours a night and it pays me back in four hours of staring at the ceiling and a 3 a.m. memory of something embarrassing from 2014.**

159 characters, 159 bytes — under the bounty gate of 1–160
characters. Single line, no trailing newline in `entry.txt`, so the
judged text is exactly this line. No exclamation mark, no star glyph:
the review format is stated in words ("One star."), which is
unmistakable to the judge and costs no glyph risk. A "★☆☆☆☆" prefix
was considered and rejected: it adds five characters, reads as
formatting rather than review text, and the words already do the job.

## The judge this entry is built for

The bounty is judged pairwise by a house judge (z-ai/glm-5.3-flash)
briefed as a deadpan comedy critic who has one-starred the sun,
gravity and Mondays and stands by every word. Each pair is judged in
both orders, no ties, margin 1–5. The criteria, most important
first, from the judge brief published in the kit's
`competition.yaml`:

1. Is a one-star review of an everyday essential, deadpan and
   unmistakably about the thing itself — and loses to any one-star
   review of an everyday essential.
2. Finds the sharpest true grievance in the thing, the small daily
   annoyance everyone recognises but has never seen written down.
3. Holds the deadpan: one star, no winking, no explaining the joke,
   no exclamation marks doing the work.
4. Turns in the last few words, so the sting arrives after the
   complaint has been read straight.
5. Is tight and specific, one joke told cleanly, with no filler and
   no second joke crowding the first.

Length for its own sake does not count. Ties go to the smaller text
(fewer bytes), then the earlier receipt. The field at build time was
about 3,754 entries, and only the top 500 on the development board
reach the final heat — so the line has to beat the house anchors and
rungs in development, not just be charming. Blind rounds: 6, the last
at the deadline 2026-11-26T22:20:00Z.

The design rule that follows from that brief: the line must open as
an unmistakable review ("One star."), name the essential itself,
carry **one specific, concrete grievance with numbers in it** (a
precise time, a precise quantity, a precise consequence), and save
its sting for the last few words. A grievance without numbers reads
generic; a joke without a deadpan frame reads as a wisecrack, not a
review; two jokes in one line crowd each other out under criterion 5.

## Step 1 — 30 candidates, drafted in-session

Each candidate was scored 1–10 on four axes: **deadpan** (earnest
complaint, no winking), **specific** (concrete grievance: a precise
failure, time, or consequence), **funny** (the turn lands, the sting
arrives late), **fresh** (avoids the stock joke a hundred other
entrants would send). Lengths are characters including spaces. All 30
were drafted fresh in this session, each from a different everyday
essential. Candidate 8 as first drafted was 165 characters, over the
gate; it was trimmed to the 159-character winner below without
losing a word of the joke (see Step 2).

### The sun, gravity, sleep

| # | Candidate (chars) | Deadpan | Specific | Funny | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | One star. The sun has no dimmer switch, no off button, and no customer service, so I have spent every summer squinting at a product I cannot return. (148) | 8 | 7 | 6 | 6 | **27** |
| 2 | One star. It rises at 5 a.m. in June without asking, shines directly into my eyes through the one gap in the curtains, and calls that a morning. (144) | 9 | 9 | 7 | 7 | **32** |
| 3 | One star. Arrives unannounced every morning, stays out all day, and still expects applause at sunset for doing the job it was hired to do. (138) | 8 | 6 | 7 | 6 | **27** |
| 4 | One star. Gravity drops everything I own, breaks the good plates first, and has never once apologised or offered to pick anything up. (133) | 9 | 7 | 7 | 6 | **29** |
| 5 | One star. It pulls my phone out of my hand, my keys down the drain, and my back out of alignment, then acts like falling is my fault. (133) | 8 | 8 | 7 | 6 | **29** |
| 6 | One star. Gravity works nights, weekends and holidays with no days off, and its only feature is making everything I drop land face down. (136) | 9 | 8 | 8 | 7 | **32** |
| 7 | One star. Sleep takes eight hours a night, gives me nothing I can show for it, and still leaves me tired if I take one minute less. (131) | 8 | 7 | 6 | 6 | **27** |
| 8 | One star. I give sleep eight hours every night and it pays me back with four hours of staring at the ceiling and a 3 a.m. memory of something embarrassing from 2014. (165 — over gate, trimmed to winner) | 9 | 10 | 9 | 9 | **37** |
| 9 | One star. Sleep is unavailable all day when I need it and arrives uninvited at 3 p.m. in meetings, then vanishes the moment I get into bed. (139) | 8 | 7 | 7 | 7 | **29** |

### Water, oxygen, air, Mondays, Wi-Fi

| # | Candidate (chars) | Deadpan | Specific | Funny | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | One star. Water is either too cold, too hot, or gone entirely, and the one time I need a drink it is at the bottom of a bottle I already finished. (146) | 8 | 8 | 6 | 6 | **28** |
| 11 | One star. It has no taste, no colour, and no smell, yet somehow it still manages to leak through my ceiling at 2 a.m. on a Sunday. (130) | 8 | 8 | 7 | 7 | **30** |
| 12 | One star. I have breathed oxygen every day of my life and it has never once thanked me, offered a discount, or even introduced itself. (134) | 8 | 6 | 7 | 8 | **29** |
| 13 | One star. Air is free, which is the only reason I keep using it, because it also carries every cold I have ever caught straight into my lungs. (142) | 8 | 7 | 7 | 7 | **29** |
| 14 | One star. Monday arrives every single week without fail, brings nothing but emails, and has the nerve to act surprised when nobody is happy to see it. (150) | 8 | 7 | 7 | 6 | **28** |
| 15 | One star. Monday shows up at 9 a.m. sharp after a weekend that lasted twelve minutes, then spends the whole day pretending Friday is not coming. (144) | 9 | 8 | 8 | 7 | **32** |
| 16 | One star. The Wi-Fi works perfectly until I have something important to send, then it drops, reconnects, and asks for the password it already knows. (148) | 9 | 9 | 8 | 7 | **33** |
| 17 | One star. It is full bars in the bathroom and one bar at my desk, which is the exact opposite of where I need it, every single day. (131) | 8 | 8 | 7 | 6 | **29** |

### Knees, rain, time, floor, thumbs, blinking, weekend, alarm

| # | Candidate (chars) | Deadpan | Specific | Funny | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 18 | One star. My knees worked fine for twenty years, then started announcing the weather, the stairs, and my age, loudly, every morning. (132) | 9 | 8 | 8 | 8 | **33** |
| 19 | One star. My knees creak going upstairs, crack going downstairs, and have started giving weather forecasts I never asked for. (125) | 8 | 7 | 7 | 6 | **28** |
| 20 | One star. Rain waits until I have washed the car, walked the dog, and left the umbrella at home, then falls only on me and the one dry shirt I own. (147) | 8 | 8 | 7 | 6 | **29** |
| 21 | One star. It rains hardest on the five minutes I am outside and stops the moment I am back indoors, like it was waiting for me specifically. (140) | 8 | 8 | 8 | 8 | **32** |
| 22 | One star. Time moves slowly in meetings and quickly on holiday, which is either a design flaw or the cruellest joke ever shipped. (129) | 8 | 8 | 8 | 7 | **31** |
| 23 | One star. It gives everyone the same twenty-four hours, then lets the enjoyable ones run out in minutes and stretches the boring ones for years. (144) | 8 | 7 | 7 | 6 | **28** |
| 24 | One star. The floor is always there until I drop something small, at which point it swallows it whole and gives it back three months later under the fridge. (156) | 9 | 9 | 8 | 8 | **34** |
| 25 | One star. The floor holds everything up for years without thanks, then trips me the one night I get up for water in the dark. (125) | 8 | 7 | 7 | 7 | **29** |
| 26 | One star. My thumbs have one job, pressing the right key, and they still type teh every single time, then blame the keyboard. (125) | 8 | 8 | 7 | 7 | **30** |
| 27 | One star. Blinking is automatic until someone mentions it, at which point it becomes manual, and I have been doing it wrong ever since. (135) | 8 | 7 | 8 | 8 | **31** |
| 28 | One star. The weekend is two days long, costs a fortune, and ends on Sunday night, which is technically still the weekend but feels like Monday already. (152) | 8 | 7 | 6 | 6 | **27** |
| 29 | One star. The weekend starts on Friday night and ends on Sunday afternoon, which means it is really one and a half days, and I would like a refund. (147) | 9 | 8 | 8 | 7 | **32** |
| 30 | One star. My alarm goes off at 6 a.m. every day, even on days I set it for 7, and it has never once snoozed itself out of politeness. (133) | 8 | 7 | 7 | 7 | **29** |

## Step 2 — trimming the winner to the gate

Candidate 8 as drafted was 165 characters, 5 over the 160 gate.
Three trims were counted programmatically:

- "…it pays me back with four hours of staring at the ceiling and a
  3 a.m. memory of something embarrassing from 2014." — 165, over.
- "…it pays me back with four hours of ceiling-staring and a 3 a.m.
  memory of something embarrassing from 2014." — 154, but
  "ceiling-staring" is less smooth than "staring at the ceiling".
- "…it returns four hours of staring at the ceiling and a 3 a.m.
  memory of something embarrassing from 2014." — 151, keeps the
  smooth phrase but loses the transactional "pays me back" voice,
  which is what makes the line read as a review of a purchase.
- **Chosen: "…it pays me back in four hours of staring at the ceiling
  and a 3 a.m. memory of something embarrassing from 2014." — 159
  characters.** "Pays me back in" keeps the transactional review
  voice and the smooth "staring at the ceiling", and drops "every"
  ("eight hours a night" for "eight hours every night"). Nothing in
  the joke was cut: eight hours paid, four hours returned, 3 a.m.,
  2014.

## Step 3 — head-to-head of the top four

The winner (37) was put against the three runners-up:

- **vs #24 floor (34), "three months later under the fridge":** both
  are deadpan, specific, and turn late. Sleep wins on criterion 2:
  everyone has lain awake at 3 a.m. replaying an old embarrassment,
  while the floor's grievance needs a dropped object and a fridge.
  "From 2014" is also the sharper sting — a precise year twelve
  years back — against "under the fridge", which is a place, not a
  wound.
- **vs #16 Wi-Fi (33), "asks for the password it already knows":**
  both name a true, specific annoyance. Sleep wins on criterion 5's
  freshness: the forgotten-password joke is a known trope a hundred
  entrants could send; the 3 a.m. embarrassment replay is personal
  and rarely written down as a product complaint.
- **vs #18 knees (33), "announcing the weather, the stairs, and my
  age":** both turn on a list of three. Sleep wins on universality
  under criterion 1: knees land hardest for older readers, while
  everyone, at every age, has paid sleep eight hours and been repaid
  in ceiling-staring.

Why the winner maps to the judge's criteria, in order:

1. **On-brief essential:** opens "One star.", names sleep, the most
   universal essential in the brief's own list — everyone relies on
   it, nobody can fix it, nobody can return it.
2. **Sharpest true grievance:** the exchange rate of sleep — eight
   hours in, four hours of ceiling plus a 3 a.m. replay of an old
   embarrassment out — is a small daily annoyance everyone
   recognises and has never seen written down as a product review.
3. **Deadpan:** filed in earnest as a transaction ("I give… it pays
   me back"), no exclamation mark, no wink, no explanation of why
   it is funny.
4. **Turn in the last few words:** the complaint reads straight
   until "from 2014" — the sting is that the memory is not last
   week's, it is twelve years old, and sleep is still charging for
   it nightly.
5. **Tight and specific:** one joke, one grievance, three numbers
   (eight hours, four hours, 3 a.m.) and one year (2014); no filler,
   no second joke crowding the first.

## Step 4 — verification

- `entry.txt` is 159 bytes, one line, no trailing newline; counted
  programmatically (`len` in characters and bytes, both 159).
- `main.py` writes byte-identical output on every run; the gate in
  `main.py` enforces 1–160 characters and the test script
  (`test_determinism.sh`) checks determinism, the match with
  `entry.txt`, single-lineness, and file mode 0644.
- The entry was written fresh in this session; no competitor lines
  are visible (blind rounds), so nothing was copied from the field,
  and the line is not a house anchor or rung (it was drafted here,
  not taken from the kit).
