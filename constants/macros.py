"""
Contains information about built-in macros.
"""


def built_in_macros() -> list:
    """
    Return a list of hardcoded built-in macros.
    """

    macros_list = [
        {
            'name': 'Two-handing a right weapon',
            'keyline': 'event_action+attack',
            'comment': 'For those who miss the days when it could be done with one button.',
        },
        {
            'name': 'Two-handing a left weapon',
            'keyline': 'event_action+guard',
            'comment': 'For those who miss the days when it could be done with one button.',
        },
        {
            'name': 'Four invasion attempts (wide)',
            'keyline': (
                               f'{keyline_to_invade_as_bloody_finger(True)}|pause4000|{keyline_to_invade_as_recusant(True)}|pause4000|'
                               * 2
                       )[:-10],
            'comment': 'Performs an attempt to invade as bloody finger,\n'
                       'then attempt to invade as recusant, and so two times.\n'
                       '\n'
                       "Usually that's enough to invade even with mediocre connection\n"
                       'and get a snack from kitchen.\n'
                       '\n'
                       'Invades over all map.',
        },
        {
            'name': 'Four invasion attempts (local)',
            'keyline': (
                               f'{keyline_to_invade_as_bloody_finger()}|pause4000|{keyline_to_invade_as_recusant()}|pause4000'
                               * 2
                       )[:-10],
            'comment': 'Performs an attempt to invade as bloody finger,\n'
                       'then attempt to invade as recusant, and so two times.\n'
                       '\n'
                       "Usually that's enough to invade even with mediocre connection\n"
                       'and get a snack from kitchen.\n'
                       '\n'
                       'Invades locally.',
        },
        {
            'name': 'Six invasion attempts (wide)',
            'keyline': (
                f'{keyline_to_invade_as_bloody_finger(True)}|pause4000|{keyline_to_invade_as_recusant(True)}|pause4000|'
                * 1
            )[:-10],
            'comment': 'Performs an attempt to invade as bloody finger,\n'
            'then attempt to invade as recusant, and so three times.\n'
            '\n'
            "Usually that's enough to invade even with mediocre connection\n"
            'and get a snack from kitchen.\n'
            '\n'
            'Invades over all map.',
        },
        {
            'name': 'Six invasion attempts (local)',
            'keyline': (
                f'{keyline_to_invade_as_bloody_finger()}|pause4000|{keyline_to_invade_as_recusant()}|pause4000'
                * 3
            )[:-10],
            'comment': 'Performs an attempt to invade as bloody finger,\n'
            'then attempt to invade as recusant, and so three times.\n'
            '\n'
            "Usually that's enough to invade even with mediocre connection\n"
            'and get a snack from kitchen.\n'
            '\n'
            'Invades locally.',
        },
        {
            'name': 'Fast quit to main menu',
            'keyline': 'esc|up|e|z|e|left|e',
            'comment': 'Quits to main menu very fast.\n'
            '\n'
            'Useful if you lost to gravity but still want to cheat death.',
        },
        {
            'name': "Use Duelist's Furled Finger",
            'keyline': 'esc|up|up|e|down|down|e',
            'comment': "Uses Duelist's Furled Finger to get back to battle after\n"
            'loosing as fast as possible.',
        },
        {
            'name': "Use Tarnished's Furled Finger",
            'keyline': 'esc|up|up|e|down|e',
            'comment': "Uses Tarnished's Furled Finger to help other Tarnished\n"
            'as fast as possible.',
        },
        {
            'name': 'Sort all: Asc. Acquisition',
            'keyline': keyline_to_sort_all_lists(),
            'comment': "Sorts all lists that are used by Melina's Fingers to\n"
            '"Order of Acquisition", ascended.\n'
            '\n'
            "It's very important hotkey due to the fact that equipment hotkeys\n"
            "just won't work if lists are ordered differently.\n"
            '\n'
            'Press it once in the beginning of gaming session\n'
            'and everything will be fine.\n'
            '\n'
            'By the way, "Order of Acquisition", Asc. is chosen due to two reasons:\n'
            "   1) that's easiest order to be calculated via save file;\n"
            '   2) it allows to pick up new weapons in PvE as new weapons go to\n'
            '      the end of the list.',
        },
        {
            'name': 'Crouch attack',
            'keyline': 'crouch|attack',
            'comment': "May be very useful on weapons with powerful crouch attack,\n"
                       "like claymore. ",
        },
        {
            'name': 'Crouch attack (dual wield)',
            'keyline': 'crouch|guard',
            'comment': "May be very useful on weapons with powerful crouch attack,\n"
                       "like dual katanas or dual lances. ",
        },
        {
            'name': 'Stance attack',
            'keyline': 'skill|attack',
            'comment': 'Goes to stance, then immediately perform an attack.',
        },
        {
            'name': 'Stance strong attack',
            'keyline': 'skill|strong_attack',
            'comment': 'Goes to stance, then immediately perform a strong attack.',
        },
        {
            'name': 'Left weapon skill',
            'keyline': 'event_action+guard|pause200|skill',
            'comment': 'Takes weapons from left hand to both hands and performs\n'
            "it's skill immediately.",
        },
        {
            'name': 'Next weapon (right)',
            'keyline': keyline_to_choose_next_weapon(),
            'comment': 'Chooses next weapon in list for right hand.\n'
            '\n'
            'You can choose 3 weapons for Right Hand Armament 1 slot\n'
            'and play like Dante in classic weapon-juggling Devil May Cry style.',
        },
        {
            'name': 'Previous weapon (right)',
            'keyline': keyline_to_choose_previous_weapon(),
            'comment': 'Chooses previous weapon in list for right hand.\n'
            '\n'
            'You can choose 3 weapons for Right Hand Armament 1 slot\n'
            'and play like Dante in classic weapon-juggling Devil May Cry style.',
        },
        {
            'name': 'Next weapon (left)',
            'keyline': keyline_to_choose_next_weapon(left_hand=True),
            'comment': 'Chooses next weapon in list for left hand.\n'
            '\n'
            'You can choose 3 weapons for Left Hand Armament 1 slot\n'
            'and play like Vergil in classic weapon-juggling Devil May Cry style.',
        },
        {
            'name': 'Previous weapon (left)',
            'keyline': keyline_to_choose_previous_weapon(left_hand=True),
            'comment': 'Chooses previous weapon in list for left hand.\n'
            '\n'
            'You can choose 3 weapons for Left Hand Armament 1 slot\n'
            'and play like Vergil in classic weapon-juggling Devil May Cry style.',
        },
    ]

    # Use item macros.
    for i in range(1, 11):
        macros_list.append(
            {
                'name': f'Switch to quick item {str(i)}',
                'keyline': f'switch_item_press600{"|switch_item|pause10" * (i - 1)}',
                'comment': f'Selects item {i} from quick item list.',
            }
        )

    # Switch to spell macros.
    for i in range(1, 13):
        macros_list.append(
            {
                'name': f'Switch to spell {str(i)}',
                'keyline': f'switch_spell_press600{"|switch_spell|pause10" * (i - 1)}',
                'comment': f'Selects spell {i} from spell list.',
            }
        )

    # Six gestures.
    macros_list.append(
        {
            'name': f'Gesture 1',
            'keyline': f'esc|right|down|down|down|e|esc',
            'comment': f'Performs gesture 1.',
        }
    )
    macros_list.append(
        {
            'name': f'Gesture 2',
            'keyline': f'esc|left|down|down|down|e|esc',
            'comment': f'Performs gesture 2',
        }
    )
    macros_list.append(
        {
            'name': f'Gesture 3',
            'keyline': f'esc|right|up|up|e|esc',
            'comment': f'Performs gesture 2',
        }
    )
    macros_list.append(
        {
            'name': f'Gesture 4',
            'keyline': f'esc|left|up|up|e|esc',
            'comment': f'Performs gesture 2',
        }
    )
    macros_list.append(
        {
            'name': f'Gesture 5',
            'keyline': f'esc|right|up|e|esc',
            'comment': f'Performs gesture 2',
        }
    )
    macros_list.append(
        {
            'name': f'Gesture 6',
            'keyline': f'esc|left|up|e|esc',
            'comment': f'Performs gesture 2',
        }
    )


    # Six pouch items.
    macros_list.append(
        {
            'name': f'Pouch item 1',
            'keyline': f'esc|right|e|esc',
            'comment': f'Use item 1 in pouch.',
        }
    )
    macros_list.append(
        {
            'name': f'Pouch item 2',
            'keyline': f'esc|left|e|esc',
            'comment': f'Use item 2 in pouch.',
        }
    )
    macros_list.append(
        {
            'name': f'Pouch item 3',
            'keyline': f'esc|right|down|e|esc',
            'comment': f'Use item 3 in pouch.',
        }
    )
    macros_list.append(
        {
            'name': f'Pouch item 4',
            'keyline': f'esc|left|down|e|esc',
            'comment': f'Use item 4 in pouch.',
        }
    )
    macros_list.append(
        {
            'name': f'Pouch item 5',
            'keyline': f'esc|right|down|down|e|esc',
            'comment': f'Use item 5 in pouch.',
        }
    )
    macros_list.append(
        {
            'name': f'Pouch item 6',
            'keyline': f'esc|left|down|down|e|esc',
            'comment': f'Use item 6 in pouch.',
        }
    )
    return macros_list


