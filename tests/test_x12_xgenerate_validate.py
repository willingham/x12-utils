from x12_utils.x12_generator import x12_generate
from x12_utils.x12_validator import x12_validate
import tests.edi_samples as foo

from tests.edi_samples import (
    generator_input_valid_edi,
    valid_edi
)


def test_generate_validate_valid():
    edi = x12_generate(
        src=generator_input_valid_edi,
    )
    result = x12_validate(
        src=edi
    )
    assert result["ok"] is True
