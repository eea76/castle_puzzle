# Castle Puzzle

#### About

This app is a faithful re-creation of a challenging puzzle in Final Fantasy VIII, in which users explore a series of rooms in a castle to discover twelve paintings hanging on the walls. Their titles are in Latin.
A thirteenth painting hangs in the main room with its title smudged. It is the player's task to consider the titles of each of the other twelve paintings and determine the likely title of the unnamed painting.
From a certain vantage point the player eventually glimpses a large clock on the floor with its hour hand pointing to VIII, minute hand pointing to IIII (not IV), and second hand pointing to VI. The player is to realize the nubmers I through XII are contained in each of the twelve paintings, use the order one would read a clock (H > M S), and use the corresponding titles to deduce the name of the thirteenth painting.

#### Technical details
This app was built in Django. In order for multiple people to play at once I implemented a user authentication system. A player must login and then can explore the rooms. For each painting a user views, a UserPainting object is created in the database. Only the paintings that a player views are available as possible options for the unnamed painting's title. The more paintings they discover, the more that are available as a title.
In Django terms, this means: 
`viewed_paintings = UserPainting.objects.filter(user=request.user)` 
and then in the template we iterate over the titles contained in the filtered queryset.
With this method, multiple users can be logged in at once and not have to worry about anyone else's progress interfering with their own.

Each room is an imagemap that contains the coordinates for each painting hardcoded into the html element. I found a cool javascript library that preserves the hotspots on the imagemap regardless of zoom level, so it doesn't matter how large your screen is.
The `painting_guess` view contains plenty of logic that compares a player's guess with the actual answer, records timestamps for each title clicked, and the timestamp a player submits their guess. If it's incorrect they just see an alert, but if they are correct, a css modal fades in with the correct answer. The text and image with the correct answer are passed in from the backend via a callback response instead of simply storing them in the html (any savvy web user can inspect the source and find such hardcoded strings).

I don't know what else to put in this readme but I'll probably update it as I think of other things.

