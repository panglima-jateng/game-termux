#!/bin/python
#coding:utf-8

# module/library
import sys, random
from os import system
from time import sleep as s

# bermain lagi
def nanya():
  nanya=input(' {?} Mau main lagi?[Y/T]: ')
  if nanya=='y' or nanya=='Y':
    game()
  elif nanya=='t' or nanya=='T':
    exit();
  else:
    print(f'Tidak ada pilihan {nanya}')

# tampilan
def game():
  system('clear')
  print()
  print()
  print()
  print('         {•} game anda vs komputer {•}')
  print('•===============================================•')
  print(' [1] batu')
  print(' [2] gunting')
  print(' [3] kertas')
  print('•===============================================•')
  pil=input(' {+} Pilih: ')
  kom=random.choice(['batu','gunting','kertas'])
  if pil=='1':
    print(' {•} Kamu     : batu')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {•} Imbang')
    if kom=='gunting':
      print(' {√} Kamu menang')
    if kom=='kertas':
      print(' {×}Kamu kalah')
    nanya()
  elif pil=='2':
    print(' {•} Kamu     : gunting')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {×} Kamu kalah')
    if kom=='gunting':
      print(' {•} Imbang')
    if kom=='kertas':
      print(' {√} Kamu menang')
    nanya()
  elif pil=='3':
    print(' {•} Kamu     : kertas')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {√} Kamu menang')
    if kom=='gunting':
      print(' {×} Kamu kalah')
    if kom=='kertas':
      print(' {•} Imbang')
    nanya()
if __name__=='__main__':
  game()
