from state import state
from act3 import act3
from endings import ending_bad_4, ending_bad_5, ending_bad_6, ending_bad_7, ending_normal_3, ending_normal_4
from utils import get_choice

from ascii_hunter import show_hunter


def act2():
    print("\nACT II")
    print("Outside, the wolf sees a grim, bear-like creature before him.")
    print("Its frame is broad and heavy, yet there is something human in the way it stands.")
    print("In its grasp gleams a long, sharp claw.\n")

    show_hunter()

    trait = state["trait"]

    if trait == "savage":
        act2_savage()
    elif trait == "condescension":
        act2_condescension()
    elif trait == "fright":
        act2_fright()
    elif trait == "mistrust":
        act2_mistrust()
    elif trait == "caution":
        act2_caution()
    else:
        print("The path ahead has not been written for this trait yet.\n")
        act3()


def act2_savage():
    print("What will the wolf do?")
    print("-  Charge mindlessly at the enemy (aggression)")
    print("+  Advance with cold precision (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nAt the sight of the wolf, the opponent freezes.")
        print("A faint trembling spreads through its body.")
        print("Like a mad beast, the wolf lunges forward without thought.\n")

        print("The creature answers with a sweeping strike of its long sharp claw.")
        print("The blow throws the wolf back and tears a deep wound into his body.")
        print("Breath leaves him. His mind begins to dim.\n")

        print("Still, he throws himself into another attack.")
        print("This time he is met with a crushing kick.\n")

        ending_bad_7()
    else:
        print("\nThe wolf keeps the cold composure of a true predator.")
        print("He moves forward slowly, almost mockingly.\n")

        print("The opponent rushes in with the strike the wolf was waiting for.")
        print("He dodges and sinks his jaws into its arm.")
        print("The long claw tears free from it.\n")

        print("With a swift motion, the wolf rakes above its eye and leaps away.")
        print("The creature lashes out wildly, but the wolf evades and answers wound for wound.")
        print("Bleeding heavily, covered in bites and torn skin, the foe finally drops to its knees.\n")

        print("The wolf ends the battle by crushing its throat and leaves the corpse behind, drenched in blood, following the path ahead.\n")

        state["trait"] = "guile"
        act3()


def act2_condescension():
    print("What will the wolf do?")
    print("-  Pretend indifference, then strike (aggression)")
    print("+  Walk closer and sit before him (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nThe wolf acts as if the human is beneath his interest and walks toward him at an angle.")
        print("As expected, the creature swings sharply.\n")

        print("The wolf slips aside and bites into its arm.")
        print("The long sharp claw tears away from the creature's hand.")
        print("At once, the wolf slashes deeply above its eye with his paw.\n")

        print("Blood blinds the creature. Its other hand fails to find its mark.")
        print("In frantic desperation, it flails in every direction and falls to the ground.")
        print("The wolf leaps onto its chest and growls with a bloodstained muzzle.\n")

        print("Accepting death, the creature stares back at him.")
        print("Drool drips onto its face.")
        print("The wolf spares it mercifully and departs along the path.\n")

        state["trait"] = "mercifulness"
        act3()
    else:
        print("\nThe wolf bravely walks closer and sits.")
        print("The creature approaches with its long sharp claw raised.")
        print("It looks at the wolf's face and grimaces.\n")

        print("After a single blink, the wolf sees his own body from the outside.\n")

        ending_bad_6()


def act2_fright():
    print("\nFear makes the wolf clumsy.")
    print("As he stumbles, the passage behind him opens fully, revealing the old woman lying in a pool of blood.\n")

    print("At the sight of the creature's reaction, the wolf bolts.")
    print("He runs through the thicket for what feels like forever.\n")

    print("Suddenly, something with razor-sharp teeth clamps down on his leg.")
    print("A cry bursts from him.")
    print("Not far away, heavy footsteps begin to approach.\n")

    print("What will the wolf do?")
    print("+  Submit completely to fate (composure)")
    print("0  Bite off his own leg and flee (fear)")

    choice = get_choice(["+", "0"])

    if choice == "+":
        print("\nThe wolf does nothing.")
        print("He abandons himself to fate.\n")

        print("From the bushes emerges the same creature as before.")
        print("It comes closer.\n")

        ending_bad_5()
    else:
        print("\nFilled with despair and terror, the wolf tears off his own trapped leg.")
        print("Before the unknown beast can find him, he limps away into the wild.\n")

        ending_normal_4()


def act2_mistrust():
    print("What will the wolf do?")
    print("-  Growl and act first (aggression)")
    print("+  Trust him despite it all (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nThe wolf growls at him, trusting nothing.")
        print("The creature swings its long sharp claw and misses, its gaze caught by something else.\n")

        print("The wolf slips aside and repeats what he once did with the fang.")
        print("He goes under the strike, bites lightly, snatches the claw free, and flings it aside with a jerk of his head.\n")

        print("Leaving the stunned creature behind, he walks quickly down the path.\n")

        state["trait"] = "despair"
        act3()
    else:
        print("\nDespite his mistrust, the wolf chooses to trust him.")
        print("He steps forward a little and sits before the creature.\n")

        print("With the long sharp claw raised, the creature approaches.")
        print("Then it lowers the weapon, staring at the shiny trinket on the wolf's neck.")
        print("With a gesture, it signals that the wolf may go on his way.\n")

        state["trait"] = "calmness"
        act3()


def act2_caution():
    print("\nAt the mere sight of the creature, the wolf runs.")
    print("He crashes through the thicket in terror for a long time.\n")

    print("Suddenly, something with razor-sharp teeth closes on his leg.")
    print("He lets out a loud cry and can no longer go on.")
    print("Unable to move, he begins his mournful song.\n")

    print("The creature keeps coming closer.")
    print("When it emerges from the bushes, its long sharp claw is already raised above the wolf's head.")
    print("Then it stops abruptly after seeing the shiny trinket on the wolf's neck.")
    print("Calmly, the jaws gripping the wolf's leg release.\n")

    print("What will the wolf do?")
    print("+  Endure the pain and leave calmly (composure)")
    print("0  Flee again in panic (fear)")

    choice = get_choice(["+", "0"])

    if choice == "+":
        print("\nThe wolf forces himself onward.")
        print("He numbs the pain and leaves the grim creature behind with quiet courage.\n")

        print("Further ahead in the forest, he finds a shelter that distantly reminds him of what he recently lost.\n")

        ending_normal_3()
    else:
        print("\nFreed from the jaws, the wolf runs even faster through unbearable pain.")
        print("The pain and confusion deepen his fear until thought itself breaks apart.\n")

        print("He stumbles and begins to fall.\n")

        ending_bad_4()
