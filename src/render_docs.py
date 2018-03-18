print("[RENDER DOCS] render_docs.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir
from time import time

from PIL import Image

import global_constants
import utils as utils
import unsinkable_sam

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

docs_src = os.path.join(currentdir, 'src', 'docs_templates')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src,'index.html'), docs_output_path)

static_dir_src = os.path.join(docs_src, 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

# we'll be processing some extra images and saving them into the img dir
images_dir_dst = os.path.join(static_dir_dst, 'img')

import markdown
from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(docs_src, format='text')

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()



ships = unsinkable_sam.get_ships_in_buy_menu_order()
# default sort for docs is by ship intro date
ships = sorted(ships, key=lambda ship: ship.intro_date)

from rosters import registered_rosters

metadata = {}
dates = sorted([i.intro_date for i in ships])
metadata['dates'] = (dates[0], dates[-1])
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?f=26&t=44613'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/unsinkable_sam/repository'
metadata['issue_tracker'] = 'http://dev.openttdcoop.org/projects/unsinkable_sam/issues'

class DocHelper(object):
    # dirty class to help do some doc formatting

    def get_ships_by_subclass(self):
        ships_by_subclass = {}
        for ship in ships:
            subclass = type(ship)
            if subclass in ships_by_subclass:
                ships_by_subclass[subclass].append(ship)
            else:
                ships_by_subclass[subclass] = [ship]
        return ships_by_subclass

    def get_roster_name(self, index):
        return base_lang_strings.get('STR_PARAM_ROSTER_OPTION_' + str(index), '')

    def fetch_prop(self, result, prop_name, value):
        result['ship'][prop_name] = value
        result['subclass_props'].append(prop_name)
        return result

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for ship in self.get_ships_by_subclass()[subclass]:
            result = {'ship':{}, 'subclass_props': []}

            result = self.fetch_prop(result, 'Ship Name', ship.get_name_substr() + base_lang_strings[ship.get_str_name_suffix()])
            result = self.fetch_prop(result, 'Extra Info', base_lang_strings[ship.get_str_type_info()])
            result = self.fetch_prop(result, 'Speed Laden', int(ship.speed))
            result = self.fetch_prop(result, 'Intro Date', ship.intro_date)
            result = self.fetch_prop(result, 'Vehicle Life', ship.vehicle_life)
            result = self.fetch_prop(result, 'Capacity', ship.default_capacity)
            result = self.fetch_prop(result, 'Buy Cost', ship.buy_cost)
            result = self.fetch_prop(result, 'Running Cost', ship.running_cost)
            result = self.fetch_prop(result, 'Loading Speed', ship.loading_speed)

            props_to_print[ship] = result['ship']
            props_to_print[subclass] = result['subclass_props']

        return props_to_print

    def get_base_numeric_id(self, vehicle):
        return vehicle.numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]

def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(ships=ships, registered_rosters=registered_rosters, global_constants=global_constants,
                       makefile_args=makefile_args, base_lang_strings=base_lang_strings, metadata=metadata,
                       utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates['markdown_wrapper.pt']
            doc = markdown_wrapper(content=markdown.markdown(doc), global_constants=global_constants, makefile_args=makefile_args,
                              metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if file_type == 'html':
            subdir = 'html'
        else:
            subdir = ''
        # save the results of templating
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()

def render_docs_images():
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    vehicle_graphics_src = os.path.join(currentdir, 'generated', 'graphics')
    buy_menu_bb = global_constants.spritesheet_bounding_boxes[6]
    for ship in ships:
        vehicle_spritesheet = Image.open(os.path.join(vehicle_graphics_src, ship.id + '.png'))
        processed_vehicle_image = vehicle_spritesheet.crop(box=(buy_menu_bb[0],
                                                                10 + ship.buy_menu_bb_y_offset,
                                                                buy_menu_bb[0] + global_constants.buy_menu_sprite_width,
                                                                10 + ship.buy_menu_bb_y_offset + global_constants.buy_menu_sprite_height))
        # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
        processed_vehicle_image = processed_vehicle_image.resize((4 * global_constants.buy_menu_sprite_width, 4 * global_constants.buy_menu_sprite_height),
                                                                  resample=Image.NEAREST)
        output_path = os.path.join(images_dir_dst, ship.id + '.png')
        processed_vehicle_image.save(output_path, optimize=True, transparency=0)

def main():
    start = time()
    # render standard docs from a list
    html_docs = ['ships', 'code_reference', 'get_started', 'translations']
    txt_docs = ['license', 'readme']
    markdown_docs = ['changelog']

    render_docs(html_docs, 'html')
    render_docs(txt_docs, 'txt')
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt')
    render_docs(markdown_docs, 'html', use_markdown=True)
    # process images for use in docs
    render_docs_images()
    # eh, how long does this take anyway?
    print(format((time() - start), '.2f')+'s')

if __name__ == '__main__':
    main()
