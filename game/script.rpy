# Greetings Agent! Welcome to the script of your life. 
# In this document you will discover several possible fates which may befall you.
# Read on at your own peril.

# Define characters and properties

define a = Character("Agent Redacted", color="#e38444")
define m = Character("Monster-Handler Tyson", color="#7ad0df")
define ma = Character("Monster-Handler Tyler", color="#7ad0df")
define mb = Character("Camp Counselor Tyson?", color="#7ad0df")
define d = Character("Agent Dee", color="#5176a0")
define b = Character("Agent Blank", color="#e0bc6d", who_font="classy")
define n = Character("Agent Null", color="#9b9b7b")
define ch = Character("Agent Chill", color="#154c79")
define s = Character("MA431X", color="#873e23", who_font="dirty", what_font="dirty")
define w = Character("Wub_Daemon", color="#bc39c1")
define r = Character("DOMA REPORT", color="#6c6b5a")

define config.font_name_map["dirty"] = "Premio.otf"
define config.font_name_map["classy"] = "AsenPro-Black.otf"

init python:
    renpy.music.register_channel("music2", "music", loop=True, synchro_start=True)


transform fullscreen:
    xysize (1920,1080)

transform halfsize:
    xysize (400,400)

transform middleright:
    yalign 0.7

transform middleleft:
    yalign 0.1

image blackscreen = "#000000"
image scopes = Movie(play="m-testscopes.webm", loop=True, xalign=0.80, yalign=0.50)
image waves = Movie(play="m-testwaves.webm", loop=True, xalign=0.10, yalign=0.50)
image overflow = Movie(play="v-bufferoverflow.webm", loop=True)
image credits = Movie(play="m-credits.webm", loop=True)





# Rise and shine Agent.
# Rise and... shine
label start:


    scene bg morning
    with fade

    $ renpy.music.play("m-wakeup-intro.mp3")
    $ renpy.music.queue("m-wakeup-loop.mp3", clear_queue=False)

    "BRRRRRRRRRING!"

    "BRRRRRRRRRRRRIIIIIIIIINNNNNGGG!!"

    voice "v-nar-001.mp3"
    "The alarm chirps its cicada song, rousing you from your peaceful repose once more."

    voice "v-nar-002.mp3"
    "The start of another day."

    menu:
        "Time to wake up":
            jump get_dressed

        "Hit snooze":
            jump late_end


# You're late for work!
# LATE ENDING
label late_end:


    scene blackscreen
    with fade

    stop music

    voice "v-nar-003.mp3"
    "Slamming the snooze button you roll over, back into the warm embrace of your bed."

    voice "v-nar-004.mp3"
    "The world fades out around you. Nothing is wrong, all is quiet."

    voice "v-nar-005.mp3"
    "You're going to be extremely late for work..."

    scene bg badend

    pause 0.25

    play sound "s-beeg-slam.mp3"

    show img badend
    with vpunch
    
    pause

    return


# Once more with feeling
# Continue waking up
label get_dressed:


    scene bg closet
    with fade

    voice "v-nar-006.mp3"
    "Crawling out of bed, you swing open the closet."

    show char backguy

    voice "v-agent-a1.mp3"
    a "Hmm, what to wear..."

    menu:
        "Black Suit":
            jump keep_getting_dressed
        "Black Suit":
            jump keep_getting_dressed
        "Black Suit":
            jump keep_getting_dressed
        "Black Suit":
            jump keep_getting_dressed

label keep_getting_dressed:

    voice "v-nar-007.mp3"
    "An excellent choice."

    hide char backguy
    show char suitguy

    voice "v-nar-008.mp3"
    "Clad in your suit of armor, you are ready for the challenges of the day."

    hide char suitguy
    show char neutralguy

    voice "v-nar-009.mp3"
    "At least you will be once you have your morning coffee."


# time to make coffee
label make_coffee:


    scene bg kitchen
    with fade

    voice "v-nar-010.mp3"
    "Your efficient, and functional kitchen greets you with the usual cold detatchment."

    voice "v-agent-a5.mp3"
    a "Yaaaaaaaawn"

    show char sadguy

    voice "v-nar-011.mp3"
    "Any good Agent's day begins with a single slice of plain toast, and a rich cup of instant coffee."

    voice "v-nar-012.mp3"
    "You prime the toaster with a slice of enriched white bread, before stirring one scoop of instant coffee into a mug of tap water."

    scene bg toaster

    play sound "s-toaster.mp3"
    play sound "s-gloop.mp3"

    voice "v-nar-013.mp3"
    "Placing the mug into the microwave, you heat the coffee for 60 seconds."

    play sound "s-microwave.mp3"

    pause

    show img coffee at truecenter

    a "*ssssip*"

    voice "v-agent-a1.mp3"
    a "Ahhhh, tepid."

    voice "v-nar-014.mp3"
    "You down the brown liquid in a few determined gulps, then with satchel in hand, and toast in mouth, head out for the day."


