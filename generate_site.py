import os

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Lace Market Hair Studio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Lato:wght@300;400;700&display=swap');
        body {{
            font-family: 'Lato', sans-serif;
            background-color: #faf9f8;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6, .font-serif {{
            font-family: 'Playfair Display', serif;
        }}
        .bg-premium {{
            background-color: #1a1a1a;
        }}
        .text-premium {{
            color: #d4af37; /* Gold */
        }}
        .btn-primary {{
            background-color: #d4af37;
            color: #fff;
            transition: all 0.3s ease;
        }}
        .btn-primary:hover {{
            background-color: #b3932e;
            transform: translateY(-2px);
        }}
        .hero-bg {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1521590832167-7bfcfaa6362f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
        }}
    </style>
    <!-- Google Translate for Kannada -->
    <script type="text/javascript">
        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{pageLanguage: 'en', includedLanguages: 'en,kn', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}}, 'google_translate_element');
        }}
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>
<body class="flex flex-col min-h-screen">
"""

navbar = """
    <!-- Google Translate Widget for Kannada -->
<div id="google_translate_element" style="text-align:right; padding: 5px 20px; background: #1a1a1a; color: white;"></div>
<!-- Navigation -->
    <nav class="bg-premium text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <a href="index.html" class="flex-shrink-0 flex items-center gap-3">
                        <!-- Placeholder for Logo -->
                        <span class="font-serif text-2xl font-bold text-premium tracking-wider">LACE MARKET</span>
                        <span class="text-sm font-light uppercase tracking-widest hidden sm:block pt-1">Hair Studio</span>
                    </a>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="index.html" class="text-gray-300 hover:text-premium transition duration-300">Home</a>
                    <a href="about.html" class="text-gray-300 hover:text-premium transition duration-300">About</a>
                    <a href="services.html" class="text-gray-300 hover:text-premium transition duration-300">Services</a>
                    <a href="contact.html" class="text-gray-300 hover:text-premium transition duration-300">Contact</a>
                    <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-primary px-6 py-2 rounded-full font-semibold tracking-wide uppercase text-sm">Book Appointment</a>
                </div>
                <!-- Mobile menu button -->
                <div class="flex items-center md:hidden">
                    <button type="button" onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="text-gray-300 hover:text-white focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div class="hidden md:hidden bg-premium border-t border-gray-700" id="mobile-menu">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-premium">Home</a>
                <a href="about.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-premium">About</a>
                <a href="services.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-premium">Services</a>
                <a href="contact.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-premium">Contact</a>
                <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="block px-3 py-2 mt-4 text-center btn-primary rounded-md font-semibold">Book Now</a>
            </div>
        </div>
    </nav>
"""

footer = """
    <!-- Footer -->
    <footer class="bg-premium text-white mt-auto py-12 border-t border-gray-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <h3 class="font-serif text-2xl text-premium mb-4">Lace Market Hair Studio</h3>
                    <p class="text-gray-400 font-light mb-4">A calm, relaxing Hairdresser, specialising in all colours including Balayage, Foliage, Highlights for that beautiful blonde.</p>
                    <div class="flex space-x-4">
                        <a href="https://instagram.com/lacemarkethairstudio" target="_blank" class="text-gray-400 hover:text-premium text-xl transition"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="font-serif text-lg mb-4 uppercase tracking-wider">Quick Links</h4>
                    <ul class="space-y-2 font-light text-gray-400">
                        <li><a href="index.html" class="hover:text-premium transition">Home</a></li>
                        <li><a href="about.html" class="hover:text-premium transition">About Us</a></li>
                        <li><a href="services.html" class="hover:text-premium transition">Services & Pricing</a></li>
                        <li><a href="contact.html" class="hover:text-premium transition">Contact & Location</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-serif text-lg mb-4 uppercase tracking-wider">Contact Info</h4>
                    <ul class="space-y-3 font-light text-gray-400">
                        <li class="flex items-start gap-3"><i class="fas fa-map-marker-alt mt-1 text-premium"></i> 1A Plumptre St, Nottingham NG1 1JL, UK</li>
                        <li class="flex items-center gap-3"><i class="fas fa-phone-alt text-premium"></i> +44 7970 175942</li>
                        <li class="flex items-start gap-3"><i class="far fa-clock mt-1 text-premium"></i> 
                            <div>
                                <p>Mon - Sat: 09:00 - 20:00</p>
                                <p>Sun: Closed</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-10 pt-6 text-center text-gray-500 text-sm font-light">
                &copy; 2026 Lace Market Hair Studio. All rights reserved. Designed for excellence.
            </div>
        </div>
    </footer>
