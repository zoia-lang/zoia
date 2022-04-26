
// Generated from grammar/zoia.g4 by ANTLR 4.10.1

#pragma once


#include "antlr4-runtime.h"
#include "zoiaParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by zoiaParser.
 */
class  zoiaVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by zoiaParser.
   */
    virtual std::any visitZoiaFile(zoiaParser::ZoiaFileContext *context) = 0;

    virtual std::any visitHeader(zoiaParser::HeaderContext *context) = 0;

    virtual std::any visitLine(zoiaParser::LineContext *context) = 0;

    virtual std::any visitLineElements(zoiaParser::LineElementsContext *context) = 0;

    virtual std::any visitLineElementsInner(zoiaParser::LineElementsInnerContext *context) = 0;

    virtual std::any visitLineElementsArg(zoiaParser::LineElementsArgContext *context) = 0;

    virtual std::any visitEm3LineElement(zoiaParser::Em3LineElementContext *context) = 0;

    virtual std::any visitEm2LineElement(zoiaParser::Em2LineElementContext *context) = 0;

    virtual std::any visitEm1LineElement(zoiaParser::Em1LineElementContext *context) = 0;

    virtual std::any visitTextFragment(zoiaParser::TextFragmentContext *context) = 0;

    virtual std::any visitTextFragmentReq(zoiaParser::TextFragmentReqContext *context) = 0;

    virtual std::any visitTextFragmentWord(zoiaParser::TextFragmentWordContext *context) = 0;

    virtual std::any visitAlias(zoiaParser::AliasContext *context) = 0;

    virtual std::any visitCommand(zoiaParser::CommandContext *context) = 0;

    virtual std::any visitArguments(zoiaParser::ArgumentsContext *context) = 0;

    virtual std::any visitArgument(zoiaParser::ArgumentContext *context) = 0;

    virtual std::any visitKwdArgument(zoiaParser::KwdArgumentContext *context) = 0;

    virtual std::any visitStdArgument(zoiaParser::StdArgumentContext *context) = 0;

    virtual std::any visitWhitespace(zoiaParser::WhitespaceContext *context) = 0;


};
