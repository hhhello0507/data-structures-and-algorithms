cmake_minimum_required(VERSION 3.24)
project(untitled C)

set(CMAKE_C_STANDARD 11)

add_executable(untitled ring_queue/IntQueue.h ring_queue/IntQueue.c ring_queue/main.c)
