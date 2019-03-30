//
// Created by vitowu on 3/2/19.
//

#ifndef PROJECT_HUFFMANCOMPRESSION_H
#define PROJECT_HUFFMANCOMPRESSION_H

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

#include "fileUtils.h"

/**
 * @struct of each node in Huffman Coding Tree
 */
struct node {

  // frequency of a symbol
  int freq;

  // sequence of symbol in ASCII
  std::string symbol;

  struct node* left;
  struct node* right;

  inline void operator delete(void* n) {
      node* tmp = (node*) n;
      delete tmp->left;
      delete tmp->right;
      ::operator delete(n);
  }

};

/**
 * @class of Huffman Coding with encoding and decoding method
 */
class HuffmanCoding {

 public:

  HuffmanCoding(int wordLen = 0);

  ~HuffmanCoding();

  virtual void encoding(const std::string& dir, const std::string& destdir);

  void decoding(std::string src_dir, std::string dest_dir);

 protected:

  virtual int inSegList(const std::string& c);

  virtual void getSegList();

  virtual void getCodingDict(node* n, const std::string& prefix);

  virtual struct node* newHuffmanTree();

  virtual void genCompressedFile(const std::string& destdir);

  // length of each symbol
  int codeLen;

  // segments of raw file
  std::vector<node*> segList;

  // coding result
  std::map<std::string, std::string> HuffmanDic;

  // raw string of file
  std::string rawFile;

  struct node* root;

};

inline bool compareByFreq(node* a, node* b) {
    return a->freq < b->freq;
}

#endif //PROJECT_HUFFMANCOMPRESSION_H
