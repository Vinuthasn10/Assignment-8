
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:5\n",
      "Enter number at location 0 :\n",
      "2\n",
      "Enter number at location 1 :\n",
      "4\n",
      "Enter number at location 2 :\n",
      "6\n",
      "Enter number at location 3 :\n",
      "8\n",
      "Enter number at location 4 :\n",
      "10\n",
      "The list is= [2, 4, 6, 8, 10]\n",
      "The Sum of elements in the list is 30\n"
     ]
    }
   ],
   "source": [
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list is=\",List1)\n",
    "print(\"The Sum of elements in the list is\",sum(List1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:4\n",
      "Enter number at location 0 :\n",
      "3\n",
      "Enter number at location 1 :\n",
      "5\n",
      "Enter number at location 2 :\n",
      "7\n",
      "Enter number at location 3 :\n",
      "9\n",
      "The list is= [3, 5, 7, 9]\n",
      "The Multiplication of elements in the list is 945\n"
     ]
    }
   ],
   "source": [
    "def ListMultiply(myList) :\n",
    "    result = 1\n",
    "    for x in myList: \n",
    "         result = result * x  \n",
    "    return result\n",
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list is=\",List1)\n",
    "print(\"The Multiplication of elements in the list is\",ListMultiply(List1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:5\n",
      "Enter number at location 0 :\n",
      "7\n",
      "Enter number at location 1 :\n",
      "5\n",
      "Enter number at location 2 :\n",
      "4\n",
      "Enter number at location 3 :\n",
      "9\n",
      "Enter number at location 4 :\n",
      "2\n",
      "The list is= [7, 5, 4, 9, 2]\n",
      "The Maximum element in the list is 9\n",
      "The Minimum element in the list is 2\n"
     ]
    }
   ],
   "source": [
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list is=\",List1)\n",
    "print(\"The Maximum element in the list is\",max(List1))\n",
    "print(\"The Minimum element in the list is\",min(List1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list:6\n",
      "Enter number at location 0 :\n",
      "1\n",
      "Enter number at location 1 :\n",
      "2\n",
      "Enter number at location 2 :\n",
      "3\n",
      "Enter number at location 3 :\n",
      "3\n",
      "Enter number at location 4 :\n",
      "2\n",
      "Enter number at location 5 :\n",
      "1\n",
      "The list with the duplicate values is= [1, 2, 3, 3, 2, 1]\n",
      "The list with deleted duplicate values is= [1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "def Remove(List1): \n",
    "    final_list=[] \n",
    "    for n in List1: \n",
    "        if n not in final_list: \n",
    "            final_list.append(n) \n",
    "    return final_list \n",
    "List1=[]\n",
    "n=int(input(\"Enter the size of the list:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    List1.append(item)\n",
    "print(\"The list with the duplicate values is=\",List1)\n",
    "print(\"The list with deleted duplicate values is=\",Remove(List1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty List\n"
     ]
    }
   ],
   "source": [
    "def Verify(list1): \n",
    "    if len(list1) == 0: \n",
    "        return True\n",
    "    else: \n",
    "        return False\n",
    "list1=[]\n",
    "if Verify(list1): \n",
    "    print (\"Empty List\") \n",
    "else: \n",
    "    print(\"The list is not Empty\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}