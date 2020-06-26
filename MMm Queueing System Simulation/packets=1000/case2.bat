@echo off
for /L %%A in (5, 5, 95) do python new_mm1.py -M 2 -A %%A -S 50  -N 10000 --no-trace>> mm2.out