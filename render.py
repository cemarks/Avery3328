import jinja2
import os
from jinja2 import Template
from subprocess import Popen, PIPE, STDOUT
import pandas as pd
import io
import os

latex_jinja_env = jinja2.Environment(
    block_start_string = '\\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\\VAR{',
    variable_end_string = '}',
    comment_start_string = '\\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def get_names_excel(
        input_xlsx: str,
        col: str = "Name"
    ) -> list:
    """Read Names from Excel

    Parameters
    ----------
    input_xlsx : str
        The excel file name
    col : str
        The column name to read in

    Returns
    ----------
    list
    """

    df = pd.read_excel(input_xlsx)
    return df[col].to_list()

def get_names_text(
        input_txt: str
    ) -> list:
    """Read Names from Excel

    Parameters
    ----------
    input_txt : str
        The text file name

    Returns
    ----------
    list
    """

    with open(input_txt, 'r') as f:
        names = f.readlines()
    
    return [name.rstrip() for name in names]


if __name__ == "__main__":

    TEMPLATE = "Avery3328.jinja2"
    INPUT_TXT = "names.txt"
    template = latex_jinja_env.get_template(TEMPLATE)
    names = get_names_text(INPUT_TXT)

    tex_source = io.BytesIO(
        template.render({'names': names}).encode()
    )
    
    ## Output .tex for debugging
    # tex_source.seek(0)
    # with open('out.tex', 'wb') as f:
    #     f.write(tex_source.read())

    tex_source.seek(0)

    p = Popen(["lualatex",
               "--shell-escape"
            ],
            stdin = PIPE
        )
    
    p.communicate(input=tex_source.read())
    
    os.remove(os.path.join(
        "texput.aux"
    ))
    os.remove(os.path.join(
        "texput.log"
    ))

    os.rename(
        'texput.pdf',
        "table_tents.pdf"
    )
