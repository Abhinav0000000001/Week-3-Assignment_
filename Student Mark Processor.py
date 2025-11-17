{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "564e0f6e-7212-4afb-b2b2-e0fc7d941605",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Rules defined to calcuating Grades\n",
    "def assign_grade(mark):\n",
    "    if mark >= 90:\n",
    "        return \"A\"\n",
    "    elif mark >= 80:\n",
    "        return \"B\"\n",
    "    elif mark >= 70:\n",
    "        return \"C\"\n",
    "    elif mark >= 60:\n",
    "        return \"D\"\n",
    "    else:\n",
    "        return \"F\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "34c19db9-8649-45de-b0c3-a28608e2a314",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Count  Percentage\n",
      "Grade                   \n",
      "B          3        60.0\n",
      "D          1        20.0\n",
      "F          1        20.0\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Registration_Number</th>\n",
       "      <th>Exam_Mark</th>\n",
       "      <th>Coursework_Mark</th>\n",
       "      <th>Overall_Marks</th>\n",
       "      <th>Grade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>REG001</td>\n",
       "      <td>78</td>\n",
       "      <td>85</td>\n",
       "      <td>80.1</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>REG002</td>\n",
       "      <td>65</td>\n",
       "      <td>72</td>\n",
       "      <td>67.1</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>REG003</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>89.4</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>REG004</td>\n",
       "      <td>55</td>\n",
       "      <td>60</td>\n",
       "      <td>56.5</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>REG005</td>\n",
       "      <td>82</td>\n",
       "      <td>79</td>\n",
       "      <td>81.1</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Registration_Number  Exam_Mark  Coursework_Mark  Overall_Marks Grade\n",
       "0              REG001         78               85           80.1     B\n",
       "1              REG002         65               72           67.1     D\n",
       "2              REG003         90               88           89.4     B\n",
       "3              REG004         55               60           56.5     F\n",
       "4              REG005         82               79           81.1     B"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd#pandas library imported for data analysis\n",
    "df=pd.read_excel(r'D:\\Data_Science\\student_marks.xlsx')#Excel file is read\n",
    "df[\"Overall_Marks\"] = df[\"Exam_Mark\"] * 0.7 + df[\"Coursework_Mark\"] * 0.3#70% Exam Marks and 30% Course Marks\n",
    "df[\"Grade\"] = df[\"Overall_Marks\"].apply(assign_grade)#Calculating Grade Counts\n",
    "grade_stats = df[\"Grade\"].value_counts().to_frame(name=\"Count\")\n",
    "grade_stats[\"Percentage\"] = (grade_stats[\"Count\"] / len(df)) * 100\n",
    "print(grade_stats)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "7a4e97a8-2aec-4998-a223-263e591ebd6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('REG001', 78, 85, 80.1) ('REG002', 65, 72, 67.1)\n",
      " ('REG003', 90, 88, 89.4)]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "# Define the data type for the structured array\n",
    "student_dtype = np.dtype([\n",
    "    (\"reg_no\", \"U10\"),# string column (max length 10)\n",
    "    (\"exam_mark\", \"i4\"),# integer column\n",
    "    (\"coursework_mark\", \"i4\"),# integer column\n",
    "    (\"overall_mark\", \"f4\")# Float column\n",
    "])\n",
    "# Create data (like rows)\n",
    "students = np.array([\n",
    "    (\"REG001\", 78, 85, 0.7*78 + 0.3*85),\n",
    "    (\"REG002\", 65, 72, 0.7*65 + 0.3*72),\n",
    "    (\"REG003\", 90, 88, 0.7*90 + 0.3*88),\n",
    "], dtype=student_dtype)\n",
    "\n",
    "print(students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "24ffdd9b-0865-4513-b94c-d504d59cb008",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('REG002', 65, 72, 67.1) ('REG001', 78, 85, 80.1)\n",
      " ('REG003', 90, 88, 89.4)]\n"
     ]
    }
   ],
   "source": [
    "sorted_students = np.sort(students, order=\"overall_mark\")#Sorting Students overall marks\n",
    "print(sorted_students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e728543-330b-4e85-ba50-4071fa3df1f1",
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
