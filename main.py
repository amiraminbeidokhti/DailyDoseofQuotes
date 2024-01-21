from enum import Enum
import os
import random
from notion_client import APIResponseError, Client
from dotenv import load_dotenv
import typing as tp


load_dotenv()


class Colors(str, Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset the color


def get_env_variable(env_variable: str) -> str:
    """Retrieve an environment variable or raise an error if not found."""
    value = os.getenv(env_variable, None)
    if value is None:
        raise ValueError(f'{env_variable} is not set.')
    return value


def fetch_quotes_from_notion(notion: Client, page_id: str) -> tp.List[str]:
    """Fetch quotes from a Notion page and return them as a list of strings."""
    try:
        page_content: dict = notion.blocks.children.list(block_id=page_id)
    except APIResponseError as e:
        raise RuntimeError(f"Failed to fetch Notion page content: {e}")

    return [block['bulleted_list_item']['rich_text'][0]['text']['content']
            for block in page_content.get("results", [])
            if block['type'] == 'bulleted_list_item']


def print_colorful(text: str, quote_color: Colors, author_color: Colors):
    quote_parts = text.split('\n')
    quote, author = '\n'.join(quote_parts[:-1]), quote_parts[-1]

    print(f"\n{quote_color.value}{quote}\n\n\t{author_color.value}{author}{Colors.RESET.value}")


def main():
    """Main function to fetch and display a random quote."""
    notion = Client(auth=get_env_variable("NOTION_TOKEN"))
    page_id = get_env_variable("PAGE_ID")

    quotes = fetch_quotes_from_notion(notion, page_id)
    if quotes:
        quote = random.choice(quotes)
        print_colorful(quote, Colors.GREEN, Colors.CYAN)
    else:
        print("No quotes found.")


if __name__ == "__main__":
    main()