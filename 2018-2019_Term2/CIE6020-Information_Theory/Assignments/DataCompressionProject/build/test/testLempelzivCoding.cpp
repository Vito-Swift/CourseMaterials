//
// Created by vitowu on 3/9/19.
//

#include "lz_encoder.h"

int main() {
    std::string raw_file_path = "/home/vitowu/Github/CIE6020-DataCompression/assets/sourceText/plrabn12.txt";
    std::string com_file_path = "/home/vitowu/Github/CIE6020-DataCompression/assets/compressedText/lzcoding/plrabn12.lz.bin";
    LempelzivEncoder lze(raw_file_path, com_file_path);
    stat(raw_file_path, com_file_path);
    lze.encoding();
    
    return EXIT_SUCCESS;
}