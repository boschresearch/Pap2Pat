import json
from pathlib import Path
import re
import time
import sglang as sgl
from rich.console import Console
from sglang.lang.interpreter import ProgramState


sgl.set_default_backend(sgl.RuntimeEndpoint("http://localhost:59532"))

# import debugpy
# debugpy.listen(59531)
# debugpy.wait_for_client()


SYSTEM = """
### TASK

Your task is to extract all reference numerals from a patent text the user will provide.

### EXAMPLES

Consider the examples below. The reference numerals are numbers that refer to a certain component or step of the invention.
They typically follow the name of the component they refer to, but might also be written before the name sometimes.
After a numeral has been introduced, it might be also used alone without its component name.

#### Example 1

```md
"In FIG. 1, the system 10 includes a processor 12, a memory 14, and an interface 16. The processor 12 is connected to the memory 14 through a bus 18."
```

Reference numerals to extract:

```md
- 10: system
- 12: processor
- 14: memory
- 16: interface
- 18: bus
```

#### Example 2

```md
"The method 20 includes a step 22 of receiving a signal, a step 24 of processing the signal, and a step 26 of transmitting the signal. The signal is received by the receiver 28."
```

Reference numerals to extract:

```md
- 20: method
- 22: step of receiving a signal
- 24: step of processing the signal
- 26: step of transmitting the signal
- 28: receiver
```

### OUTPUT FORMAT

Your task is to extract all reference numerals from the input text and output them in a list format, along with their corresponding component or step names.
Use the same output format as in the examples above. Reply with nothing but the list of reference numerals in a markdown block.

### CONSTRAINTS

- The reference numerals can be written in various formats, e.g., with or without parantheses
- The component or step names can be written in various formats, such as "system", "processor unit", "step of receiving a signal", etc.
- The reference numerals can be used alone without their component or step names after they have been introduced.
- The same reference numeral might be used along with slightly different component names throughout the document. Use the most common one.
- The input text may contain multiple sections.
""".strip()

USER = """
```md
{patent}
```

Extract the reference numerals from this patent. Be careful and make sure component names appear verbatim in the patent, do not paraphrase.
"""

@sgl.function
def extract_reference_numerals(s: ProgramState, patent: str):
    item_regex = r"(?:- ([^\n\:]*)\:([^\n\:]*)\n)"

    s += sgl.system(SYSTEM)  # type: ignore
    s += sgl.user(USER.format(patent=patent))  # type: ignore
    s += sgl.assistant(sgl.gen(max_tokens=2048, temperature=0.3, top_p=0.6, regex=fr"```md\n{item_regex}*```"))

    reply = s.messages()[-1]["content"]
    s.reference_numerals = dict(re.findall(item_regex, reply))

# def extract_reference_numerals(patent: str):
#     state = extract_reference_numerals_.run(patent)
#     return state.reference_numerals

