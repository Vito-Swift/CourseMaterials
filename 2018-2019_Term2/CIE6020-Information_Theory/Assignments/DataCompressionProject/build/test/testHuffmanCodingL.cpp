//
// Created by vitowu on 3/5/19.
//

#include "huff_encoder.h"

int main() {
    HuffmanCoding h(1);
    std::string dir = "/home/vitowu/Github/CIE6020-DataCompression/assets/sourceText/alice29.txt";
    std::string destdir = "/home/vitowu/Github/CIE6020-DataCompression/assets/compressedText/huffman/alice29.buf.bin";
    h.encoding(dir, destdir);
    stat(dir, destdir);
    return EXIT_SUCCESS;
}