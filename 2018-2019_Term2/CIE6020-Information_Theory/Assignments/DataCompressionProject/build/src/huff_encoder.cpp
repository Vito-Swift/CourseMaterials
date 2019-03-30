//
// Created by vitowu on 3/2/19.
//

#include "huff_encoder.h"

// meaningless string to identify a compound node
std::string identifier = "c0i1";

/**
 * @function constructor of Huffman Coding
 * @param wordLen
 *                length of each symbol in Huffman Coding (one or dual words etc.)
 *                when wordLen == 0, apply Huffman Coding over letters only
 */
HuffmanCoding::HuffmanCoding(int wordLen) {
    codeLen = wordLen;
}

HuffmanCoding::~HuffmanCoding() {
    for (node* n : segList)
        delete n;
}


/**
 * @function encoding method
 * @param dir
 *           directory of file need to be compressed
 */
void HuffmanCoding::encoding(const std::string& dir, const std::string& destdir) {
    rawFile = readRawFile(dir);
    getSegList();
    node* root = newHuffmanTree();

    if (root->symbol == identifier) {
        if (root->left)
            getCodingDict(root->left, "0");
        if (root->right)
            getCodingDict(root->right, "1");
    } else {
        HuffmanDic[root->symbol] = "0";
    }

    std::cout << "[INFO] Huffman Coding Dictionary Size: " << HuffmanDic.size() << std::endl;

    for (auto const& key: HuffmanDic)
        std::cout << "key: " << key.first << "\tcodeword: " << key.second << std::endl;

    genCompressedFile(destdir);

    if (codeLen) {
        unsigned long size = 0;
        for (auto const& key: HuffmanDic)
            size = size + 8*key.first.size() + key.second.size();
        std::cout << "Dictionary Size: " << size/8 << std::endl;
    }
}


/**
 * @function decoding method
 * @param dir
 *           directory of file need to be decoded
 */
void HuffmanCoding::decoding(std::string src_dir, std::string dest_dir) {

}


/**
   * @function to determine whether a character got in stringstream is in seg list
   * @param c character
   * @return if in, return index, otherwise return 0
   */

int HuffmanCoding::inSegList(const std::string& c) {
    for (int i = 0; i < segList.size(); i++)
        if (segList[i]->symbol == c)
            return i;
    return -1;
}


/**
 * @function transform a raw string to segment list
 *            e.g "I love Information Theory" -> Vector ["I Love ", "Information Theory "]
 */
void HuffmanCoding::getSegList() {
    std::stringstream istream(rawFile);

    if (codeLen == 0) {
        // get segment list by letters
        std::cout << "[INFO] Splitting raw file by letters." << std::endl;

        char c;
        int seg_index;
        while (istream.get(c)) {
            if ((seg_index = inSegList(std::to_string(c))) != -1)  // c in seg list
                segList[seg_index]->freq++;
            else {
                node* n = new node;
                n->freq = 1;
                n->symbol = std::to_string(c);
                n->left = nullptr;
                n->right = nullptr;

                segList.push_back(n);
            }
        }

    } else {
        // get segment list by codeLen-length words
        std::cout << "[INFO] Splitting raw file by " << codeLen << "-length words." << std::endl;

        std::string line;
        int seg_index;

        node* nl = new node;
        nl->freq = 0;
        nl->symbol = "\n";
        nl->left = nullptr;
        nl->right = nullptr;

        segList.push_back(nl);

        int linecount = 0;

        while (std::getline(istream, line, '\n')) {
            // get line segment
             std::cout << "[DEBUG] compressing line: " << ++linecount << std::endl;
            std::queue<std::string> sl;
            std::string seg;
            std::stringstream lstrem(line);
            while (std::getline(lstrem, seg, ' ')) {
                std::stringstream ls(seg);
                std::string sseg;
                while (std::getline(ls, sseg, '\t')) {
                    sseg.erase(std::remove_if(sseg.begin(), sseg.end(), [](const char c) { return !isalpha(c); }),
                              sseg.end());
                    sl.push(sseg);
                }
            }
            std::string s;
            while (!sl.empty()) {
                if (s.empty() && sl.size() < codeLen) {
                    s = sl.front();
                    sl.pop();
                    while (!sl.empty()) {
                        s += " " + sl.front();
                        sl.pop();
                    }
                } else {
                    int wordCount = 1;
                    s = sl.front();
                    sl.pop();
                    while (wordCount < codeLen) {
                        s += " " + sl.front();
                        sl.pop();
                    }
                }

                if ((seg_index = inSegList(s) != -1)) {
                    segList[seg_index] -> freq++;
                } else {
                    node* n = new node;
                    n->freq = 1;
                    n->symbol = s;
                    n->left = nullptr;
                    n->right = nullptr;
                    segList.push_back(n);
                }
            }
        }
    }
}


