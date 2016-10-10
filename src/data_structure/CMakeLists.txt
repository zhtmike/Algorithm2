cmake_minimum_required(VERSION 3.6)
project(data_structure)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
include_directories(/anaconda/include/python3.5m/)

set(SOURCE_FILES union_find.c)
add_executable(data_structure ${SOURCE_FILES})