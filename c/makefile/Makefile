CC=gcc
EXE=test
OBJS=main.o sum.o sum2.o
CFLAGS=-I./include


$(EXE) : $(OBJS) 
	$(CC) $(CFLAGS) -o $@ $^

clean : 
	rm *.o
	rm test

good : 
	echo good
