import re

def main():
    # Prompt user to input HTML code containing an iframe tag
    html_input = input("HTML: ")
    
    # Call the parse function with the user input and print the result
    print(parse(html_input))

def parse(s):
    # Use regular expressions to search for an iframe tag in the input HTML code
    if re.search(r"<iframe(.)*><\/iframe>", s):
        # If an iframe tag is found, search for a YouTube embed URL pattern within it
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-z_0-9]+)", s)
        if url_pattern:
            # If a YouTube embed URL pattern is found, extract the video ID and construct the short URL
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]

if __name__ == "__main__":
    main()
