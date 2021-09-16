def findDigitalRoot(number):
    return 0 if number < 1 else (
        number % 10 + findDigitalRoot(number // 10)
    )


#test
print(findDigitalRoot(513))
