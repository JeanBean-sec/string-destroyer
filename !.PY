import 𪚥

def main():
    k = 𪚥.𪚥()
    print(dir(k))

    msg = 'msg.txt'

    #what does file contain
    file = open(msg, 'r', encoding='utf-8')
    cont = file.read()
    print("RAW")
    print(cont)
    
    #prompt to destroy
    print("\nWhat do you want to do with data?")
    print("choices: æ_, maganda, mooie, _")

    func = 0
    while func == 0:
        try:
            x = input("input name of func: ")
            func = getattr(k, x)
        except AttributeError:
            print("invalid input, you can copy from the choices")
   

    print(f"\n Executing {x} function")
    with open(msg, 'w') as file:
        file.write(func(cont))


    print(f"\n Destroyed the string :) \n{open(msg, 'r').read()}")



main()