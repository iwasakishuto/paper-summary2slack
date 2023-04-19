# coding: utf-8
import os

__all__ = ["UTILS_DIR", "MODULE_DIR"]

UTILS_DIR: str = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR: str = os.path.dirname(UTILS_DIR)
