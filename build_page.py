import json

with open('fonts_b64.json', 'r', encoding='utf-8') as f:
    fonts = json.load(f)

# Read template or write clean file
css_fonts = f"""
    @font-face {{
      font-family: 'Archivo Black';
      font-style: normal;
      font-weight: 400;
      font-display: swap;
      src: url('data:font/woff2;base64,{fonts["archivo_black"]}') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }}
    @font-face {{
      font-family: 'DM Mono';
      font-style: normal;
      font-weight: 400;
      font-display: swap;
      src: url('data:font/woff2;base64,{fonts["dm_mono_400"]}') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }}
    @font-face {{
      font-family: 'DM Mono';
      font-style: normal;
      font-weight: 500;
      font-display: swap;
      src: url('data:font/woff2;base64,{fonts["dm_mono_500"]}') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }}
    @font-face {{
      font-family: 'Inter';
      font-style: normal;
      font-weight: 100 900;
      font-display: swap;
      src: url('data:font/woff2;base64,{fonts["inter_var"]}') format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }}
"""

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

output = template.replace('/* __FONTS_CSS__ */', css_fonts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print('Generated index.html successfully! Size:', len(output))
