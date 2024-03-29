from enum import Enum, auto

from sourcelib.extension import Extension, create_extensions_mapping
from sourcelib.file import File


class DocumentFileMode(Enum):
    default = auto()
    error = auto()


TEXT_EXTENSION = Extension((".txt",))
MARKDOWN_EXTENSION = Extension((".md",))
TEXTPARTS_EXTENSION = Extension((".tpt",), folder_coupled=lambda path: path.with_suffix(""))


DOCUMENT_EXTENSIONS = create_extensions_mapping(
    [TEXT_EXTENSION, MARKDOWN_EXTENSION, TEXTPARTS_EXTENSION]
)


class DocumentFile(File):

    EXTENSIONS = DOCUMENT_EXTENSIONS
    IDENTIFIER = "doc"
