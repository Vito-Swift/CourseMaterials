//
// Created by vitowu on 3/28/19.
//

#include "advhuff_encoder.h"

int main() {
    std::string raw_file_path = "/home/vitowu/Github/CIE6020-DataCompression/assets/sourceText/plrabn12.txt";
    std::string dest_file_path = "/home/vitowu/Github/CIE6020-DataCompression/assets/compressedText/advhuffman/plrabn12.buf.bin";
    advancedHuffmanCoding h;
    h.encoding(raw_file_path, dest_file_path);
    stat(raw_file_path, dest_file_path);
    return EXIT_SUCCESS;
}
