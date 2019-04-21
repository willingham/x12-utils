from pyx12 import params as x12n_params, x12n_document  # type: ignore
from io import StringIO
from contextlib import redirect_stderr, redirect_stdout
from typing import Any, Dict, IO, Union


def x12_validate(
    src: Union[str, IO[str]],
    params: Union[Any, None] = None,
    generate_html: bool = False,
    generate_997: bool = False,
    generate_xml: bool = False,
) -> Dict[str, Union[str, bool, list]]:
    """
    Validate x12 EDI string or contents of file descriptor.
    """
    src_fd: IO[str]
    if isinstance(src, str):
        src_fd = StringIO(src)
    else:
        src_fd = src

    pyx12_params = params
    if not isinstance(pyx12_params, type(x12n_params)):
        pyx12_params = x12n_params.params(None)

    nn7: StringIO = StringIO()
    html: StringIO = StringIO()
    xml: StringIO = StringIO()

    stderr: StringIO = StringIO()
    with redirect_stderr(stderr):
        # Capture errors from pyx12
        ok = x12n_document.x12n_document(
            param=pyx12_params,
            src_file=src_fd,
            fd_997=nn7 if generate_997 else None,
            fd_html=html if generate_html else None,
            fd_xmldoc=xml if generate_xml else None,
            map_path=None,
        )

    # Get string values
    html_val = html.getvalue()
    nn7_val = nn7.getvalue()
    stderr_val = stderr.getvalue().splitlines()
    xml_val = xml.getvalue()

    return {
        "html": html_val,
        "997": nn7_val,
        "xml": xml_val,
        "errors": stderr_val,
        "ok": ok,
    }