# set out for the day
label set_out:


    scene bg street
    with fade

    show char toastguy

    play sound "s-running.mp3"

    voice "v-nar-015.mp3"
    "Setting out as you do every day at a full dead sprint, you move with purpose and determination towards The Department."

    voice "v-nar-016.mp3"
    "Rounding the corner with reckless abandon and slam headlong into..."


    scene blackscreen

    stop music fadeout 1

    play sound "s-thud.mp3"

    "THUD"

    scene bg corner

    show char bonkguy

    "Owwwww"

    $ renpy.music.play("m-city-intro.mp3")
    $ renpy.music.queue("m-city-loop.mp3", clear_queue=False)

    voice "v-nar-017.mp3"
    "...your neighbor, who you've successfully bowled over... again."

    voice "v-agent-a2.mp3"
    a "Oh, good morning Tyler. Sorry about that."

    voice "v-tyson-1.mp3"
    ma "Good morning Agent! Not a problem, I should have been looking where I was going. I was just so distracted by my latest findings, I wasn't paying attention!"

    voice "v-nar-018.mp3"
    "Tyson lives next door, and works as a zoo keeper. Or is he the head of a youth choir, or maybe a cartographer?"

    voice "v-tyson-2.mp3"
    mb "It's just so exciting! Our recent expeditionary excursions and field observation posts have greatly expanded our cataloging capabilities."
    
    voice "v-tyson-4.mp3"
    m "We've made some, frankly shocking discoveries of colossal proportions which are shaking our very understanding of the world!"

    voice "v-tyson-3.mp3"
    m "And you wouldn't believe, while tracking some new readings, we've seen matching resonances between local events and the newfound Pairo-"

    voice "v-agent-a3.mp3"
    a "Sorry Tyson, I'd love to catch up more, but I'm already running late. Let's grab water at some point. Bye!"

    voice "v-nar-019.mp3"
    "He certainly loves to gab, but you don't have time for his idle musings right now. Back to the road!"

    voice "v-tyson-5.mp3"
    m "Okay bye~! And Haaaaappy Mon~~~"


# arrive at DOMA office
label arrival:


    scene bg officefront
    with move

    show char happyguy

    voice "v-nar-020.mp3"
    "A flock of agents mill about the promenade sprawling before the imposing facade of The Department of Monstrous Anomalies."

    voice "v-agent-a1.mp3"
    a "Good morning Agent."

    show char agentd1

    voice "v-agent-d1.mp3"
    d "Ah Red, running a bit late aren't we?"

    voice "v-nar-021.mp3"
    "Agent Dee cuts a striking figure amidst a sea of bookish suits, shuffling their way to work."

    voice "v-nar-022.mp3"
    "His veneer of confidence however, is paper thin. And you have places to be."

    voice "v-agent-a4.mp3"
    a "Are you sure you should be out here posing? I heard that MA903 broke containment last night."

    hide char agentd1
    show char agentd2

    voice "v-agent-d2.mp3"
    d "Wh-who told you?"

    voice sustain
    d "It's fine, containment has already been re-established, and we only had to blank out 2 blocks."

    voice "v-agent-a1.mp3"
    a "uh huh, see you later Dee. Try to keep it together."


    scene bg officedoor
    with dissolve

    voice "v-nar-023.mp3"
    "The main security interlock of the DOMA office, and the gateway to adventure awaits your entry."

    voice "v-nar-024.mp3"
    "Incredible how a simple assortment of pneumatics, solenoids and bimetallics can contain such an overwhelming, rapturous amount of science and wonder."

    scene blackscreen
    with fade

    play sound "s-security-door-scan.mp3"

    pause

    voice "v-nar-025.mp3"
    "Thorough scans of your biometrics, psychometrics, etherometrics, vanity metrics, and KPI's are recorded upon entry."


# Enter the Department
# Encounter Chill Dude
label office_normal_a:

    scene bg office2

    #$ renpy.music.play("m-office-intro.mp3")
    $ renpy.music.play("m-office-loop.mp3", loop=True, fadein=1, if_changed=True)

    voice "v-nar-026.mp3"
    "The Analysis floor at the Department is bustling with activity, as Agents throw themselves at another exciting day of observation."

    voice "v-nar-027.mp3"
    "Busily monitoring, analyzing, and cataloging anomalies from around the globe, Agents dot the floor."

    show char agentchill

    voice "v-agent-ch1.mp3"
    ch "Yo Red, you see the new map?"

    voice "v-agent-ch2.mp3"
    ch "We've been waiting on this thing for like 14 months, and this is what they came up with."

    show img realdonut

    voice "v-nar-028.mp3"
    "It's just a donut."


    menu:
        "Why are you showing me your breakfast?":
            jump office_normal_b
        "Can I eat it?":
            jump office_normal_b
        "I think the new map is better, honestly.":
            jump office_normal_c


# I'm Hungry
label office_normal_b:

    voice "v-agent-a1.mp3"
    a "Sigh. Good morning Agent Chill."

    voice "v-agent-a3.mp3"
    a "If you're going to tease me with your breakfast, at least share."

    voice "v-agent-ch1.mp3"
    ch "Haha, come on dude! Everyone's all Torus this, and Torus that. Doesn't it just make you hungry?"

    voice "v-nar-029.mp3"
    "'Most' Agents, at least are bustling with activity..."

    jump office_normal_d


# I'm Right
label office_normal_c:

    voice "v-nar-030.mp3"
    "This hotly debated topic, and Agent Chill's attempt to initiate humor this early in the morning fail to connect in your mind."

    voice "v-agent-a3.mp3"
    a "The old mapping models were getting quite cumbersome as we continued to expand our scanning capabilities."

    voice "v-agent-a4.mp3"
    a "Previous rotational models only operated in 2 dimensions. Which made absolutely no sense to begin with."

    voice "v-agent-a3.mp3"
    a "We already struggle to understand 4 dimensional space. What business did we have trying to model a 2D universe?"

    ch "..."

    voice "v-agent-ch3.mp3"
    ch "The sprinkles are pretty good though."

    voice "v-nar-031.mp3"
    "With a grimmace, you continue on with your morning."

    jump office_normal_d


