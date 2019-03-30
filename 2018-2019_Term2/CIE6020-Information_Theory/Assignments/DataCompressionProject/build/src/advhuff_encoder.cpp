//
// Created by vitowu on 3/25/19.
//

#include "advhuff_encoder.h"


std::string identifier_ = "c0i1";


advancedHuffmanCoding::advancedHuffmanCoding() {
    codeLen = 1;
}


advancedHuffmanCoding::~advancedHuffmanCoding() {
    for (const auto& p: segMap) {
        for (node* n : segMap[p.first])
            delete n;
    }
}


void advancedHuffmanCoding::encoding(const std::string &dir, const std::string& destdir) {
    rawFile = readRawFile(dir);
    getSegList();
    for (const auto& p : segMap) {
        advHuffmanTree[p.first] = newHuffmanTree(p.second);

        if (advHuffmanTree[p.first]->symbol == identifier_) {
            if (advHuffmanTree[p.first]->left)
                getCodingDict(p.first, advHuffmanTree[p.first]->left, "0");
            if (advHuffmanTree[p.first]->right)
                getCodingDict(p.first, advHuffmanTree[p.first]->right, "1");

        } else {
            HuffmanDic[advHuffmanTree[p.first]->symbol] = "0";
        }

        std::cout << "[INFO] Huffman Coding Dict: " << p.first << " Size: " << advHuffmanDic[p.first].size() << std::endl;
    }

    for (const auto& p : advHuffmanDic) {
        for (const auto & q : p.second)
            std::cout << "[DEBUG] Pre-word: " << p.first << " Consecutive-word: " << q.first << " Codeword: " << q.second << std::endl;
    }

    genCompressedFile(destdir);
}


int advancedHuffmanCoding::inSegList(const char&c, const char& previousChar) {
    for (int i = 0; i < segMap[previousChar].size(); i++)
        if (segMap[previousChar][i]->symbol == std::to_string(c))
            return i;

    return -1;
}


void advancedHuffmanCoding::getSegList() {
    std::stringstream istream(rawFile);
    std::cout << "[INFO] Splitting raw file by learning semantic structure" << std::endl;

    char c;
    char previousCharacter;
    int seg_index;
    istream.get(c);
    firstChar = c;
    previousCharacter = c;
    while (istream.get(c)) {
        if ((seg_index = inSegList(c, previousCharacter)) != -1) {
            segMap[previousCharacter][seg_index]->freq++;
        } else {
            node* n = new node;
            n->freq = 1;
            n->symbol = std::to_string(c);
            n->left = nullptr;
            n->right= nullptr;
            segMap[previousCharacter].push_back(n);
        }
        previousCharacter = c;
    }

}


void advancedHuffmanCoding::getCodingDict(char c, node* n, const std::string &prefix) {
    if (n->symbol != identifier_)
        advHuffmanDic[c][char(stoi(n->symbol))] = prefix;
    else {
        if (n->left)
            getCodingDict(c, n->left, prefix+"0");
        if (n->right)
            getCodingDict(c, n->right, prefix+"1");
    }
}


node* advancedHuffmanCoding::newHuffmanTree(std::vector<node*> segList) {
    std::sort(segList.begin(), segList.end(), compareByFreq);

    while (segList.size() > 1) {
        node* firstNode = segList[0];
        node* secondNode = segList[1];

        node* mergedNode = new node;
        mergedNode->freq = firstNode->freq + secondNode->freq;
        mergedNode->symbol = identifier_;
        mergedNode->left = firstNode;
        mergedNode->right = secondNode;

        segList.erase(segList.begin());
        segList.erase(segList.begin());

        if ((*(segList.begin()))->freq >= mergedNode->freq) {
            segList.insert(segList.begin(), mergedNode);
        } else if ((*(segList.end()))->freq <= mergedNode->freq) {
            segList.insert(segList.end(), mergedNode);
        } else {
            for (int i = 1; i < segList.size()-1; ++i)
                if (segList[i]->freq <= mergedNode ->freq &&
                    segList[i+1]->freq >= mergedNode->freq) {
                    segList.insert(segList.begin() + i + 1, mergedNode);
                    break;
                }
        }
    }

    return segList[0];
}


void advancedHuffmanCoding::genCompressedFile(const std::string& destdir) {
    std::string cfile;
    std::stringstream istream(rawFile);

    char c;
    char previousCharacter = firstChar;


    cfile += charttobin(firstChar);

    while (istream.get(c)) {
        cfile += advHuffmanDic[previousCharacter][c];
        previousCharacter = c;
    }

    std::ofstream out(destdir);
    out << bin2str(cfile);
    out.close();
}
