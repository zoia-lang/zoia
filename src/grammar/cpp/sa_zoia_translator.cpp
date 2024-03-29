/*
 * This file was auto-generated by speedy-antlr-tool v1.4.1
 *  https://github.com/amykyta3/speedy-antlr-tool
 */

#include "sa_zoia_translator.h"


SA_zoiaTranslator::SA_zoiaTranslator(speedy_antlr::Translator *translator) {
    this->translator = translator;
}

SA_zoiaTranslator::~SA_zoiaTranslator() {
    Py_XDECREF(ZoiaFileContext_cls);
    Py_XDECREF(HeaderContext_cls);
    Py_XDECREF(LineContext_cls);
    Py_XDECREF(LineElementsContext_cls);
    Py_XDECREF(LineElementsInnerContext_cls);
    Py_XDECREF(LineElementsArgContext_cls);
    Py_XDECREF(Em3LineElementContext_cls);
    Py_XDECREF(Em2LineElementContext_cls);
    Py_XDECREF(Em1LineElementContext_cls);
    Py_XDECREF(TextFragmentContext_cls);
    Py_XDECREF(TextFragmentWordContext_cls);
    Py_XDECREF(AliasContext_cls);
    Py_XDECREF(CommandContext_cls);
    Py_XDECREF(ArgumentsContext_cls);
    Py_XDECREF(ArgumentContext_cls);
    Py_XDECREF(KwdArgumentContext_cls);
    Py_XDECREF(StdArgumentContext_cls);
    Py_XDECREF(WhitespaceContext_cls);
}


antlrcpp::Any SA_zoiaTranslator::visitZoiaFile(zoiaParser::ZoiaFileContext *ctx){
    if(!ZoiaFileContext_cls) ZoiaFileContext_cls = PyObject_GetAttrString(translator->parser_cls, "ZoiaFileContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, ZoiaFileContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitHeader(zoiaParser::HeaderContext *ctx){
    if(!HeaderContext_cls) HeaderContext_cls = PyObject_GetAttrString(translator->parser_cls, "HeaderContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, HeaderContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitLine(zoiaParser::LineContext *ctx){
    if(!LineContext_cls) LineContext_cls = PyObject_GetAttrString(translator->parser_cls, "LineContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, LineContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitLineElements(zoiaParser::LineElementsContext *ctx){
    if(!LineElementsContext_cls) LineElementsContext_cls = PyObject_GetAttrString(translator->parser_cls, "LineElementsContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, LineElementsContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitLineElementsInner(zoiaParser::LineElementsInnerContext *ctx){
    if(!LineElementsInnerContext_cls) LineElementsInnerContext_cls = PyObject_GetAttrString(translator->parser_cls, "LineElementsInnerContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, LineElementsInnerContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitLineElementsArg(zoiaParser::LineElementsArgContext *ctx){
    if(!LineElementsArgContext_cls) LineElementsArgContext_cls = PyObject_GetAttrString(translator->parser_cls, "LineElementsArgContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, LineElementsArgContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitEm3LineElement(zoiaParser::Em3LineElementContext *ctx){
    if(!Em3LineElementContext_cls) Em3LineElementContext_cls = PyObject_GetAttrString(translator->parser_cls, "Em3LineElementContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, Em3LineElementContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitEm2LineElement(zoiaParser::Em2LineElementContext *ctx){
    if(!Em2LineElementContext_cls) Em2LineElementContext_cls = PyObject_GetAttrString(translator->parser_cls, "Em2LineElementContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, Em2LineElementContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitEm1LineElement(zoiaParser::Em1LineElementContext *ctx){
    if(!Em1LineElementContext_cls) Em1LineElementContext_cls = PyObject_GetAttrString(translator->parser_cls, "Em1LineElementContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, Em1LineElementContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitTextFragment(zoiaParser::TextFragmentContext *ctx){
    if(!TextFragmentContext_cls) TextFragmentContext_cls = PyObject_GetAttrString(translator->parser_cls, "TextFragmentContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, TextFragmentContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitTextFragmentWord(zoiaParser::TextFragmentWordContext *ctx){
    if(!TextFragmentWordContext_cls) TextFragmentWordContext_cls = PyObject_GetAttrString(translator->parser_cls, "TextFragmentWordContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, TextFragmentWordContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitAlias(zoiaParser::AliasContext *ctx){
    if(!AliasContext_cls) AliasContext_cls = PyObject_GetAttrString(translator->parser_cls, "AliasContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, AliasContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitCommand(zoiaParser::CommandContext *ctx){
    if(!CommandContext_cls) CommandContext_cls = PyObject_GetAttrString(translator->parser_cls, "CommandContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, CommandContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitArguments(zoiaParser::ArgumentsContext *ctx){
    if(!ArgumentsContext_cls) ArgumentsContext_cls = PyObject_GetAttrString(translator->parser_cls, "ArgumentsContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, ArgumentsContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitArgument(zoiaParser::ArgumentContext *ctx){
    if(!ArgumentContext_cls) ArgumentContext_cls = PyObject_GetAttrString(translator->parser_cls, "ArgumentContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, ArgumentContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitKwdArgument(zoiaParser::KwdArgumentContext *ctx){
    if(!KwdArgumentContext_cls) KwdArgumentContext_cls = PyObject_GetAttrString(translator->parser_cls, "KwdArgumentContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, KwdArgumentContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitStdArgument(zoiaParser::StdArgumentContext *ctx){
    if(!StdArgumentContext_cls) StdArgumentContext_cls = PyObject_GetAttrString(translator->parser_cls, "StdArgumentContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, StdArgumentContext_cls);
    return py_ctx;
}

antlrcpp::Any SA_zoiaTranslator::visitWhitespace(zoiaParser::WhitespaceContext *ctx){
    if(!WhitespaceContext_cls) WhitespaceContext_cls = PyObject_GetAttrString(translator->parser_cls, "WhitespaceContext");
    PyObject *py_ctx = translator->convert_ctx(this, ctx, WhitespaceContext_cls);
    return py_ctx;
}
