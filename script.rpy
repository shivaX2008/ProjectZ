# Declare characters
define Suzanne = Character('Suzanne', color="#E03B8B")
define Jonathan = Character('Jonathan', color="#5FA9E8")

# Define flash transition
define flash = Fade(0.1, 0.0, 0.5, color="#FFFFFF")

# Start of game
label start:
    scene bg lab
    with fade

    "The old science lab door creaks open."

    show suzanne neutral at left
    show jonathan neutral at right

    Suzanne "Welcome to the heart of chaos — the old lab!"
    Jonathan "And this is for a 'school project'?"
    Suzanne "Project... Z."
    Jonathan "Sounds boring already."
    Suzanne "Wait till you see this!"

    "Suzanne walks to an old machine labeled: *Project Z — Temporal Prototype*."

    menu:
        "Ask about the machine or stay quiet?"

        "Ask about it":
            Jonathan "What’s that? A futuristic coffee maker?"
            Suzanne "Nope. A time glitch generator!"

        "Stay quiet":
            Jonathan "I have a bad feeling about this..."
            Suzanne "Relax. Just one button. What could go wrong?"

    "Suzanne presses the button. The machine flashes pink and blue, humming loudly."

    with flash
    "Everything freezes for a moment."

    Jonathan "Uh... Suzanne? Are you frozen or am I in slow motion?"
    Suzanne "Both, maybe. Did we just enter a time loop?"

    menu:
        "Investigate the machine or step back?"

        "Investigate":
            Suzanne "Let’s see if we can control it."
            Jonathan "Or break reality further..."

        "Step back":
            Jonathan "We should stop. This feels dangerous."
            Suzanne "Where’s your sense of adventure?"

    "The lab flickers — now shiny and futuristic."

    scene bg future_lab
    with dissolve

    show suzanne neutral at left
    show jonathan neutral at right

    Jonathan "Whoa! What happened?!"
    Suzanne "Future lab! We jumped forward in time!"
    Jonathan "Another button?"
    Suzanne "Go deeper!"
    Jonathan "NOOO—!"

    # MENU 1: Explore the futuristic lab
    menu:
        "What should they do in the future lab?"

        "Search for clues":
            Suzanne "Good idea. There might be logs or notes here."
            Jonathan "Or more creepy machines..."

        "Touch random buttons":
            Jonathan "I can’t resist. These buttons are glowing!"
            Suzanne "WAIT—!!"
            "An alarm briefly flashes, then stops."
            Jonathan "Oops."

        "Stay still and observe":
            Suzanne "Maybe nothing will happen if we just wait."
            Jonathan "For once, that sounds like a plan."

    "Jonathan accidentally presses another button."
    scene black
    with flash
    "The screen distorts — everything fades to black."
    
    scene bg glitch
    with fade

    show suzanne neutral at left
    show jonathan neutral at right

    Suzanne "Great. Glitch dimension."
    Jonathan "You find this cool when I panic!"
    Suzanne "Chaos equals creativity!"
    Jonathan "Hospitals equal our next stop!"

    menu:
        "Try to fix the machine or explore the glitch?"

        "Fix the machine":
            Suzanne "We need the right combination to escape."
            Jonathan "Or end up in dinosaurs!"

        "Explore the glitch":
            Jonathan "Let’s see what this place hides."
            Suzanne "Careful. Reality’s unstable."

    # MENU 2: Encounter something strange in the glitch
    menu:
        "A strange figure appears in the glitch... What do they do?"

        "Talk to it":
            Suzanne "Hello...? Are you real?"
            "The figure distorts, then responds in broken speech."
            Jonathan "Creepy."

        "Run away":
            Jonathan "NOPE. I’m out!"
            Suzanne "Jonathan, wait!!"

        "Analyze the glitch figure":
            Suzanne "Its code pattern looks... familiar."
            Jonathan "Why do you sound excited?!"

    "The machine beeps softly."

    Suzanne "Wait! Log says 'Project Z initiated by Jonathan.'"
    Jonathan "WHAT?! I didn’t touch anything!"
    Suzanne "Maybe your alternate version did."
    Jonathan "Even my duplicates are troublemakers?"

    # MENU 3: Reaction to the log message
    menu:
        "How should Jonathan react to the log?"

        "Panic":
            Jonathan "This is bad. Really, really bad."
            Suzanne "You think?!"

        "Laugh it off":
            Jonathan "Haha. Funny how it's always me."
            Suzanne "This isn't a joke!"

        "Blame Suzanne":
            Jonathan "You’re the one pressing everything!"
            Suzanne "Excuse me?!"

    "Another bright flash — everything resets to normal."

    scene bg lab
    with fade

    show suzanne neutral at left
    show jonathan neutral at right

    Jonathan "Finally... normal again."
    Suzanne "See? Time isn’t that hard."
    Jonathan "Lesson learned — never let you touch buttons."
    Suzanne "Next up: teleportation?"
    Jonathan "Skipping school that day."

    # MENU 4: Epilogue choice
    menu:
        "How should the story end?"

        "Suzanne plans another experiment":
            Suzanne "Next time, we’ll break physics AND chemistry!"
            Jonathan "Great... I can’t wait to survive that."

        "Jonathan smashes the machine":
            Jonathan "NO more glitches!"
            "He picks up a wrench dramatically."
            Suzanne "HEY! That’s vintage tech!"

        "They both laugh and leave the lab":
            "Suzanne laughs mischievously."
            Jonathan "Let’s just go home."
            Suzanne "Deal. Adventure tomorrow?"

    return
