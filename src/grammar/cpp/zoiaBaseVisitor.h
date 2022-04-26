
// Generated from grammar/zoia.g4 by ANTLR 4.10.1

#pragma once


#include "antlr4-runtime.h"
#include "zoiaVisitor.h"


/**
 * This class provides an empty implementation of zoiaVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  zoiaBaseVisitor : public zoiaVisitor {
public:

  virtual std::any visitZoiaFile(zoiaParser::ZoiaFileContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHeader(zoiaParser::HeaderContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLine(zoiaParser::LineContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLineElements(zoiaParser::LineElementsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLineElementsInner(zoiaParser::LineElementsInnerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLineElementsArg(zoiaParser::LineElementsArgContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEm3LineElement(zoiaParser::Em3LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEm2LineElement(zoiaParser::Em2LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEm1LineElement(zoiaParser::Em1LineElementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTextFragment(zoiaParser::TextFragmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTextFragmentReq(zoiaParser::TextFragmentReqContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTextFragmentWord(zoiaParser::TextFragmentWordContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAlias(zoiaParser::AliasContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCommand(zoiaParser::CommandContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArguments(zoiaParser::ArgumentsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArgument(zoiaParser::ArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitKwdArgument(zoiaParser::KwdArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStdArgument(zoiaParser::StdArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWhitespace(zoiaParser::WhitespaceContext *ctx) override {
    return visitChildren(ctx);
  }


};
