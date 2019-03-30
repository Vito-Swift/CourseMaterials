//
// Created by vitowu on 3/25/19.
//

#ifndef CIE6020DC_ADVHUFF_ENCODER_H
#define CIE6020DC_ADVHUFF_ENCODER_H

#include <iostream>
#include <vector>
#include <queue>
#include <map>

#include <string>
#include <fstream>
#include <streambuf>
#include <sstream>

#include <algorithm>
#include <bitset>

#include <iomanip>

#include "huff_encoder.h"
#include "fileUtils.h"


class advancedHuffmanCoding: HuffmanCoding {
 public:
  advancedHuffmanCoding();
  ~advancedHuffmanCoding();
  void encoding(const std::string& dir, const std::string& destdir) override;
 private:
  int inSegList(const char& c, const char& previousChar);
  void getSegList() override;
  void getCodingDict(char c, node* n, const std::string& prefix);
  struct node* newHuffmanTree(std::vector<node*> segList);
  void genCompressedFile(const std::string& destdir) override;
  struct node* root;
  std::map<char, std::vector<node*>> segMap;
  std::map<char, std::map<char, std::string>> advHuffmanDic;
  std::map<char, node*> advHuffmanTree;
  char firstChar;
};

inline char* charttobin(char c) {
    static char bin[8+1] = {0};
    int i;
    for (i = 8-1; i >= 0; i--) {
        bin[i] = (c % 2) + '0';
        c /= 2;
    }
    return bin;
}
#endif //CIE6020DC_ADVHUFF_ENCODER_H
