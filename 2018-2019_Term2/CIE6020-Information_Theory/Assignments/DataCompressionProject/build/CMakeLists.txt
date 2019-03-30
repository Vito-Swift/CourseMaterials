CMAKE_MINIMUM_REQUIRED(VERSION 3.5)
PROJECT(CIE6020DC)

SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)

MESSAGE("-Building CIE6020 Data Compression Project")

SET(DC_DIR ${CMAKE_CURRENT_LIST_DIR})

include_directories(${DC_DIR}/src)
include_directories(${DC_DIR}/include)

file(GLOB DC_SOURCE ${DC_DIR}/src/*.cpp)
file(GLOB DC_HEADER ${DC_DIR}/include/*.h)
add_library(DC_LIB SHARED ${DC_SOURCE} ${DC_HEADER})

add_executable(testHuffmanCoding test/testHuffmanCodingL.cpp ${DC_SOURCE} ${DC_HEADER})
target_link_libraries(testHuffmanCoding DC_LIB)

add_executable(testLZCoding test/testLempelzivCoding.cpp ${DC_SOURCE} ${DC_HEADER})
target_link_libraries(testLZCoding DC_LIB)

add_executable(testAdvHuffmanCoding test/testAdvHuffmanCoding.cpp ${DC_SOURCE} ${DC_HEADER})
target_link_libraries(testAdvHuffmanCoding DC_LIB)

add_executable(HuffmanEncoding exec/HuffmanCoding.cpp ${DC_SOURCE} ${DC_HEADER})
target_link_libraries(HuffmanEncoding DC_LIB)