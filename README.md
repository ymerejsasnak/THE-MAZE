# THE-MAZE
* a simple, semi-polished(?) pygame game
* a really difficult maze, with limited visibility, but with that difficulty
mitigated by items the player picks up along the way

## some plans/ideas
* likely incorporate difficulty levels with different maze sizes, different item frequencies
* for simplicity, keep maze and its display basically square, but have a side
window for displaying inventory/messages/etc
* saveable game (save maze, position, inventory)
* move counter for end-game scoring (with high score list)
* timer also?
* add sounds/music!!! (make simple stuff - walk sound, item get sound, wall bump sound, creepy drone music loop(s))
* randomly add flavor/atmosphere text every so often
(ie 'its cold in here', 'i don't like the way my footsteps echo', etc)
* SEE ALL MESSY 'MAZESTUFF' FILES FOR SOME OF ABOVE ALREADY WORKED OUT SEPERATELY
* KEEP IT CLEAN, MODULARIZED, ETC

## possible items
* breadcrumb pouch: get a random number of breadcrumbs - these can be placed as
markers on the maze floor (And also picked back up)
* lantern fuel: increases your sight range (not meant to be realistic in any way)
* compass: shows rough direction (n,s,e,w,ne,se,nw,sw) to the finish (or maybe make it graphical
using atan or whatever to draw the line)
* robot: use A* to move along correct path and draws arrows on floor, but only for a limited # of moves (x battery power)
* map - visited cells remain (dimly) visible

## TO DO:
* clean up everything done so far, esp maze class, and add comments, etc.
* change maze display to drawing on a seperate surface for maze vs sidebar
* work on inventory/message sidebar
* implement items/inventory
* add music (stream longer baseline atmosphere with other looped 'sounds' over it) 
* and sfx (footsteps, item get, item use, etc)
* implement win condition, timer, scoring
* add instructions (opens new window?)


