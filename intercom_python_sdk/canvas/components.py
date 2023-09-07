from typing import List
from dataclasses import dataclass
from enum import Enum


DEFAULT_SUBMIT_TEXT = "Submit"


class ActionType(Enum):
    SUBMIT = "submit"
    URL = "url"
    SHEET = "sheet"


class SpacerSize(Enum):
    EXTRA_SMALL = "xs"
    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"


class TextStyle(Enum):
    HEADER = "header"
    MUTED = "muted"
    PARAGRAPH = "paragraph"
    ERROR = "error"


class TextAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class ButtonStyle(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    LINK = "link"


@dataclass
class InputParameters:
    """
    This class is used to configure an input component.
    Reference: https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/input/#parameters
    """

    id: str
    label: str = "label"
    placeholder: str = None
    value: str = None
    disabled: bool = False


@dataclass
class TextParameters:
    """
    This class is used to configure a text component.
    Reference: https://developers.intercom.com/docs/references/canvas-kit/presentationcomponents/text/#parameters
    """

    id: str = None
    text: str = "text"
    style: TextStyle = TextStyle.PARAGRAPH
    align: TextAlign = TextAlign.LEFT


@dataclass
class OptionParameters:
    """
    This class is used to configure an option component.
    Reference: https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/dropdown/#dropdown-parameters
    """

    id: str
    text: str = "text"
    disabled: bool = False


@dataclass
class DropdownParameters:
    """
    This class is used to configure a dropdown component.
    Reference: https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/dropdown/#dropdown-parameters
    """

    id: str
    options: List[OptionParameters]
    label: str = "label"
    value: str = None
    disabled: bool = False


@dataclass
class ActionParameters:
    """
    This class is used to configure an action component. It has three types: submit, url, and sheet.

    Reference for submit: https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/submit-action/#parameters
    Reference for url: https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/url-action/#parameters
    Reference for sheets: https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/sheets-action/
    """

    type: ActionType = ActionType.SUBMIT
    url: str = None


@dataclass
class ButtonParameters:
    """
    This class is used to configure a button component.
    Reference: https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/button/#parameters
    """

    id: str
    label: str = "label"
    disabled: bool = False
    style: ButtonStyle = ButtonStyle.PRIMARY
    action: ActionParameters = ActionParameters()


@dataclass
class SpacerParameters:
    id: str = None
    size: SpacerSize = SpacerSize.MEDIUM
