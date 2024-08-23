# Castle Puzzle
https://castlepuzzle.herokuapp.com/

#### About

This app is a faithful re-creation of a challenging puzzle in Final Fantasy VIII, in which users explore a series of rooms in a castle to discover twelve paintings hanging on the walls. Their titles are in Latin.

A thirteenth painting hangs in the main room with its title smudged. It is the player's task to consider the titles of each of the other twelve paintings and determine the likely title of the unnamed painting.

From a certain vantage point the player eventually glimpses a large clock on the floor with its hour hand pointing to VIII, minute hand pointing to IIII (not IV), and second hand pointing to VI. The player is to realize the numerals __I__ through __XII__ are contained in each of the twelve paintings' titles, use the order one would read a clock (H > M > S), and find the corresponding paintings that contain those roman numerals, then assemble the three-word title and submit it.

----

#### Technical details
This app was built in Django, which is an MVC web framework written in Python. It's robust and relatively easy to learn! In order for multiple people to play at once I implemented its user authentication system so that players must login and explore the rooms. For each painting a user views, a UserPainting object is created in the database. Only the paintings that a player views are available as possible options for the unnamed painting's title. The more paintings they discover, the more that are available as choices.

In Django terms, this means getting all existing UserPainting objects and filtering to only those associated with the currently logged-in user:
`viewed_paintings = UserPainting.objects.filter(user=request.user)`
and then in the template we iterate over the titles contained in the filtered queryset.

With this method, multiple users can play at once and not have to worry about anyone else's progress interfering with their own.

Each room is an html imagemap with the paintings' coordinates embedded inside it. I found a cool javascript library that preserves the hotspots on the imagemap regardless of zoom level, so it doesn't matter how large your screen is (https://github.com/davidjbradshaw/image-map-resizer).

The `painting_guess` view contains plenty of Python logic that compares a player's guess with the actual answer, records timestamps for each title clicked, and the timestamp of a painting title submission. If it's incorrect they just see an alert, but if they are correct, a css modal fades in with the correct answer along with the number of guesses they've made (`Attempt.objects.filter(user=request.user).count()`. The text and image are passed in from the backend via a callback response instead of simply storing them in the html (any savvy web user can inspect the source and find such hardcoded strings).

https://programminghead.com/Projects/find-coordinates-of-image-online.html

I don't know what else to put in this readme but I'll probably update it as I think of other things.

