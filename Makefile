CFLAGS = -g -Wall -std=c99
TARGET = xyz2cif.c
CC = gcc

default: all
all:
	gcc ${TARGET} -lm -o xyz2cif
