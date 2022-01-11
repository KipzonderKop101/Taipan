import taipan

while True:
    text = input('taipan ~ > ')
    result, error = taipan.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)
