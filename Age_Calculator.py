{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bbd31404-de7c-4e3e-9e5c-626030431b68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age in mm/dd/yyyy format 02/25/1991\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your birthdate (European format) is: 25/02/1991\n",
      "Your age is: 34 years\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime#imported datetime module to handle today date, birthdate\n",
    "def age_calculator():#function name age_calculator is defined\n",
    "    while True:#infine loop created which will keep asking the user to enter input untill its true\n",
    "        dob_input=input('Enter your age in mm/dd/yyyy format')#ask the user to enter their age\n",
    "        try: #validate input format\n",
    "            dob=datetime.strptime(dob_input,\"%m/%d/%Y\")#python tries to conver the date in mmddyyyy format\n",
    "            break#if format is correct exit the loop\n",
    "        except ValueError:#if user enter wrong input Python jumps here\n",
    "            print('Invalid Format Please Enter the age in mm/dd/yyyy format')\n",
    "    today = datetime.today()#it get input from laptop\n",
    "    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))#to check whether birthday has passed this year\n",
    "    euro_format = dob.strftime(\"%d/%m/%Y\")#Convert the date format in ddmmyyyy\n",
    "    #Use print statement o display the output\n",
    "    print(f\"Your birthdate (European format) is: {euro_format}\")\n",
    "    print(f\"Your age is: {age} years\")\n",
    "age_calculator()#Calling the function which will take dob as the input\n",
    "            \n",
    "\n",
    "\n",
    "        \n",
    "\n",
    "\n",
    "    \n",
    "        \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eda25be5-5138-4bec-a3e9-264995d61741",
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
