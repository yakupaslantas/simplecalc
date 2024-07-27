safe_words = [".", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "+", "/", "-"]



if __name__ == "__main__":
    illegal_character_dedected = False
    while True:
        illegal_character_dedected = False
        entry = input(" enter some mathematical operation (only + / * - supported) : ")
        for i in entry:
            if illegal_character_dedected == True:
                continue
            if i in safe_words:
                pass
            else:
                illegal_character_dedected = True
                print("Illegal characters!")
        if illegal_character_dedected == True:
            continue
        try:
            print(eval(entry))
        except Exception as e:
            print(f"Error : {e}")

                
            
