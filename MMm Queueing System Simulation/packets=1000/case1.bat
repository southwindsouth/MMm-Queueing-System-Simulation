@echo off 
for /L %%A in (5, 5, 95) do python new_mm1.py -M 1 -A %%A -S 100 -N 10000  --no-trace>> mm1.out
for /L %%A in (5, 5, 95) do python new_mm1.py -M 2 -A %%A -S 50  -N 10000  --no-trace>> mm2.out
for /L %%A in (5, 5, 95) do python new_mm1.py -M 5 -A %%A -S 20  -N 10000  --no-trace>> mm3.out