# Debate Bros
label office_normal_d:


    scene bg office3

    voice "v-nar-032.mp3"
    "A team huddled around stacks of archive boxes is debating the plausibility of certain model assumptions."

    show char agentnull

    voice "v-agent-n1.mp3"
    n "Postulate all you want, but the evidence is clear."

    show img fakedonut at truecenter
    with dissolve

    voice "v-agent-n2.mp3"
    n "Phase 1 readings clearly demonstrate a pair of inverted Einstein-Podolsky-Rosen bridges, terminating toward one another. This explains its initial form!"

    hide img fakedonut
    show img superfakedonut at truecenter
    with dissolve

    voice "v-agent-n3.mp3"
    n "Phase 2's results obviously illustrate a lattice of 18 spiral patterns, collapsing the phase space, and engulfing the toroid."

    voice "v-nar-033.mp3"
    "The audience stands in rapt attention."

    hide img superfakedonut
    show img ultrafakedonut at truecenter
    with dissolve

    voice "v-agent-n2.mp3"
    n "Thus we can surmise that without intervention, the toroidal forces will continue to entwine, expanding at a logarithmic rate, until the toroid space and our present phase space collide in a catastrophic..."

    hide img ultrafakedonut
    show char agentblank

    voice "v-agent-b1.mp3"
    b "Ok, ok. Let's all calm down here."

    voice "v-agent-b2.mp3"
    b "The Department encourages a solutions focused mindset, especially on Monday mornings. But I'm not hearing a lot of 'can do's' in this little monologue."

    voice "v-nar-034.mp3"
    "A Senior Observer osmoses their way through the crowd, diffusing the nascent fervor."

    voice "v-agent-b3.mp3"
    b "Nothing's collapsing, nothing is twisting out of control. Agent Null, I think you need to box up these samples and take them back to storage."

    voice "v-agent-n4.mp3"
    n "But..!"

    voice "v-nar-035.mp3"
    "You decide to continue on before someone phases themselves out of a job."


# Let's analyze
label office_cubicle:

    scene bg cubicle

    $ renpy.music.play("m-working-intro.mp3")
    $ renpy.music.queue("m-working-loop.mp3", clear_queue=False)

    voice "v-nar-036.mp3"
    "You plop down at your terminal, ready to begin a riviting day of analysis."

    show char busyguy2 at right

    play sound "s-computer-on.mp3"
    $ renpy.sound.play("s-scopes-loop2.mp3")

    voice "v-nar-037.mp3"
    "The morning passes in a blink as you click though audio readings."

    voice "v-nar-038.mp3"
    "Torus analysis can be very relaxing, as the random sounds running through your radio stereograph almost seem rhythmic. Musical even."

    voice "v-nar-039.mp3"
    "Alas, one Agent can hardly crack this decades long mystery on their own. So soldier on, and analyze like you've never analyzed before!"

    scene blackscreen
    with fade

    pause 1.0

    jump office_cubicle_return



# I'm back here again
label office_cubicle_return:

    scene bg cubicle
    with fade

    voice "v-nar-040.mp3"
    "Instruments humming with the anticipation of yet unknown discovery set the tempo of your workday."

    show scopes
    with dissolve

    $ renpy.music.play("m-working-loop.mp3", loop=True, if_changed=False, synchro_start=True, channel='music')
    $ renpy.music.play("m-working-loop-active.mp3", loop=True, if_changed=False, synchro_start=True, channel='music2')
    $ renpy.music.set_volume(0, delay=0.25, channel='music')
    $ renpy.music.set_volume(1, delay=0.25, channel='music2')
    $ renpy.sound.play("s-scopes-loop1.mp3")

    voice "v-nar-041.mp3"
    "Today's harmonies embrace your senses in an all too familiar way."

    voice "v-nar-042.mp3"
    "They bring you a sense of comfort, contentment, and ease. Almost as if you were humming them yourself."

    show waves
    with dissolve

    voice "v-nar-043.mp3"
    "Are you?"

    voice "v-nar-044.mp3"
    "The all too familiar cadence grips you with a sense of nostalgia, or even deja vu."

    voice "v-nar-045.mp3"
    "What {i}is{/i} that song?"

    voice "v-nar-046.mp3"
    "Hours pass as you get lost in the melodies. Enriched. Fulfilled."

    scene blackscreen
    with fade

    pause 1.0

    $ renpy.music.set_volume(1, delay=0.25, channel='music')
    $ renpy.music.set_volume(0, delay=0.25, channel='music2')
    $ renpy.sound.stop("s-scopes-loop1.mp3")
    $ renpy.sound.stop("s-scopes-loop2.mp3")

    scene bg cubicle
    with dissolve

    voice "v-agent-a1.mp3"
    a "Is it lunch time already?"

    voice "v-nar-048.mp3"
    "Up like a shot, you head out for your mid-day bowl of caloric supplements."


