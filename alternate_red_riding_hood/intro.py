from state import state
from act1 import act1
from endings import ending_bad_1, ending_normal_1
from utils import get_choice

from ascii_hut import show_hut
from ascii_granny import show_granny
from ascii_bowl import show_bowl
from ascii_wolf_pet import show_wolf_pet
from ascii_wolf_collar import show_wolf_collar
from ascii_fearful_wolf import show_fearful_wolf


def intro():
    print("\nA cold wind moves through the silent forest.")
    print("Tall trees whisper above as a lone wolf walks between them.")
    print("Hunger gnaws at his stomach, yet something unfamiliar reaches his senses.")
    print("Smoke. Humans. A dwelling.\n")

    show_hut()

    print("\nAhead stands a small wooden hut.")
    print("The door opens with a soft creak.\n")

    show_granny()

    print("\nAn old woman steps outside.")
    print("She squints at the wolf for a moment, then suddenly smiles.\n")

    print('"Badde? Is that you again?"')
    print('"Come here, you stubborn creature..."')
    print("She seems to have mistaken the wolf for a dog.\n")

    print("Without fear, she places a bowl of food on the ground before him.")
    show_bowl()

    print("\nThen, slowly, she reaches toward his neck.\n")

    print("What will the wolf do?")
    print("+  Stay calm and observe (composure)")
    print("-  Growl and show aggression (aggression)")
    print("0  Panic and run away (fear)")

    choice = get_choice(["+", "-", "0"])

    if choice == "-":
        intro_aggression_path()
    elif choice == "+":
        intro_composure_path()
    else:
        ending_normal_1()


def intro_aggression_path():
    print("\nThe wolf bares his teeth and begins to growl.")
    print("His body tenses, prepared for violence.")
    print("Yet the old woman shows no fear in return.\n")

    print('"Oh my, still temperamental as ever..."')
    print("She gently nudges the bowl closer.\n")

    print("\nHer hand continues moving toward his neck.\n")

    print("What will the wolf do now?")
    print("-  Attack her (aggression)")
    print("+  Hold back and endure it (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        ending_bad_1()
    else:
        print("\nThe wolf restrains himself.")
        print("The growl fades into a low warning rumble.\n")

        print('The old woman chuckles softly.')
        print('"Badde, you stubborn creature as always!"')

        show_wolf_pet()

        print("\nHer wrinkled hand gently strokes the wolf.\n")

        state["name"] = "Badde"
        act1()


def intro_composure_path():
    print("\nThe wolf remains still.")
    print("He watches the old woman with calm, unreadable eyes.\n")

    print("She sets the bowl before him.")

    print("\nThen she lifts something made of leather.")
    print("A small shining object dangles from it.\n")

    print("What will the wolf do?")
    print("+  Remain calm and allow it (composure)")
    print("0  Startle and jump back (fear)")

    choice = get_choice(["+", "0"])

    if choice == "+":
        print("\nThe wolf shows remarkable composure.")
        print("Proud, quiet, and still.\n")

        print('The old woman smiles warmly.')
        print('"Amable, how long I have not seen you, my friend!"')

        show_wolf_collar()

        print("\nShe finishes placing the collar around his neck.\n")

        state["name"] = "Amable"
        act1()
    else:
        print("\nThe unfamiliar object startles the wolf.")
        print("He quickly jumps back.\n")

        print('The old woman raises her hand gently and speaks in a soothing voice.')
        print('"Ah, Harmless, it is you! Do not be afraid."')
        print('"I will not hurt you."\n')

        print("Her voice is kind.")
        print("Slowly, the wolf calms down.\n")

        print("This time, she simply reaches out with her hand.")
        print("The wolf allows her to touch him.")

        show_wolf_pet()

        print("\nShe softly pets his fur.\n")

        state["name"] = "Harmless"
        act1()
        