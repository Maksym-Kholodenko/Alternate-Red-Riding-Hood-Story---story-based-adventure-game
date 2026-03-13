from state import state
from act2 import act2
from endings import ending_bad_2, ending_bad_3, ending_normal_2
from utils import get_choice

from ascii_hut_inside import show_hut_inside
from ascii_granny_with_knife import show_granny_with_knife
from ascii_bloody_token import show_bloody_token
from ascii_broken_heart import show_broken_heart
from ascii_watchful_wolf import show_watchful_wolf


def act1():
    print("\nACT I")
    print("A few days have already passed.")
    print("The wolf now lives with the old woman and sleeps inside the warm hut.")
    print("During the day, he goes outside and watches her gather branches and move about the yard.")
    print("The strange peace does not feel natural, yet it has become familiar.\n")

    show_hut_inside()

    print("\nOne morning, the wolf wakes and sees the old woman rushing toward him.")
    print("Ahead of her gleams a large shining fang.")
    print("As she stumbles forward, she begins to fall.\n")

    show_granny_with_knife()

    if state["name"] == "Badde":
        act1_badde()
    elif state["name"] == "Amable":
        act1_amable()
    elif state["name"] == "Harmless":
        act1_harmless()


def act1_badde():
    print("What will the wolf do?")
    print("-  React with anger and strike first (aggression)")
    print("0  Leap away in fear (fear)")

    choice = get_choice(["-", "0"])

    if choice == "-":
        print("\nAnger and wounded pride surge through the wolf.")
        print("By reflex, he moves around the fang and bites into her arm.")
        print("The shining fang flies from her grasp.")
        print("The old woman falls and lies unconscious on the floor.\n")

        print("What will the wolf do now?")
        print("-  Give in to rage (aggression)")
        print("+  Spare her and leave (composure)")

        subchoice = get_choice(["-", "+"])

        if subchoice == "-":
            print("\nIn mindless fury, the wolf attacks.")
            print("He tears into her until she lies dead.")
            print("With blood on his mouth and paws, he leaves the house behind.\n")

            state["trait"] = "savage"
            act2()
        else:
            print("\nBy the right of the stronger creature, the wolf turns away.")
            print("He leaves the hut with only a little blood on his muzzle.\n")

            state["trait"] = "condescension"
            act2()
    else:
        print("\nFear grips the wolf.")
        print("He springs back toward the door.")
        print("In that instant, the old woman falls onto the shining fang herself.")
        print("It drives into her stomach, and blood begins to spread.\n")

        print("At the sight of this, the wolf abandons the house and flees.\n")

        state["trait"] = "fright"
        act2()


def act1_amable():
    print("What will the wolf do?")
    print("-  Lunge toward the threat (aggression)")
    print("+  Remain where he is and trust her (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nConfusion flashes through the wolf.")
        print("Instinct drives him forward.")
        print("He catches the side of the fang with his jaws and wrenches it free from her grasp.")
        print("The old woman continues falling and lands hard, unconscious.\n")

        print("What will the wolf do now?")
        print("+  Leave warily (composure)")
        print("0  Leave in fearful caution (fear)")

        subchoice = get_choice(["+", "0"])

        if subchoice == "+":
            print("\nThe wolf leaves the hut slowly and watchfully.")
            print("He does not understand the violence of the first member of his pack.\n")

            state["trait"] = "mistrust"
            act2()
        else:
            print("\nThe wolf survived, yet it feels like defeat.")
            print("His own lack of caution brought him close to death.")
            print("Fear follows him as he leaves the hut behind.\n")

            state["trait"] = "caution"
            act2()
    else:
        print("\nThe wolf stays where he is, trusting his mistress.")
        print("But she keeps stumbling forward.")
        print("She falls onto him, and the shining fang pierces his neck.\n")

        print("He collapses onto his side, unable to resist.")

        print("\nBefore his eyes close, he hears sorrowful crying.")
        print("A bloodstained shiny trinket lies before him.\n")

        ending_bad_2()


def act1_harmless():
    print("What will the wolf do?")
    print("+  Stay and trust her despite his fear (composure)")
    print("0  Panic and bark, then flee (fear)")

    choice = get_choice(["+", "0"])

    if choice == "+":
        print("\nThe wolf forces himself to trust her.")
        print("He remains where he is, trying to overcome his fear of this strange being.")
        print("But she continues to stumble forward.")
        print("She falls onto him, and the fang pierces his neck.\n")

        print("He collapses onto his side, powerless.")
        print("Before darkness takes him, he hears her grief-stricken crying.\n")

        ending_bad_3()
    else:
        print("\nThe sheer size of the fang overwhelms him with fear.")
        print("In panic, he lets out a bark.")
        print("The fang slips free from her grasp, but she keeps falling and crashes to the floor unconscious.\n")

        print("The wolf does not wait.")
        print("He bolts from the house and races back into the forest, seeing no one and nothing in his path.\n")

        ending_normal_2()
        