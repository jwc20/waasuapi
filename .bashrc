#! /usr/bin/env bash
export PYTHONPATH=$SCM_PATH/py
export PYTHONBREAKPOINT="ipdb.set_trace"

export PS1='\[\033[01;91m\]($name)\[\033[00m\] \[\033[01;34m\]\W\[\033[00m\] 🛸 '
