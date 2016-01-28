#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import inspect

def _is_some_method(object):
    return inspect.ismethod(object) or inspect.ismethoddescriptor(object)

def allmethods(cl):
    methods = {}
    for key, value in inspect.getmembers(cl, _is_some_method):
        methods[key] = 1
    for base in cl.__bases__:
        methods.update(allmethods(base)) # all your base are belong to us
    for key in methods.keys():
        methods[key] = getattr(cl, key)
    return methods