</body>
</html>
"""

booking_url = "https://booksy.com/en-gb/167547_lace-market-hair-studio_hair-salon_37343_nottingham"

# PAGE: INDEX
index_content = html_head.format(title="Home") + navbar.format(booking_url=booking_url) + f"""
    <!-- Hero Section -->
    <header class="hero-bg h-[80vh] flex items-center justify-center text-center">
        <div class="max-w-4xl px-4">
            <h2 class="text-premium text-lg sm:text-xl md:text-2xl font-light tracking-[0.3em] uppercase mb-4">Luxury Hairdressing</h2>
            <h1 class="text-5xl sm:text-6xl md:text-7xl font-serif text-white mb-6 drop-shadow-lg">Discover Your Perfect Blonde</h1>
            <p class="text-lg sm:text-xl text-gray-200 font-light mb-10 max-w-2xl mx-auto drop-shadow-md">Specialising in Balayage, Foliage, and Highlights for richness and depth. Experience a calm, relaxing environment in the heart of Nottingham.</p>
            <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-primary inline-block px-10 py-4 rounded-full text-lg font-semibold tracking-wide uppercase shadow-xl">Book Your Transformation</a>
        </div>
    </header>

    <!-- Intro Section -->
    <section class="py-20 px-4 bg-white">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-16">
            <div class="w-full md:w-1/2">
                <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Salon Interior" class="rounded-xl shadow-2xl">
            </div>
            <div class="w-full md:w-1/2">
                <h3 class="text-premium text-sm font-bold tracking-[0.2em] uppercase mb-2">Welcome to</h3>
                <h2 class="font-serif text-4xl md:text-5xl mb-6 text-gray-900">Lace Market Hair Studio</h2>
                <p class="text-gray-600 font-light leading-relaxed mb-6 text-lg">
                    A renowned hair salon nestled in the heart of Nottingham. This exquisite venue boasts a warm and welcoming atmosphere, inviting you to relax while our expert stylists work their magic.
                </p>
                <p class="text-gray-600 font-light leading-relaxed mb-8 text-lg">
                    We take immense pride in the work we do, from creative cutting to lived-in foliage blondes. Our goal is to provide maximum flexibility with little impact on the pocket, creating a studio where hairdressers and clients alike feel completely at ease.
                </p>
                <a href="about.html" class="inline-flex items-center gap-2 text-premium font-semibold hover:text-yellow-700 transition uppercase tracking-wider text-sm">
                    Read Our Story <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Services Highlight -->
    <section class="py-20 px-4 bg-[#faf9f8]">
        <div class="max-w-7xl mx-auto text-center mb-16">
            <h2 class="font-serif text-4xl text-gray-900 mb-4">Our Premium Services</h2>
            <div class="w-24 h-1 bg-premium mx-auto mb-6"></div>
            <p class="text-gray-600 max-w-2xl mx-auto font-light text-lg">Elevate your style with our specialized coloring and cutting services tailored to you.</p>
        </div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">
            <!-- Service 1 -->
            <div class="bg-white rounded-xl shadow-lg overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1617391764985-059c381c63cb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Balayage" class="w-full h-full object-cover group-hover:scale-110 transition duration-700">
                </div>
                <div class="p-8 text-center">
                    <h4 class="font-serif text-2xl mb-3">Balayage & Highlights</h4>
                    <p class="text-gray-500 font-light mb-6">Achieve that perfect blonde with our signature partial, half-head, and full-head highlight services.</p>
                    <a href="services.html" class="text-premium font-semibold uppercase tracking-wider text-sm hover:underline">View Pricing</a>
                </div>
            </div>
            <!-- Service 2 -->
            <div class="bg-white rounded-xl shadow-lg overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1595476108010-b4d1f10d5e43?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Cut and Styling" class="w-full h-full object-cover group-hover:scale-110 transition duration-700">
                </div>
                <div class="p-8 text-center">
                    <h4 class="font-serif text-2xl mb-3">Cut & Blowdry</h4>
                    <p class="text-gray-500 font-light mb-6">Precision cutting and flawless blowdries to start off your day feeling fresh and confident.</p>
                    <a href="services.html" class="text-premium font-semibold uppercase tracking-wider text-sm hover:underline">View Pricing</a>
                </div>
            </div>
            <!-- Service 3 -->
            <div class="bg-white rounded-xl shadow-lg overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Colouring" class="w-full h-full object-cover group-hover:scale-110 transition duration-700">
                </div>
                <div class="p-8 text-center">
                    <h4 class="font-serif text-2xl mb-3">Full Head Colour</h4>
                    <p class="text-gray-500 font-light mb-6">Rich, deep, and perfect tints tailored specifically to match your skin tone and style.</p>
                    <a href="services.html" class="text-premium font-semibold uppercase tracking-wider text-sm hover:underline">View Pricing</a>
                </div>
            </div>
        </div>
        <div class="text-center mt-12">
            <a href="services.html" class="btn-primary inline-block px-8 py-3 rounded-full font-semibold tracking-wide uppercase">View All Services</a>
        </div>
    </section>

    <!-- Review Section -->
    <section class="py-20 px-4 bg-premium text-white text-center">
        <div class="max-w-4xl mx-auto">
            <div class="flex justify-center gap-2 text-premium text-2xl mb-6">
                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
            </div>
            <h2 class="font-serif text-4xl mb-8">Rated 5.0 on Booksy</h2>
            <p class="text-xl font-light italic text-gray-300 mb-10">"Absolutely amazing experience. The salon is beautiful, relaxing, and the stylists are incredibly talented. I wouldn't trust anyone else with my blonde hair!"</p>
            <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-primary inline-block px-10 py-4 rounded-full text-lg font-semibold tracking-wide uppercase shadow-xl">Experience It Yourself</a>
        </div>
    </section>
