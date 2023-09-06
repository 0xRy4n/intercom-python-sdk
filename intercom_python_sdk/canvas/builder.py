from . import components as cmps

from typing import Dict, List, Any, Optional
from copy import deepcopy


class CanvasBuilder:
    """
    This class is used to build a Canvas for Intercom Canvas Kit (https://developers.intercom.com/docs/canvas-kit/).
    You can add components to the canvas using the methods in this class. The build() method returns the canvas as a
    dictionary that can be returned to Intercom.
    """

    _INITIAL_CANVAS = {"canvas": {"content": {"components": []}}}

    def __init__(self):
        self._current_build = self._INITIAL_CANVAS

    def build(self) -> Dict:
        """
        Returns a deep copy of the canvas as a dictionary. Removes None values.

        :return: The final canvas as a dictionary
        """
        current_build_copy = deepcopy(self._current_build)
        components = current_build_copy["canvas"]["content"]["components"]
        new_components = []

        for component in components:
            new_component = {k: v for k, v in component.items() if v is not None}
            new_components.append(new_component)
        
        current_build_copy["canvas"]["content"]["components"] = new_components

        return current_build_copy
    
    def reset(self):
        """
        Resets the canvas to its initial state.
        """
        self._current_build = self._INITIAL_CANVAS

    ### Wrappers around other methods/components ###

    def add_header(
        self, text: str, options: Optional[cmps.TextParameters] = None
    ) -> "CanvasBuilder":
        """
        Adds a header to the canvas. This is a wrapper around the add_text method.

        :param text: The text to display in the header.
        :param options: The text options to use for the header. Its text and style parameters are ignored.
        :return: The CanvasBuilder instance.
        """
        options_copy = deepcopy(options) if options else cmps.TextParameters()
        options_copy.text = text
        options_copy.style = cmps.TextStyle.HEADER
        self.add_text(options_copy)
        return self

    def add_submit_button(
        self, text: str = cmps.DEFAULT_SUBMIT_TEXT
    ) -> "CanvasBuilder":
        """
        Adds a submit button to the canvas. This is a wrapper around the add_button method.

        :param text: The text to display on the button.
        :return: The CanvasBuilder instance.
        """

        params = cmps.ButtonParameters(
            id="submit", label=text, style=cmps.ButtonStyle.PRIMARY
        )
        self.add_button(params)
        return self

    def add_error_message(self, text: str) -> "CanvasBuilder":
        """
        Adds an error message to the canvas. This is a wrapper around the add_text method.

        :param text: The text to display in the error message.
        :return: The CanvasBuilder instance.
        """
        err_text = f"*Error:* {text}"
        self.add_text(cmps.TextParameters(text=err_text, style=cmps.TextStyle.ERROR))
        return self

    ### Components ###

    def add_button(self, parameters: cmps.ButtonParameters) -> "CanvasBuilder":
        """
        Adds a button to the canvas. The button can be customized using the ButtonParameters class.

        :param parameters: The button parameters to add to the canvas.
        :return: The CanvasBuilder instance.
        """
        action_type = parameters.action.type
        action_obj = {
            "type": action_type.value,
            **(
                {"url": parameters.action.url}
                if action_type != cmps.ActionType.SUBMIT
                else {}
            ),
        }

        button = {
            "type": "button",
            "id": parameters.id,
            "label": parameters.label,
            "style": parameters.style.value,
            "action": action_obj,
        }

        self._append_component(button)
        return self

    def add_dropdown(
        self, parameters: cmps.DropdownParameters, options: List[cmps.OptionParameters]
    ) -> "CanvasBuilder":
        """
        Adds a dropdown to the canvas.

        :param parameters: The dropdown parameters to add to the canvas.
        :param options: The options to display in the dropdown.
        :return: The CanvasBuilder instance.
        """
        final_options = [
            {
                "type": "option",
                "text": option.text,
                "id": option.id,
                "disabled": option.disabled,
            }
            for option in options
        ]

        dropdown = {
            "id": parameters.id,
            "label": parameters.label,
            "type": "dropdown",
            "options": final_options,
        }

        self._append_component(dropdown)
        return self

    def add_text(self, parameters: cmps.TextParameters) -> "CanvasBuilder":
        """
        Adds a text component to the canvas.

        :param parameters: The text parameters to add to the canvas.
        :return: The CanvasBuilder instance.
        """
        text = {
            "id": parameters.id,
            "align": parameters.align.value,
            "type": "text",
            "text": parameters.text,
            "style": parameters.style.value,
        }
        self._append_component(text)
        return self

    def add_space(self, parameters: cmps.SpacerParameters) -> "CanvasBuilder":
        """
        Adds a space component to the canvas.

        :param parameters: The space parameters to add to the canvas.
        :return: The CanvasBuilder instance.
        """
        space = {
            "type": "spacer",
            "size": parameters.size.value,
            "id": parameters.id,
        }
        self._append_component(space)
        return self

    def add_text_input(self, parameters: cmps.InputParameters) -> "CanvasBuilder":
        """
        Adds an input component to the canvas.

        :param parameters: The input parameters to add to the canvas.
        :return: The CanvasBuilder instance.
        """
        text_input = {
            "type": "input",
            "id": parameters.id,
            "label": parameters.label,
            "placeholder": parameters.placeholder,
            "disabled": parameters.disabled,
            "value": parameters.value,
        }
        self._append_component(text_input)
        return self

    def set_stored_data(self, key: str, value: Any) -> "CanvasBuilder":
        """
        Sets the stored data of the canvas.

        :param key: The key of the stored data.
        :param value: The value of the stored data.
        :return: The CanvasBuilder instance.
        """
        self._current_build["canvas"].setdefault("stored_data", {})[key] = value
        return self

    def _append_component(self, component: Dict):
        """
        Appends a component to the canvas.

        :param component: The component to append to the canvas.
        """
        self._current_build["canvas"]["content"]["components"].append(component)
