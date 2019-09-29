CC = g++
CFLAGS = -ggdb
LFLAGS = 
OUTPUT = make_env

SRC = $(wildcard *.cpp)
OBJ = $(SRC:%.cpp=%.o)

all: $(OBJ) $(OUTPUT)
	@echo done!

%.o: %.cpp
	@echo compiling $@...
	@$(CC) $(CFLAGS) -c $< -o $@

$(OUTPUT): $(OBJ)
	@echo linking...
	@$(CC) $(CFLAGS) $(LFLAGS) -o $@ $(OBJ)

clean:
	rm -f $(OBJ)
	rm -f $(OUTPUT)
