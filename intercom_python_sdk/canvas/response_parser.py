from typing import Dict
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class CanvasResponse:
    stored_data: Dict = None


class CanvasResponseParser:
    """
    This class is used to parse the canvas response from the Intercom Messenger.
    You must initialize it with the canvas response JSON object and then call the parse method.
    It'll return a CanvasResponse object with the parsed data.
    """

    def __init__(self, canvas: Dict):
        """
        Initializes the CanvasResponseParser class. It makes a deepcopy of the canvas.

        :param canvas: The canvas response JSON object.
        """
        self._canvas = deepcopy(canvas)

    def parse(self) -> CanvasResponse:
        """
        Parses the canvas response and returns a CanvasResponse object.

        :return: The CanvasResponse object.
        """
        current_canvas = self._canvas.get("current_canvas", {})
        stored_data = current_canvas.get("stored_data", {})

        canvas_response = CanvasResponse(
            stored_data=stored_data,
        )

        return canvas_response
