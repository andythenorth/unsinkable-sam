#!/usr/bin/env python

print("[RENDER NML] render_nml.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import sys
import os
currentdir = os.curdir
from multiprocessing import Pool

import unsinkable_sam
import utils
import global_constants
from rosters import registered_rosters

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)
num_pool_workers = repo_vars.get('num_pool_workers', 0) # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
if num_pool_workers == 0:
    use_multiprocessing = False
else:
    use_multiprocessing = True

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

generated_nml_path = os.path.join(unsinkable_sam.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

def render_consist_nml(consist):
    consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'w','utf8')
    consist_nml.write(utils.unescape_chameleon_output(consist.render()))
    consist_nml.close()

def main():
    # 'consists' even though they are ships, it's just more consistent with other grfs, makes maintaining these files simpler
    consists = unsinkable_sam.get_ships_in_buy_menu_order()

    grf_nml = codecs.open(os.path.join('unsinkable-sam.nml'),'w','utf8')
    header_items = ['header', 'cargo_table', 'disable_default_vehicles']
    for header_item in header_items:
        template = templates[header_item + '.pynml']
        grf_nml.write(utils.unescape_chameleon_output(template(consists=consists, global_constants=global_constants,
                                                      registered_rosters=registered_rosters,
                                                      utils=utils, sys=sys, repo_vars=repo_vars)))

    if use_multiprocessing == False:
        utils.echo_message('Multiprocessing disabled: (pw=0)')
        for consist in consists:
            render_consist_nml(consist)
    else:
        # multiprocessing is not always a win for rendering chameleon templates, the overhead can increase render time substantially
        # worth testing occasionally for empirical results
        pool = Pool(processes=num_pool_workers)
        pool.map(render_consist_nml, consists)

    for consist in consists:
        # makefile passes 'roster' arg, but there is no python compile support for compiling a single roster yet
        consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'r','utf8').read()
        grf_nml.write(consist_nml)

    grf_nml.close()

if __name__ == '__main__':
    main()
