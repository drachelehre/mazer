# Mazer

### BootDev Hackathon 2025 submission

---


I have made a maze game that looks simple on its surface, but there is a twist! The game doesn't think it's quite enough to beat the player, so it's going to do anything it can to block your path at any turn! Even if it has to throw walls at you to keep you from the goal!

Not hard enough? Good (or bad) news! The goal will run from you! Just don't think the goal is operating with the same rules as you are...

---

![Chasing that dang goal!](/mazer_pic.png)

---

## How to Install

Clone

```
git clone https://github.com/drachelehre/mazer
cd mazer
python3 -m venv .venv

pip install -r requirements.txt
#you only need to install once

#to play make sure you activate the virtual environment
source .venv/bin/activate
# if windows .venv\Scripts\activate.bat
python main.py
```

## How to Play

Arrows or WASD to move. Keep in mind, the sprite uses tank controls.

As you play, a small wall is placed front of the player every second and-a-half.

You have 30 seconds to chase down the fleeing flag!

It will ask if you want to play again in the terminal. Be warned that if you want, it will start immediately.

---

## Under the Hood

Randomly generated layout

New obstacles appear regularly.

If you get close to the flag, it starts moving away

Written entirely in Python using PyGame module

---

Built for the BootDev Hackathon 2025.

Judges, developers... Anyone, really! Feel free to:

- Install and play the game

- Fork it and put your own spin on it

- Spread the word!

#bootdev #hackathon #drachelehre
