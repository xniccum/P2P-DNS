CC=gcc
CFLAGS=-g -lm -Wall -c
LDFLAGS=-g -lm -Wall -o

all: whitelist_mgr

whitelist_mgr: src/whitelist_mgr.o libs/cJSON.o
	$(CC) src/whitelist_mgr.o libs/cJSON.o $(LDFLAGS) whitelist_mgr

cJSON.o: libs/cJSON.c libs/cJSON.h
	$(CC) libs/cJSON.c $(CFLAGS)

whitelist_mgr.o: src/whitelist_mgr.c libs/cJSON.h
	$(CC) src/whitelist_mgr.c $(CFLAGS)

clean:
	rm -f *.o
