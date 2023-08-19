# colour defaults
CC1 = 198
CC2 = 80
construction_purple = 136
house_magic_red_colour = 40
house_magic_safe_colour = 170

recolour_CC2_to_CC1 = {
    CC2: CC1,
    CC2 + 1: CC1 + 1,
    CC2 + 2: CC1 + 2,
    CC2 + 3: CC1 + 3,
    CC2 + 4: CC1 + 4,
    CC2 + 5: CC1 + 5,
    CC2 + 6: CC1 + 6,
    CC2 + 7: CC1 + 7,
}
recolour_CC1_to_CC2 = {
    CC1: CC2,
    CC1 + 1: CC2 + 1,
    CC1 + 2: CC2 + 2,
    CC1 + 3: CC2 + 3,
    CC1 + 4: CC2 + 4,
    CC1 + 5: CC2 + 5,
    CC1 + 6: CC2 + 6,
    CC1 + 7: CC2 + 7,
}

construction_purple_recolour_CC1 = {
    construction_purple: CC1,
    construction_purple + 1: CC1 + 1,
    construction_purple + 2: CC1 + 2,
    construction_purple + 3: CC1 + 3,
    construction_purple + 4: CC1 + 4,
    construction_purple + 5: CC1 + 5,
    construction_purple + 6: CC1 + 6,
    construction_purple + 7: CC1 + 7,
}
hull_recolour_CC1 = construction_purple_recolour_CC1
construction_purple_recolour_CC2 = {
    construction_purple: CC2,
    construction_purple + 1: CC2 + 1,
    construction_purple + 2: CC2 + 2,
    construction_purple + 3: CC2 + 3,
    construction_purple + 4: CC2 + 4,
    construction_purple + 5: CC2 + 5,
    construction_purple + 6: CC2 + 6,
    construction_purple + 7: CC2 + 7,
}
hull_recolour_CC2 = construction_purple_recolour_CC2
hull_recolour_white = {
    construction_purple: 8,
    construction_purple + 1: 9,
    construction_purple + 2: 10,
    construction_purple + 3: 11,
    construction_purple + 4: 12,
    construction_purple + 5: 13,
    construction_purple + 6: 14,
    construction_purple + 7: 15,
}
hull_recolour_silver = {
    construction_purple: 16,
    construction_purple + 1: 17,
    construction_purple + 2: 18,
    construction_purple + 3: 19,
    construction_purple + 4: 20,
    construction_purple + 5: 21,
    construction_purple + 6: 22,
    construction_purple + 7: 23,
}
hull_recolour_dark_blue = {
    construction_purple: 144,
    construction_purple + 1: 145,
    construction_purple + 2: 146,
    construction_purple + 3: 147,
    construction_purple + 4: 148,
    construction_purple + 5: 149,
    construction_purple + 6: 150,
    construction_purple + 7: 151,
}
hull_recolour_dark_grey = {
    construction_purple: 33,
    136 + 1: 34,
    136 + 2: 6,
    136 + 3: 7,
    136 + 4: 20,
    136 + 5: 21,
    136 + 6: 22,
    136 + 7: 39,
}
hull_recolour_dirty_black = {
    construction_purple: 70,
    136 + 1: 71,
    136 + 2: 33,
    136 + 3: 5,
    136 + 4: 6,
    136 + 5: 35,
    136 + 6: 7,
    136 + 7: 8,
}

tanker_livery_recolour_maps = {
    construction_purple: CC1,
    construction_purple + 1: CC1 + 1,
    construction_purple + 2: CC1 + 2,
    construction_purple + 3: CC1 + 3,
    construction_purple + 4: CC1 + 4,
    construction_purple + 5: CC1 + 5,
    construction_purple + 6: CC1 + 6,
    construction_purple + 7: CC1 + 7,
}

# used because it's nicer to draw with dark red as magic colour, but it's not safe as a magic colour, so it's remapped to a spare purple range
house_make_magic_red_safe_recolour_map = {
    house_magic_red_colour: house_magic_safe_colour,
    house_magic_red_colour + 1: house_magic_safe_colour + 1,
    house_magic_red_colour + 2: house_magic_safe_colour + 2,
    house_magic_red_colour + 3: house_magic_safe_colour + 3,
    house_magic_red_colour + 4: house_magic_safe_colour + 4,
    house_magic_red_colour + 5: house_magic_safe_colour + 5,
    house_magic_red_colour + 6: house_magic_safe_colour + 6,
    house_magic_red_colour + 7: house_magic_safe_colour + 7,
}
# arbitrary house recolouring maps
house_recolour_roof_CC1_1 = {
    house_magic_safe_colour: CC1,
    house_magic_safe_colour + 1: CC1 + 1,
    house_magic_safe_colour + 2: CC1 + 2,
    house_magic_safe_colour + 3: CC1 + 3,
    house_magic_safe_colour + 4: CC1 + 4,
    house_magic_safe_colour + 5: CC1 + 5,
    house_magic_safe_colour + 6: CC1 + 6,
    house_magic_safe_colour + 7: CC1 + 7,
}
house_recolour_roof_dark_red_1 = {
    house_magic_safe_colour: 40,
    house_magic_safe_colour + 1: 41,
    house_magic_safe_colour + 2: 42,
    house_magic_safe_colour + 3: 43,
    house_magic_safe_colour + 4: 44,
    house_magic_safe_colour + 5: 45,
    house_magic_safe_colour + 6: 46,
    house_magic_safe_colour + 7: CC1 + 7,
}
house_recolour_roof_silver_1 = {
    house_magic_safe_colour: 16,
    house_magic_safe_colour + 1: 17,
    house_magic_safe_colour + 2: 18,
    house_magic_safe_colour + 3: 19,
    house_magic_safe_colour + 4: 20,
    house_magic_safe_colour + 5: 21,
    house_magic_safe_colour + 6: 22,
    house_magic_safe_colour + 7: 23,
}
house_recolour_roof_rust_1 = {
    house_magic_safe_colour: 60,
    house_magic_safe_colour + 1: 72,
    house_magic_safe_colour + 2: 123,
    house_magic_safe_colour + 3: 74,
    house_magic_safe_colour + 4: 75,
    house_magic_safe_colour + 5: 76,
    house_magic_safe_colour + 6: 77,
    house_magic_safe_colour + 7: 78,
}

# arbitrary deck recolouring maps
deck_recolour_map_CC1 = {
    70: CC1,
    60: CC1 + 1,
    72: CC1 + 2,
    123: CC1 + 3,
    74: CC1 + 4,
    75: CC1 + 5,
}
deck_recolour_map_dark_red_1 = {
    70: 40,
    60: 41,
    72: 42,
    123: 43,
    74: 44,
    75: 45,
}
deck_recolour_map_merchandise_1 = {
    70: 104,
    60: 105,
    72: 32,
    123: 33,
    74: 34,
    75: 35,
}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 100
spritesheet_top_margin = 10
spritesheet_width = 1200

# --- Livery Recolour Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# keep cargos in alphabetical order for ease of reading
# DFLT label is a hack to provide specific livery for unknown cargos and should not be added to cargo translation table

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = (
    {170 + i: CC1 + i for i in range(8)},
    {170 + i: CC2 + i for i in range(8)},
    {170 + i: 8 + i for i in range(8)},
)
