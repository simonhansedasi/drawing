Visualizing the unseen: a toddler's literature review.

I've been keeping statistics on library trips with Heiki. Each book gets counted for how many times it's read, how many times he asks to have it read again, and whether he ever abandoned it before finishing.

The eyeball attempts to illustrate a taste overlap: the radius of the circle represents read counts and the color represents my rating. Small yellows in the circle and large, dark rings are encouraging, however, the math only explains 15% of the overlap.

The second plot breaks down the statistics by genre. An obvious mismatch between our styles jumps out: he prefers animal/nature fiction and I have a penchant for rhyming and verse.

Anyone else's rating power under 20%? Tell me I'm not alone.

%%%%%
NOTES
%%%%%

Data: `dada_science/library_recommender/library.db`, a real family library-tracking app I run on a Raspberry Pi — the `user_ratings` table for user=heiki, the 72 books with at least one recorded read as of 2026-08-17. Read count, reread demands, and false starts are running counters updated in the app over time, not timestamped events, so this is a snapshot, not a reading-history timeline. Rating-vs-read-count correlation: Pearson r=0.385 (r²≈0.148, rounded to 15%) across the 70 rated books. Genre buckets in the second plot are a manual collapse of the catalog's raw genre tags into 5 groups — General fiction, Nonfiction, Rhyme/verse, Animal/nature fiction, Folklore — after finding most of the raw tags were duplicate cataloging labels, not real genre distinctions.

### AI usage:
Built with Claude Code. Ideation, direction, validation, and the actual judgment calls were mine, Simon-Hans Edasi. Claude implemented code for statistical tests and image generation.