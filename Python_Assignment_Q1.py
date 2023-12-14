# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:45:16 2023

@author: guoli
"""

def Stack(our_list, operation, new_element = None):
    """
    Stack is used for add or remove an element in a stack.

    Parameters
    ----------
    our_list : stack
        please input a stack.
    operation : add / delete
        please only input add or delete so as to finish adding an element.
    new_element : int/fload/string
        please input int/fload/string type elements.

    Returns
    new_list
    None.

    """
    new_list = our_list
    if operation == "add":
        
        insert_index = 0
        for i in range(len(new_list)):
            if new_list[i] < new_element:
                insert_index = i + 1
            else:
                break
        
        new_list.insert(insert_index, new_element)
        print("Adding new element to the stack") 
        print(new_list)                
        return new_list
    elif operation == "delete":
        if new_list:
            new_list.pop(0)
        print("Adding remove an element to the stack")
        print(new_list) 
        return new_list
    else:
        print("Invalid Operation in queue, please input add or delete!")
        return new_list


def Queue(our_list, operation, new_element = None):
    """
    Stack is used for add or remove an element in a queue.

    Parameters
    ----------
    our_list : list
        please input a list.
    operation : add / delete
        please only input add or delete so as to finish adding an element.
    new_element : int/fload/string
        please input int/fload/string type elements.

    Returns
    new_list
    None.

    """
    new_list = our_list
    if operation == "add":
        
        insert_index = 0
        for i in range(len(new_list)):
            if new_list[i] < new_element:
                insert_index = i + 1
            else:
                break
        
        new_list.insert(insert_index, new_element)
        print("Adding new element to the queue") 
        print(new_list)                
        return new_list
    elif operation == "delete":
        if new_list:
            new_list.pop()
        print("Adding remove an element to the queue")
        print(new_list) 
        return new_list
    else:
        print("Invalid Operation in queue, please input add or delete!")
        return new_list

our_list =[1,2,3,4]
Stack(our_list, "add",0)
Stack(our_list, "delete")

Queue(our_list, "add",5)
Queue(our_list, "delete")
