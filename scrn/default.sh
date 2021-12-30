#!/bin/bash

xrandr --output DVI-I-0 --off --output DVI-I-1 --mode 1920x1200 --pos 1920x0 --rotate left --output DP-0 --off --output DP-1 --mode 1920x1200 --pos 0x0 --rotate normal
sleep 0.2
xrandr --output DVI-I-0 --off --output DVI-I-1 --mode 1600x1200 --pos 1920x0 --rotate left --output DP-0 --off --output DP-1 --mode 1920x1200 --pos 0x0 --rotate normal
sleep 0.3
xrandr --output DVI-I-0 --off --output DVI-I-1 --mode 1920x1200 --pos 1920x0 --rotate left --output DP-0 --off --output DP-1 --mode 1920x1200 --pos 0x0 --rotate normal