# On the way to lunch
label office_normal_e:

    scene bg office1
    with dissolve

    voice "v-nar-049.mp3"
    "The Agency floor is largely vacant, as the more punctual Agents have made a break for the elevators."

    voice "v-nar-050.mp3"
    "Several anomalous materials have been left unattended at work stations and testing benches."

    show img taco at truecenter
    with dissolve

    voice "v-agent-a4.mp3"
    a "Anguiform extrusion always seems to lead the floor teams to carelessness. Leaving a class 8 consumable out in the open like this, tsk."

    voice "v-agent-a3.mp3"
    a "Someone is going to return to a severe case of anamorphositis if this is left out."

    hide img taco
    with dissolve
    
    show img fishbox at truecenter
    with dissolve

    voice "v-nar-051.mp3"
    "Perhaps the pep in your step is coloring your vision."

    voice "v-nar-052.mp3"
    "Perhaps you're experiencing a bout of apophenia, as these seemingly unrelated specimens appear connected to your rhythmically firing neurons."

    voice "v-nar-053.mp3"
    "Perhaps you're just hungry..."


    scene bg elevator
    with fade

    voice "v-nar-054.mp3"
    "You're late, and the elevators are crowded. A large group of Agents is ahead of you, waiting to head down to the canteen."

    play sound "s-elevator-ding.mp3"

    voice "v-nar-055.mp3"
    "Your hunger is getting the better of you."
    
    voice "v-nar-056.mp3"
    "As you desperately consider going back to eat MA554, or continuing to wait, you spot something in the periphery of your vision."

    scene bg cursedelevator
    with dissolve

    voice "v-agent-a1.mp3"
    a "Was this elevator always here?"

    voice "v-nar-057.mp3"
    "The chatter of your fellow agents fades away as you look at the solitary door."

    voice "v-nar-058.mp3"
    "Why was no one taking this elevator?"

    menu:
        "Take the elevator":
            jump cursed_elevator

        "Wait with other Agents":
            jump good_end_1


# GOOD END WITH FISH
label good_end_1:

    scene blackscreen
    with dissolve

    stop music fadeout 1

    voice "v-nar-059.mp3"
    "Returning to the crowded elevators, you choose to wait patiently for your turn."

    voice "v-nar-060.mp3"
    "You reach the canteen just in time to enjoy a pleasant fish paste extrusion for lunch."

    scene bg goodend
    
    pause 0.25

    play sound "s-beeg-slam.mp3"

    show img goodend
    with vpunch
    
    pause

    return


# Get in the elevator Shinji
label cursed_elevator:

    scene bg insideelevator
    with fade

    stop music fadeout 1

    voice "v-nar-061.mp3"
    "Stepping into the isolated elevator, you are greeted with an oppressive atmosphere."

    voice "v-nar-062.mp3"
    "You stand in a fugue state for what feels like hours before snapping back to attention, realizing that you haven't pushed a button yet."

    play sound "s-elevator-sounds.mp3"

    voice "v-nar-063.mp3"
    "With only one choice before you, you depress the solitary control mechanism..."

    show char crouchguy

    voice "v-nar-064.mp3"
    "The elevator shudders violently, while somehow not giving the impression of vertical motion."

    voice "v-agent-a1.mp3"
    a "I don't remember the canteen being this many floors away."

    voice "v-nar-065.mp3"
    "A sudden realization strikes."

    voice "v-agent-a4.mp3"
    a "Oh no, did I unwittingly step into the parkade elevator? My clearance doesn't permit me access to Agency transportation."

    voice "v-agent-a5.mp3"
    a "I'm going to get cited for this..."
  
    play sound "s-elevator-ding.mp3"

    voice "v-nar-066.mp3"
    "The door unceremoniously opens."


# This is fine
label office_cursed_1:

    scene bg darkoffice02
    with dissolve

    $ renpy.music.play("m-creepy-intro.mp3")
    $ renpy.music.queue("m-creepy-loop.mp3", clear_queue=False)
  
    show char scaredguy

    voice "v-agent-a1.mp3"
    a "Uh, did I get off on the wrong floor?"

    voice "v-nar-067.mp3"
    "Stepping out of the elevator, the door closes and you quickly notice that there are no buttons to call it back."

    voice "v-nar-068.mp3"
    "Wherever you are, you're stuck here."

    voice "v-nar-069.mp3"
    "While on the surface this floor appears to mirror the Analyst level you work on every day, something is clearly, eerily different."

    voice "v-nar-070.mp3"
    "The atmosphere is suffocating, and a low hum permeates the air. You can hear music reverberating in the distance."

    voice "v-agent-a2.mp3"
    a "Guess I should look around."

    "There are workstations, storage cabinets, and a hallway leading to █ level containment cells. Familiar music is coming from the containment rooms."

    menu:
        "Go to the workstations":
            jump office_cursed_2

        "Go to the storage cabinets":
            jump office_cursed_3

        "Go to the containment rooms":
            jump office_containment_hall
    

# Workstation Arrival
label office_cursed_2:

    scene bg darkoffice01
    with dissolve

    voice "v-nar-071.mp3"
    "Long abandoned workstations line the aisles. Research reports, catologue files, and ransacked containment vessels are scattered among the cubicles."

    voice "v-nar-072.mp3"
    "A rhythmic pulse becomes apparent as you make your way through the floor."

    play sound "s-humm.mp3" volume 1


    menu:
        "Look around":
            jump office_cursed_2_explore

        "Explore elsewhere":
            jump office_cursed_2_leave


# Workstation exploration
label office_cursed_2_explore:

    voice "v-nar-073.mp3"
    "As you sift through the piles of detritus, your hand grazes something cool."

    show img snowball at halfsize, truecenter
    with dissolve

    voice "v-nar-074.mp3"
    "A snowball rests on the office floor in defiance of the laws of thermodynamics."

    voice "v-nar-075.mp3"
    "A wave of child-like wonder grips you as you attempt to pick up the orb."

    a "Hrrrrrnnn"

    voice "v-nar-076.mp3"
    "This proves to be a monumental task, as the object refuses to budge. Though, while you can't lift it, it does appear that you can push it."

    menu:
        "Shove the snowball":
            jump bigger_ball

