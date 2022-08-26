# Declare characters used by this game.
define n = Character('Mysterious Old wiseman', color="#7f0000")
define h = Character('Harry', color="#FF8C00")
define fag = Character('Ron', color="#FF0800")
define bitch = Character('Hermione', color="#FFF600")
define d = Character('Dumbledore', color="#FF072C")
define ni = Character('Neville', color="#550000")
define p = Character('A 1st Year Girl who is a midget', color="#FF6DD0")
define humas = Character('Harry & Ron', color="#FF42C0")
define homosexualme = Character('Virtual Game Instruction Program', color="#000000")
define hint = Character('The Hint Goblin!', color="#6AFF00")
define pink = Character('The Fat Lady', color="#FFBCFD")
define green = Character('Malfoy', color="#1FA700")
define hrh = Character('Harry Ron and Hermione', color="#FF6063")
define hrh = Character('Nearly Headless Nick', color="#C4F6FF")
define percy = Character('Percy', color="#FF3200")
define fuck = Character('Frog of Doom', color="#2D2800")
define gry = Character('Everybody in the fucking common room', color="#00CDFF")
image source0 = "source0.png"
image percy = "gitlord.png"
image source1 = "source1.png"
image source2 = "source2.png"
image source3 = "source3.png"
image hintl = "hand.png"
image fuck = "frogofdoom.png"
image signpost = "dormpost.png"
image muck = "dream0.png"
image begin bg = "beggining_bg.png"
image wiseguy = "theoldmanglitch.png"
image end = "theendqm.png"
image entry = "entry.png"
image d = "dumbledore.png"
image neville = "neville.png"
image hobnob = "Hintgoblin.png"
image ron = "ron.png"
image hermione = "hermione.png"
image ro2 = "ro2.png"
image harry = "harry.png"
image nude = "nakedharry.png"
image ro1 = "ro1.png"
image hermi1 = "hermi1.png"
image hari1 = "hari1.png"
image carpet = "carpet.png"
image boys = "pals.png"
image girls = "gals.png"
image black = "hell.png"
image pink = "pink.png"
image dii = "pinkiepie.png"
image nick = "nick.png"
image slide = "sals.png"
image scarry = "scarry.png"
image black = "hell.png"
image duk = "thegodself.png"
label start:
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Mysterious Man.mp3"
    scene begin bg
    show wiseguy:
        xalign 0.0
        yalign 1.9
        linear .5 xalign 1.0 yalign 1.7
        xalign 1
        linear .5 xalign 0.0 yalign 1.3
        linear .1 xalign 0.0 yalign 1.9
        repeat
    n "Hello little boys & girls! I'm here to tell you the story of Harry Potter (& the frog of doom striking back)!"
    n "Harry was a wary boy for not dying after a huge attack by the main bad guy, Voldemort! Who we don't give a shit about in THIS Harry potter game."
    n "He was raised all fucked up but that basically changed since he turned 11 because of stuff that happened with hogwarts and all."
    n "Either way, he was a truly glorious boy, who ate pumkin pasties & chocolate frogs not only because they tasted good, but because they replenished his health!"
    n "And you get to play as his flesh & mind! WOW!"
    n "Harry was going back to hogwarts (school of whitchcraft & wizardry) this year, with some of his best friends (keyword, SOME, because Neville is a loser)!"
    n "Amazing, he learns about magic AND gets friends that aren't dickholes {b}AND{/b} fucking awesome food in the process? It's like burning two phoenixes with one... old age!
       Even know after they die they come back to life but fuck that."
    n "Now, let me take you down, into the depths of my dubious story!"
    scene entry
    with irisout
    show d:
        xalign 0.08
        yalign 1.0
        linear 2 yalign 1.2
        linear 2 yalign 1.0
        repeat
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Hoping a Year of no Fear.mp3"
    d "Welcome back to hogwarts!"
    p "But this is my first time!"
    d "That's what she said! (or milkshakemanCP)"
    d "Now, the sorting ceremony shall start for you first years!"
    show ron:
        xalign 0.5
        yalign 1.7
        linear 1.3 xalign .7
        linear 1.3 xalign .5
        repeat
    fag "Hey Harry, nice to see you again"
    h "Same; hey Hermione!"
    hide ron
    show hermione:
        xalign 0.5
        yalign 2.5
        linear .9 yalign 2.8
        linear .9 yalign 2.5
        repeat
    bitch "Hey you two!"
    humas "Hey you blue!"
    hide hermione
    show neville:
        xalign 0.4
        yalign 1.8
        linear .5 yalign 2.0 xalign 0.65
        linear .5 yalign 1.8 xalign 0.4
        repeat
    ni "Speaking of those nitty-witty... shitty blues, I have them right now!"
    show hermi1:
        xalign 1.1
        yalign 1.2
    bitch "Not to worry, I read about a spell over the summer that can send the blues over to next christmas!"
    show hari1:
        xalign 5
        yalign 1.2
    h "Haha!"
    bitch "Shut the fuck up."
    hide hari1
    h "Waaaaaah..."
    show ro1:
        xalign 5
        yalign .7
    fag "Harry, are you falling down a cliff?"
    show hari1:
        xalign 5
        yalign 1.2
    h "No, it's just that I say 'WAAAH' when I fall down cliffs as well!"
    bitch "Oh, bother; well, anwyays, let me cast the spell for ridding those blues!"
    hide neville
    show neville:
        xalign 0.4
        yalign 1.8
        linear .2 yalign 2.0 xalign 0.65
        linear .2 yalign 1.8 xalign 0.4
        repeat
    ni "Yeah, quick! Before they eat me into itty bities!"
    hide hari1
    hide ro1
    hide hermi1
    show harry:
        xalign 0.5
        yalign 2.3
    show hermione:
        xalign .99
        yalign 9.3
    show ron:
        xalign 0.15
        yalign 3.8
    menu:
        homosexualme "Choose which character to cast a spell, unless you want to go to hell!"
        "Harry!":
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
            h "But I don't know {i}how{/i} to cast a spell like that!"
            ni "Aaw man, I'll be dealing with this until next THANKSGIVING!"
        "Ron":
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
            fag "But I don't know the first {i}thing{/I} on how to cast a spell like that!!"
            ni "Oh no! I'll be dealing with this for AGES!"
            bitch "You should've let ME do it!"
        "Hermione":
            bitch "Here, solar plex- I mean Neville, let me cast a spell I read about over the summer in my new 2nd favourite study manual: The Berenstain Bears - Too Much Magic!"
            hide neville
            show neville:
                    xalign 0.4
                    yalign 1.8
                    linear .05 yalign 2.0
                    linear .05 yalign 1.0
                    repeat
            ni "QUICKLIIIIII!"
            bitch "Prappity Protus!"
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/You win the Duel!.mp3"
            hide neville
            show neville:
                xalign 0.4
                yalign 1.8
            ni "Whoah! You really fixed me up! Thank you Hermione!"
            bitch "No problem, Neville!"
            h "But mind if you place your ass {b}elsewhere{/b}, Neville?"
            ni "Sort of..."
        "Hint!":
            scene hintl
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/The Hint Goblin!.mp3"
            show hobnob:
                xalign 0.4
                yalign 9.3
                linear .8 xalign 0.8
                linear .8 xalign 0.4
                repeat
            hint "If you don't choose Hermione, then she'll want to slap your heiny!"
            scene entry
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Hoping a Year of no Fear.mp3"
            show d:
                xalign 0.08
                yalign 1.0
                linear 2 yalign 1.2
                linear 2 yalign 1.0
                repeat
            show neville:
                xalign 0.4
                yalign 1.8
                linear .2 yalign 2.0 xalign 0.65
                linear .2 yalign 1.8 xalign 0.4
                repeat
            menu:
                homosexualme "Choose which character to cast a spell, unless you want to go to hell!"
                "Harry":
                    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
                    h "But I don't know {i}how{/i} to cast a spell like that!"
                    ni "Aaaaw, I'll be dealing with this until next THANKSGIVING!"
                "Ron":
                    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
                    fag "But I don't know the first {i}thing{/I} on how to cast a spell like that!!"
                    ni "Oh no! I'll be dealing with this for AGES!"
                    bitch "You should've let ME do it! I mean, seriously you even got the hint goblin to tell you the answer!"
                    ni "Yeah yeah yeah, Her-me-one!"
                    bitch "I told you not to call me that, RONALD!"
                "Hermione":
                    bitch "Here, solar plex- I mean Neville, let me cast a spell I read about over the summer in my new 2nd favourite study manual: 
                    The Berenstain Bears - Too Much Magic!"
                    hide neville
                    show neville:
                        xalign 0.4
                        yalign 1.8
                        linear .05 yalign 2.0
                        linear .05 yalign 1.0
                        repeat
                    ni "QUICKLIIIIII!"
                    bitch "Prappity Protus!"
                    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/You win the Duel!.mp3"
                    hide neville
                    show neville:
                        xalign 0.4
                        yalign 1.8
                    ni "Whoah! You really fixed me up! Thank you Hermione!"
                    bitch "No problem, Neville!"
                    h "But mind if you place your ass {b}elsewhere{/b}, Neville?"
                    ni "Sort of..."
    hide harry
    hide ron
    hide hermione
    hide neville
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/End of a Long day! (Wet your feet in magic showers!).mp3"
    show harry:
        xalign 0.5
        yalign 1.7
    h "Well, what a day 'twas today! But I'm gettign so sleepy, that my dick is going weepy!"
    hide harry
    show ron:
        xalign 0.5
        yalign 1.7
    fag "Same, let's have dinner at the Great Hall!"
    hide ron
    show hermione:
        xalign 0.5
        yalign 3.2
    bitch "Great!"
    hide hermione
    d "I'm just here to look pretty."
    stop music fadeout 1.0
    hide d
    hide entry
    show black
    n "But then, as they were getting ready for a bit of beddie..."
    n "A fat ass-motherfuker blocked their way!"
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Mountania.mp3"
    scene dii
    show pink:
        xalign 0.5
        yalign -0.1
        linear .5 yalign -0.5
        linear .3 yalign -0.1
        repeat
    h "The good ol' fat lady!"
    pink "It's good to see your again, Harry!"
    fag "So Mrs. lady, what's the password this year?"
    play sound "Obtain!.mp3"
    pink "It's {b}Mountania{/b}!"
    green "I heard that!"
    pink "Well I can tell wheteher you're a slytherin or not, Malfoy!"
    h "OWNNNNNNNED!"
    fag "Snot WAAAeTH it, Harry!"
    h "Wait a second! Why did you tell us the password anyways?"
    pink "Because I'm a nice woman!"
    show percy:
        xalign 0.0
        yalign 0.0
    percy "How {b}dare{/B} you!"
    hide percy
    h "Shut the fuck up."
    scene carpet
    show boys:
        xalign 0.0
        yalign 0.0
    show girls:
        xalign 1.0
        yalign 0.0
    "Harry then entered the Gryffindor common room..."
    show harry:
        xalign 0.5
        yalign 1.5
    h "aah, back in beddie!"
    hide harry
    show harry:
        xalign 0.5
        yalign 2.0
    show hermione:
        xalign 0.86
        yalign 4.5
    bitch "Not quite yet, Harry! There are two spiral staircases of wonder in front of you!"
    h "Oh wow!"
    show ro1:
        xalign 0.0
        yalign 1.5
    fag "Yeah, the left one is the boy's dormitory, and the right is the girls! Enter the boy's to go to bed; and {i}don't{/I} enter the gal's!"
    hide ro1
    menu:
        bitch "Yeah!"
        "Boys":
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/You win the Duel!.mp3"
            h "I better just go to my normal dormitory, duh!"
            bitch "Duh"
            show ro1:
                xalign 0.0
                yalign 1.5
            fag "Fuck you."
            bitch "Oh, you & your black-washed mouth!"
            h "Well, you kinda deserved that, Hermione..."
            h "You rude piece of shit!"
            fag "Shut up."
        "Girls":
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
            bitch "How {b}dare you{/B}, you perverted motherfucker!"
            h "Hey, respect my choices; nothing is wrong!"
            bitch "Okay, if you really want to then, walk up the stairs."
            h "k"
            play sound "london bridge.mp3"
            hide girls
            show slide:
                xalign 1.0
                yalign 0.0
            hide harry
            show scarry:
                xalign 0.5
                yalign -4.0
                linear 3.0 yalign 10.0
            $ renpy.pause(1.7)
            show harry:
                xalign 0.5
                yalign 1.5
            h "*CRASH* Ouch!"
            bitch "If you walk up the stairs of the girls' dorm, it'll turn into a slide!"
            show ro1:
                xalign 0.0
                yalign 1.5
            fag "But you've been in our dormitory before."
            bitch "Well that's probably just because Dumbledore is a male faggot... A-a-a-anways, seriously, get up to your real dormitory!"
            bitch "Hey if you were this stupid about an obvious choice, you could've at {i}least{/i} asked the hint goblin for advice!"
            h "He rhymes too much..."
        "Hint!":
            scene hintl
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/The Hint Goblin!.mp3"
            show hobnob:
                xalign 0.4
                yalign 9.3
                linear .8 xalign 0.8
                linear .8 xalign 0.4
                repeat
            hint "If you perv into the girls', your balls will get kicked so many times that to keep them alive, they'd have to be hard as pearls!"
            scene carpet
            play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Mountania.mp3"
            show boys:
                xalign 0.0
                yalign 0.0
            show girls:
                xalign 1.0
                yalign 0.0
            show harry:
                xalign 0.5
                yalign 2.0
            show hermione:
                xalign 0.86
                yalign 4.5
            menu:
                "Boys":
                    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/You win the Duel!.mp3"
                    h "I better just go to my normal dormitory, duh!"
                    bitch "Duh"
                    show ro1:
                        xalign 0.0
                        yalign 1.5
                    fag "Fuck you."
                    hide hermione
                    with fade
                    n "Hermione ran away up the spiral staircase crying all over her tits."
                    h "Tanks, Ron!"
                    fag "Fuck you."
                "Girls":
                    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/A shameful Mistake.mp3"
                    bitch "How {b}dare{/B} you, you perverted motherfucker!"
                    h "Hey, respect my choices; nothing is wrong!"
                    bitch "Okay, if you really want to then, walk up the stairs."
                    h "k"
                    hide girls
                    show slide:
                        xalign 1.0
                        yalign 0.0
                    hide harry
                    show scarry:
                        xalign 0.5
                        yalign -4.0
                        linear 3.0 yalign 10.0
                    $ renpy.pause(1.7)
                    show harry:
                        xalign 0.5
                        yalign 1.5
                    h "*CRASH* Ouch!"
                    bitch "If you walk up the stairs of the girls' dorm, it'll turn into a slide, haha!"
                    show ro1:
                        xalign 0.0
                        yalign 1.5
                    fag "But you've been in our dormitory before."
                    bitch "Well that's probably just because Dumbledore is a male faggot... A-a-a-anways, seriously, get up to your real dormitory!"
                    fag "Fuck."
    scene black with fade
    n "Harry had gone to bed to rest for the night."
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Sleep Times.mp3"
    show source3
    hide source3
    n "And the night came down... (No orgasm pun intended)"
    play music "medusa.mp3"
    scene duk with fade
    scene muck with fade
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/Trouble Indeed.mp3"
    show fuck:
        xalign .5
        yalign 0.3
    h "By no! Where am I? Why are my nipples 1 milimiter bigger than normal? Why do I know that? WHATHAVE YOU DONE TO GInY!?"
    fuck "I'll tell you what, bitch..."
    fuck "{b}I{/b} am back, mothafucka! And worse than ever!"
    h "Oh shit!"
    h "What about the jail?"
    h "I mean What about the azkaban?"
    show source0:
        xalign 3
        yalign 4
    fuck "Ask a band? Why should I?"
    show source1:
        xalign 3
        yalign 4
        linear 3 xalign 2
        linear 4 yalign 4
    h "Fuck you you fucking asshole I hope you die prick what the fuck are you doing die or go back to jail I don't care fuck you."
    hide source0
    fuck "That's rude!"
    h "Well, {i}are{/i} you plotting anything... you know, bad, like last time?"
    fuck "Well, having a sprite as ugly as mine is a bad action enough, even know I didn't choose it (that's how fucking bad it is, makes me look like if Mr. Potatohead got SACKED from his job and became the towndrunk)."
    fuck "Ass I do have a few evil ideas... that I dwon't tell you!"
    h "Ass?"
    show source3:
        xalign 1
        yalign 1
    fuck "But(Jimmy {b}T{/b})!"
    h "oh...."
    show source2:
        xalign .423
        yalign 2.3
        linear 20 xalign 0.8 yalign 12
    fuck "Well, I'm gonna wake you up from this stupid dream in a second whether you want to or not, k harry?"
    h "Fuck you."
    fuck "Well, anyways, I'll meet you IRL soon. Details just text uh.... the frog of doom jail. After all, they decided to make me the boss of that place, can you believe it? I was promoted from prisoner for my knowledge abotu the cells!"
    n "And then Harry realized.... the devious plan."
    play sound "Oh dear.mp3"
    h "YOU USED THAT POSITION TO FREE YOURSELF FROM JAIL!!!"
    fuck "Right... of course. Just that the guards were kinda.. well, one adjective to describe him was that his name was Mundungus and he is much lazier than gus fring."
    h "Finky-"
    scene carpet
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/In Your Light.mp3"
    show signpost:
        xalign .5
        yalign 0
    show nude:
        xalign .5
        yalign 1.5
    n "Harry had then woken up... naked!"
    hide nude
    show nude:
        xalign .2
        yalign 1.5
        linear .3 xalign 0.8
        linear .3 xalign 0.2
        repeat
    h "Oh {b}SHIT!{/b}"
    show ro2:
        xalign 0.0
        yalign 0.55
    fag "Morning, harry."
    h "Oh, hi, Ron..."
    fag "btw, nice size on that thing."
    h "*groooooan*..."
    scene black
    stop music
    n "One timeturner later..."
    scene carpet
    play music "Harry Potter & the Frog of Doom 2 - The Frog Strikes Back/In Your Light.mp3"
    show hermione:
        xalign .2
        yalign 1.5
    bitch "Good morning, Harry!"
    show harry:
        xalign 4
        yalign 1
    h "Morning, Hermione!"
    show percy:
        xalign .5
        yalign 1
    percy "Everone, out to your classes please."
    play sound "yipyap.mp3"
    gry "We know what the fuck we're doing!"
    percy "..."
    hide percy
    n "And after Percy cut his bullcrap, they went to have breakfast."
scene end
n "That was a great tale, wasn't it? Now to fap to YOU, listening child..."
return