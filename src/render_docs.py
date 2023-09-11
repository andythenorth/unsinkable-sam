import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
import multiprocessing
from itertools import repeat
from time import time
from PIL import Image
import markdown

import global_constants
import utils as utils
import unsinkable_sam
from polar_fox import git_info
from doc_helper import DocHelper

# !! this is done differently in iron horse, with registered rosters fetched from iron_horse module
from rosters import registered_rosters

metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

docs_src = os.path.join(currentdir, "src", "docs_templates")

def render_docs(
    doc_list,
    file_type,
    docs_output_path,
    doc_helper,
    ships,
    use_markdown=False,
    source_is_repo_root=False,
):
    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(doc_path, format="text")

    for doc_name in doc_list:
        template = docs_templates[
            doc_name + ".pt"
        ]  # .pt is the conventional extension for chameleon page templates
        doc = template(
            ships=ships,
            registered_rosters=registered_rosters,
            global_constants=global_constants,
            makefile_args=makefile_args,
            git_info=git_info,
            metadata=metadata,
            utils=utils,
            doc_helper=doc_helper,
            doc_name=doc_name,
        )
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates["markdown_wrapper.pt"]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                global_constants=global_constants,
                makefile_args=makefile_args,
                git_info=git_info,
                metadata=metadata,
                utils=utils,
                doc_helper=doc_helper,
                doc_name=doc_name,
            )
        if file_type == "html":
            subdir = "html"
        else:
            subdir = ""
        # save the results of templating
        doc_file = codecs.open(
            os.path.join(docs_output_path, subdir, doc_name + "." + file_type),
            "w",
            "utf8",
        )
        doc_file.write(doc)
        doc_file.close()


def render_docs_vehicle_details(ship, docs_output_path, doc_helper, ships):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(docs_src, format="text")
    template = docs_templates["vehicle_details.pt"]
    doc_name = ship.id
    doc = template(
        ship=ship,
        ships=ships,
        global_constants=global_constants,
        registered_rosters=unsinkable_sam.registered_rosters,
        makefile_args=makefile_args,
        git_info=git_info,
        metadata=metadata,
        utils=utils,
        doc_helper=doc_helper,
        doc_name=doc_name,
    )
    doc_file = codecs.open(
        os.path.join(docs_output_path, "html", doc_name + ".html"), "w", "utf8"
    )
    doc_file.write(doc)
    doc_file.close()


def render_docs_images(ship, docs_output_path, doc_helper):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    vehicle_graphics_src = os.path.join(currentdir, "generated", "graphics")
    buy_menu_bb = global_constants.spritesheet_bounding_boxes[6]
    vehicle_spritesheet = Image.open(
        os.path.join(vehicle_graphics_src, ship.id + ".png")
    )
    processed_vehicle_image = vehicle_spritesheet.crop(
        box=(
            buy_menu_bb[0],
            10
            + global_constants.spritesheet_bounding_boxes[2][2]
            - global_constants.docs_ship_image_height,
            buy_menu_bb[0] + ship.buy_menu_width,
            10 + global_constants.spritesheet_bounding_boxes[2][2],
        )
    )
    # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
    processed_vehicle_image = processed_vehicle_image.resize(
        (
            4 * ship.buy_menu_width,
            4 * global_constants.buy_menu_sprite_height,
        ),
        resample=Image.Resampling.NEAREST,
    )

    output_path = os.path.join(
        currentdir,
        "docs",
        "html",
        "static",
        "img",
        ship.id + ".png",
        # ship.id + "_" + colour_name + ".png",
    )
    processed_vehicle_image.save(output_path, optimize=True, transparency=0)


def main():
    print("[RENDER DOCS] render_docs.py")
    start = time()
    unsinkable_sam.main()

    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = makefile_args.get("num_pool_workers", 0)
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print("Multiprocessing disabled: (PW=0)")
    else:
        use_multiprocessing = True
        # logger = multiprocessing.log_to_stderr()
        # logger.setLevel(25)
        # just print, no need for a coloured echo_message
        print("Multiprocessing enabled: (PW=" + str(num_pool_workers) + ")")

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir
    )
    if not os.path.exists(chameleon_cache_path):
        os.mkdir(chameleon_cache_path)
    os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

    docs_output_path = os.path.join(currentdir, "docs")
    if os.path.exists(docs_output_path):
        shutil.rmtree(docs_output_path)
    os.mkdir(docs_output_path)

    shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)

    static_dir_src = os.path.join(docs_src, "html", "static")
    static_dir_dst = os.path.join(docs_output_path, "html", "static")
    shutil.copytree(static_dir_src, static_dir_dst)

    ships = unsinkable_sam.get_ships_in_buy_menu_order()
    # default sort for docs is by ship intro date
    ships = sorted(ships, key=lambda ship: ship.intro_date)

    doc_helper = DocHelper(lang_strings=utils.get_lang_data("english", ships)["lang_strings"])

    dates = sorted([i.intro_date for i in ships])
    metadata["dates"] = (dates[0], dates[-1])

    # render standard docs from a list
    html_docs = [
        "ships",
        "code_reference",
        "get_started",
        "translations",
        "tech_tree_table_blue",
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]

    render_docs(html_docs, "html", docs_output_path, doc_helper, ships)
    render_docs(txt_docs, "txt", docs_output_path, doc_helper, ships)
    render_docs(
        license_docs,
        "txt",
        docs_output_path,
        doc_helper,
        ships,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, "txt", docs_output_path, doc_helper, ships)
    render_docs(markdown_docs, "html", docs_output_path, doc_helper, ships, use_markdown=True)

    # render vehicle details
    for ship in ships:
        render_docs_vehicle_details(ship, docs_output_path, doc_helper, ships)


    # process images for use in docs
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    slow_start = time()
    if use_multiprocessing == False:
        for ship in ships:
            render_docs_images(ship, docs_output_path, doc_helper)
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = multiprocessing.Pool(processes=num_pool_workers)
        pool.starmap(
            render_docs_images,
            zip(ships, repeat(docs_output_path), repeat(doc_helper)),
        )
        pool.close()
        pool.join()
    print("render_docs_images", time() - slow_start)

    print(
        "[RENDER DOCS]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
