cmake_minimum_required(VERSION 3.24)
project(untitled C)

set(CMAKE_C_STANDARD 11)

#add_executable(untitled stack/IntStack.h stack/IntStack.c stack/main.c queue/ArrayIntQueue.h queue/ArrayIntQueue.c queue/main.c)
add_executable(untitled #[[stack/IntStack.h stack/IntStack.c stack/main.c]] queue/ArrayIntQueue.h queue/ArrayIntQueue.c queue/main.c)
