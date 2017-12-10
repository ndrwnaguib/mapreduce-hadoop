#!/usr/bin/python

import sys


def _format_and_split(line, separator=','):
    # remove leading and trailing whitespace and split on separator
    return line.strip().split(separator)


def _emit(elements, separator=','):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print output_string


def _user_changed(user_previous_id, user_current_id):
    return user_previous_id and (user_previous_id != user_current_id)


def reducer():
    location = None
    true_location = "-"
    user_previous_id = None
    for line in sys.stdin:
        # parse the input we got from mapper.py
        line_elements = _format_and_split(line)
        # check if the input is valid data
        if len(line_elements) != 3:
            # if not ignore/discard this line
            continue
        user_current_id, product_id, location = line_elements
        if location != "-":
            true_location = location
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: store) before it is passed to the reducer
        if _user_changed(user_previous_id, user_current_id):
            product_id = "-"
        if product_id != "-" and true_location != "-":
            # write result to STDOUT through _emit function
            _emit([product_id, true_location])
        user_previous_id = user_current_id


if __name__ == '__main__':
    reducer()
