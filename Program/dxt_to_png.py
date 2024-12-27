import os
import ezdxf
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import MatplotlibBackend
from PIL import Image

def convert_dxf_to_image(input_folder, output_folder, file_format='png'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".dxf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.{file_format}")
            try:
                # Load the .dxf file
                doc = ezdxf.readfile(input_path)
                modelspace = doc.modelspace()

                # Set up MatplotlibBackend for rendering
                backend = MatplotlibBackend()
                backend.draw_modelspace(modelspace)

                # Create a figure and axis for rendering
                fig, ax = plt.subplots()
                backend.render(fig, ax)  # Render the drawing

                # Save to the selected image format
                plt.axis('off')  # Turn off axis
                plt.savefig(output_path, bbox_inches='tight', pad_inches=0, dpi=300)
                plt.close(fig)
                print(f"Successfully converted {filename} to {output_path}")

                # Optionally, convert to JPG using Pillow (if needed)
                if file_format.lower() == 'jpg':
                    with Image.open(output_path) as img:
                        img.convert('RGB').save(output_path, 'JPEG')
                        print(f"Converted {filename} to JPG at {output_path}")

            except Exception as e:
                print(f"Error converting {filename}: {e}")

# Example usage:
convert_dxf_to_image("D:/AI/cad_dataset", "D:/AI/png_cad_dataset", file_format='png')  # Use 'jpg' for JPG
