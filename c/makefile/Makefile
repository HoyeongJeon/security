CC=gcc
EXE=run
DEFINES=-DDEBUG
LDFLAGS=-lpthread
CFLAGS=-g -I./include $(DEFINES)

C_SRC = $(wildcard *.c)
OBJ = $(C_SRC: .c=.o)

all : $(EXE)
	echo completed!

$(EXE) : $(OBJ) 
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

clean : 
	rm *.o
	rm test

good : 
	echo good
