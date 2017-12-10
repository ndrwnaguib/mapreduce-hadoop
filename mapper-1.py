#!/usr/bin/python
import sys

USER_ID_INDEX_UDI = 0  # ID in UserDemographicInformation Dataset
PRODUCT_ID_INDEX = 1
USER_ID_INDEX_ITP = 2  # ID in ItemPurchases Dataset
USER_LOCATION_INDEX = 3


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


def mapper():
    location = "-"
    product_id = "-"
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # parse the input we got from mapper.py
        line_elements = _format_and_split(line)
        # check if the input is valid data
        if len(line_elements) == 4:  # Which means it is an UserDemographicInformation ROW
            user_id, email, language, location = line_elements
            _emit([user_id, product_id, location])
            location = '-'
            product_id = '-'
        elif len(line_elements) == 5:
            t_id, product_id, user_id, purchase_amount, product_description = line_elements
            _emit([user_id, product_id, location])
            location = '-'
            product_id = '-'
        else:
            # if not ignore/discard this line
            continue


if __name__ == '__main__':
    mapper()
