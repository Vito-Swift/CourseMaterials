/*
 * File: RemoveComments.cpp
 * ------------------------
 * Prints out a file after removing comments.
 */

#include <iostream>
#include <fstream>
#include "filelib.h"     // promptUserForFile
using namespace std;

/* Function prototypes */

void removeComments(istream & is, ostream & os);

/* Main program */

int main() {
   ifstream infile;
   promptUserForFile(infile, "Input file: ");
   removeComments(infile, cout);
   infile.close();
   return 0;
}

/*
 * Function: removeComments
 * Usage: removeComments(is, os);
 * ------------------------------
 * Copies characters from the input stream is to the output stream os,
 * removing any comments it finds.  This program eliminates both the
 * /* and // comment forms but does not check to see if those characters
 * are embedded within strings.
 */

void removeComments(istream & is, ostream & os) {
	// TODO
}
