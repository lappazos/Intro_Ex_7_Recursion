##################################################################
# FILE : ex7.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex7 2017-2018
# DESCRIPTION : a number of various functions that are using recursion,
# with the top among them - hanoi!!!!!! how fun to play with
##################################################################


def print_to_n(n):
    """
    prints int 1 to n by order
    :param n: integer
    :return: None
    """
    n = int(n)
    if n > 0:
        #recursion base case
        print_to_n(n - 1)
        print(n)


def print_reversed(n):
    """
    prints int n to 1 by declining order
    :param n: integer
    :return: None
    """
    n = int(n)
    if n > 0:
        #recursion base case
        print(n)
        print_reversed(n - 1)


def is_prime(n):
    """
    Prime check
    :param n: integer
    :return: True if prime, False if not
    """
    n = int(n)
    if n < 2:
        # prime must be 2 and above
        return False
    if n == 2:
        # because later i False all of the Even nums
        return True
    if n % 2 == 0:
        return False
    temp = 1
    if has_divisor_smaller_than(n, int(n ** 0.5), temp):
        # if a number divides into another number smaller then him - not prime
        # we only check up until square roots to save time - its ok
        # mathematically
        return False
    else:
        return True


def has_divisor_smaller_than(n, i, temp):
    """
    helper func - checks whether or not a number has divisors smaller than x
    :param n: an integer we would like to check his divisors
    :param i: the limit to our divisors check
    :param temp: for internal use - determine the progress of our recursion
    :return: True if indeed has divisors
    """
    temp += 1
    # we check the next number every time
    if temp - 1 == i:
        # recursion base case
        return False
    elif n % temp == 0:
        return True
    else:
        # if the number division to temp gives us a remainder different from
        #  0, we continue our check to  the next num
        return has_divisor_smaller_than(n, i, temp)


def divisors(n):
    """
    gives us all of the numbers that divides n without a remainder
    :param n: an integer
    :return: divisors list
    """
    n = int(n)
    temp = 0
    temp_list = []
    # we use a different function
    return (divisors_append(n, temp, temp_list))


def divisors_append(n, temp, temp_list):
    """
    helper func to give me the divisors of a number
    :param n: the number we check
    :param temp: determines the progress of our func
    :param temp_list: the temp results for every recurson of the function
    :return: divisors list
    """
    if n == 0:
        # edge case
        return temp_list
    temp += 1
    # progress indicator
    if (temp == n) or (temp == -n):
        # recursion base case
        temp_list.append(temp)
        return temp_list
    if n % temp == 0:
        temp_list.append(temp)
        # if the number division to temp gives us a remainder 0,
        # we append him as a divisor & continue our check to  the next num
    divisors_append(n, temp, temp_list)
    return temp_list


def fact(n):
    """
    factorial math operator
    :param n: integer
    :return: n!
    """
    if n < 2:
        return 1
    return n * fact(n - 1)


def exp_n_x(n, x):
    """
    epx(x) operator
    :param n: precision rate for our function - as higher, results more
    accurate
    :param x: the number we would like to exp
    :return: exp(x)
    """
    i = -1
    return exp(n, x, i)


def exp(n, x, i):
    """
    helper func to exp
    :param n: accuracy integer
    :param x: the number we would like to operate on
    :param i: progress meter
    :return: exp(x)
    """
    n = int(n)
    i += 1
    result = (x ** i) / fact(i)
    # the calculation of exp
    if i == n:
        # recursion base case
        return result
    else:
        result = result + exp(n, x, i)
        # the summing action - the recursion
        return result


def play_hanoi(hanoi, n, src, dest, temp):
    """
    determines the logic to Hanoi graphic game
    :param hanoi: internal use
    :param n: number of discs
    :param src: origin tower
    :param dest: destination tower
    :param temp: temp station tower
    :return: None
    """
    if n <= 0:
        # edge cases
        return
    if n == 1:
        # base case of recursion
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        # move all the discs but 1 to temp tower, as the previous attempt
        hanoi.move(src, dest)
        # move bottom disc to dest tower
        play_hanoi(hanoi, n - 1, temp, dest, src)
        # moves the rest of discs to dest tower, as the previous attempt


def print_binary_sequences(n):
    """
    prints binary options in length n
    :param n: requested length of binary num
    :return: None
    """
    for item in print_sequences_sub([0, 1], int(n), 0):
        # use of helper function
        if len(item) == n:
            # prints only the correct options out of the list
            print(item)


def print_sequences_sub(char_list, n, mode):
    """
    helper func to all binary & sequence functions
    :param char_list: list of requested chars to operate on
    :param n: requested length
    :param mode: 0 or 1 - with or without repetition
    :return: list of options
    """
    if n == 0:
        base = [""]
        # recursion base camp
        return base
    else:
        combinations = print_sequences_sub(char_list, n - 1, mode)
        # the recursion stage
        # here we add to every item in the list (length n-1) the different
        # options according our char_list
        for comb in combinations:
            if len(comb) == n - 1:
                for char in char_list:
                    # 2 modes - with or without repeat
                    if mode is 0:
                        combinations.append(comb + str(char))
                    elif mode is 1:
                        if char not in comb:
                            combinations.append(comb + str(char))
        return combinations


def print_sequences(char_list, n):
    """
    prints the different sequences i can make out of X different chars
    :param char_list: list of different strings
    :param n: requested length of word
    :return: None
    """
    for item in print_sequences_sub(char_list, int(n), 0):
        # use of helper function
        if len(item) == n:
            # prints only the correct options out of the list
            print(item)


def print_no_repetition_sequences(char_list, n):
    """
    prints the different sequences i can make out of X different chars,
    without chars repeat
    :param char_list: list of different strings
    :param n: requested length of word
    :return: None
    """
    for item in print_sequences_sub(char_list, int(n), 1):
        # use of helper function
        if len(item) == n:
            # prints only the correct options out of the list
            print(item)


def no_repetition_sequences_list(char_list, n):
    """
    gives me a list with the different sequences i can make out of X different
    chars,
    without chars repeat
    :param char_list: list of different strings
    :param n: requested length of word
    :return: sequences list
    """
    lst = []
    for item in print_sequences_sub(char_list, int(n), 1):
        # use of helper function
        if len(item) == n:
            # new list with the correct options
            lst.append(item)
    return lst