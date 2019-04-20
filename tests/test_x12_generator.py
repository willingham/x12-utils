from x12_utils.x12_generator import x12_generate
import tests.edi_samples as foo

from tests.edi_samples import (
    generator_input_basic,
    generator_input_empty_elements,
    generator_input_no_elements,
    generator_output_basic,
    generator_output_basic_custom_separators,
    generator_output_empty_elements,
    generator_output_no_elements
)


def test_generator_basic():
    result = x12_generate(
        src=generator_input_basic,
    )
    assert result == generator_output_basic

def test_generator_empty_elements():
    result = x12_generate(
        src=generator_input_empty_elements,
    )
    assert result == generator_output_empty_elements

def test_generator_no_elements():
    result = x12_generate(
        src=generator_input_no_elements,
    )
    assert result == generator_output_no_elements

def test_generator_custom_separators():
    result = x12_generate(
        src=generator_input_basic,
        element_separator="@",
        segment_separator="#",
        sub_element_separator="$"
    )
    assert result == generator_output_basic_custom_separators
