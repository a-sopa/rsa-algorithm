CC = gcc
CFLAGS_COMMON = -Wall -std=gnu17 -Isrc

# Otimization Flags for benchmark
CFLAGS_BENCH = $(CFLAGS_COMMON) -O3
CFLAGS_DEV   = $(CFLAGS_COMMON) -g

SRCS = src/key_gen.c src/encryption.c src/decryption.c
OBJS = $(SRCS:.c=.o)

.PHONY: all presentation benchmark clean

all: presentation benchmark

# Compila a versão interativa
presentation: $(OBJS) presentation/main.c
	$(CC) $(CFLAGS_DEV) $(OBJS) presentation/main.c -o presentation_app

# Compila a versão de benchmark otimizada (-O3)
benchmark: $(SRCS) tests/benchmark.c
	$(CC) $(CFLAGS_BENCH) $(SRCS) tests/benchmark.c -o benchmark_app

src/%.o: src/%.c
	$(CC) $(CFLAGS_DEV) -c $< -o $@

clean:
	rm -f src/*.o presentation_app benchmark_app