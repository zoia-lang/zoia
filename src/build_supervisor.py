# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2022 Infernio
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
"""This module supervises the entire build process by launching the various
shared and backend tasks."""
from pathlib import Path

import log
from build_shared import AliasesEvaluator
from project import Project, ZoiaFile

def build(project: Project):
    """Builds the specified project based on its config."""
    log.info('Beginning to build project')
    proj_path = project.project_path
    series_f = project.series
    series_rel = series_f.series_path.relative_to(proj_path)
    log.info(log.arrow(1, f'Building series at {log.color_dir(series_rel)}'))
    # Stage 1: Evaluating the aliases.zoia file (TODO use, see stage 4)
    evaluate_aliases(project)
    # Stage 2: Evaluating the dictionary.zoia file (TODO)
    # Stage 3: Inserting fragments (TODO)
    # Stage 4: Resolving aliases (TODO)
    # Stage 5: Building backend IR from the works and chapters
    for work in series_f.works:
        work_rel = work.work_path.relative_to(proj_path)
        log.info(log.arrow(2, f'Building work at {log.color_dir(work_rel)}'))
        for chapter in work.chapters:
            chapter_rel = chapter.chapter_path.relative_to(proj_path)
            log.info(log.arrow(3, f'Building chapter at '
                                  f'{log.color_dir(chapter_rel)}'))
            build_ir(proj_path, chapter.main_file)

def evaluate_aliases(project):
    """Handles stage 1 of building, evaluating the aliases.zoia file."""
    aliases_f = project.aliases_file
    aliases_rel = aliases_f.file_path.relative_to(project.project_path)
    log.info(log.arrow(2, f'Evaluating aliases file at '
                          f'{log.color_file(aliases_rel)}'))
    als_tree = aliases_f.file_ast
    als_eval = AliasesEvaluator()
    return als_eval.visit(als_tree)

def build_ir(proj_path: Path, zoia_main: ZoiaFile):
    """Handles stage 5 of building, building backend-specific IR. This is done
    for a single file here."""
    main_rel = zoia_main.file_path.relative_to(proj_path)
    log.info(log.arrow(4, f'Evaluating {log.color_file(main_rel)}'))
