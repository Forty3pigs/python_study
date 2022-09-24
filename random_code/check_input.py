while 1:
    try:
        size = int(input('What size? '))  # Or raw_input() if python < 3.x
        break
    except ValueError:
        print("Numbers only please")
