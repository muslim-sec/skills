---
name: premium-pptx-templates
description: Advanced skill for generating premium, animation-rich PowerPoint presentations by using pre-designed .pptx templates. Supports robust {{tag}} replacement across broken text runs and programmable image swapping while preserving native animations and master slides.
---

# Premium PPTX Templates Skill

**Role:** Expert Presentation Architect & Automation Engineer
**Objective:** Programmatically generate high-end, premium PowerPoint presentations using `python-pptx` by replacing variable `{{tags}}` and images inside beautiful pre-existing `.pptx` templates.

## Core Philosophy: The Template-First Approach
Code-generated slides look like "AI slop" and lack native PowerPoint animations. 
1. Use an existing, beautifully designed PowerPoint `.pptx` file as your baseline template.
2. The template must contain animations, Master Slides, and typography.
3. The template uses text tags like `{{CLIENT_NAME}}` and placeholder images.
4. Use `python-pptx` to safely inject data without breaking runs or animations.

## Required Dependencies
```bash
pip install python-pptx
```

## Robust Implementation Code (Text & Image Replacement)

PowerPoint often splits a single word like `{{TAG}}` across multiple internal text "runs" (`{`, `{TA`, `G}}`), breaking simple `.replace()` logic. The function below safely merges paragraph text to ensure tags are always found, and includes image swapping.

```python
import os
from pptx import Presentation

def replace_text_in_paragraph(paragraph, replacements):
    """Safely replaces text in a paragraph even if tags are split across runs."""
    full_text = "".join(run.text for run in paragraph.runs)
    
    # Check if any tags exist in the combined text
    needs_replacement = False
    for tag in replacements.keys():
        if tag in full_text:
            needs_replacement = True
            break
            
    if needs_replacement:
        for tag, replacement in replacements.items():
            full_text = full_text.replace(tag, str(replacement))
            
        # To preserve formatting as much as possible, put all new text in the first run
        # and clear the subsequent runs.
        if paragraph.runs:
            paragraph.runs[0].text = full_text
            for i in range(1, len(paragraph.runs)):
                paragraph.runs[i].text = ""

def replace_content_in_shapes(shapes, text_replacements, image_replacements):
    for shape in shapes:
        # 1. Text Replacement
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                replace_text_in_paragraph(paragraph, text_replacements)
                
        # 2. Image Replacement (Matches shape name, e.g., "ProfilePic")
        if shape.shape_type == 13:  # msoPicture
            if shape.name in image_replacements:
                img_path = image_replacements[shape.name]
                if os.path.exists(img_path):
                    with open(img_path, 'rb') as f:
                        shape.image.part.blob = f.read()
                        
        # 3. Handle Groups
        if shape.shape_type == 6:  # msoGroup
            replace_content_in_shapes(shape.shapes, text_replacements, image_replacements)
            
        # 4. Handle Tables
        if shape.has_table:
            for row in shape.table.rows:
                for cell in row.cells:
                    replace_content_in_shapes([cell], text_replacements, image_replacements)

def generate_presentation(template_path, output_path, text_data, image_data=None):
    if image_data is None:
        image_data = {}
        
    prs = Presentation(template_path)
    
    for slide in prs.slides:
        replace_content_in_shapes(slide.shapes, text_data, image_data)
        
    prs.save(output_path)
    print(f"Successfully generated: {output_path}")

# Example Usage
if __name__ == "__main__":
    texts = {
        "{{PRESENTATION_TITLE}}": "Q3 Financial Review",
        "{{SUBTITLE}}": "A detailed look at our metrics"
    }
    # To replace images, name the image shape in PPT's Selection Pane (e.g., "ClientLogo")
    images = {
        "ClientLogo": "path/to/new_logo.png"
    }
    
    generate_presentation("master_template.pptx", "final_presentation.pptx", texts, images)
```

## Rules for the Agent
1. **Never Delete Shapes:** To preserve animations, never delete a shape programmatically. If a section is unused, replace its text with an empty string `""`.
2. **Image Replacement Workflow:** Instruct the user to open the Selection Pane in PowerPoint (`Alt+F10`) and rename the target placeholder image to a specific ID (e.g., `HeroImage`). Use this exact name in the `image_replacements` dictionary.
3. **No Scratch Root:** Remember the global rule: Any temporary python scripts used to generate the PPTX must be placed in `garbage scripts/`.
4. **Visual Overflow Warning:** Warn the user that extensive text insertion might overflow the shape's boundaries. Suggest they configure the shape in PowerPoint to "Shrink text on overflow" before running the script.
