# Avery 3328 LateX and Jinja2 Templates

Dealing with the Avery [downloadable templates](https://www.avery.com/templates) or the online editor is such a pain.  Hey Avery!  The 1990's called--they want their `.doc` file format back!

Every time I have to make another one of these, I'm going to add it here and improve upon this repo.

## Usage

`Avery3328-borders.tex` checks that the borders line up with the PDF template available from Avery.  `Avery3328.tex` removes the borders and adds a small amount of spacing.  These files can be modified directly as needed. 

`render.py` reads in a text or Excel file (configured inside `render.py`) and renders a PDF from the `Avery3328.jinja2` Jinja template. 

### Example

#### Create Python virtual environment (recommended)

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### Render the template with the example names in `names.txt`.

```sh
python render.py
```

The script will produce a PDF file `table_tents.pdf` with the example names formatted according to the template.

## Dependencies

### Python

Any recent version of Python with standard modules should be fine, along with installed packages:

- `pandas` (only for reading in Excel inputs, if required)
- `jinja2`

### TeX

Currently the `render.py` calls LuaLaTeX.  XeLaTeX should also work fine, but I haven't tested it.

### Font

Note that these templates use the **Apple Chancery** font, which is a system font available on Mac.  This specification is easy to change in the `.tex` and `.jinja2` templates.