/**
 * @function initialize a new Huffman Tree
 * @return pointer of root node
 */
struct node* HuffmanCoding::newHuffmanTree() {
    std::sort(segList.begin(), segList.end(), compareByFreq);

    while (segList.size() > 1) {
        node* firstNode = segList[0];
        node* secondNode = segList[1];

        node* mergedNode = new node;
        mergedNode->freq = firstNode->freq + secondNode->freq;
        mergedNode->symbol = identifier;
        mergedNode->left = firstNode;
        mergedNode->right = secondNode;

        segList.erase(segList.begin()+1);
        segList[0] = mergedNode;
//        segList.erase(segList.begin());
//        segList.erase(segList.begin());

//        if ((*(segList.begin()))->freq >= mergedNode->freq) {
//
//            segList.insert(segList.begin(), mergedNode);
//
//        } else if ((*(segList.end()))->freq <= mergedNode->freq) {
//
//            segList.insert(segList.end(), mergedNode);
//
//        } else {
//
//            for (int i = 1; i < segList.size()-1; ++i)
//                if (segList[i]->freq <= mergedNode ->freq &&
//                    segList[i+1]->freq >= mergedNode->freq) {
//                    segList.insert(segList.begin() + i + 1, mergedNode);
//                    break;
//                }
//
//        }

        std::sort(segList.begin(), segList.end(), compareByFreq);

        std::cout << "[DEBUG] Huffman Tree Size: " << segList.size() << std::endl;
    }

    return segList[0];
}


void HuffmanCoding::getCodingDict(node* n, const std::string& prefix) {
    if (n->symbol != identifier)
        HuffmanDic[n->symbol] = prefix;
    else {
        if (n->left)
            getCodingDict(n->left, prefix + "0");

        if (n->right)
            getCodingDict(n->right, prefix + "1");
    }
}

/**
 * @function generate a compressed file based on Huffman Tree
 */
void HuffmanCoding::genCompressedFile(const std::string& destdir) {
    std::string cfile;
    std::stringstream istream(rawFile);
    char c;

    if (codeLen) {
        std::string line;

        while (std::getline(istream, line, '\n')) {
            // get line segment
            std::queue<std::string> sl;
            std::string seg;
            std::stringstream lstrem(line);
            while (std::getline(lstrem, seg, ' ')) {
                std::stringstream ls(seg);
                std::string sseg;
                while (std::getline(ls, sseg, '\t')) {
                    sseg.erase(std::remove_if(sseg.begin(), sseg.end(), [](const char c) { return !isalpha(c); }),
                               sseg.end());
                    sl.push(sseg);
                }
            }
            std::string s;
            while (!sl.empty()) {
                if (s.empty() && sl.size() < codeLen) {
                    s = sl.front();
                    sl.pop();
                    while (!sl.empty()) {
                        s += " " + sl.front();
                        sl.pop();
                    }
                } else {
                    int wordCount = 1;
                    s = sl.front();
                    sl.pop();
                    while (wordCount < codeLen) {
                        s += " " + sl.front();
                        sl.pop();
                    }
                }

            }


            if (HuffmanDic.find(s) == HuffmanDic.end()) std::cout << s << std::endl;
            cfile += HuffmanDic[s];
            cfile += HuffmanDic["\n"];
        }

    } else {
        while (istream.get(c))
            cfile += HuffmanDic[std::to_string(c)];
    }

    std::ofstream out(destdir);
    out << bin2str(cfile);
    out.close();

}