def keyline_to_sort_all_lists() -> str:
    """
    Returns a keyline for a macros that sorts all lists to "date get - up".
    Weapons, armor, talismans, items.
    """

    # 1. Weapons.
    # 2. Armor.
    # 3. Talismans.

    keyline = (
        'esc|e|pause50|e|t|down|e|pause300|q|pause300|'
        'down|down|e|pause50|t|down|e|pause300|q|pause300|'
        'down|e|pause50|t|down|e|pause300|esc'
    )

    return keyline


def keyline_to_invade_as_bloody_finger(wide_invade: bool = True) -> str:
    """
    Returns a keyline for a macros that uses bloody finger.
    """

    keyline = 'esc|up|up|e|up|up|e|e'

    if wide_invade:
        keyline += '|pause50|right|pause400'

    keyline += '|e|esc'

    return keyline


def keyline_to_invade_as_recusant(wide_invade: bool = True) -> str:
    """
    Returns a keyline for a macros that uses recusant finger.
    """

    keyline = 'esc|up|up|e|up|up|right|e|e'

    if wide_invade:
        keyline += '|pause50|right|pause400'

    keyline += '|e|esc'

    return keyline


def keyline_to_choose_next_weapon(weapons_pass: int = 0, left_hand=False) -> str:
    """
    Returns a macro keyline that chooses next weapon.
    """

    right_amount = weapons_pass + 1

    keyline = f'esc|e|{"down|" if left_hand else ""}e|{"right|" * right_amount}pause20|e|esc'
    return keyline


def keyline_to_choose_previous_weapon(weapons_pass: int = 0, left_hand=False) -> str:
    """
    Returns a macro keyline that chooses previous weapon.
    """

    left_amount = weapons_pass + 1

    keyline = f'esc|e|{"down|" if left_hand else ""}e|{"left|" * left_amount}pause20|e|esc'

    return keyline