""" + footer

# PAGE: ABOUT
about_content = html_head.format(title="About Us") + navbar.format(booking_url=booking_url) + f"""
    <!-- Page Header -->
    <header class="bg-premium py-20 text-center">
        <h1 class="font-serif text-5xl text-white mb-4">About Our Studio</h1>
        <div class="w-16 h-1 bg-premium mx-auto"></div>
    </header>

    <section class="py-20 px-4 bg-white">
        <div class="max-w-5xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-20">
                <div>
                    <h2 class="font-serif text-4xl mb-6 text-gray-900">The Lace Market Experience</h2>
                    <p class="text-gray-600 font-light leading-relaxed mb-4 text-lg">
                        Located in the historic and vibrant Lace Market area of Nottingham, our studio was created to provide a sanctuary for both clients and stylists. 
                    </p>
                    <p class="text-gray-600 font-light leading-relaxed mb-4 text-lg">
                        We specialise in all things colour—particularly Balayage, Foliage, and creating that perfect blonde. We focus on richness, depth, and maintaining the integrity and health of your hair.
                    </p>
                    <p class="text-gray-600 font-light leading-relaxed text-lg">
                        Our stylists operate in a self-employed environment, bringing their unique flair and immense passion to every appointment. We pride ourselves on offering luxury hairdressing with maximum flexibility.
                    </p>
                </div>
                <div>
                    <img src="https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Salon details" class="rounded-xl shadow-xl w-full">
                </div>
            </div>

            <!-- Team Section -->
            <div class="text-center mb-16">
                <h2 class="font-serif text-4xl mb-4">Meet Our Expert Team</h2>
                <div class="w-16 h-1 bg-premium mx-auto"></div>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Team Member 1 -->
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-4 shadow-lg border-4 border-white">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Daniel" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-serif text-2xl mb-1">Daniel Mantle</h3>
                    <p class="text-premium text-sm uppercase tracking-wider font-semibold">Senior Stylist</p>
                </div>
                <!-- Team Member 2 -->
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-4 shadow-lg border-4 border-white">
                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Chloe" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-serif text-2xl mb-1">Chloe Rowlett</h3>
                    <p class="text-premium text-sm uppercase tracking-wider font-semibold">Stylist & Colourist</p>
                </div>
                <!-- Team Member 3 -->
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-4 shadow-lg border-4 border-white">
                        <img src="https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Jessica" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-serif text-2xl mb-1">Jessica Leivers</h3>
                    <p class="text-premium text-sm uppercase tracking-wider font-semibold">Stylist & Colourist</p>
                </div>
                <!-- Team Member 4 -->
                <div class="text-center">
                    <div class="w-48 h-48 mx-auto rounded-full overflow-hidden mb-4 shadow-lg border-4 border-white">
                        <img src="https://images.unsplash.com/photo-1554151228-14d9def656e4?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Paige" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-serif text-2xl mb-1">Paige Toplis</h3>
                    <p class="text-premium text-sm uppercase tracking-wider font-semibold">Stylist</p>
                </div>
            </div>
        </div>
    </section>
