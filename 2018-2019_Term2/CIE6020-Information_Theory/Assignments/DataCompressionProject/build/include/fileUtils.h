//
// Created by vitowu on 3/9/19.
//

#ifndef CIE6020DC_FILEUTILS_H
#define CIE6020DC_FILEUTILS_H

#include <fstream>
#include <bitset>
#include <sstream>
#include <vector>
#include <iostream>
#include <string>
#include <iomanip>

inline std::string bin2str(std::string t_) {
    std::stringstream bStream(t_);
    std::string ret;
    std::bitset<16> t;
    while(bStream >> t) {
        ret += static_cast<char>(t.to_ulong());
    }
    return ret;
}


inline long long filesize(const std::string& fn)
{
    std::streampos fsize = 0;

    std::ifstream myfile (fn, std::ios::in);  // File is of type const char*

    fsize = myfile.tellg();         // The file pointer is currently at the beginning
    myfile.seekg(0, std::ios::end);      // Place the file pointer at the end of file

    fsize = myfile.tellg() - fsize;
    myfile.close();

    static_assert(sizeof(fsize) >= sizeof(long long), "Oops.");
    return fsize;
}


inline std::string readRawFile(const std::string& dir) {
    std::ifstream f(dir);
    std::string str(
        (std::istreambuf_iterator<char>(f)),
        std::istreambuf_iterator<char>()
        );

    return str;
}

inline void stat(std::string src, std::string dest) {
    long long original_size = filesize(src);
    long long compressed_size = filesize(dest);
    double rate = 100 * (double)compressed_size / (double)original_size;

    std::cout << std::endl << "[INFO] Huffman Compression finished." << std::endl;
    std::cout << "original file size: " << original_size << " bytes." << std::endl;
    std::cout << "compressed file size: " << compressed_size << " bytes." << std::endl;
    std::cout << std::fixed;
    std::cout << std::setprecision(2);
    std::cout << "compression rate: " << rate << "%" << std::endl;
}

#endif //CIE6020DC_FILEUTILS_H
