def banner(title, border='*'):
    """Print a banner with a title.

    More precisely, this function should print a rectangle of `border`
    characters with a capitalized `title` message in the center of the
    rectangle with exactly one space of padding on either side based on the
    length of `title`.

    Args:
    title (str): The text to be displayed in the rectangle.
    border (str): The character to use for the rectangle border, defaults
    to ``'*'``.

    Raises:
    ValueError: If ``len(border) != 1``.

    See Also:
    :py:func:`test_invest.TestInvestBanner`
    """
    length = len(title)
    if (len(border) == 1):
        print(border*(length+4))
        print(border + " "+title.upper()+" "+border)
        print(border*(length+4))
    else:
        raise ValueError('test_invest.TestInvestBanner')


# -----------------------------------------------------------#


def balance(prev, c, r):
    """Return a starting balance for a basic investment.

    More precisely, it should compute the starting balance of a basic
    investment account based on the previous year's starting year (`prev`),
    a contribution amount (`c`), and a rate of return (`r`).

    Args:
    prev (float): Previous year's starting balance.
    c (float): The contribution amount.
    r (float): The rate of return.

    Returns:
    A new starting balance.

    Raises:
    ValueError: If ``c < 0``.
    ValueError: If ``not 0 <= r <= 1``.

    Examples:
    >>> from invest import balance
    >>> balance(120.25, 20.0, 0.05)
    147.26250000000002

    >>> from invest import balance
    >>> balance(120.25, 20.0, -0.05)
    Traceback (most recent call last):
    ...
    ValueError: not (0 <= r <= 1)

    See Also:
    :py:func:`test_invest.TestInvestBalance`
    """
    if (c > 0 and 0 <= r <= 1):
        prev = (prev+c) * (1+r)
        return (prev)
    elif (c < 0):
        raise ValueError('amount <= 0')
    elif (r > 1 or r < 0):
        raise ValueError('amount < 1 or amount < 0')

# -----------------------------------------------------------#


def balance_line(amount, amount_width, year):
    """Return a string containing a balance `amount` and a `year`.

    The exact format of the returned string is best explained through examples,
    which are provided in the project description. From a user's perspective,
    the returned string should contain the following elements in a single line
    and in the order described:

    1. ``'$'``;
    2. the `amount` value, adjusted to

       * only include two places after the decimal
       * use at least `amount_width` characters (padded with white space)
       * align to the right when `amount_width` permits;

    3. ``' in year '`` (note the space on either end); then
    4. the `year` value.

    Args:
        amount (float): The account balance.
        amount_width (int): The formatting width for the `amount` value.
        year (int): The number of years since the initial investment.

    Returns:
        A string containing a balance `amount` and a `year`.

    Raises:
        ValueError: If ``amount <= 0``.
        ValueError: If ``amount_width < int(math.log10(amount))+4``.

    See Also:
        :py:func:`test_invest.TestInvestBalanceLine`
    """
    import math
    if (amount <= 0):
        raise ValueError('amount <= 0')
    elif (amount_width < int(math.log10(amount))+4):
        raise ValueError('amount_width < int(math.log10(amount))+4')
    else:
        output = f'${amount:>{amount_width}.2f} in year {year}'
    return(output)

# ------------------------------------------------------------#


def askMany(prompt, func, limit, default):
    """Return user input based on defined function.

    This function will ask for input until no errors
    occur or the user has been asked limit many times.

    If the limit is reached the function will return the
    default value; otherwise the user input should be returned
    after converting it using func.

    Args:
        prompt-- the promt to use when calling input
        func-- a function to convert the input
        limit-- the number of times to ask before returning
        the default value
        default-- a default value to use when there are
        repeated errors

    Returns:
        converted user input if function if no value error
        Invalid input if there is value error
        default if limit is reached
    """
    i = 0
    while i < limit:
        try:
            return func(input(prompt))
        except ValueError:
            print("Invalid input...")
        i += 1
    print(f'Invalid input limit reached: using {default}.')
    return(default)
# ---------------------------------------------------------------------------#


def convert(x):
    """Convert input from user to see if they want to run program again.

    takes input from user and converts to boolean
    only takes values of "y","yes,"n","no"

    args:
    x-- value to be converted

    returns:
    booleans

    raises:
    ValueError if value is not one of the specified values
    """
    if x.lower() in ["yes", "y"]:
        return(True)
    elif x.lower() in ["no", "n"]:
        return(False)
    else:
        raise ValueError
# ---------------------------------------------------------------------------#


def askManyTwo(prompt, func, limit, default):
    """Return user input based on defined function.

    This function will ask for input until no errors
    occur or the user has been asked limit many times.

    If the limit is reached the function will return the
    default value; otherwise the user input should be returned
    after converting it using func.

    Args:
        prompt-- the promt to use when calling input
        func-- a function to convert the input
        limit-- the number of times to ask before returning
        the default value
        default-- a default value to use when there are
        repeated errors

    Returns:
        converted user input if function if no value error
        Invalid input if there is value error
        converted default if limit is reached
    """
    i = 0
    while i < limit:
        try:
            return func(input(prompt))
        except ValueError:
            print("Invalid input...")
        i += 1
    print(f'Invalid input limit reached: using {default}.')
    return(convert(default))

# --------------------------------------------------------------------------- #


def main():
    """Run the program as described in the :ref:`examples` section.

    The :py:func:`invest.main` function is considered the main entry point into
    the program provided by the :py:mod:`invest` module. To run the program
    from the terminal, use this command::

        $ python3 -m invest

    You can also run the program from within the Python interpreter::

        >>> import invest
        >>> invest.main()

    In both cases, the the program starts execution in the
    :py:func:`invest.main` function because the following block is present at
    the bottom of the module::

        if __name__ == "__main__":
            main()

    See Also:
        :py:func:`test_invest.TestInvestMain`

    See Also:
        https://docs.python.org/3/library/__main__.html
    """
    import math
    banner("welcome to invest!", "*")
    print("")
    calcrepeat = True
    while calcrepeat is True:
        targetbalance = askMany("Target balance? ", float, 3, 1000.00)
        prev = askMany("Principal? ", float, 3, 100.00)
        c = askMany("Contribution? ", float, 3, 50.00)
        r = askMany("Rate of return? ", float, 3, 0.05)
        print("")
        banner("calculations", "+")
        year = 0
        if (prev < targetbalance):
            while (prev < targetbalance):
                if year == 0:
                    amount = prev
                else:
                    try:
                        amount = balance(prev, c, r)
                    except ValueError as e:
                        print(f'Error! {e}')
                        break
                amount_width = int(math.log10(targetbalance))+4
                try:
                    print(balance_line(amount, amount_width, year))
                except ValueError as e:
                    print(f'Error! {e}')
                    break
                year += 1
                prev = prev+(amount-prev)
        else:
            print(balance_line(prev, amount_width, year))
        print("")
        calcrepeat = askManyTwo("Calculate another investment? ", convert, 3, "no")
    print("")
    banner("bye!", "+")
