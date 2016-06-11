# THE-MAZE
* a simple, semi-polished(?) pygame game
* a really difficult maze, with limited visibility, but with that difficulty
mitigated by items the player picks up along the way

## some plans/ideas
* generate a maze of x * x size with a depth first search algorithm
* display only maze visible in player's current range of sight
* maze scrolls: player always in center of display
* maze wraps visually: not really a toroidal maze, but make it look that way (but only draw wrapped map, no items, etc?)
for when player is at the edge (just to make it more visually confusing
instead of being able to orient self based on obvious wall)
* use pygame color object for easy nice-looking shadow fade along visibility radius
* likely incorporate difficulty levels with different maze sizes, different item frequencies
* player starts in center, finish is placed in one of four corners randomly
* for simplicity, keep maze and its display basically square, but have a side
window for displaying inventory/messages/etc
* saveable game (save maze, position, inventory)
* move counter for end-game scoring (with high score list)
* timer also?
* add sounds/music!!! (make simple atmospheric stuff)
* SEE ALL MESSY 'MAZESTUFF' FILES FOR SOME OF ABOVE ALREADY WORKED OUT SEPERATELY
* KEEP IT CLEAN, MODULARIZED, ETC

## items
* breadcrumb pouch: get a random number of breadcrumbs - these can be placed as
markers on the maze floor
* lantern fuel: increases your sight range (not meant to be realistic in any way)
* chalk: use to draw symbols on the maze floor (preset or any letter or what?)
* maybe: placeable torch (small and large) - keeps an area visible even when you aren't there
* compass: shows rough direction (n,s,e,w,ne,se,nw,sw) to the finish
* robot idea1: random movement robots (with varying - small/large - sight range?)
* robot idea2: use A* to move along correct path, but only for a limited # of moves (dies)
* other robot ideas: wall hugger robot, robot that draws on the floor
* map - visited cells remain (dimly) visible

## TO DO:
* clean up everything done so far, esp maze class, and add comments, etc.


