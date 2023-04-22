#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:36:55 2022

@author: v-cattoni

Sketch: The chinese remainder theorem can be used to generate all the twin primes, but it also
generates some 'false' twin primes. The maximum number of 'false' twin primes is easy to quantify. 
I would like to show that the number of twin primes generated by the chinese remainder theorem is 
greater than the maximum number of 'false' twin primes. 


In this code: I use the chinese remainder theorem to find the potential twin primes that are bigger than n, 
but smaller than primorial(n). The problem is that this technique will not filer out numbers whose 
prime factors are all > n. 

I have a separate code (potential_problems_chinese_remainder.py) that calculates the maximum number 
of elements that will fall through this filter. 

I would like to write an analytic sequence to represent each of these and take the limit as n -> inf. 
"""

#%%
from math import prod
import numpy as np
import itertools


# generates a list of prime numbers smaller than or equal to pn
# prime_numbers(pn) = [p1, p2, .... , pn]
def prime_numbers(pn):
    primes = []
    for i in range(2, pn + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


# Generates conditions for chinese remainder theorem
# Returns a list of possible mod values for each prime less than or equal to pn
# which_mods(p1, p2, ..., pn) =
# [[1], [2], [1, 2, 4], [1, 2, 3, 4, 6], ... , [1, 2, ..., pn - 3, pn - 1]]
def which_mods(prime_list):
    final_mod_list = []
    for i in prime_list:
        temp_list = []
        for j in range(1, i - 2):
            temp_list.append(j)
        temp_list.append(i - 1)
        final_mod_list.append(temp_list)
    return final_mod_list


# generates inverse of 'n' under multiplication modulo 'mod'
def inverse_modulo(n, mod):
    for i in range(1, mod + 1):
        if (n * i) % mod == 1:
            return i


# performs chinese remainder theorem given possible mod values and corresponding primes.
def chinese_remainder(mods, prime_list):
    n = len(mods)
    product_primes = prod(prime_list)
    initial_prods = []
    for i in prime_list:
        initial_prods.append(int((product_primes / i) % i))
    for j in range(0, n):
        if initial_prods[j] != 1:
            initial_prods[j] = inverse_modulo(initial_prods[j], prime_list[j])
    c_r = 0
    for k in range(0, n):
        c_r += int(mods[k] * product_primes / prime_list[k] * initial_prods[k])
    return c_r % product_primes


def main(prime):
    prime_list = prime_numbers(prime)
    n = len(prime_list)
    mods = which_mods(prime_list)
    product_primes = prod(prime_list)
    num_comb = 1

    for i in mods:
        num_comb *= len(i)

    mat = [p for p in itertools.product(*mods)]

    potential_twins = []
    for i in mat:
        potential_twins.append(chinese_remainder(i, prime_list))

    big_primes_list = prime_numbers(2 * product_primes)

    true_twins = []
    for i in potential_twins:
        if i in big_primes_list and (i + 2) in big_primes_list:
            true_twins.append(i)

    percentage_twins = (len(true_twins)) / len(mat)

    false_twins = []
    for prime in potential_twins:
        if prime not in true_twins:
            false_twins.append(prime)

    print("")
    print(
        "Number of 'potential' twin primes generated by chinese remainder theorem between",
        max(prime_list),
        "and",
        product_primes,
        "= ",
        len(mat),
    )
    print("")
    print(
        "Number of 'true' twin primes between",
        max(prime_list),
        "and",
        product_primes,
        "= ",
        len(true_twins),
    )
    print("")
    print(
        "Number of 'false' twin primes between",
        max(prime_list),
        "and",
        product_primes,
        "= ",
        len(mat) - len(true_twins),
    )
    print("")
    print(
        "Percentage of 'potential' twin primes that are 'true' twin primes =",
        percentage_twins,
    )
    print("")
    print("The 'potential' twin primes are:")
    print("")
    print(potential_twins)
    print("")
    print("The 'true' twin primes are:")
    print("")
    print(true_twins)
    print("")
    print("The 'false' twin primes are:")
    print("")
    print(false_twins)
    print("")

<<<<<<< HEAD
main(11)



# %%
=======
    return


main(13)
>>>>>>> fd3b5bfbb1e67c195b4efa2e6c77ee00ac39d513