label bigger_ball:

    hide img snowball

    show img snowball at truecenter
    with dissolve

    voice "v-nar-077.mp3"
    "The ball rolls with remarkable ease, absorbing everything in its path."

    voice "v-nar-078.mp3"
    "It rapidly multiplies in size until coming to a halt once more."

    voice "v-agent-a5.mp3"
    a "Uh, maybe I shouldn't do that again."

    voice "v-nar-079.mp3"
    "A flash of motion catches your eye, as you turn just in time to duck out of the path of a fast moving object."

    hide img snowball

    show img rocket at truecenter
    with fade

    voice "v-nar-080.mp3"
    "A rogue barrel rockets past, performing laps around a group of cubicles with alarming speed."

    voice "v-nar-081.mp3"
    "Had you somehow entered its flight path without noticing it before?"

    voice "v-nar-082.mp3"
    "Was it aiming for you?"

    voice "v-agent-a2.mp3"
    a "It's getting a bit dodgy in here. I should move on."


label office_cursed_2_leave:

    "There are storage cabinets, and a hallway leading to █ level containment cells. Familiar music is coming from the containment rooms."

    menu:
        "Go to the storage cabinets":
            jump office_cursed_3

        "Go to the containment rooms":
            jump office_containment_hall
    

# Cabinet Arrival
label office_cursed_3:

    scene bg darkoffice03
    with dissolve

    show char sideguy

    voice "v-nar-083.mp3"
    "Dilapidated storage cabinets and racks span the wall before you. Several containers appear to have been left carelessly opened."

    voice "v-nar-084.mp3"
    "Or rather, a number of racks appear to have breached from the inside. Chittering and scraping can be heard, but barely due to the incessant thumping coming from the Containment Hall."

    play sound "s-humm.mp3" volume 0.75


    menu:
        "Look around":
            jump office_cursed_3_explore

        "Explore elsewhere":
            jump office_cursed_3_leave


# Cabinet Exploration
label office_cursed_3_explore:

    voice "v-agent-a3.mp3"
    a "The Observers have clearly not been down here in a while."

    voice "v-agent-a4.mp3"
    a "The neglegent Agents in charge of cataloguing these anomalies should be ashamed of themselves."

    voice "v-nar-085.mp3"
    "This disgraceful display has stirred something within you."

    voice "v-agent-a2.mp3"
    a "Time to do my part."

    
    menu:
        "Clean the open cabinets":
            jump clean_cabinets
        
        "Tidy up the reports":
            jump clean_reports



label clean_cabinets:

    voice "v-nar-086.mp3"
    "Approaching the megalithic wall of cabinetry, you roll up your sleeves and get to work."

    voice "v-nar-087.mp3"
    "As if driven by compulsion, you methodically shutter every open drawer, and latch every door left ajar."

    play sound "s-slam.mp3" volume 0.75

    voice "v-nar-088.mp3"
    "Slightly out of reach, a cubby rustles audibly. Perhaps an anomaly left un-restrained remains inside."

    voice "v-nar-089.mp3"
    "Climbing up on a ladder, you reach as far as you can. While unable to see inside, you deftly reach your hand in."

    voice "v-nar-090.mp3"
    "Slowly, carefully, your hand dances past paper reports, acrylic enclosures, soft surfaces."

    play sound "s-thud.mp3"

    voice "v-nar-091.mp3"
    "Something gently caresses your hand, causing you to grip whatever you are resting on, and withdraw from the cubby immediately."

    show img jelly at truecenter

    voice "v-agent-a5.mp3"
    a "What is this ██████?"

    voice "v-nar-092.mp3"
    "The words escape your mouth like a reflex."

    voice "v-agent-a4.mp3"
    a "Some anomalies are documented to have re-written the language centers of an Agent's mind, teaching them yet indecipherable lexicons."

    voice "v-nar-093.mp3"
    "You stuff the object back into the cubby, sealing its enclosure and preventing further egress."

    voice "v-nar-094.mp3"
    "It's time to move on."

    jump office_cursed_3_leave


label clean_reports:

    voice "v-nar-095.mp3"
    "Reports, ejected from the wall of cabinets lies strewn across the office. What a mess."

    voice "v-agent-a2.mp3"
    a "Well, nothing to it but to do it."

    voice "v-nar-096.mp3"
    "The can-do attitde of a committed Agent is a hallmark of the Department. How this place reached such a state of dissaray is the real mystery here."

    voice "v-nar-097.mp3"
    "You get to work stacking, arrangeing, and most of all avoiding direct eye contact with redacted material. Just like you were trained to do."

    voice "v-nar-098.mp3"
    "Out of nowhere, a pile of refuse collapses, and a ladder once propped up tumbles in your direction, whipping across the floor."

    play sound "s-thud.mp3"

    voice "v-nar-099.mp3"
    "With cat-like reflexes you jump, though slightly too late. The edge of the ladder clips your foot, sending you into a tumble."

    voice "v-nar-100.mp3"
    "On its passing, you feel a mild zap. Almost reminiscent of a light static shock."

    show img canon at truecenter

    voice "v-nar-101.mp3"
    "An armature rotates slowly in the corner of the office space, though you can't quite make out the details."

    voice "v-nar-102.mp3"
    "A large orb the size of a small orb rolls across the floor, knocking into the recently fallen ladder."

    voice "v-agent-a2.mp3"
    a "That's it, I'm reporting this to the maintenance crews tomorrow."

    jump office_cursed_3_leave


