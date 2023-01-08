class ConsoleColor:

    def __init__(self) -> None:
        pass

    def print(self,text,type,tabs = 0):
    
        # declared color variables
        tab = "    " # 4 spaces
        step = "\033[1m[+]\033[22m "
        backstep = "\033[1m[-]\033[22m "
        success = "\033[32;1m[\u0394]\033[22m "
        error = "\033[31;1m[!]\033[22m "
        reset = "\033[0m"

        if type == "success":
            text = success+text
        if type == "error":
            text = error+text
        if type == "step":
            text = step+text
        if type == "back_step":
            text = backstep+text
        else:
            text = text
        if not tabs == 0:
            text = (tab*tabs) + text
        
        print(text+reset)
