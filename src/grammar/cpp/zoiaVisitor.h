
// Generated from grammar/zoia.g4 by ANTLR 4.9.3

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
    virtual antlrcpp::Any visitZoiaFile(zoiaParser::ZoiaFileContext *context) = 0;

    virtual antlrcpp::Any visitHeader(zoiaParser::HeaderContext *context) = 0;

    virtual antlrcpp::Any visitLine(zoiaParser::LineContext *context) = 0;

    virtual antlrcpp::Any visitLineElements(zoiaParser::LineElementsContext *context) = 0;

    virtual antlrcpp::Any visitRegularLineElements(zoiaParser::RegularLineElementsContext *context) = 0;

    virtual antlrcpp::Any visitLineElement(zoiaParser::LineElementContext *context) = 0;

    virtual antlrcpp::Any visitMarkedUpLineElements(zoiaParser::MarkedUpLineElementsContext *context) = 0;

    virtual antlrcpp::Any visitBoldItalicLineElements(zoiaParser::BoldItalicLineElementsContext *context) = 0;

    virtual antlrcpp::Any visitBoldLineElements(zoiaParser::BoldLineElementsContext *context) = 0;

    virtual antlrcpp::Any visitItalicLineElements(zoiaParser::ItalicLineElementsContext *context) = 0;

    virtual antlrcpp::Any visitTextFragment(zoiaParser::TextFragmentContext *context) = 0;

    virtual antlrcpp::Any visitWord(zoiaParser::WordContext *context) = 0;

    virtual antlrcpp::Any visitAlias(zoiaParser::AliasContext *context) = 0;

    virtual antlrcpp::Any visitCommand(zoiaParser::CommandContext *context) = 0;

    virtual antlrcpp::Any visitArguments(zoiaParser::ArgumentsContext *context) = 0;

    virtual antlrcpp::Any visitArgument(zoiaParser::ArgumentContext *context) = 0;

    virtual antlrcpp::Any visitKwdArgument(zoiaParser::KwdArgumentContext *context) = 0;

    virtual antlrcpp::Any visitStdArgument(zoiaParser::StdArgumentContext *context) = 0;

    virtual antlrcpp::Any visitWhitespace(zoiaParser::WhitespaceContext *context) = 0;


};
