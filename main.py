import os
from createPicture import createPicture

clear = lambda: os.system('cls')
clear()


def main():
    quantity_of_steps = 0
    selected_pattern = ""
    print("""
        I implemented a "Langton's ant" turing machine.
        The result of the work is the display of a picture for the selected ant pattern
        For everything to work, select the pattern according to which the pixels will change, 
        then the options will be presented and the depth of the cycle.
        P.S. To make it more interesting, I added obstacles for the ant.
        [to continue press Enter]
        """)
    
    while True:
        if input() == "":
            clear()
            break
    
    print("""
        Patterns to choose from:
        "0" - write a pattern yourself. 
        "1" - defualt pattern. At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
                               At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
          """)
    
    while True:
        selected_pattern = input()
        if selected_pattern in ["0", "1"]:
            clear()
            break

    print(f"you have chosen a pattern {selected_pattern}, now choose the number of steps for the ant:")
    print("""
        '0' - choose the quantity yourself.
        '1' - 10000
        '2' - 100000
        '3' - 1000000
          """)
    while True:
        quantity_of_steps = input()
        if quantity_of_steps == "0":
            quantity_of_steps = int(input("Enter number: "))
            clear()
            break
        elif quantity_of_steps == "1":
            quantity_of_steps = 10000
            clear()
            break
        elif quantity_of_steps == "2":
            quantity_of_steps = 100000
            clear()
            break
        elif quantity_of_steps == "3":
            quantity_of_steps = 1000000
            clear()
            break
        else:
            continue
    
    if selected_pattern == "1": #defualt
        createPicture(['1', '-1', '1', '1', '1', '1'], quantity_of_steps)
    elif selected_pattern == "0":
        print("""
        Enter a combination of numbers.
        
        At a white square:
        turn 90°:
            "0" - clockwise
            "1" - counter-clockwise
        flip the color of the square:
            "0" - no
            "1" - yes
        move:
            "0" - forward
            "1" - forward 2 step

        At a black square:
        turn 90°:
            "0" - clockwise
            "1" - counter-clockwise
        flip the color of the square:
            "0" - no
            "1" - yes
        move:
            "0" - forward
            "1" - forward 2 step

        
            """)
        pattern = []
        while True:
            combinations = input()
            if len(combinations) == 6:
                
                
                if combinations[0] == "0":
                    CDIRW = "1"
                else:
                    CDIRW = "-1"
                if combinations[3] == "0":
                    CDIRB = "1"
                else:
                    CDIRB = "-1"
                

                if combinations[1] == "0":
                    COLORW = "0"
                else:
                    COLORW = "1"
                if combinations[4] == "0":
                    COLORB = "0"
                else:
                    COLORB = "1"

                
                if combinations[2] == "0":
                    MOVEW = "1"
                elif combinations[2] == "1":
                    MOVEW = "2"


                if combinations[5] == "0":
                    MOVEB = "1"
                elif combinations[5] == "1":
                    MOVEB = "2"

                pattern = [CDIRW, CDIRB, MOVEW, MOVEB, COLORW, COLORB]
                break

        
        createPicture(pattern, quantity_of_steps)
        
    return 1

if __name__ == "__main__":
    main()
