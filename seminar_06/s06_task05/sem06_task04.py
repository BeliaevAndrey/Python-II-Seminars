def function(phrase: str, answers: list[str], attempts: int) -> int:
    print(phrase)
    start = attempts
    while attempts > 0:
        attempts -= 1
        guess = input('Enter your guess: ').lower()
        if guess in answers:
            return start - attempts
    return 0


if __name__ == '__main__':
    ans_list = ['2', '3', '5', '7', '11', '13', ]
    phr = "A prime number"
    print(function(phr, ans_list, 5))
