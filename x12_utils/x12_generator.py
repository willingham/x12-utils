from typing import List, IO, Tuple, Union


def x12_generate(
    src: List[Tuple[str, Union[List[str], None]]],
    output_file: Union[IO[str], None] = None,
    element_separator: str = "*",
    segment_separator: str = "~",
    sub_element_separator: str = ":",
):
    """
    Generates edi based on input in list format

    :param src: edi information in the format
        ["Segment Identifier" ("Element 1", "Element 2", ...)]
    :param element_separator: Separator for elements; default is "*"
    :param segment_separator: Separator for segments; default is "~"
    :param sub_element_separator: Separator for sub-elements; default is ":"
    :returns: String containing syntactically valid edi (not necessarily structurally valid)
    """
    output = ""
    total_lines = 0
    for e in src:
        car = e[0]
        cdr = e[1]

        if cdr is None:
            continue
        while len(cdr) is not 0 and cdr[-1] is "":
            # Don't leave trailing element separators
            cdr = cdr[:-1]
        if len(cdr) is 0:
            continue

        line = (
            car
            + element_separator
            + element_separator.join(cdr)
            + segment_separator
            + "\n"
        )
        output += line
        total_lines += 1

    return output
