# Basic structure

"Games" will be managed by 3 Voice rooms, "Common", "Room One", "Room Two". Players will input commands through the chat inside their voice room. Additionally, a UI will be provided to assist mobile users and those who prefer to use a mouse (Buttons are a thing I can do, right?). 

## Channel layout
3 Channels:
- Common Room
  - Visible to all server members, and is used to determine who's in the game when a match starts
- Room 1
  - Visible to: 
    - Debugger
    - Room 1
- Room 2
  - Visible to:
    - Debugger
    - Room 2

## Roles
- Room 1
- Room 2
- Debugger
- Player 1-30
- Player

By splitting each player into their own role, it allows for greater granularity of command permissions

## Game flow
Rounds will be divided into 3 sections:
- Pre-round (10s)
  - Gives the bot time to move and edit member permissions
  - No commands permitted 
- Round (Varies)
  - Allows players to send /commands and talk to each other. Text chat should work too
  
- Post-round 
  - Allows team leaders to send their hostages using the appropriate command. Since we're automating, the parley step is skipped because the player is sent automatically during pre-round.
  - Scrub player messages sent during the round
  - Only leaders are permitted to send commands, and only the send command

## Commands
- /send `player`
  - Sends a players during the post-round. `player` is only valid if it is one of the players in the leader's room, and if it is not the leader themselves. Send is not necessarily immediate, only occuring once the other leader has also chosen their hostage
- /appoint `player`
  - Appoints a player to leader. `player` is only valid if it is one of the players in the commander's room, not the commander themself, and there is not already a leader
- /reveal `player`
  - Reveal your full card to another player. `player` is only valid if they're in the same room as the commander
- /share `player`
  - Reveal your full card to another player, but only if they also show you their own card. `player` is only valid if they're in the same room as the commander
- /start
  - Only allowed for debuggers and admins. Starts the game with the number of players currently in the common room 
 