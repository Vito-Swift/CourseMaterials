# This file allows users to call find_package(Clang) and pick up our targets.



find_package(LLVM REQUIRED CONFIG
             HINTS "/home/vitowu/Documents/CourseMaterials/CourseMaterials/2018-2019_Term2/CS143-Compilers/llvmbuild/lib/cmake/llvm")

set(CLANG_EXPORTED_TARGETS "clangBasic;clangLex;clangParse;clangAST;clangDynamicASTMatchers;clangASTMatchers;clangSema;clangCodeGen;clangAnalysis;clangEdit;clangRewrite;clangARCMigrate;clangDriver;clangSerialization;clangRewriteFrontend;clangFrontend;clangFrontendTool;clangToolingCore;clangToolingRefactor;clangTooling;clangIndex;clangStaticAnalyzerCore;clangStaticAnalyzerCheckers;clangStaticAnalyzerFrontend;clangFormat;clang;clang-format;clang-import-test;clangApplyReplacements;clangReorderFields;modularize;clangTidy;clangTidyAndroidModule;clangTidyBoostModule;clangTidyBugproneModule;clangTidyCERTModule;clangTidyCppCoreGuidelinesModule;clangTidyGoogleModule;clangTidyHICPPModule;clangTidyLLVMModule;clangTidyMiscModule;clangTidyModernizeModule;clangTidyMPIModule;clangTidyPerformanceModule;clangTidyPlugin;clangTidyReadabilityModule;clang-tidy;clangTidyUtils;clangChangeNamespace;clangQuery;clangMove;clangDaemon;clangd;clangIncludeFixer;clangIncludeFixerPlugin;findAllSymbols;libclang")
set(CLANG_CMAKE_DIR "/home/vitowu/Documents/CourseMaterials/CourseMaterials/2018-2019_Term2/CS143-Compilers/llvmbuild/lib/cmake/clang")
set(CLANG_INCLUDE_DIRS "/home/vitowu/Documents/CourseMaterials/CourseMaterials/2018-2019_Term2/CS143-Compilers/testCompiler/llvm/tools/clang/include;/home/vitowu/Documents/CourseMaterials/CourseMaterials/2018-2019_Term2/CS143-Compilers/llvmbuild/tools/clang/include")

# Provide all our library targets to users.
include("/home/vitowu/Documents/CourseMaterials/CourseMaterials/2018-2019_Term2/CS143-Compilers/llvmbuild/lib/cmake/clang/ClangTargets.cmake")
