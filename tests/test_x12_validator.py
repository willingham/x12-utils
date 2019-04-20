from x12_utils import __version__
from x12_utils.x12_validator import x12_validate
from io import StringIO
from .edi_samples import invalid_edi, valid_edi


def test_version():
    assert __version__ == '0.1.0'

def test_valid_edi():
    result = x12_validate(
        src=valid_edi,
        params=None,
        generate_html=False,
        generate_997=False,
        generate_xml=False
    )
    assert result["ok"] is True
    assert result["html"] is ""
    assert result["997"] is ""
    assert result["xml"] is ""
    assert len(result["errors"]) is 0

def test_valid_edi_outputs():
    result = x12_validate(
        src=valid_edi,
        params=None,
        generate_html=True,
        generate_997=True,
        generate_xml=True
    )
    assert result["ok"] is True
    assert result["html"] is not  ""
    assert result["997"] is not ""
    assert result["xml"] is not ""
    assert len(result["errors"]) is 0

def test_custom_file_descriptor():
    fd = StringIO(valid_edi)
    result = x12_validate(
        src=fd,
        params=None,
        generate_html=False,
        generate_997=False,
        generate_xml=False
    )
    assert result["ok"] is True
    assert result["html"] is ""
    assert result["997"] is ""
    assert result["xml"] is ""
    assert len(result["errors"]) is 0

def test_invalid_edi():
    result = x12_validate(
        src=invalid_edi,
        params=None,
        generate_html=False,
        generate_997=False,
        generate_xml=False
    )
    print('result', result)
    assert result["ok"] is False
    assert result["html"] is ""
    assert result["997"] is ""
    assert result["xml"] is ""
    # @TODO Find a workaround for this test.
    # Pytest seems to be capturing the stderr,
    # thus making redirect_stderr not work.
    # assert len(result["errors"]) is not 0
