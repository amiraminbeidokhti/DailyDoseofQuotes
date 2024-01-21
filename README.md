# Notion Random Quote Fetcher

This Python project connects to a Notion page and fetches a random quote from the list of quotes available on that page. It utilizes the Notion API and the `notion-client` Python library for fetching data from Notion.

## Features

- Connects to a Notion page using the Notion API.
- Fetches all quotes listed as bulleted list items on the page.
- Randomly selects a quote and prints it.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Notion account and access to the Notion API.
- You have created a Notion integration and obtained the integration token.
- You have Python 3.7+ installed on your machine.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/amiraminbeidokhti/DailyDoseofQuotes.git
   ```

2. Create a '.env' file in the project root and add your Notion API credentials.

## Usage
The project includes a Makefile for easy setup and execution.

To install dependencies and run the project:
   ```bash
   make
   ```
To only install dependencies:
   ```bash
   make dependencies
   ```
To only run the project:
   ```bash
   make run
   ```