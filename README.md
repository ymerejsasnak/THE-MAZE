# THE-MAZE
* a simple, semi-polished(?) pygame game
* a really difficult maze, with limited visibility, but with that difficulty
mitigated by items the player picks up along the way

## some plans/ideas
* likely incorporate difficulty levels with different maze sizes, different item frequencies
* for simplicity, keep maze and its display basically square, but have a side
window for displaying inventory/etc
* saveable game (save maze, position, inventory)
* add sounds/music!!! (make simple stuff - walk sound, item get sound, wall bump sound, creepy drone music loop(s))
* randomly add flavor/atmosphere text every so often
(ie 'its cold in here', 'i don't like the way my footsteps echo', etc)
(maybe just in title bar so user might not even notice for a while)
* SEE ALL MESSY 'MAZESTUFF' FILES FOR SOME OF ABOVE ALREADY WORKED OUT SEPERATELY
* KEEP IT CLEAN, MODULARIZED, ETC

## possible items
* paint can: each has 10 splashes of paint in it to paint a cell floor with (as a marker)
* lantern fuel: increases your sight range (not meant to be realistic in any way)
* robot: use A* to move along correct path and draws arrows on floor, but only for a limited # of moves (x battery power)
(start with dead robot, collect batteries, can only use it once or pick it back up when it's done?)

## TO DO:
* clean up everything done so far
* implement timing/fps so maze runner doesn't go too fast to control
* implement picking up items (and sight increase cuz that's so easy)
* implement using paint
* implement using robot (copy A* stuff from other file, etc)

* add music (stream longer baseline atmosphere with other looped 'sounds' over it) 
* and sfx (footsteps, item get, item use, etc)
* implement win condition stuff 
* (scrap or implement timer/step counter/scoring???)
* add instructions (opens new window?)


