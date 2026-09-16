import os

with open('generate_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('</head>', '''    <!-- Google Translate for Kannada -->
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'en,kn', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>''')

code = code.replace('<!-- Navigation -->', '''<!-- Google Translate Widget for Kannada -->
<div id="google_translate_element" style="text-align:right; padding: 5px 20px; background: #1a1a1a; color: white;"></div>
<!-- Navigation -->''')

with open('generate_site.py', 'w', encoding='utf-8') as f:
    f.write(code)
