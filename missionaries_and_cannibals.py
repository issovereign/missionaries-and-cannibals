def print_story_and_rules():
    story = """
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
WELCOME TO THE MISSIONARIES AND CANNIBALS!

Story Beginning:

In ancient times, a vast river divided a mysterious jungle into two. 
On one side of the river lived a group of brave missionaries, eager to spread the seeds of peace and wisdom; 
on the other side was the territory of cannibals, who were extremely hostile to any invasion of their lands.

One day, due to a sudden flood, 
both the missionaries and the cannibals were forced to flee their homes and take refuge on a piece of land untouched by the floodwaters. 
However, this land soon became insufficient for everyone's survival, as food and resources became scarce. 
To survive, they had to cross the dangerous river to reach the fertile lands on the other side.

The missionaries knew that the distrust and hostility between them and the cannibals could erupt into tragedy during this journey. 
Therefore, they devised a plan using the only small boat available, ensuring that at any time during the crossing, 
the number of missionaries left on either side of the river would not be less than that of the cannibals, to avoid being attacked.

This was not only a challenge for survival but also a test of wisdom and trust. 
The missionaries and cannibals had to set aside their prejudices and work together to safely reach the other side. 
This was an unprecedented journey, with their fates and future hanging in the balance.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    rules = """
Game Explanation:

In this game, the players are tasked with moving a group of missionaries (M) and cannibals (C) from the right bank of a river to the left bank, 
using a small boat that can carry at most two people at a time. 
The boat is represented as [  ], and initially, all characters are on the right bank.

The rules are as follows:
- The boat can carry one or two characters (missionaries or cannibals) at a time.
- The game is won when all missionaries and cannibals have been safely transported to the left bank of the river.
- At no point in the game may the cannibals outnumber the missionaries on either bank of the river, 
  as this would lead to the missionaries being eaten, and the game would be lost. 
  In the game's display, missionaries that have been eaten will be shown as 'W' instead of 'M'.
- The boat needs at least one character aboard to cross the river.

The challenge requires strategic planning and careful consideration of each move to ensure the safety of all missionaries while successfully completing the crossing. 
Can you navigate this perilous journey and bring everyone safely to the other side?

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    print(story)
    print(rules)

def print_state(m_left, c_left, m_right, c_right, boat):
    left_side = 'M' * m_left + 'C' * c_left
    right_side = 'M' * m_right + 'C' * c_right
    river = '[ ]~~~~~' if boat == 'left' else '~~~~~[ ]'
    print(f"\n{left_side} |~{river}~| {right_side}\n")

def get_valid_input():
    while True:
        try:
            user_input = input("Enter number of missionaries and cannibals to move, separated by a space (e.g., '1 1'): ")
            input_numbers = [int(i) for i in user_input.split()]
            
            if len(input_numbers) != 2:
                raise ValueError("Please enter exactly two numbers.")
            
            m_to_move, c_to_move = input_numbers
                        
            return m_to_move, c_to_move
        
        except ValueError as e:
            print(f"Invalid input")

def get_input(m_left, c_left, m_right, c_right, boat):
    while True:
        m_to_move, c_to_move = get_valid_input()
        if 0 <= m_to_move <= 2 and 0 <= c_to_move <= 2 and m_to_move + c_to_move <= 2:
            if boat == 'right' and m_to_move <= m_right and c_to_move <= c_right:
                return m_to_move, c_to_move
            elif boat == 'left' and m_to_move <= m_left and c_to_move <= c_left:
                return m_to_move, c_to_move
        print("Invalid move. Please try again.")


def move(m_to_move, c_to_move, m_left, c_left, m_right, c_right, boat):
    if boat == 'right':
        m_right -= m_to_move
        c_right -= c_to_move
        m_left += m_to_move
        c_left += c_to_move
        boat = 'left'
    else:
        m_left -= m_to_move
        c_left -= c_to_move
        m_right += m_to_move
        c_right += c_to_move
        boat = 'right'
    return m_left, c_left, m_right, c_right, boat

def check_game_situation(m_left, c_left, m_right, c_right):
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return 1, 'left' if m_left < c_left else 'right'
    if m_left == 3 and c_left == 3:
        return 2, None
    return 0, None

# turn the Ms in failed side into Ws, which means these guys are eaten.
def print_failure_state(m_left, c_left, m_right, c_right, failed_side):
    if failed_side == 'left':
        print(f"\n{'W' * m_left}{'C' * c_left} |~~~~~~~~~~| {'M' * m_right}{'C' * c_right}\n")
    else:
        print(f"\n{'M' * m_left}{'C' * c_left} |~~~~~~~~~~| {'W' * m_right}{'C' * c_right}\n")

def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        print_story_and_rules()

        m_left, c_left = 0, 0
        m_right, c_right = 3, 3
        boat = 'right'
        game_situation = ["", "Game Over: Cannibals ate the missionaries.", "Congratulations, You Win!"]
        mode = 0

        while mode == 0:
            print_state(m_left, c_left, m_right, c_right, boat)
            m_to_move, c_to_move = get_input(m_left, c_left, m_right, c_right, boat)
            m_left, c_left, m_right, c_right, boat = move(m_to_move, c_to_move, m_left, c_left, m_right, c_right, boat)
            mode, failed_side = check_game_situation(m_left, c_left, m_right, c_right)
            if mode == 1:
                print_state(m_left, c_left, m_right, c_right, boat)
                print_failure_state(m_left, c_left, m_right, c_right, failed_side)
                print(game_situation[mode])
            
            elif mode == 2:
                print_state(m_left, c_left, m_right, c_right, boat)
                print(game_situation[mode])

        play_again = input("\nDo you want to play again? (y/n): ")

if __name__ == "__main__":
    main()
