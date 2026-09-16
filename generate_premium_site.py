import os

booking_url = "https://booksy.com/en-gb/167542_lace-market-hair-studio_hair-salon_37343_nottingham#ba_s=seo"

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Lace Market Hair Studio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <!-- Google Translate for Kannada -->
    <script type="text/javascript">
        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{pageLanguage: 'en', includedLanguages: 'en,kn', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}}, 'google_translate_element');
        }}
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Montserrat:wght@200;300;400;500&display=swap');
        
        body {{
            font-family: 'Montserrat', sans-serif;
            background-color: #F9F8F6;
            color: #2C2A29;
            -webkit-font-smoothing: antialiased;
        }}
        h1, h2, h3, h4, h5, h6, .font-serif {{
            font-family: 'Cormorant Garamond', serif;
        }}
        .text-accent {{
            color: #B89768;
        }}
        .bg-accent {{
            background-color: #B89768;
        }}
        .bg-dark {{
            background-color: #1A1A1A;
        }}
        .btn-luxury {{
            background-color: #1A1A1A;
            color: #fff;
            border: 1px solid #1A1A1A;
            transition: all 0.4s ease;
        }}
        .btn-luxury:hover {{
            background-color: transparent;
            color: #1A1A1A;
        }}
        .btn-outline {{
            background-color: transparent;
            color: #1A1A1A;
            border: 1px solid #1A1A1A;
            transition: all 0.4s ease;
        }}
        .btn-outline:hover {{
            background-color: #1A1A1A;
            color: #fff;
        }}
        .hero-overlay {{
            background: linear-gradient(to right, rgba(26, 26, 26, 0.85) 0%, rgba(26, 26, 26, 0.4) 100%);
        }}
        .nav-link {{
            position: relative;
        }}
        .nav-link::after {{
            content: '';
            position: absolute;
            width: 0;
            height: 1px;
            bottom: -4px;
            left: 0;
            background-color: #B89768;
            transition: width 0.3s ease;
        }}
        .nav-link:hover::after {{
            width: 100%;
        }}
        
        /* Fade in animation */
        .fade-in {{
            animation: fadeIn 1.5s ease-out forwards;
            opacity: 0;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body class="flex flex-col min-h-screen relative">
    <div id="google_translate_element" style="text-align:right; padding: 5px 20px; background: #1A1A1A; color: white; font-size: 12px;"></div>
"""

navbar = f"""
    <!-- Minimalist Navigation -->
    <nav class="bg-[#F9F8F6] border-b border-gray-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-6 lg:px-12">
            <div class="flex justify-between items-center h-24">
                <!-- Links (Left) -->
                <div class="hidden md:flex space-x-10 w-1/3">
                    <a href="index.html" class="text-xs uppercase tracking-[0.2em] nav-link text-gray-800">Home</a>
                    <a href="about.html" class="text-xs uppercase tracking-[0.2em] nav-link text-gray-800">Studio</a>
                    <a href="services.html" class="text-xs uppercase tracking-[0.2em] nav-link text-gray-800">Services</a>
                </div>
                
                <!-- Logo (Center) -->
                <div class="flex-shrink-0 flex flex-col items-center justify-center w-1/3 text-center">
                    <a href="index.html" class="flex flex-col items-center">
                        <span class="font-serif text-3xl tracking-widest text-[#1A1A1A]">LACE MARKET</span>
                        <span class="text-[0.65rem] uppercase tracking-[0.4em] text-gray-500 mt-1">Hair Studio</span>
                    </a>
                </div>

                <!-- CTA (Right) -->
                <div class="hidden md:flex justify-end items-center space-x-6 w-1/3">
                    <a href="contact.html" class="text-xs uppercase tracking-[0.2em] nav-link text-gray-800">Contact</a>
                    <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-luxury px-8 py-3 text-xs tracking-[0.2em] uppercase">Book Now</a>
                </div>

                <!-- Mobile menu button -->
                <div class="flex items-center md:hidden w-1/3 justify-end">
                    <button type="button" onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="text-gray-800 focus:outline-none">
                        <i class="fas fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile Menu -->
        <div class="hidden md:hidden bg-white border-t border-gray-100 absolute w-full" id="mobile-menu">
            <div class="px-6 py-6 space-y-4 text-center shadow-2xl">
                <a href="index.html" class="block text-sm uppercase tracking-widest text-gray-800 hover:text-accent">Home</a>
                <a href="about.html" class="block text-sm uppercase tracking-widest text-gray-800 hover:text-accent">Studio</a>
                <a href="services.html" class="block text-sm uppercase tracking-widest text-gray-800 hover:text-accent">Services</a>
                <a href="contact.html" class="block text-sm uppercase tracking-widest text-gray-800 hover:text-accent">Contact</a>
                <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="block mt-6 btn-luxury py-3 text-xs tracking-[0.2em] uppercase">Book Now</a>
            </div>
        </div>
    </nav>
"""

footer = f"""
    <!-- Elegant Footer -->
    <footer class="bg-dark text-white mt-auto py-20">
        <div class="max-w-7xl mx-auto px-6 lg:px-12">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 text-center md:text-left">
                
                <div class="md:col-span-1">
                    <h3 class="font-serif text-2xl tracking-widest mb-6">LACE MARKET</h3>
                    <p class="text-gray-400 font-light text-sm leading-loose mb-6">Elevating hairdressing to an art form. Specialists in balayage, foliage, and high-end colour formulations.</p>
                    <a href="https://instagram.com/lacemarkethairstudio" target="_blank" class="text-gray-400 hover:text-white transition">
                        <i class="fab fa-instagram text-xl"></i>
                    </a>
                </div>
                
                <div>
                    <h4 class="text-xs tracking-[0.2em] uppercase text-gray-500 mb-6">Menu</h4>
                    <ul class="space-y-4 text-sm font-light text-gray-300">
                        <li><a href="index.html" class="hover:text-accent transition">Home</a></li>
                        <li><a href="about.html" class="hover:text-accent transition">The Studio</a></li>
                        <li><a href="services.html" class="hover:text-accent transition">Treatments & Pricing</a></li>
                        <li><a href="contact.html" class="hover:text-accent transition">Contact</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-xs tracking-[0.2em] uppercase text-gray-500 mb-6">Visit Us</h4>
                    <ul class="space-y-4 text-sm font-light text-gray-300">
                        <li>1A Plumptre Street</li>
                        <li>Nottingham NG1 1JL</li>
                        <li>United Kingdom</li>
                        <li class="pt-2"><a href="tel:+447970175942" class="hover:text-accent transition">+44 7970 175942</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-xs tracking-[0.2em] uppercase text-gray-500 mb-6">Hours</h4>
                    <ul class="space-y-4 text-sm font-light text-gray-300">
                        <li class="flex justify-between md:justify-start gap-4"><span>Mon - Sat</span> <span>09:00 - 20:00</span></li>
                        <li class="flex justify-between md:justify-start gap-4"><span>Sunday</span> <span>Closed</span></li>
                    </ul>
                    <a href="{booking_url}" target="_blank" class="inline-block mt-8 text-xs uppercase tracking-[0.2em] border-b border-accent text-accent pb-1 hover:text-white hover:border-white transition">Reserve a Chair</a>
                </div>

            </div>
            
            <div class="border-t border-gray-800 mt-16 pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-600 uppercase tracking-wider">
                <p>&copy; 2026 Lace Market Hair Studio.</p>
                <p class="mt-4 md:mt-0">Design for Excellence</p>
            </div>
        </div>
    </footer>
    
    <!-- Floating Mobile Booking Button -->
    <a href="{booking_url}" target="_blank" class="md:hidden fixed bottom-0 left-0 w-full bg-dark text-white text-center py-4 text-xs tracking-[0.2em] uppercase font-semibold z-50 border-t border-gray-800">
        Book Appointment
    </a>
</body>
</html>
"""

# PAGE: INDEX
index_content = html_head.format(title="Luxury Hair Salon") + navbar + f"""
    <!-- Luxury Hero Section -->
    <header class="relative h-[85vh] w-full overflow-hidden flex items-center">
        <!-- High Quality Background Image -->
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Luxury Salon Interior" class="w-full h-full object-cover">
        </div>
        
        <!-- Sophisticated Gradient Overlay -->
        <div class="absolute inset-0 hero-overlay z-10"></div>
        
        <!-- Content -->
        <div class="relative z-20 max-w-7xl mx-auto px-6 lg:px-12 w-full fade-in">
            <div class="max-w-2xl">
                <p class="text-accent text-xs tracking-[0.4em] uppercase mb-6 pl-1 border-l-2 border-accent">Nottingham's Premier Destination</p>
                <h1 class="text-6xl md:text-8xl font-serif text-white mb-6 leading-tight">Mastery in <br><span class="italic text-gray-300">Blonde</span></h1>
                <p class="text-gray-300 font-light text-lg mb-12 max-w-lg leading-relaxed">Experience uncompromised luxury and flawless technique. Specialising in balayage, foliage, and high-end colour correction in a serene, private environment.</p>
                
                <div class="flex flex-col sm:flex-row gap-6">
                    <a href="{booking_url}" target="_blank" class="bg-white text-dark text-center px-10 py-4 text-xs tracking-[0.2em] uppercase transition hover:bg-gray-200">Reserve Your Experience</a>
                    <a href="services.html" class="border border-white text-white text-center px-10 py-4 text-xs tracking-[0.2em] uppercase transition hover:bg-white hover:text-dark">Explore Services</a>
                </div>
            </div>
        </div>
    </header>

    <!-- Art of Hair Section (Split Design) -->
    <section class="py-32 px-6 lg:px-12 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-20 items-center">
            <div class="relative">
                <div class="absolute -top-6 -left-6 w-32 h-32 bg-accent opacity-20 z-0"></div>
                <img src="https://images.unsplash.com/photo-1617897903246-719242758050?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Balayage Styling" class="relative z-10 w-full h-[600px] object-cover shadow-2xl">
            </div>
            <div>
                <p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">Our Philosophy</p>
                <h2 class="font-serif text-5xl mb-8 leading-tight">The intersection of <br><span class="italic text-accent">art and technique.</span></h2>
                <p class="text-gray-600 font-light leading-relaxed mb-6">
                    Nestled in the historic heart of Nottingham, Lace Market Hair Studio is a sanctuary for those who appreciate the finer details. We don't just cut and colour; we sculpt and formulate specifically for your hair type, lifestyle, and aesthetic.
                </p>
                <p class="text-gray-600 font-light leading-relaxed mb-10">
                    We operate as a collective of elite, self-employed stylists who take immense pride in their craft. From lived-in foliage blondes to sharp, creative cuts, our goal is to deliver unparalleled results in a relaxed, opulent atmosphere.
                </p>
                <a href="about.html" class="text-xs tracking-[0.2em] uppercase border-b border-dark pb-1 font-medium hover:text-accent hover:border-accent transition">Discover Our Studio</a>
            </div>
        </div>
    </section>

    <!-- Featured Treatments (Minimalist Grid) -->
    <section class="bg-white py-32 border-t border-gray-100">
        <div class="max-w-7xl mx-auto px-6 lg:px-12">
            <div class="text-center mb-20">
                <p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">Curated Offerings</p>
                <h2 class="font-serif text-5xl">Signature Treatments</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                <!-- Card 1 -->
                <div class="group cursor-pointer">
                    <div class="overflow-hidden mb-6 h-80">
                        <img src="https://images.unsplash.com/photo-1595152772835-219674b2a8a6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Precision Cutting" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    </div>
                    <div class="text-center">
                        <h3 class="font-serif text-2xl mb-2">Precision Cutting</h3>
                        <p class="text-gray-500 font-light text-sm mb-4">Tailored cuts from £35</p>
                        <a href="{booking_url}" target="_blank" class="text-xs uppercase tracking-widest text-accent group-hover:text-dark transition">Book Service &rarr;</a>
                    </div>
                </div>
                
                <!-- Card 2 -->
                <div class="group cursor-pointer">
                    <div class="overflow-hidden mb-6 h-80">
                        <img src="https://images.unsplash.com/photo-1522337660859-02fbefca4702?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Advanced Colour" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    </div>
                    <div class="text-center">
                        <h3 class="font-serif text-2xl mb-2">Advanced Colour</h3>
                        <p class="text-gray-500 font-light text-sm mb-4">Full head & tinting from £75</p>
                        <a href="{booking_url}" target="_blank" class="text-xs uppercase tracking-widest text-accent group-hover:text-dark transition">Book Service &rarr;</a>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="group cursor-pointer">
                    <div class="overflow-hidden mb-6 h-80">
                        <img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Balayage Mastery" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    </div>
                    <div class="text-center">
                        <h3 class="font-serif text-2xl mb-2">Balayage Mastery</h3>
                        <p class="text-gray-500 font-light text-sm mb-4">Signature highlights from £85</p>
                        <a href="{booking_url}" target="_blank" class="text-xs uppercase tracking-widest text-accent group-hover:text-dark transition">Book Service &rarr;</a>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-16">
                <a href="services.html" class="btn-outline px-10 py-4 text-xs tracking-[0.2em] uppercase inline-block">View Full Menu</a>
            </div>
        </div>
    </section>

    <!-- High-Converting Testimonial / Social Proof -->
    <section class="py-32 bg-[#141414] text-white text-center px-6">
        <div class="max-w-4xl mx-auto">
            <div class="text-accent text-2xl mb-8 space-x-2">
                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
            </div>
            <h2 class="font-serif text-3xl md:text-5xl leading-tight mb-12">"An absolute triumph. The level of care, the chic environment, and the flawless blonde I walked out with—unmatched in Nottingham."</h2>
            <p class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-2">Sarah Jenkins</p>
            <p class="text-accent text-sm italic">Verified Booksy Review</p>
            
            <div class="mt-16">
                <a href="{booking_url}" target="_blank" class="bg-accent text-white hover:bg-white hover:text-dark transition px-12 py-5 text-xs tracking-[0.2em] uppercase inline-block">Transform Your Look</a>
            </div>
        </div>
    </section>
""" + footer

# PAGE: ABOUT
about_content = html_head.format(title="The Studio") + navbar + f"""
    <!-- Page Header -->
    <header class="pt-32 pb-20 bg-white text-center border-b border-gray-100">
        <p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">Our Heritage</p>
        <h1 class="font-serif text-6xl">The Studio</h1>
    </header>

    <section class="py-24 px-6 lg:px-12 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center mb-32">
            <div>
                <h2 class="font-serif text-4xl mb-6">A space designed for comfort and creativity.</h2>
                <p class="text-gray-600 font-light leading-relaxed mb-6">
                    Located in the historic Lace Market, our studio blends industrial heritage with modern luxury. We believe your salon visit should be an escape—a moment of pure indulgence.
                </p>
                <p class="text-gray-600 font-light leading-relaxed">
                    Our team of independent stylists ensures that you receive direct, personalized attention from industry leaders. We use only the highest quality products to preserve the integrity of your hair.
                </p>
            </div>
            <div>
                <img src="https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Salon Details" class="w-full h-[500px] object-cover shadow-xl">
            </div>
        </div>

        <!-- Team -->
        <div class="text-center mb-20">
            <h2 class="font-serif text-4xl mb-4">The Collective</h2>
            <div class="w-12 h-[1px] bg-accent mx-auto"></div>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-12">
            <!-- Team 1 -->
            <div class="text-center group">
                <div class="overflow-hidden mb-6">
                    <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Daniel" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-500">
                </div>
                <h3 class="font-serif text-2xl mb-1">Daniel Mantle</h3>
                <p class="text-xs tracking-[0.2em] uppercase text-gray-500">Senior Stylist</p>
            </div>
            <!-- Team 2 -->
            <div class="text-center group">
                <div class="overflow-hidden mb-6">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Chloe" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-500">
                </div>
                <h3 class="font-serif text-2xl mb-1">Chloe Rowlett</h3>
                <p class="text-xs tracking-[0.2em] uppercase text-gray-500">Stylist & Colourist</p>
            </div>
            <!-- Team 3 -->
            <div class="text-center group">
                <div class="overflow-hidden mb-6">
                    <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Jessica" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-500">
                </div>
                <h3 class="font-serif text-2xl mb-1">Jessica Leivers</h3>
                <p class="text-xs tracking-[0.2em] uppercase text-gray-500">Stylist & Colourist</p>
            </div>
            <!-- Team 4 -->
            <div class="text-center group">
                <div class="overflow-hidden mb-6">
                    <img src="https://images.unsplash.com/photo-1554151228-14d9def656e4?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Paige" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-500">
                </div>
                <h3 class="font-serif text-2xl mb-1">Paige Toplis</h3>
                <p class="text-xs tracking-[0.2em] uppercase text-gray-500">Stylist</p>
            </div>
        </div>
    </section>
""" + footer

# PAGE: SERVICES
services_content = html_head.format(title="Treatments") + navbar + f"""
    <!-- Page Header -->
    <header class="pt-32 pb-20 bg-white text-center border-b border-gray-100">
        <p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">Bespoke Offerings</p>
        <h1 class="font-serif text-6xl">Treatments & Pricing</h1>
    </header>

    <section class="py-24 px-6 lg:px-12 max-w-4xl mx-auto">
        <div class="text-center mb-16">
            <p class="text-gray-500 font-light max-w-2xl mx-auto">Skin tests are required 48 hours prior to any colour service for new clients. Prices may vary slightly based on hair length and complexity.</p>
        </div>
        
        <!-- Category: Cutting & Styling -->
        <div class="mb-20">
            <h2 class="font-serif text-3xl mb-8 border-b border-gray-200 pb-4 text-gray-800">Cutting & Styling</h2>
            
            <div class="space-y-4">
                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Wash, Cut and Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Signature precision cut & finish</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8">
                        <span class="text-lg font-medium text-gray-800">£45.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Short Hair (Wash, Cut & Blowdry)</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Finger length precision</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8">
                        <span class="text-lg font-medium text-gray-800">£35.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Category: Colour & Highlights -->
        <div class="mb-20">
            <h2 class="font-serif text-3xl mb-8 border-b border-gray-200 pb-4 text-gray-800">Colour, Highlights & Balayage</h2>
            
            <div class="space-y-4">
                
                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Partial Highlights w/ Toner, Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Targeted brightness</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£85.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Half Head Highlights w/ Toner, Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Dimension & depth</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£100.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Full Head Highlights w/ Toner, Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Maximum blonding</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£120.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Root Tint w/ Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Seamless touch-up</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£75.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Full Head Colour w/ Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Rich, uniform shade</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£80.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>
                
                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Toner w/ Cut & Blowdry</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Refresh & refine</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£60.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>
                
                <div class="flex flex-col sm:flex-row justify-between sm:items-center py-6 border-b border-gray-100 hover:bg-white p-4 transition group">
                    <div>
                        <h3 class="font-serif text-xl mb-1">Bleach & Tone (under 8 weeks)</h3>
                        <p class="text-gray-400 font-light text-xs uppercase tracking-wider">Total transformation</p>
                    </div>
                    <div class="mt-4 sm:mt-0 flex items-center justify-between sm:gap-8 flex-shrink-0">
                        <span class="text-lg font-medium text-gray-800">£120.00</span>
                        <a href="{booking_url}" target="_blank" class="btn-outline px-6 py-2 text-xs tracking-widest uppercase">Book</a>
                    </div>
                </div>

            </div>
        </div>
        
        <div class="mt-16 text-center">
            <h3 class="font-serif text-3xl mb-6">Ready to elevate your style?</h3>
            <a href="{booking_url}" target="_blank" class="btn-luxury inline-block px-12 py-4 text-xs tracking-[0.2em] uppercase">Secure Your Appointment</a>
        </div>
    </section>
""" + footer

# PAGE: CONTACT
contact_content = html_head.format(title="Contact") + navbar + f"""
    <!-- Page Header -->
    <header class="pt-32 pb-20 bg-white text-center border-b border-gray-100">
        <p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">Connect</p>
        <h1 class="font-serif text-6xl">Contact & Location</h1>
    </header>

    <section class="py-24 px-6 lg:px-12 max-w-6xl mx-auto flex-grow">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-20">
            
            <!-- Contact Details -->
            <div class="flex flex-col justify-center">
                <h2 class="font-serif text-4xl mb-8">We await your visit.</h2>
                <p class="text-gray-500 font-light mb-12 leading-relaxed">Appointments are highly recommended to ensure you receive the dedicated time your hair deserves. Walk-ins are accommodated when possible.</p>
                
                <div class="space-y-10 border-l border-gray-300 pl-8">
                    <div>
                        <h4 class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-2">Location</h4>
                        <p class="font-serif text-2xl text-gray-800">1A Plumptre Street<br>Nottingham NG1 1JL</p>
                    </div>
                    
                    <div>
                        <h4 class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-2">Direct Line</h4>
                        <p class="font-serif text-2xl text-gray-800"><a href="tel:+447970175942" class="hover:text-accent transition">+44 7970 175942</a></p>
                    </div>

                    <div>
                        <h4 class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-2">Availability</h4>
                        <p class="font-serif text-2xl text-gray-800">Mon-Sat: 9am — 8pm<br>Sun: Rest Day</p>
                    </div>
                </div>

                <div class="mt-16">
                    <a href="{booking_url}" target="_blank" class="btn-luxury inline-block px-10 py-4 text-xs tracking-[0.2em] uppercase">Book Your Visit</a>
                </div>
            </div>

            <!-- Image/Map abstraction -->
            <div class="h-[600px] bg-gray-200 relative">
                <img src="https://images.unsplash.com/photo-1513622470522-26c311512b97?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Nottingham Architecture" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-dark bg-opacity-30 flex items-center justify-center">
                    <a href="https://maps.google.com/?q=1A+Plumptre+St,+Nottingham+NG1+1JL,+UK" target="_blank" class="bg-white text-dark px-8 py-4 text-xs tracking-widest uppercase font-medium hover:bg-accent hover:text-white transition shadow-2xl">
                        Open in Maps
                    </a>
                </div>
            </div>
            
        </div>
    </section>
""" + footer

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_content)
with open("services.html", "w", encoding="utf-8") as f:
    f.write(services_content)
with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)

print("Premium HTML files generated successfully.")
