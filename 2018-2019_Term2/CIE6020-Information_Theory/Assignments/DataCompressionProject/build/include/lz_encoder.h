//
// Created by vitowu on 3/2/19.
//

#ifndef PROJECT_LEMEL_ZIVENCODER_H
#define PROJECT_LEMEL_ZIVENCODER_H

#include <iostream>
#include <vector>
#include <map>
#include "fileUtils.h"


class LempelzivEncoder {

 public:

  LempelzivEncoder(std::string& rfp, std::string& cfp)
                : rawFilePath(rfp), compressedFilePath(cfp) {};

  void encoding();

 private:

  const std::string empty_identifier = "LZES";

  std::string rawFile;

  std::string rawFilePath;

  std::string compressedFilePath;

  std::vector<std::string> codebook;

  std::vector<int16_t> compressedFile;

  int16_t inSegList(const std::string& s);

  void genCompressedFile();
};


#endif //PROJECT_LEMEL_ZIVENCODER_H
