import taipan

while True:
    text = input('taipan ~ > ')
    result, error = taipan.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
