CC = gcc
CFLAGS = -Wall -std=c17 -g

SRCS = main.c key_gen.c
OBJS = $(SRCS:.c=.o)
TARGET = main

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)


clean:
	rm -f *.o $(TARGET)

run: 
	./main