label office_cursed_3_leave:


    "There are workstations, and a hallway leading to █ level containment cells. Familiar music is coming from the containment rooms."

    menu:
        "Go to the workstations":
            jump office_cursed_2

        "Go to the containment rooms":
            jump office_containment_hall



# Maybe they keep godzilla here
label office_containment_hall:

    scene bg darkoffice04
    with dissolve

    show char backguy

    $ renpy.music.play("m-danger-intro.mp3")
    $ renpy.music.queue("m-danger-loop.mp3", clear_queue=False)
    $ renpy.music.play("m-danger-loop-intense.mp3", loop=True, channel='music2')
    $ renpy.music.set_volume(1, delay=0.25, channel='music')
    $ renpy.music.set_volume(0, delay=0.25, channel='music2')
    

    voice "v-nar-103.mp3"
    "A long hallway filled with containment cells stretches on for as long as you can see."

    voice "v-nar-104.mp3"
    "Most of the containment units are securely locked and powered down. However a conspicuous number of active locked rooms, and a few open doors catch your attention."

    voice "v-nar-105.mp3"
    "Containment cell ███ is producing audible interference even at a distance, though it remains locked. Anomaly storage chamber MA████'s door is swung wide, exposing its contents to the world."


    menu:
        "Look around":
            jump containment_explore

        "Explore elsewhere":
            jump containment_leave


label containment_leave:

    "There are workstations, and a wall of storage cabinets lining the office."

    menu:
        "Go to the workstations":
            jump office_cursed_2
        "Check the cabinets":
            jump office_cursed_3



label containment_explore:

    menu:
        "Investigate the loud sounds":
            jump loud_room_false

        "Check on the open room":
            jump water_chamber


label water_chamber:

    scene bg openchamber
    with dissolve

    voice "v-nar-106.mp3"
    "Approaching Anomaly storage chamber MA███, the room is in dissaray, with the solitary exception of a vibrant blue bottle sitting on a raised dais."

    show img water
    with dissolve

    voice "v-nar-107.mp3"
    "Labeled MA0997, the bottle and its designation are unfamiliar to you."

    voice "v-nar-108.mp3"
    "But it's appeal is undeniable."

    menu:
        "Drink the water":
            jump auspicious_encounter
        
        "Leave it be":
            jump wander_aimlessly


# Once more from the top
label wander_aimlessly:

    scene bg darkoffice01
    with dissolve

    $ renpy.music.play("m-working-intro-active.mp3", relative_volume=0.5, fadein=0.5)
    $ renpy.music.queue("m-working-loop-active.mp3", clear_queue=False, relative_volume=0.5)

    show char struggleguy1

    voice "v-nar-109.mp3"
    "A savvy agent knows better than to carelessly handle Toroidal anomalies. You leave the water behind and continue to explore the floor."

    voice "v-agent-a5.mp3"
    a "I sure am thirsty though."

    voice "v-nar-110.mp3"
    "A familiar tune enters your head. With each rhythmic step, your mind slowly returns to that calm, comfortable place."

    voice "v-agent-a1.mp3"
    a "Where have I heard this song before?"

    voice "v-nar-111.mp3"
    "Cabinets, workstations, Containment Cells."

    voice "v-nar-112.mp3"
    "Cabinets, workstations, Containment Cells."

    voice "v-agent-a3.mp3"
    a "That's nice, someone's humming along with me..."

    voice "v-nar-113.mp3"
    "That's you Agent."

    voice "v-nar-114.mp3"
    "You continue to wander the halls, without aim for what feels like an eternity."

    voice "v-agent-a5.mp3"
    a "I just wanted my fish lunch..."

    scene blackscreen
    with dissolve

    stop music fadeout 1

    jump office_cubicle_return


# Drink deep of my bloooooo
label auspicious_encounter:

    scene bg openchamber
    with dissolve

    show img water
    with dissolve

    voice "v-nar-115.mp3"
    "You chug the bottle of water in one go."

    play sound "s-chug.mp3"

    voice "v-agent-a2.mp3"
    a "oooooh, that's gooooooood~"

    voice "v-nar-116.mp3"
    "This is quite possibly the most refreshing water you've ever consumed."

    voice "v-nar-117.mp3"
    "Glacial, is how you would describe it."
    
    voice "v-nar-118.mp3"
    "If you were pedestrian."
    
    voice "v-nar-119.mp3"
    "When people describe the raw, primordial crispness of an isolated mountain spring, you can only imagine how those experiences pale in comparison to what you are being gifted this day."

    hide img water

    $ renpy.music.set_volume(0, delay=0.25, channel='music')
    $ renpy.music.set_volume(1, delay=0.25, channel='music2')

    voice "v-huzzah1.mp3"
    s "HUZZAH!"
    with vpunch

    show char monstermacro
    with dissolve

    voice "v-agent-a5.mp3"
    a "WHA?!"

    voice "v-huzzah2.mp3"
    s "HUZZAH!"
    with hpunch

    voice "v-nar-120.mp3"
    "An indecipherable mass of hair and sound has materialized behind you, exclaiming in your general direction."

    voice "v-huzzah3.mp3"
    s "Huzzz...bah."

    voice "v-nar-121.mp3"
    "Is it trying to communicate?"

    voice "v-agent-a3.mp3"
    a "Look, I have no idea what you're huzzah to tell me."

    voice "v-huzzah1.mp3"
    s "Huzzah?"

    voice "v-agent-a3.mp3"
    voice "v-huzzah3.mp3"
    a "I know, you huzzah'd that already, but I huzzah huzzah."

    voice "v-nar-122.mp3"
    "The words begin to flow naturally."

    voice "v-huzzah2.mp3"
    s "HUZZAH!"
    with vpunch

    voice "v-huzzah1.mp3"
    a "HUZZAH?"

    voice "v-nar-123.mp3"
    "We are one."

    voice "v-huzzah1.mp3"
    voice "v-huzzah2.mp3"
    s "HUZZAH!"

    scene blackscreen
    with fade

    hide char monstermacro
    with fade

    $ renpy.music.stop(channel='music', fadeout=1)
    $ renpy.music.stop(channel='music2', fadeout=1)

    pause 3.0

    scene bg openchamber

    voice "v-nar-124.mp3"
    "You wake up on the floor, alone."

    show char struggleguy1

    voice "v-nar-125.mp3"
    "Climbing to your feet, a phrase resonates in your mind. Over and over."

    play sound "s-beeg-slam.mp3" volume 0.5

    show img huzzah
    with vpunch
    
    voice "v-nar-126.mp3"
    "You would be hearing nothing else, if not for the growing drone coming the containment corridor."

    #voice "v-nar-127a.mp3"
    "The control panel outside of Containment room MA███ radiates anticipation."

    jump loud_room_true


