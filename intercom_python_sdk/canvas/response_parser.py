from typing import Dict, Optional
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class CanvasResponse:
    stored_data: Optional[Dict] = None
    component_id: Optional[str] = None
    input_values: Optional[Dict] = None


class CanvasResponseParser:
    """
    Parses the canvas response.
    """

    def __init__(self, canvas: Dict):
        """
        Initializes a new CanvasResponseParser instance.

        :param canvas: The canvas response JSON object.
        """
        self._canvas = deepcopy(canvas)

    def parse(self) -> CanvasResponse:
        """
        Parses the canvas response.

        :return: The CanvasResponse object.
        """
        component_id = self._canvas.get("component_id", None)
        input_values = self._canvas.get("input_values", None)
        current_canvas = self._canvas.get("current_canvas", {})
        stored_data = current_canvas.get("stored_data", {})

        canvas_response = CanvasResponse(
            stored_data=stored_data,
            component_id=component_id,
            input_values=input_values,
        )

        return canvas_response
