CC=gcc
CFLAGS=-g -Wall -c
LDFLAGS=-g -Wall -o

all: client

client: client.o
	$(CC) client.o $(LDFLAGS) client

client.o: client.c
	$(CC) client.c $(CFLAGS)

clean:
	rm -f *.o client