# Let's wub it up
label loud_room_false:

    scene bg testchamber
    with dissolve

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    $ renpy.music.set_volume(0, delay=0, channel='music2')

    $ renpy.music.play("m-wub-intro-muffle.mp3")
    $ renpy.music.queue("m-wub-loop-muffle.mp3", clear_queue=False)    

    voice "v-nar-127.mp3"
    "Containment room MA███ is locked."

    voice "v-nar-128.mp3"
    "As you approach the room, an aggressive drone grows louder and louder."

    voice "v-nar-129.mp3"
    "A keypad on the doorway is smeared with blue liquid, patiently awaiting your input."

    menu:
        "Enter Passcode":
            jump input_passphrase_false
        "Return to the hallway":
            jump office_containment_hall


label input_passphrase_false:


    menu:
        "password123":
            jump loud_room_locked
        "asdfjkl;":
            jump loud_room_locked
        "██████":
            jump loud_room_locked




label loud_room_locked:

    "PASSWORD INCORRECT"

    "Please enter correct password"

    jump loud_room_false


# Let's wub it up for realz
label loud_room_true:

    scene bg testchamber
    with dissolve

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    $ renpy.music.set_volume(0, delay=0, channel='music2')

    $ renpy.music.play("m-wub-intro-muffle.mp3")
    $ renpy.music.queue("m-wub-loop-muffle.mp3", clear_queue=False) 

    voice "v-nar-127.mp3"
    "Containment room MA███ is locked."

    voice "v-nar-128.mp3"
    "As you approach the room, an aggressive drone grows louder and louder."

    voice "v-nar-129.mp3"
    "A keypad on the doorway is smeared with blue liquid, patiently waiting your input."

    menu:
        "Enter Passcode":
            jump input_passphrase_true


label input_passphrase_true:


    menu:
        "password123":
            jump input_passphrase_true
        "asdfjkl;":
            jump input_passphrase_true
        "██████":
            jump input_passphrase_true
        "HUZZAH":
            jump loud_room_unlocked



label loud_room_unlocked:

    voice "v-nar-130.mp3"
    "Of course, only one thing comes to mind."

    voice "v-nar-131.mp3"
    "The door unlatches, and with a heavy groan swings open."    

    play sound "s-heavy-door.mp3"

    voice "v-nar-132.mp3"
    "Entering the test chamber, an anomaly, the source of the interference sits at the center."

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    $ renpy.music.set_volume(0, delay=0, channel='music2')

    $ renpy.music.play("m-wub-intro-beeg.mp3")
    $ renpy.music.queue("m-wub-loop-beeg.mp3", clear_queue=False)
    
    scene bg wubterminal
    with dissolve

    voice "v-agent-a5.mp3"
    a "Isn't this....?"

label terminal_exposure:

    voice "v-nar-133.mp3"
    "The terminal hums to life displaying an all too familiar interface."

    voice "v-agent-a4.mp3"
    a "This looks like an Agent Analysis terminal, but these applications are not at all sanctioned."

    voice "v-agent-a2.mp3"
    a "What is the World Wide Wub?"

    voice "v-agent-a3.mp3"
    a "Oh, the IC's are going to have a field day with this one."
    
    voice "v-nar-134.mp3"
    "Lost in the endless rolling fields, the azure sky and the low roar of the terminal, several icons are haphazardly placed on the desktop."

    menu:
        "Folder labeled ███████ GOLD ████":
            jump browse_the_wubnet
        "Wub.exe":
            jump enter_the_wubnet_false
        "████████ Avatar █████":
            jump browse_the_wubnet



# Welcome to the Wubnet
label browse_the_wubnet:

    voice "v-nar-136.mp3"
    "Contrary to your training, you decide to indulge in a bit of 'browsing.' As icons dance across the screen, you play a game of cat and mouse."

    voice "v-nar-137.mp3"
    "Your cursor, finally finding its quarry, lands a decisive click on a wayward icon."

    voice "v-nar-138.mp3"
    "The program executes."

    show img error:
        xalign 0.1
        yalign 0.1

    w "████████ WUB WUB ████████████ ████ ████"

    voice "v-nar-139.mp3"
    "A text prompt and an error vascilate on screen."

    voice "v-agent-a3.mp3"
    a "Is this some kind of bbs or usenet?"

    w "WUB ████████ ████ VVVVVV ████"

    show img error:
        xalign 0.2
        yalign 0.2

    pause 0.1

    show img error:
        xalign 0.3
        yalign 0.3

    pause 0.1

    show img error:
        xalign 0.4
        yalign 0.4

    jump enter_the_wubnet_true


