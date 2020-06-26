@echo off
for /L %%A in (5, 5, 95) do python new_mm1.py -M 5 -A %%A -S 20 --no-trace>> mm3.out