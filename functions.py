import os
import streamlit as st

FILEPATH = "todos.txt"

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

def get_todos(filepath=FILEPATH):
    """ Get todos from a text file"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-dos to a text file"""
    with open(filepath, "w") as write_file:
        write_file.writelines(todos_arg)


if __name__ == "__main__":
    print("Only runs when I can functions directly, useful for test")
    print(get_todos())