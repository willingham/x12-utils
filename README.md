# X12 Utils
Lightweight utilities for working with x12 EDI

## Background & Purpose
Around 2010, I started working with EDI in a limited capacity.  At the time, I had no clue what it was, and didn't seem to find too much free help on the internet.  So, after spending countless hours digging through vendor-specific companion guides and comparing them to previously generated EDI, I was finally able to understand what was going on.  

I've been writing Python packages to generate EDI for various organizations since around 2013.  In those projects I have used string concatenatiion, Jinja templating, Django templating, and a few more methods to generate EDI.  After much trial and error, I landed on a method to generate the EDI that was easy to maintain.  That is the `x12_generator` included in this repository.

Since there is another crucial step, validating the resulting EDI, I have also included the `x12_validator` module which is a lightweight wrapper around the great work done on [pyx12](https://github.com/azoner/pyx12) by @azoner.

## Included Utilities
### Generator
The `x12_generator` is a small helper for generating syntactically correct x12 EDI, however, does not assist in ensuring correct structure at all.
#### Usage
``` py
from x12_utils.x12_generator import x12_generate

generator_input = [
    ("ISA", ["00", "          ", "00", "          ", "ZZ"]),
    ("GS", ["BE", "          ", "00", "          ", "ZZ"]),
    ("ST", ["00", "          ", "00", "          ", "ZZ"]),
    ("SE", ["00", "          ", "00", "          ", "ZZ"]),
    ("GE", ["00", "          ", "00", "          ", "ZZ"]),
    ("IEA", ["00", "          ", "00", "          ", "ZZ"]),
]

edi = x12_generate(src=generator_input)

# `edi` will look like:

# ISA*00*          *00*          *ZZ~
# GS*BE*          *00*          *ZZ~
# ST*00*          *00*          *ZZ~
# SE*00*          *00*          *ZZ~
# GE*00*          *00*          *ZZ~
# IEA*00*          *00*          *ZZ~
#
# Note: This is not structurally valid EDI, just an example to show the format.

```

### Validator
The `x12_validator` is a light wrapper around @azoner's [pyx12](https://github.com/azoner/pyx12) intended for use in other projects.
#### Usage
``` py
from x12_utils.x12_validator import x12_validate

result = x12_validate(
    src=edi,             # String or file-like object
    params=None,         # Valid [pyx12](https://github.com/azoner/pyx12) params or None
    generate_html=False, # Passed to [pyx12](https://github.com/azoner/pyx12)
    generate_997=False,  # Passed to [pyx12](https://github.com/azoner/pyx12)
    generate_xml=False,  # Passed to [pyx12](https://github.com/azoner/pyx12)
)
# Assuming valid EDI, `result` will look like
# {
#   "997": "",
#   "errors": "",
#   "html": "",
#   "ok": True,
#   "xml": ""
# }

```

