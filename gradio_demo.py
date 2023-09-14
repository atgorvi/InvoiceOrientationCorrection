import gradio as gr
import numpy as np

from src.orientation_correction import correct_orientation
from typing import Tuple


def demo_correction(input_image: np.ndarray) -> Tuple[int, np.ndarray]:
    correction_angle, corrected_image = correct_orientation(input_image)
    return correction_angle, corrected_image

if __name__ == "__main__":
    demo = gr.Interface(fn=demo_correction,
                        inputs=gr.inputs.Image(type="numpy"),
                        outputs=[gr.outputs.Textbox(label="Correction angle"), gr.outputs.Image(type="numpy")],
                        examples=[["data/images/0.png"], ["data/images/10.png"]],
                        )

    demo.launch()