""" + footer

# PAGE: SERVICES
services_content = html_head.format(title="Services") + navbar.format(booking_url=booking_url) + f"""
    <!-- Page Header -->
    <header class="bg-premium py-20 text-center">
        <h1 class="font-serif text-5xl text-white mb-4">Our Services</h1>
        <p class="text-gray-400 font-light text-lg max-w-2xl mx-auto px-4">Specialising in blonde transformations, balayage, and precision cutting. Skin tests are required 48hr prior to any colour for new clients.</p>
    </header>

    <section class="py-20 px-4 bg-[#faf9f8]">
        <div class="max-w-4xl mx-auto">
            
            <!-- Category: Cutting & Styling -->
            <div class="mb-16">
                <h2 class="font-serif text-3xl mb-8 border-b border-gray-300 pb-4 text-gray-800">Cutting & Styling</h2>
                
                <div class="space-y-6">
                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div>
                            <h3 class="font-serif text-xl mb-1">Wash, Cut and Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">A relaxing wash, precision cut, and professional styling.</p>
                        </div>
                        <div class="text-right flex items-center gap-6">
                            <span class="text-xl font-semibold text-gray-800">£45.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div>
                            <h3 class="font-serif text-xl mb-1">Short Hair (Wash, Cut & Blowdry)</h3>
                            <p class="text-gray-500 font-light text-sm">Length determined by stylist. Includes the options of finger length.</p>
                        </div>
                        <div class="text-right flex items-center gap-6">
                            <span class="text-xl font-semibold text-gray-800">£35.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Category: Colour & Highlights -->
            <div class="mb-16">
                <h2 class="font-serif text-3xl mb-8 border-b border-gray-300 pb-4 text-gray-800">Colour, Highlights & Balayage</h2>
                
                <div class="space-y-6">
                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Partial Highlights w/ Toner, Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£85.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Half Head Highlights w/ Toner, Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£100.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Full Head Highlights w/ Toner, Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£120.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Root Tint w/ Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£75.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Full Head Colour w/ Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£80.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Toner w/ Cut & Blowdry</h3>
                            <p class="text-gray-500 font-light text-sm">Refresh your blonde. Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£60.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                    <div class="flex justify-between items-center bg-white p-6 rounded-lg shadow-sm hover:shadow-md transition">
                        <div class="pr-4">
                            <h3 class="font-serif text-xl mb-1">Bleach & Tone (under 8 weeks)</h3>
                            <p class="text-gray-500 font-light text-sm">Patch test required min 48 hours before appointment.</p>
                        </div>
                        <div class="text-right flex items-center gap-6 flex-shrink-0">
                            <span class="text-xl font-semibold text-gray-800">£120.00</span>
                            <a href="{booking_url}" target="_blank" class="btn-primary px-6 py-2 rounded font-semibold uppercase text-sm">Book</a>
                        </div>
                    </div>

                </div>
            </div>

            <div class="text-center mt-12 bg-white p-8 rounded-xl shadow-lg border border-gray-100">
                <h3 class="font-serif text-2xl mb-4 text-gray-800">Ready for a new look?</h3>
                <p class="text-gray-600 mb-6">Our stylists manage their own schedules. Walk-ins are welcome, but we mainly work on an appointment-only system to ensure you receive our full, undivided attention.</p>
                <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-primary inline-block px-10 py-4 rounded-full text-lg font-semibold tracking-wide uppercase shadow-md">Book Your Appointment Now</a>
            </div>
        </div>
    </section>