# Be more playful
label enter_the_wubnet_false:

    "Welcome to WubNet, please enter password."
    
    menu:
        "HUZZAH":
            jump wrong_wubnet_pass
        "WUBNET":
            jump wrong_wubnet_pass
        "Where's My Lunch?":
            jump wrong_wubnet_pass



label wrong_wubnet_pass:

    "Incorrect Password"

    jump terminal_exposure


# A true wub_daemon
label enter_the_wubnet_true:

    "Welcome to WubNet, please enter password."
    
    menu:
        "HUZZAH":
            jump wrong_wubnet_pass
        "WUBNET":
            jump wrong_wubnet_pass
        "WUBBABUNGA":
            jump true_end


# TRUE END
label true_end:

    scene overflow

    voice "v-nar-140.mp3"
    "Non-sinusoidal waveforms thump, and whump into the depths of your soul."

    voice "v-nar-141.mp3"
    "The digital world washes over you, and embraces you."

    voice "v-nar-142.mp3"
    "You are euphoric."

    w "██████ ███ █████████ ^_~"

    voice "v-agent-a5.mp3"
    a "It's... musical..."

    voice "v-agent-a5.mp3"
    a "Ha... ppy..."

    voice "v-agent-a5.mp3"
    a "Happy... Monstering..."

    scene blackscreen
    with fade
  
    pause 3.0

    scene bg domascreen
    with dissolve

    pause 1.0

    show img true
    with dissolve

    pause

    $ renpy.music.stop(channel='music', fadeout=1)
    $ renpy.music.stop(channel='music2', fadeout=1)

    jump post_report


# TRUE FINAL END
label post_report:

    scene bg domareport
    with fade

    $ renpy.music.play("m-working-intro.mp3")
    $ renpy.music.queue("m-working-loop.mp3", clear_queue=False)
    $ renpy.music.set_volume(0.75, delay=0, channel='music')

    voice "v-agent-a3.mp3"
    r "DOMA REPORT on MA00653\nTYPE: ████\nCLASS: █████\nReporting Agent: ███ ███████"

    voice "v-agent-a4.mp3"
    r "MA00653 presented itself as an elevator located adjacent to lift foyer █ on Analysis floor █."

    voice "v-agent-a4.mp3"
    r "The presumed elevator, being under observation since ██/██/████ has been recorded as rejecting all attempts to enter it."

    voice "v-agent-a3.mp3"
    r "Experiments consisted of loading the elevator with weights, and synthesized ██████l cubes, to simulate a variety of potential occupants."

    voice "v-agent-a4.mp3"
    r "All experiments resulted in the simulated materials being ejected promptly, and the door closing.\nMA00653 had been sealed and its file closed."

    voice "v-agent-a3.mp3"
    r "As of ██/██/████, MA00653 has undergone a notable change. The symbol appearing next to the doorway has changed. "

    voice "v-agent-a3.mp3"
    r "Glyphs continue to baffle cryptographic teams.\nObservation has resumed on the subject."

    voice "v-agent-a4.mp3"
    r "Addendum:\nAgent REDACTED has been absent from work as of ██/██/████, after failing to claim their allotted meal chit on fish day."

    voice "v-agent-a5.mp3"
    r "FILE REMAINS OPEN"

    scene bg cursedelevator2
    with fade

    play sound "s-elevator-ding.mp3"

    pause

    jump credits

    
label credits:

    scene credits
    with dissolve

    $ quick_menu = False
    window hide
    $ credits_speed = 20

    pause 1.0

    show thend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve

    $ renpy.pause(2.0)
    hide thend
    show endcredits at Move((0.5,3.0), (0.5,00), credits_speed, repeast=False, bounce=False, xanchor="center", yanchor="bottom")
    pause(credits_speed)

    scene credits
    with dissolve

    show nexttime:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve


    pause

    return




init python:
    credits = ('Agent Redacted', '████████'), ('Monster-Handler Tyson', 'Owen Wilson'), ('Agent Dee', '████████'), ('Agent Blank', '████████'), ('Agent Null', '████████'), ('Agent Chill', '████████'), ('MA413X', '?????'), ('WUB_DAEMON', '?????'), ('Narrator', 'The Director'), ('Backgrounds, Characters, Art', 'The Monster-Handlers'), ('Music and Sound', 'The Monster-Handlers'), ('Story and Programming', 'The Monster-Handlers')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}{b}" + c[0] + "\n"
        credits_s += "{size=28}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Art, Music, and Characters are the original works\nand copyright of Big Blue Bubble Inc."
    credits_s += "\n\n"
    credits_s += "\n{size=40}DOMA and My Singing Monsters\nare copyright of Big Blue Bubble Inc."
    credits_s += "\n\n"
    credits_s += "\n{size=40}Engine\n{size=30}Ren'Py 8.3.4"


init:
    image thend = Text("{size=48}{b}True Final End", text_align = 0.5)
    image nexttime = Text("{size=48}{b}See You Next Monstering", text_align = 0.5)
    image endcredits = Text(credits_s, text_align=0.5)

