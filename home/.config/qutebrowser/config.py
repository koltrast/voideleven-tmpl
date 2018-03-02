# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.cmd_history_max_items = 0

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history_max_items = 0

# Store cookies. Note this option needs a restart with QtWebEngine on Qt
# < 5.9.
# Type: Bool
c.content.cookies.store = False

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.geolocation = False

# User agent to send. Unset to send the default.
# Type: String
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt Iosevka'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt Iosevka'

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '10pt Iosevka'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt Iosevka'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt Iosevka'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt Iosevka'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt Iosevka'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt Iosevka'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt Iosevka'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt sans-serif'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '10pt Iosevka'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = '10pt Iosevka'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = None

# Maximum time (in minutes) between two history items for them to be
# considered being from the same browsing session. Items with less time
# between them are grouped when being displayed in `:history`. Use -1 to
# disable separation.
# Type: Int
c.history_gap_interval = 0

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://start.duckduckgo.com'

# Bindings for normal mode
config.bind('C', 'back')
config.bind('J', 'buffer')
config.bind('R', 'forward')
config.bind('S', 'tab-prev')
config.bind('T', 'tab-next')
config.bind('c', 'scroll left')
config.bind('h', 'tab-only')
config.bind('l', 'reload')
config.bind('r', 'scroll right')
config.bind('s', 'scroll up')
config.bind('t', 'scroll down')
