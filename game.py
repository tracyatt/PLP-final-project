import random

class LudoGame:
    def __init__(self):
        self.dice_face = {
            1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
        }

        self.players = {1: {"P1": 0, "P2": 0, "P3": 0, "P4": 0}, 2: {"P1": 0, "P2": 0, "P3": 0, "P4": 0}}
        self.first_six = {1: True, 2: True}
        self.current_player = random.choice([1, 2])
    
    #This function prints the face of the
    def print_dice(self, dice_value):
        for line in self.dice_face[dice_value]:
            print(line)
    
    #This function helps you choose which piece to initialized
    def start_piece(self, player):
        while True:
            pawn_to_initialize = input(f"Player {player}, select a pawn to initialize (P1, P2, P3, or P4):\n").upper()
            if pawn_to_initialize in self.players[player]:
                if self.players[player][pawn_to_initialize] == 0:
                    self.players[player][pawn_to_initialize] = 1
                    print(f"Player {player} has initialized pawn {pawn_to_initialize}.")
                    break
                else:
                    print("Piece already in play. Select a pawn not initialized.")
            else:
                print("Invalid selection. Choose an available pawn.")

    #this function checks whether a piece is already initialized or not yet initialized.
    def update_or_initialize_pawn(self, player, dice_value):                                             
        initialized_pawns = [piece for piece, position in self.players[player].items() if 1 <= position < 57] 
        uninitialized_pawns = [pawn for pawn, position in self.players[player].items() if position == 0]

        if dice_value == 6:
            #checks if there are existing pawns or uninitialized pawns
            if initialized_pawns or uninitialized_pawns:
                #loops until a valid choice is made
                while True:
                    #ask the use to enter 'A' to update an existing pawn or 'S' to initialize a new one
                    choice = input(f"Player {player}, you rolled a six! Update an existing pawn (A) or initialize a new one (S)?\n").upper()
                    
                    #updates an existing pawn if 'A' is chosen and there are initialized pawns 
                    if choice == 'A' and initialized_pawns:
                        pawn_to_move = self.choose_pawn(player, initialized_pawns)
                        self.move_pawn(player, pawn_to_move, dice_value)
                        break
                    
                    #initialized a new pawn if 'S' is chosen and there are uninitialized pawns
                    elif choice == 'S' and uninitialized_pawns:
                        self.start_piece(player)
                        break
                    
                    #prompts the user to enter 'A' or 'S' if wrong letter is
                    else:
                        print("Invalid choice. Please enter 'A' to update an existing pawn or 'S' to initialize a new one.")
            else:
                print(f"No valid moves for Player {player}. Initializing a new piece.")
                self.start_piece(player)
        else:
            if initialized_pawns:
                pawn_to_move = self.choose_pawn(player, initialized_pawns)
                self.move_pawn(player, pawn_to_move, dice_value)
            else:
                print(f"No valid moves for Player {player}. Moving to the next player.")

    def choose_pawn(self, player, available_pawns):
        while True:
            pawn_to_move = input(f"Player {player}, which pawn would you like to move ({', '.join(available_pawns)})?\n").upper()
            if pawn_to_move in available_pawns:
                return pawn_to_move
            else:
                print(f"Invalid selection. Choose a pawn in play.")
    #this function ensures the movement of the pawns
    def move_pawn(self, player, pawn, dice_value):
        #this updates the position of the pawn 
        new_position = self.players[player][pawn] + dice_value
        if new_position <= 57:
            self.players[player][pawn] = new_position
            print(f"Player {player} moves pawn {pawn} to position {new_position}.")
            
        else:
            print("Invalid move. Pawn cannot exceed position 57.")

    def play_game(self):
        print("Welcome to GROUP 5 Ludo Game Version 2 :(")

        while True:
            dice_value = random.randint(1, 6)
            
            #if current player is 1 type R1 to play
            if self.current_player == 1:
                player_input = input(f"Player {self.current_player}, press 'R1' to roll the dice...").upper()
                #if key entered is not equal to R1 yell at the user and ask him to enter the right thing
                if player_input != "R1":
                    print("Invalid input. Enter 'R1' to roll the dice.")
                    continue 
            else:
                player_input = input(f"Player {self.current_player}, press 'R2' to roll the dice...").upper()
                #if key entered is not equal to R2 yell at the user and ask him to enter the right thing
                if player_input != "R2":
                    print("Invalid input. Enter 'R2' to roll the dice.")
                    continue
                
            
            #dice_value = random.randint(1, 6)

            print(f"Player {self.current_player} got a {dice_value}")
            self.print_dice(dice_value)
            print("\n")

            if dice_value == 6 and self.first_six[self.current_player]:
                self.update_or_initialize_pawn(self.current_player, dice_value)
                self.first_six[self.current_player] = False
                #checks if a pawn is already initialized
            elif any(pos > 0 for pos in self.players[self.current_player].values()):
                self.update_or_initialize_pawn(self.current_player, dice_value)

            self.print_board()
            #checks if the total movement by a pawn is met
            if all(position == 57 for position in self.players[self.current_player].values()):
                print(f"Player {self.current_player} wins the Game!! Game Over.")
                break

            if dice_value != 6:
                self.switch_player()

    def switch_player(self):
        self.current_player = 3 - self.current_player #Switch player function
        return self.current_player
    def print_board(self):
        print("Board Status:")
        for player, pawns in self.players.items():
            print(f"Player {player}: Positions {pawns}")

if __name__ == "__main__":
    ludo_game = LudoGame()
    ludo_game.play_game()
