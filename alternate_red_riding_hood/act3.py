from state import state
from utils import get_choice

from endings import ending_bad_8, ending_normal_5, ending_good_1, ending_good_2, ending_good_3, ending_supernatural_1, ending_supernatural_2, ending_supernatural_3

from ascii_red_riding_hood import show_red_riding_hood


def act3():
    print("\nACT III")
    print("Following the path, the wolf sees the true embodiment of a monster before him.")
    print("The beast is clothed entirely in red.")
    print("Muscles bulge beneath the fabric.")
    print("Behind its back is hidden a double-edged curved claw.")
    print("Its eyes are completely white.")
    print("Its face is twisted with madness.")
    print("And from the second hand holding something comes the sharp smell of blood.")
    print("It is a sight that awakens a primal fear.\n")

    show_red_riding_hood()

    trait = state["trait"]

    if trait == "guile":
        act3_guile()
    elif trait == "mercifulness":
        act3_mercifulness()
    elif trait == "despair":
        act3_despair()
    elif trait == "calmness":
        act3_calmness()
    else:
        print("The path forward has not been written for this trait yet.\n")


def act3_guile():
    print("What will the wolf do?")
    print("+  Coldly assess the monster (composure)")
    print("0  Instinctively jump back (fear)")

    choice = get_choice(["+", "0"])

    if choice == "+":
        print("\nLike a true predator, the wolf judges his enemy with bloodthirsty eyes.")
        print("The monster strikes in a flash with its curved claw.")
        print("Again and again, it tears through empty air as the wolf dodges.\n")

        print("Before long, the wolf's thirst for blood pushes him into a counterattack.")
        print("Right after the enemy's swing, he lunges forward, but...\n")

        ending_bad_8()
    else:
        print("\nAt the sight of a stronger predator, the wolf leaps back on instinct.")
        print("The monster's strike cuts through the place where he stood a moment before.")
        print("A blindingly fast series of swings follows.\n")

        print("The wolf retreats without taking his eyes off the danger, backing deeper into the forest.")
        print("Young trees, bushes, and long grass are torn apart around them.\n")

        print("Suddenly, the wolf realizes there is a stone behind him.")
        print("In a fraction of a second, he ducks.")
        print("The double-edged claw whistles above his ears.")
        print("A sharp ring sounds out.\n")

        print("The claw has lodged itself in the stone.")
        print("The monster struggles to pull it free.")
        print("The wolf understands there will never be a better chance.\n")

        print("He attacks and sinks his fangs into the creature's hard neck.")
        print("The enemy's paws clamp around the wolf's throat in return.")
        print("Blood spreads beneath the foe.")
        print("Pain crushes the wolf's neck.")
        print("The world grows dim.\n")

        ending_supernatural_2()


def act3_mercifulness():
    print("What will the wolf do?")
    print("-  Press the fight with confidence (aggression)")
    print("0  Flee from certain death (fear)")

    choice = get_choice(["-", "0"])

    if choice == "-":
        print("\nThe wolf's mind is clear.")
        print("He feels as though he could defeat anyone.\n")

        print("Seconds pass.")
        print("The monster unleashes series after series of attacks.")
        print("The wolf slips away from every one of them.")
        print("The battle drags on.\n")

        print("Unable to catch him, the monster falls to one knee.")
        print("The wolf senses something strange.")
        print("With one last effort, the creature flings dirt toward his eyes.\n")

        print("The wolf jumps aside.")
        print("The double-edged claw flashes past his muzzle.")
        print("The opponent collapses, powerless now, able only to gaze upon him.\n")

        print("The wolf magnificently shakes himself, displaying his fur in all its glory.")
        print("Now he looks down upon the defeated foe from above and proudly departs.\n")

        ending_supernatural_3()
    else:
        print("\nThe creature's face fills the wolf with a sense of unavoidable death.")
        print("He chooses to flee.\n")

        print("At first, the monster pursues him, cutting apart everything in its path.")
        print("But the wolf knows the forest well, and at last he escapes.\n")

        print("Still hiding, he reaches the edge of the woods.")
        print("He decides to leave the forest and walks along a stream.\n")

        ending_normal_5()


def act3_despair():
    print("What will the wolf do?")
    print("-  Gather his strength and growl (aggression)")
    print("+  Sit down and close his eyes (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nGathering all his strength despite his despair, the wolf begins to growl.")
        print("The monster seems to admire his courage.\n")

        print("With one hand, it takes something from the container held in the other and offers it to him.")
        print('"How fearless you are! If that is so, go on, have some!!!"')
        print("Her gentle voice calms the wolf.\n")

        print("He tastes the offering.")
        print("It is half-raw meat, strange and slightly crunchy inside and out.\n")

        ending_good_1()
    else:
        print("\nThe wolf's chest pounds.")
        print("He knows he cannot defeat this opponent.")
        print("He sits on the ground and closes his eyes.\n")

        print("Unaccepted by anyone, he feels a deep sorrow.")
        print("He hears confident steps coming closer.")
        print("His heart begins to hammer wildly.")
        print("He feels the monster's breath.")
        print("Then it wraps around him and squeezes.\n")

        ending_supernatural_1()


def act3_calmness():
    print("What will the wolf do?")
    print("-  Bark sharply in hostility (aggression)")
    print("+  Look straight into the opponent's eyes (composure)")

    choice = get_choice(["-", "+"])

    if choice == "-":
        print("\nDespite the enemy's overwhelming strength, the wolf chooses hostility and lets out a piercing bark.")
        print("The monster looks at him in confusion.\n")

        print("It sets something down with one hand, takes something from inside with the other, and holds it out to him.")
        print('"What a talent!!! You would guard against anyone with impure thoughts! Here, have some!"')
        print("Her confident voice calms the wolf.\n")

        print("He tastes the offering.")
        print("It is half-raw meat, with a strange, slightly crunchy texture inside and out.\n")

        ending_good_2()
    else:
        print("\nThe wolf studies the opponent carefully, then looks directly into its eyes.")
        print("The opponent notices.\n")

        print("With the second hand, it throws something toward him.")
        print("With the first, it gestures for him to look inside.")
        print('"How clever you are! Eat, and I shall make more!!!"')
        print("Her calm voice encourages the wolf.\n")

        print("He tastes the offering.")
        print("It is half-raw meat, strange and slightly crunchy inside and out.\n")

        ending_good_3()