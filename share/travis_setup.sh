#!/bin/bash
set -evx

mkdir ~/.geekcash

# safety check
if [ ! -f ~/.geekcash/.geekcash.conf ]; then
  cp share/geekcash.conf.example ~/.geekcash/geekcash.conf
fi
