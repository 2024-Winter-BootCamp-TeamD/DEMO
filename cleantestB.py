def handle_input(text, number):
    result = []
    for i in range(number):
        result.append(text + str(i))
    print("Result:", result)

    if len(result) > 10:
        print("Too many results!")
    return result