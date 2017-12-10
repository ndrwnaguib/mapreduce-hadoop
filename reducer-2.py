#!/usr/bin/python
import sys


def _format_and_split(line, separator=','):
    # remove leading and trailing whitespace and split on separator
    return line.strip().split(separator)


def _key_changed(key_of_previous_line, key_of_current_line):
    return (key_of_previous_line) and (key_of_previous_line != key_of_current_line)


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by appling function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print output_string


def reducer():
    total_sales_of_product = 0
    product_of_previous_line = None
    country_of_previous_line = None
    for line in sys.stdin:
        # parse the input we got from mapper.py
        line_elements = _format_and_split(line)
        # check if the input is valid data
        if len(line_elements) != 2:
            # if not ignore/discard this line
            continue

        product_of_current_line, country_of_current_line = line_elements

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: Key) before it is passed to the reducer
        if _key_changed(product_of_previous_line, product_of_current_line):
            _emit([product_of_previous_line, total_sales_of_product])
            total_sales_of_product = 0

        if _key_changed(country_of_previous_line, country_of_current_line):
            total_sales_of_product = total_sales_of_product + 1
        product_of_previous_line = product_of_current_line
        country_of_previous_line = country_of_current_line
    if product_of_previous_line:
        _emit([product_of_previous_line, total_sales_of_product])


if __name__ == '__main__':
    reducer()
