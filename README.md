# Advent of Code 2024

[Advent of Code](https://adventofcode.com) is an annual programming challenge that runs throughout December, offering daily puzzles that test problem-solving and algorithmic thinking. This was my first time participating, and it was a great opportunity to explore different problem-solving strategies and sharpen my coding skills.

In this repo, I document the problems I solved (or at least tried to) in the [2024 edition](https://adventofcode.com/2024), along with a [log of my progress](#daily-progress) and some [thoughts on the experience](#final-thoughts). I chose **Python** for this challenge, though it isn’t my *lingua franca*, so I’d appreciate any feedback on parts of my solutions that aren’t very *pythonic*.

Although most of my scripts don't have external dependencies, I used [Poetry](https://python-poetry.org) for dependency management. Run the solutions with a command like `poetry run python main.py input.txt`, but be aware that some scripts may require additional arguments.

## Daily Progress

This log captures the status of the problems I tackled, how I felt while solving them, and a brief comment on each solution.

| Day      | P1             | P2             | Feeling            | Remarks |
|:--------:|:--------------:|:--------------:|:------------------:|:--------|
| [1](01)  | :green_circle: | :green_circle: | :ok_hand:          | Iterated through all elements to calculate distances and similarities. A perfect warm-up exercise. |
| [2](02)  | :green_circle: | :green_circle: | :shrug:            | Part 1 was straightforward. For part 2, trying to be clever didn’t work, but brute forcing the solution did. |
| [3](03)  | :green_circle: | :green_circle: | :relaxed:          | Regex saved the day. |
| [4](04)  | :green_circle: | :green_circle: | :upside_down_face: | Part 1's approach seemed easy but was deceptively tricky. Refactoring in part 2 made it straightforward. |
| [5](05)  | :green_circle: | :green_circle: | :smile:            | The key was building a rules dictionary. Easy peasy. |
| [6](06)  | :green_circle: | :red_circle:   | :dizzy_face:	  | Part 1 was easy; brute force in part 2 doesn’t work because it hangs in some cases. |
| [7](07)  | :green_circle: | :green_circle: | :thumbsup:         | Recursion was the hero. A small optimization for part 2 nearly halved the execution time. |
| [8](08)  | :green_circle: | :green_circle: | :hand_over_mouth:  | The solution came out very C-like, but it was great to get back on track. |
| [9](09)  | :green_circle: | :green_circle: | :wink:             | Tried to be clever with the programming, but a simpler approach worked better. Focus on the data issues first, then the programming. |
| [10](10) | :green_circle: | :green_circle: | :bowtie:           | Solved quickly using recursion and a dictionary with tuples as keys. Elegant and efficient. |
| [11](11) | :green_circle: | :red_circle:   | :exploding_head:   | Part 1 was easy but a trap. For part 2, optimizing speed exhausted memory, while optimizing memory drastically slowed runtime. |
| [12](12) | :green_circle: | :red_circle:   | :weary:            | Thought both parts would be fine, but part 2 didn't work. Sample results are correct, but the problem input gives the wrong result, and I can’t find the bug. |
| [13](13) | :green_circle: | :green_circle: | :nerd_face:        | For part 1, brute force did the trick. For part 2, good ol' math saved the day. Lucky 13, it feels great to be back on track after two unfinished days. |
| [14](14) | :green_circle: | :green_circle: | :blush:            | Part 2 was intriguing and exciting: searching for the tree tip over 10k seconds narrowed the possible answers to 48, which I manually analyzed to find the tree. |
| [15](15) | :green_circle: | :green_circle: | :grin:             | Part 1 was a good warm-up for part 2, which, although tricky, I solved with the same algorithm and a bit of recursion. |

## Final Thoughts

Participating in Advent of Code 2024 was more than just solving puzzles. It became a personal challenge that tested both my technical skills and adaptability.

Initially, I aimed to keep up with the daily problems, but December was packed with events: I gave two tech talks (PosaDev and DevFest) and attended several social gatherings, making it difficult to stay on track. Instead of giving up, I chose to move at my own pace, extending the challenge first until the end of the year, then until Epiphany, and finally wrapping up on January 12. This experience taught me the importance of being flexible, but also the value of setting hard limits to close projects. I also set myself a realistic goal to attempt at least 60% of the problems (15) and solve 90% of those (27 out of 30, considering both parts).

One key lesson I learned was to avoid premature optimization; over-optimizing a part 1 solution often made part 2 harder to adapt. I also realized that sometimes using one approach for part 1 and a completely different one for part 2 could be more effective. Embracing that flexibility was crucial.

Focusing on data handling before jumping into coding often led to better solutions. Sometimes, straightforward methods like brute force or recursion worked better than premature optimizations. Struggling with certain problems taught me patience and strategic thinking.

This challenge also deepened my understanding of Python and sharpened my grasp of algorithms, especially in recursion and data structures, but also in managing time and space complexity. Beyond technical growth, I found value in discussing problems (classic *rubber duck debugging*), stepping away and returning with fresh eyes, or simply letting a problem go.

My favorite problem was day 14, part 2, which was the most ambiguous but led me to a clever solution. In contrast, day 12, part 2 was the most frustrating. My solution passed the sample cases but consistently failed with the actual input due to a bug I couldn’t find.

Finally, this experience helped strengthen my bonds with fellow programmers, giving us a shared space to learn, discuss, and grow together.

Advent of Code 2024 wasn’t just about coding. It was about learning to adapt, persist, and connect. I’m excited for the 2025 edition!
