//
// Created by vitowu on 3/2/19.
//

#include "lz_encoder.h"



void LempelzivEncoder::encoding() {

    rawFile = readRawFile(rawFilePath);

    codebook.push_back(empty_identifier);

    {
        std::string seg = empty_identifier;

        int line = 0;
        for (const char &c : rawFile) {
            std::cout << "[DEBUG] Compressing segment: " << ++line << "\t"<< seg << std::endl;
            seg += std::to_string(c);
            if (inSegList(seg) == -1) {
                codebook.push_back(seg);
                char newWord = *(seg.end() - 1);
                seg.erase(seg.end() - 1);
                int16_t p = inSegList(seg);
                int16_t code = (p << 8) + newWord;
                compressedFile.push_back(code);
                seg = empty_identifier;
            }
        }
    }
    genCompressedFile();

}

int16_t LempelzivEncoder::inSegList(const std::string& s) {
    for (int16_t i = 0; i < codebook.size(); i++)
        if (codebook[i] == s)
            return i;

    return -1;
}

void LempelzivEncoder::genCompressedFile() {
    std::ofstream out(compressedFilePath);

    for (int16_t i : compressedFile)
        out.write(reinterpret_cast<const char*>(&i), sizeof(i));
}