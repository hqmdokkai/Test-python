from flask import Flask
from flask import Flask, url_for
from markupsafe import Markup
import markdown
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Markdown content
    content = """
# Hello World

Lập trình web bằng Python, Flask, Markdown, Markupsafe free

Lướt xuống để xem video

<img src="/static/OIP.jpg" width="100%" height="100%" alt="Image description">
"""

    # Convert Markdown content to HTML
    html_content = markdown.markdown(content)

    # Render the HTML using a separate template file
    return render_template('index.html', html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
