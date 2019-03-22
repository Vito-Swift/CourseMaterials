/*
 * File: TestIntArray.cpp
 * ----------------------
 * Tests the IntArray class.
 */

#include <iostream>
#include <string>
#include "intarray.h"
#include "strlib.h"
using namespace std;

/* Function prototypes */

void test(string str, int value, int expected);

/* Test program */

int main() {
   IntArray array(5);
   test("array.size()", array.size(), 5);
   for (int i = 0; i < 5; i++) {
      test("array.get(" + integerToString(i) + ")", array.get(i), 0);
      cout << "array.set(" << i << ", " << i << ");" << endl;
      array.set(i, i);
      test("array.get(" + integerToString(i) + ")", array.get(i), i);
   }
   return 0;
}

/*
 * Function: test
 * Usage: test(str, value, expected);
 * ----------------------------------
 * Generates a line of test output, making sure that the value of value
 * is equal to the expected parameter.
 */

void test(string str, int value, int expected) {
   cout << str << " -> " << value;
   if (value != expected) cout << " (should be " << expected << ")";
   cout << endl;
}
