import os

with open('generate_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace single braces with double braces so format() doesn't fail
js_snippet = '''    <!-- Google Translate for Kannada -->
    <script type="text/javascript">
        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{pageLanguage: 'en', includedLanguages: 'en,kn', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}}, 'google_translate_element');
        }}
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>'''

code = code.replace('''    <!-- Google Translate for Kannada -->
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'en,kn', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>''', '</head>') # undo first

code = code.replace('</head>', js_snippet)

with open('generate_site.py', 'w', encoding='utf-8') as f:
    f.write(code)
