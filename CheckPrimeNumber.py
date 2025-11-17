{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "88f25de9-0141-403d-992d-16543462adfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the range (start end):  -10 200\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Give Positive Number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the range (start end):  100 200\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime numbers between 100 and 200 :\n",
      "101\n",
      "103\n",
      "107\n",
      "109\n",
      "113\n",
      "127\n",
      "131\n",
      "137\n",
      "139\n",
      "149\n",
      "151\n",
      "157\n",
      "163\n",
      "167\n",
      "173\n",
      "179\n",
      "181\n",
      "191\n",
      "193\n",
      "197\n",
      "199\n"
     ]
    }
   ],
   "source": [
    "def check_prime_number():  # function to get valid input\n",
    "    while True:  # loop until input is valid\n",
    "        try:\n",
    "            a, b = map(int, input(\"Enter the range (start end): \").split())#Give User input\n",
    "            # check positive\n",
    "            if a > 0 and b > 0:\n",
    "                # swap if needed\n",
    "                if a > b:\n",
    "                    a, b = b, a\n",
    "                return a, b  # return values to use outside function\n",
    "            else:\n",
    "                print(\"Give Positive Number\")\n",
    "        except ValueError:\n",
    "            print(\"Invalid Input. Give Positive Integer Value\")\n",
    "# get cleaned + validated range\n",
    "a, b = check_prime_number()\n",
    "print(\"Prime numbers between\", a, \"and\", b, \":\")\n",
    "# check prime numbers in range\n",
    "for num in range(a, b + 1):\n",
    "    if num < 2:\n",
    "        continue  # skip 0 and 1   \n",
    "    is_prime = True\n",
    "    # check divisors till sqrt(num)\n",
    "    for i in range(2, int(num ** 0.5) + 1):\n",
    "        if num % i == 0:\n",
    "            is_prime = False\n",
    "            break   \n",
    "    if is_prime:\n",
    "        print(num)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d174fcc3-5440-46d4-a7bd-4987868c8e5e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
