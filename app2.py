
#THE FUNCTION FOR MATHEMATICAL EXPRESSIONS

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from PIL import Image
import io
import base64

def create_math_image(latex_str):
    # Set up headless Chrome
    # if "$" in latex_str or "\\" in latex_str:
    #     # It's a mathematical expression, handle as LaTeX
    #     latex_str = latex_str
    # else:
    #     # It's regular text, escape LaTeX special characters and preserve spaces
    #     latex_str = '\\text{' + latex_str.replace(' ', '\\ ') + '}'
    if all(c.isalpha() or c.isspace() for c in latex_str):
        # It's regular text, wrap it with \text{} but don't escape spaces.
        latex_str = f"\\text{{{latex_str}}}"
    else:
        # It's a LaTeX expression, so we escape spaces and handle it as LaTeX.
        latex_str = latex_str.replace(' ', '\\ ')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    # MathJax script to render LaTeX
    mathjax_script = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML'

    # Prepare HTML content with LaTeX embedded
    content = f"""
    <html>
      <head>
        <script type="text/javascript" async src="{mathjax_script}"></script>
      </head>
      <body>
        <div id="content" style="font-size: 20px;">
          $$ {latex_str} $$
        </div>
      </body>
    </html>
    """

    # Load HTML in headless browser
    driver.get("data:text/html;charset=utf-8," + content)

    # Wait for MathJax to finish rendering
    driver.implicitly_wait(10)

    # Take a screenshot of the result
    element = driver.find_element(By.ID, 'content')
    png = element.screenshot_as_png

    driver.quit()

    # Convert PNG data to an image
    image_stream = io.BytesIO(png)
    image = Image.open(image_stream)
    
    return image

# Example usage
#latex_expression = "e^{i\\pi} + 1 = 0"
latex_expression = "e^2+b^2"

image = create_math_image(latex_expression)
#image.show()