""" + footer

# PAGE: CONTACT
contact_content = html_head.format(title="Contact") + navbar.format(booking_url=booking_url) + f"""
    <!-- Page Header -->
    <header class="bg-premium py-20 text-center">
        <h1 class="font-serif text-5xl text-white mb-4">Contact Us</h1>
        <div class="w-16 h-1 bg-premium mx-auto"></div>
    </header>

    <section class="py-20 px-4 bg-white flex-grow">
        <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16">
            
            <!-- Contact Info -->
            <div>
                <h2 class="font-serif text-4xl mb-8 text-gray-900">Get in Touch</h2>
                <p class="text-gray-600 font-light mb-10 text-lg">Whether you have a question about our services, need to consult before a colour change, or want to say hello, we're here for you.</p>
                
                <div class="space-y-8">
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 rounded-full bg-[#f4f0ec] flex items-center justify-center text-premium flex-shrink-0">
                            <i class="fas fa-map-marker-alt text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-serif text-xl mb-1">Our Location</h4>
                            <p class="text-gray-600 font-light">1A Plumptre Street<br>Nottingham NG1 1JL<br>United Kingdom</p>
                        </div>
                    </div>
                    
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 rounded-full bg-[#f4f0ec] flex items-center justify-center text-premium flex-shrink-0">
                            <i class="fas fa-phone-alt text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-serif text-xl mb-1">Phone Number</h4>
                            <p class="text-gray-600 font-light">+44 7970 175942</p>
                        </div>
                    </div>

                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 rounded-full bg-[#f4f0ec] flex items-center justify-center text-premium flex-shrink-0">
                            <i class="far fa-clock text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-serif text-xl mb-1">Business Hours</h4>
                            <p class="text-gray-600 font-light">Monday - Saturday: 09:00 - 20:00<br>Sunday: Closed</p>
                        </div>
                    </div>
                </div>

                <div class="mt-12">
                    <a href="{booking_url}" target="_blank" rel="noopener noreferrer" class="btn-primary inline-block px-8 py-3 rounded-full font-semibold tracking-wide uppercase text-center w-full sm:w-auto shadow-md">Book an Appointment</a>
                </div>
            </div>

            <!-- Map/Image Area -->
            <div class="h-full min-h-[400px] bg-gray-200 rounded-xl overflow-hidden shadow-xl relative">
                <!-- Using a high-quality placeholder image representing location since iframe maps require API keys or exact embed links -->
                <img src="https://images.unsplash.com/photo-1513622470522-26c311512b97?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Nottingham Architecture" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center pointer-events-none">
                    <div class="bg-white p-4 rounded-lg shadow-lg text-center pointer-events-auto">
                        <h4 class="font-serif text-lg font-bold">Lace Market Hair Studio</h4>
                        <p class="text-sm text-gray-500 mb-2">1A Plumptre St, Nottingham</p>
                        <a href="https://maps.google.com/?q=1A+Plumptre+St,+Nottingham+NG1+1JL,+UK" target="_blank" class="text-premium text-sm font-semibold hover:underline">Get Directions</a>
                    </div>
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

print("All HTML files generated successfully.")
