import random
import time

# -----------------------------
# Bludgeons & Flagons: Tavern Clash
# -----------------------------
# HOW TO PLAY:
# 1. Enter your character name and role.
# 2. Each round, you draw a card (Attack, Defend, Heal, or Special).
# 3. Roll dice to determine the strength of your action.
# 4. Enemy also draws a card and rolls dice.
# 5. First to reach 0 HP loses. Critical rolls (natural 1 or max) have special effects.
#
# Cards + Dice = chaotic tavern fun!

# Deck of cards (simple list, can expand later)
deck = ["Attack", "Defend", "Heal", "Special"]

def draw_card():
    """Draw a random card from the deck."""
    return random.choice(deck)

def roll_die(sides=6):
    """Roll a die with given number of sides."""
    return random.randint(1, sides)

def print_dramatic_text(text: str, delay=0.05):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    # Character creation
    name = input("Enter your character's name: ")
    role = input("Enter your role (Warrior, Mage, Rogue, etc.): ")
    print_dramatic_text(f"{name} the {role} enters the tavern...")

    # Starting stats
    player_hp = 20
    enemy_hp = 20
    round_num = 1

    # Main game loop
    while player_hp > 0 and enemy_hp > 0:
        print(f"\n--- Round {round_num} ---")
        round_num += 1

        # Player turn
        input("Press Enter to draw your card...")
        player_card = draw_card()
        print(f"You drew: {player_card}")
        player_roll = roll_die(6)
        print(f"You rolled a d6: {player_roll}")

        # Enemy turn
        enemy_card = draw_card()
        enemy_roll = roll_die(6)
        print(f"Enemy drew: {enemy_card}")
        print(f"Enemy rolled a d6: {enemy_roll}")

        # Resolve actions
        if player_card == "Attack":
            damage = player_roll
            if player_roll == 6:  # critical hit
                damage += 3
                print("Critical strike!")
            enemy_hp -= damage
            print(f"You deal {damage} damage! Enemy HP: {enemy_hp}")

        elif player_card == "Defend":
            print("You brace yourself. Reduce enemy damage this round.")
            # Enemy attack reduced later

        elif player_card == "Heal":
            heal = player_roll
            player_hp += heal
            print(f"You heal {heal} HP! Player HP: {player_hp}")

        elif player_card == "Special":
            print("You unleash a chaotic tavern move!")
            damage = roll_die(4) + roll_die(4)
            enemy_hp -= damage
            print(f"Special attack deals {damage} damage! Enemy HP: {enemy_hp}")

        # Enemy action
        if enemy_card == "Attack":
            damage = enemy_roll
            if enemy_roll == 6:
                damage += 3
                print("Enemy lands a critical strike!")
            # If player defended, reduce damage
            if player_card == "Defend":
                damage = max(0, damage - 3)
                print("Your defense reduced the damage!")
            player_hp -= damage
            print(f"Enemy deals {damage} damage! Player HP: {player_hp}")

        elif enemy_card == "Heal":
            heal = enemy_roll
            enemy_hp += heal
            print(f"Enemy heals {heal} HP! Enemy HP: {enemy_hp}")

        elif enemy_card == "Special":
            print("Enemy unleashes a chaotic tavern move!")
            damage = roll_die(4) + roll_die(4)
            player_hp -= damage
            print(f"Special attack deals {damage} damage! Player HP: {player_hp}")

    # End of game
    if player_hp <= 0 and enemy_hp <= 0:
        print_dramatic_text("Both collapse in the tavern... It's a draw!")
    elif player_hp <= 0:
        print_dramatic_text("You fall! The enemy wins the tavern brawl...")
    else:
        print_dramatic_text("Victory! You stand tall in the tavern!")
    