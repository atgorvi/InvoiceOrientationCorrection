import gradio as gr
import numpy as np

from src.orientation_correction import correct_orientation
from typing import Tuple


def demo_correction(input_image: np.ndarray) -> Tuple[float, np.ndarray]:
    correction_angle, corrected_image = correct_orientation(input_image)
    return correction_angle, corrected_image

if __name__ == "__main__":
    demo = gr.Interface(fn=demo_correction,
                        inputs=gr.inputs.Image(type="numpy"),
                        outputs=[gr.outputs.Textbox(label="Correction angle"), gr.outputs.Image(type="numpy")],
                        examples=[[f"data/images/{i}.png"] for i in range(11)],
                        )

    demo.launch()