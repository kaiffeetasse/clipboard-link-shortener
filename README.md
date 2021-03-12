# clipboard-link-shortener (Windows)

## Installation
``pip install -r requirements.txt``

## Usage

1. Create a API Key for your Kutt account (either at [kutt.it](https://kutt.it) or at your self hosted instance)
2. Paste your API Key and Kutt URL into the ``.env`` file under your ``clipboard-link-shortener`` folder (see below for a sample ``.env`` file)
3. Start the clipboard-link-shortener with ``python main.py``

**sample .env file**
```
KUTT_URL=https://kutt.it/api/v2/links
KUTT_API_KEY=12345
```

## Credits
Thanks to [kutt.it](https://github.com/thedevs-network/kutt) for their amazing free URL shortener!