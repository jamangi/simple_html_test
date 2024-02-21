import re


def read_file_names(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        html_content = f.read()
        filenames = extract_image_filenames(html_content)
        return filenames

def extract_image_filenames(html_content):
    try:
        # Use a regular expression to find all filenames with .jpg or .png extensions
        filenames = re.findall(r'src=".*?/(\w+\.(?:jpg|png))"', html_content)

        print("Image filenames extracted successfully.")
        return filenames
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    # Example usage
    file_path = "index.html"
    with open(file_path, mode='r', encoding='utf-8') as f:
        html_content = f.read()
        filenames = extract_image_filenames(html_content)
        print("Image filenames found:")
        print(filenames)

    html_content = """
    <div class="w3-col m3">
        <img src="/w3images/p1.jpg" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="The mist over the mountains">
    </div>
    """

    filenames = extract_image_filenames(html_content)
    print(filenames)