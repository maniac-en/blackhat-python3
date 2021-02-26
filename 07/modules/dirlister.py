#!/usr/bin/env python3
import os


def run():
    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)
