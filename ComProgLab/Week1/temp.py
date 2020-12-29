def miles_to_kilometer(m):
    return m * KILOMETERS_PER_MILE

KILOMETERS_PER_MILE = 1.609

distance = float(input("Enter the distance in miles: "))
print(f"The distance is {miles_to_kilometer(distance):.2f} kilometers.")



def miles_to_kilometers(x):
    return x * KILOMETERS_PER_MILE

KILOMETERS_PER_MILE = 1.609

distance = float(input("Enter the distance in miles: "))
print(f"The distance is {miles_to_kilometers(distance):.2f} kilometers.")
# Cartoons

popeye = r"""
          ____
          \__/         # ##
         `(  `^=_ p _###_
          c   /  )  |   /
   _____- //^---~  _c  3
 /  ----^\ /^_\   / --,-
(   |  |  O_| \\_/  ,/
|   |  | / \|  `-- /
(((G   |-----|
      //-----\\
     //       \\
   /   |     |  ^|
   |   |     |   |
   |____|    |____|
  /______)   (_____\
"""

casper = r"""
    .-----.
   .' -   - '.
  /  .-. .-.  \
  |  | | | |  |
   \ \o/ \o/ /
  _/    ^    \_
 | \  '---'  / |
 / /`--. .--`\ \
/ /'---` `---'\ \
'.__.       .__.'
    `|     |`
     |     \
     \      '--.
      '.        `\
        `'---.   |
   jgs     ,__) /
            `..'
"""

simpsons = r"""
    |\/\  ,.
    /   `' |,-,
   /         /_
 _/            /
(.-,--.       /
/o/  o \     /
\_\    /   _/
(__`--'    _)
 /         |
(_____,'    \  hjw
   \_       _\
     `._..-'
"""

smurfs = r"""
       .-""'"--.
      /         )
     /      --"`
    /       _`:---.
   |     .-'       `\
    \   /    .----'./
     \  : ,-' ~(.).)\
      \_| \      ._) |
       /   |  \.__, /
  _.--'    )`///-,-'
 /        / _| (_\\
|        (____/____)
 \     ___/       | _
  `---(            ` )
       `-,          .'
        (__.'._/'._/
             |`| |
          __/ / /
         //   | `--.
        ||    /_____)
  jgs   `=---`
"""

mickey_mouse = r"""
            .-"'"-.
           /       \
           \       /
    .-"'"-.-`.-.-.<  _
   /      _,-\ ()()_/:)
   \     / ,  `     `|
    '-..-| \-.,___,  /
          \ `-.__/  /
     jgs / `-.__.-\`
        / /|    ___\
       ( ( |.-"`   `'\
        \ \/    {}{}  |
         \|           /
          \        , /
          ( __`;-;'__`)
          `//'`   `||`
         _//       ||
 .-"-._,(__)     .(__).-""-.
/          \    /           \
\          /    \           /
 `'-------`      `--------'`
"""

# Sports & Outdoors

baseball = r"""
                                  dMb
 +  +    +                         MMM         _--_     
                +                   MMM       ( A's)   
+  (}{)                              MMM      /___7
     \\\   +                          "MM   .~~\ /~~.
  +    \\                               MM/""_  V    \             
        "\                               om /____/   / 
                                         '{:)      _/
                                            `"---" |          
                                           |        \
                                           \    /\   |
                                           /   /  \   \
                                         /"   /    \   \
                                         \__/"      \__/
                                         / /        | |
                                        .^V^.      .^V^.
                                         +-+        +-+

                                           '94 the wolfe
"""

golf = r"""
     '\                   .  .                        |>18>>
       \              .         ' .                   |
      O>>         .                 'o                |
       \       .                                      |
       /\    .                                        |
      / /  .'                                         |
jgs^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

basketball = r"""
           ____|
        o  \%/ |~~\
  o//              |
  8                |
 / >               |
~ ~             ~~~~~~
"""

ice_hockey = r"""
   ,
    -   \O                                     ,  .-.___
  -     /\                                   O/  /xx\XXX\
 -   __/\ `\                                 /\  |xx|XXX|
    `    \, \_ =                          _/` << |xx|XXX|
jgs"""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""

billiards = r"""
                                                        .-"'"-.
                                                       /   _   \
 ___                                                   |  (8)  |
/\`````````""""""=--......................___________  \   ^   /
\//__________________)))__________________)))________]] '-...-'
"""

# Logos

biohazards = r"""
            _   _
          .-_; ;_-.
         / /     \ \
        | |       | |
         \ \.---./ /
     .-"~   .---.   ~"-.
   ,`.-~/ .'`---`'. \~-.`,
   '`   | | \(_)/ | |   `'
   ,    \  \ | | /  /    ,
   ;`'.,_\  `-'-'  /_,.'`;
jgs '-._  _.-'^'-._  _.-'
        ``         ``
"""

caduceus = r"""
           .-.
     ___  (   )  ___
,_.-'   `'-| |-'`   '-._,
 '.      .-| |-.      .'
   `~~~~`  |.') `~~~~` 
          (_.|
           |._)
           |.')
          (_.|
           |._)
          ('.|
           |._)
    jgs    '-'
"""

peace = r"""
        ..--+++--..
     .-'     |     `-.
   +'        |        `+
  '          |          `
 '           |           `
:            |            :
:          +'|`+          :
.        +'  |  `+        ;
 +     +'    |    `+     +
  `. +'      |      `+ .'
    `._      |      _.'
       `--.._|_..--' mh
"""

playboy = r"""
        |\ |\
        \ \| |
         \ | |
       .--''/
      /o     \
      \      /
jgs   {>o<}='
"""

recycle = r"""
    _____\    _______
   /      \  |      /\
  /_______/  |_____/  \
 |   \   /        /   /
  \   \         \/   /
   \  /          \__/_
    \/ ____    /\
      /  \    /  \
     /\   \  /   /
jgs    \   \/   /
        \___\__/
"""

# Define a list to be choosen
cartoons_list = [popeye, casper, simpsons, smurfs, mickey_mouse]
sports_list = [baseball, golf, basketball, ice_hockey, billiards]
logos_list = [biohazards, caduceus, peace, playboy, recycle]

# Define a name that print out
cartoons_name = ["popeye", "casper", "simpsons", "smurfs", "mickey_mouse"]
sports_name = ["baseball", "golf", "basketball", "ice_hockey", "billiards"]
logos_name = ["biohazards", "caduceus", "peace", "playboy", "recycle"]

print("Enter a number to select a category (0 - Cartoons, 1 - Sports & outdoors, 2-Logos):")
category = int(input("> "))
print("Enter a number from 0 to 5 to see an ascii Logos:")
ascii_logo = int(input("> "))
if category = 1
print(cartoons_list[ascii_logo])