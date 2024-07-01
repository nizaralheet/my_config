#!/bin/sh
sleep & dunst &
picom --blur-method dual_kawase --blur-strength 5 --vsync --crop-shadow-to-monitor --animations & wal -R 
