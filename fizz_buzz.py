def fizz_buzz(n):
    """
    If n is divisible by 3, return 'fizz'
    Else if n is divisible by 5, return 'buzz'
    If n is divisible by both (15), return 'fizz_buzz'
    Else if it is divisible by none, return ''

    >>> fizz_buzz(6)
    'fizz'

    >>> fizz_buzz(20)
    'buzz'

    >>> fizz_buzz(45)
    'fizz_buzz'

    >>> fizz_buzz(8)
    ''
    """
    result = ''
    if 0 == n % 15:
        result = 'fizz_buzz'
    elif 0 == n % 5:
        result = 'buzz'
    elif 0 == n % 3:
        result = 'fizz'
    return result
