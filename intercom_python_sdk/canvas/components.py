from typing import List, Optional
from dataclasses import dataclass, field
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

    References:
    https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/input/#parameters
    """

    id: str
    label: str = "label"
    placeholder: Optional[str] = None
    value: Optional[str] = None
    disabled: bool = False


@dataclass
class TextParameters:
    """
    This class is used to configure a text component.

    References:
    https://developers.intercom.com/docs/references/canvas-kit/presentationcomponents/text/#parameters
    """

    id: Optional[str] = None
    text: str = "text"
    style: TextStyle = TextStyle.PARAGRAPH
    align: TextAlign = TextAlign.LEFT


@dataclass
class OptionParameters:
    """
    This class is used to configure an option component.

    References:
    https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/dropdown/#dropdown-parameters
    """

    id: Optional[str]
    text: str = "text"
    disabled: bool = False


@dataclass
class DropdownParameters:
    """
    This class is used to configure a dropdown component.

    References:
    https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/dropdown/#dropdown-parameters
    """

    id: str
    options: List[OptionParameters]
    label: str = "label"
    value: Optional[str] = None
    disabled: bool = False


@dataclass
class ActionParameters:
    """
    This class is used to configure an action component. It has three types: submit, url, and sheet.

    References:
    https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/submit-action/#parameters
    https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/url-action/#parameters
    https://developers.intercom.com/docs/references/canvas-kit/actioncomponents/sheets-action/
    """

    type: ActionType = ActionType.SUBMIT
    url: Optional[str] = None


@dataclass
class ButtonParameters:
    """
    This class is used to configure a button component.

    References:
    https://developers.intercom.com/docs/references/canvas-kit/interactivecomponents/button/#parameters
    """

    id: str
    label: str = "label"
    disabled: bool = False
    style: ButtonStyle = ButtonStyle.PRIMARY
    action: ActionParameters = field(default_factory=lambda: ActionParameters())


@dataclass
class SpacerParameters:
    id: Optional[str] = None
    size: SpacerSize = SpacerSize.MEDIUM
