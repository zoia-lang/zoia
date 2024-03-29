/*
 * This file was auto-generated by speedy-antlr-tool v1.4.1
 *  https://github.com/amykyta3/speedy-antlr-tool
 */

#pragma once

#include "zoiaBaseVisitor.h"
#include "speedy_antlr.h"

class SA_zoiaTranslator : public zoiaBaseVisitor {
    speedy_antlr::Translator *translator;

    // Cached context classes
    PyObject *ZoiaFileContext_cls = NULL;
    PyObject *HeaderContext_cls = NULL;
    PyObject *LineContext_cls = NULL;
    PyObject *LineElementsContext_cls = NULL;
    PyObject *LineElementsInnerContext_cls = NULL;
    PyObject *LineElementsArgContext_cls = NULL;
    PyObject *Em3LineElementContext_cls = NULL;
    PyObject *Em2LineElementContext_cls = NULL;
    PyObject *Em1LineElementContext_cls = NULL;
    PyObject *TextFragmentContext_cls = NULL;
    PyObject *TextFragmentWordContext_cls = NULL;
    PyObject *AliasContext_cls = NULL;
    PyObject *CommandContext_cls = NULL;
    PyObject *ArgumentsContext_cls = NULL;
    PyObject *ArgumentContext_cls = NULL;
    PyObject *KwdArgumentContext_cls = NULL;
    PyObject *StdArgumentContext_cls = NULL;
    PyObject *WhitespaceContext_cls = NULL;

    public:
    SA_zoiaTranslator(speedy_antlr::Translator *translator);
    ~SA_zoiaTranslator();
    antlrcpp::Any visitZoiaFile(zoiaParser::ZoiaFileContext *ctx);

    antlrcpp::Any visitHeader(zoiaParser::HeaderContext *ctx);

    antlrcpp::Any visitLine(zoiaParser::LineContext *ctx);

    antlrcpp::Any visitLineElements(zoiaParser::LineElementsContext *ctx);

    antlrcpp::Any visitLineElementsInner(zoiaParser::LineElementsInnerContext *ctx);

    antlrcpp::Any visitLineElementsArg(zoiaParser::LineElementsArgContext *ctx);

    antlrcpp::Any visitEm3LineElement(zoiaParser::Em3LineElementContext *ctx);

    antlrcpp::Any visitEm2LineElement(zoiaParser::Em2LineElementContext *ctx);

    antlrcpp::Any visitEm1LineElement(zoiaParser::Em1LineElementContext *ctx);

    antlrcpp::Any visitTextFragment(zoiaParser::TextFragmentContext *ctx);

    antlrcpp::Any visitTextFragmentWord(zoiaParser::TextFragmentWordContext *ctx);

    antlrcpp::Any visitAlias(zoiaParser::AliasContext *ctx);

    antlrcpp::Any visitCommand(zoiaParser::CommandContext *ctx);

    antlrcpp::Any visitArguments(zoiaParser::ArgumentsContext *ctx);

    antlrcpp::Any visitArgument(zoiaParser::ArgumentContext *ctx);

    antlrcpp::Any visitKwdArgument(zoiaParser::KwdArgumentContext *ctx);

    antlrcpp::Any visitStdArgument(zoiaParser::StdArgumentContext *ctx);

    antlrcpp::Any visitWhitespace(zoiaParser::WhitespaceContext *ctx);

};