
// Generated from grammar/zoia.g4 by ANTLR 4.9.3

#pragma once


#include "antlr4-runtime.h"
#include "zoiaVisitor.h"


/**
 * This class provides an empty implementation of zoiaVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  zoiaBaseVisitor : public zoiaVisitor {
public:

  virtual antlrcpp::Any visitZoiaFile(zoiaParser::ZoiaFileContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitHeader(zoiaParser::HeaderContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLine(zoiaParser::LineContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLineElements(zoiaParser::LineElementsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLineElementsInner(zoiaParser::LineElementsInnerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLineElementsArg(zoiaParser::LineElementsArgContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEm3LineElement(zoiaParser::Em3LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEm2LineElement(zoiaParser::Em2LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEm1LineElement(zoiaParser::Em1LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTextFragment(zoiaParser::TextFragmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTextFragmentReq(zoiaParser::TextFragmentReqContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTextFragmentWord(zoiaParser::TextFragmentWordContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitAlias(zoiaParser::AliasContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitCommand(zoiaParser::CommandContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitArguments(zoiaParser::ArgumentsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitArgument(zoiaParser::ArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitKwdArgument(zoiaParser::KwdArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStdArgument(zoiaParser::StdArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitWhitespace(zoiaParser::WhitespaceContext *ctx) override {
    return visitChildren(ctx);
  }


};
