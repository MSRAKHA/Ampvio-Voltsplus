import streamlit as st

st.set_page_config(page_title="Ampvio Voltsplus Power Solution Pvt Ltd", layout="wide",  page_icon="⚡")

# Custom CSS for styling
st.markdown("""
    <style>
    body, .main {background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;}
    .big-header {
        color: #002244;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        letter-spacing: 2px;
        margin-top: 0.5em;
        margin-bottom: 0.2em;
        text-shadow: 1px 2px 8px #b0c4de;
        background: linear-gradient(90deg, #002244 60%, #00bfae 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        color: #00bfae;
        text-align: center;
        font-size: 1.3em;
        margin-bottom: 0.5em;
    }
    .section-title {
        color: #002244;
        text-align: center;
        font-size: 2.2em;
        margin-top: 2em;
        margin-bottom: 0.5em;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .feature-card {
        background: linear-gradient(120deg, #fff 80%, #e3f2fd 100%);
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        padding: 2em 1em 1.5em 1em;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 1em;
    }
    .feature-card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 8px 32px rgba(0,0,0,0.13);
    }a
    .gallery-img {
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.13);
        margin-bottom: 0.5em;
    }
    .discount-badge {
        display: inline-block;
        background: linear-gradient(90deg, #ff512f 60%, #dd2476 100%);
        color: #fff;
        font-size: 0.95em;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.2em 0.7em;
        margin-bottom: 0.3em;
        margin-right: 0.3em;
        box-shadow: 0 2px 8px rgba(221,36,118,0.13);
    }
    .contact-info {text-align: center;}
    .download-btn {
        background: linear-gradient(90deg, #002244 60%, #00bfae 100%);
        color: #fff;
        padding: 0.6em 1.2em;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 500;
        font-size: 1.1em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: background 0.2s;
    }
    .download-btn:hover {
        background: linear-gradient(90deg, #00bfae 60%, #002244 100%);
    }
    .divider {
        border-top: 2px solid #00bfae;
        margin: 2em 0 1.5em 0;
    }
    .numbers-card {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,191,174,0.08);
        padding: 1.2em 0.5em;
        text-align: center;
        margin-bottom: 1em;
        font-size: 1.3em;
        color: #002244;
        font-weight: 600;
    }
    .highlight-offer {
        background: linear-gradient(90deg, #ff512f 60%, #dd2476 100%);
        color: #fff;
        border-radius: 10px;
        padding: 1em;
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 1em;
        box-shadow: 0 2px 8px rgba(221,36,118,0.13);
    }
    </style>
""", unsafe_allow_html=True)

#Hero Section (background image + overlay)

st.markdown(
    '''<div style="position:relative; width:100%; min-height:320px; background: linear-gradient(rgba(0,0,0,0.7), rgba(0,128,128,0.6)), url('https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=1500&q=80') center/cover no-repeat; border-radius: 18px; margin-bottom: 1.5em; box-shadow: 0 4px 24px rgba(0,0,0,0.13);">
        <div style="padding: 2.5em 0;">
            <div style="color: white; text-align: center; font-size: 3em; font-weight: bold; letter-spacing: 2px; margin-top: 0.5em; margin-bottom: 0.2em; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Ampvio Voltsplus Power Solution Pvt Ltd</div>
            <div class='subtitle' style="color: #f0f0f0; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">Powering Your Home With Innovation – Solar Panels, Electronics & More</div>
            <div class='subtitle' style="color: #f0f0f0; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">Your trusted partner for solar panels, gadgets & home solutions</div>
        </div>
    </div>''', unsafe_allow_html=True)



# Navigation (Streamlit doesn't support sticky nav, but we can use sidebar)
st.sidebar.image("Banner.jpeg", use_container_width=True)
st.sidebar.title("Navigation")
sections = ["Home", "About Us", "Products", "Services", "Order Now", "Testimonials", "Contact"]
section = st.sidebar.radio("Go to", sections)

# Home Section
if section == "Home":
    st.markdown('<div class="section-title">Welcome to Ampvio Voltsplus</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Powering Tomorrow\'s Sustainable Future</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card">🌞<br><b>Solar Solutions</b><br>High-efficiency panels with government subsidies</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card">⚡<br><b>Power Products</b><br>Quality electronic gadgets and appliances</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card">🏠<br><b>Home Hardware</b><br>Complete range of electrical supplies</div>', unsafe_allow_html=True)
    # By the Numbers Section
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">By the Numbers</div>', unsafe_allow_html=True)
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        st.markdown('<div class="numbers-card">500+<br><span style="font-size:0.8em; color:#00bfae;">Installations</span></div>', unsafe_allow_html=True)
    with n2:
        st.markdown('<div class="numbers-card">10+<br><span style="font-size:0.8em; color:#00bfae;">Years Experience</span></div>', unsafe_allow_html=True)
    with n3:
        st.markdown('<div class="numbers-card">1000+<br><span style="font-size:0.8em; color:#00bfae;">Happy Customers</span></div>', unsafe_allow_html=True)
    with n4:
        st.markdown('<div class="numbers-card">20%<br><span style="font-size:0.8em; color:#00bfae;">Avg. Savings</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.info("""\n**Why Choose Us?**\n- Government Subsidy Assistance\n- Fast Delivery & Installation\n- Genuine Products & Warranty\n- Expert Support & Consultation\n""")

# About Section
if section == "About Us":
    st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)
    st.write("""
    We specialize in solar energy solutions with government subsidies, top-notch electronic gadgets, and essential hardware supplies. 
    From solar panels to fans, switches, wires, and water tanks – we've got everything to power your home.
    """)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.success("Empowering homes and businesses with clean, reliable, and affordable energy solutions.")

# Products Section
if section == "Products":
    st.markdown('<div class="section-title">Product Gallery</div>', unsafe_allow_html=True)
    gallery_images = [
        ("abb.webp", "20% OFF"), ("abbl.webp", None), ("ABW.webp", "Limited Time Offer!"), ("ATOMBERG.webp", None), ("remote_pli_remote_1_3.webp", None), ("ivory_3_.webp", "10% OFF"), ("ivory_4_.webp", None),
        ("https://ae-solar.com/_next/image?url=%2Fimages%2FheroSectionBackground.webp&w=3840&q=100", None),
        ("https://ca-times.brightspotcdn.com/dims4/default/4e71677/2147483647/strip/true/crop/2048x1365+0+0/resize/1200x800!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F0a%2Fe7%2Ffe44c7d4ed2f28db1f7c00fe3adf%2Fla-fi-mo-incandescent-lightbulb-ban-20140101-001", "15% OFF"),
        ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvIh4agP0ddkjiP3d9FyFxdkCr3ynGwNhQIA&s", None),
        ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7pPuWYYtGijWTsdn8ylE-8fcAXfSGuF_yFQ&s", None),
        ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD0aOhZTT3TzWcTqieMbxrwVucegaYtO4JoQ&s", "Best Seller"),
        ("https://img.freepik.com/premium-photo/smart-home-concept-with-various-electronic-devices-displayed-black-background_1022970-54043.jpg", None),
        ("https://img.freepik.com/premium-photo/flat-lay-various-modern-tech-gadgets-black-background_1022970-54917.jpg", None),
        ("https://img.freepik.com/premium-photo/home-appliances-set-household-kitchen-technics-isolated-white-background_913665-4512.jpg", None),
        ("https://cbx-prod.b-cdn.net/COLOURBOX59763974.jpg?width=800&height=800&quality=70", None),
        ("https://insolationenergy.in/public/upload/blog/mobilebanner/20240305151028.jpg", "Hot Deal!"),
        ("https://img.freepik.com/free-photo/aerial-view-private-house-with-solar-panels-roof_181624-14677.jpg?t=st=1746646198~exp=1746649798~hmac=576333925af6ffff4ec36a5b4a0a8b10416fc1bb4b722b099a2398afe1d506c6&w=2000", None),
        ("https://img.freepik.com/premium-photo/compilation-electronic-gadgets-black-background_893571-15167.jpg", None)
    ]
    cols = st.columns(4)
    for i, (img, badge) in enumerate(gallery_images):
        with cols[i % 4]:
            if badge:
                st.markdown(f'<span class="discount-badge">{badge}</span>', unsafe_allow_html=True)
            if img.startswith("http"):
                st.image(img, use_container_width=True, caption="")
            else:
                st.image(img, use_container_width=True, caption=img)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Services Section
if section == "Services":
    st.markdown('<div class="section-title">Services</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**☀️ Solar Panels**")
        st.write("High-efficiency panels with government subsidies.")
        st.markdown("**💡 Lights & Fans**")
        st.write("LED lighting, ceiling fans, and more.")
    with col2:
        st.markdown("**🔌 Home Gadgets**")
        st.write("Fridges, electronics, and energy-efficient appliances.")
        st.markdown("**🛠️ Hardware Supplies**")
        st.write("Pipes, wires, switches, tanks and accessories.")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.video("Home Slider 2.mp4")

# Order Now Section
if section == "Order Now":
    st.markdown('<div class="section-title">Order Now</div>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-offer">🎉 Special Offer: Get 10% OFF on your first order! Use code <b>AMPVIO10</b> at checkout.</div>', unsafe_allow_html=True)
    with st.form("order_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        contact = st.text_input("Contact Number")
        address = st.text_area("Delivery Address")
        product = st.text_area("Product Name(s) and Quantity")
        payment = st.selectbox("Payment Method", ["Cash on Delivery", "UPI", "Net Banking"])
        submitted = st.form_submit_button("Submit Order")
        if submitted:
            st.success("Order submitted! We'll contact you soon.")
            st.balloons()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Testimonials Section
if section == "Testimonials":
    st.markdown('<div class="section-title">Customer Testimonials</div>', unsafe_allow_html=True)
    with st.expander("Ravi, Andhra Pradesh"):
        st.info('"Excellent service and top-quality solar panels!"')
    with st.expander("Priya, Kurnool"):
        st.info('"Fast delivery and great support. Highly recommended!"')
    with st.expander("Ravi Kumar, Hyderabad"):
        st.info('"Ampvio helped me switch to solar power with ease. Great service and fast installation!"')
    with st.expander("Anjali Mehta, Vijayawada"):
        st.info('"Affordable electronics and friendly staff. Highly recommend their services!"')
    with st.expander("Suresh Reddy, Warangal"):
        st.info('"Best place for all electrical and solar needs. Quick delivery and genuine products."')
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Contact Section
if section == "Contact":
    st.markdown('<div class="section-title">Contact Us</div>', unsafe_allow_html=True)
    st.image("Business Card.png", caption="Business Card")
    st.markdown('<a href="Business Card.png" download="Ampvio_Business_Card.png" class="download-btn">Download Business Card</a>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-info">
      <p><b>📞 Phone:</b> <a href="tel:+919849794727">+91 9849794727</a> & <a href="tel:+919441394727">+91 9441394727</a></p>
      <p><b>✉️ Email:</b> <a href="mailto:sales.ampviovoltsplus@gmail.com">sales.ampviovoltsplus@gmail.com</a></p>
      <p><b>🏢 Address:</b> Ampvio Voltsplus Power Solution Pvt. Ltd, Near Salfia Masjid, Bypass Road, Yemmiganur, Andhra Pradesh, India – 518360</p>
      <p><a href="https://wa.me/919849794727" target="_blank">💬 WhatsApp</a></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div style="text-align:center; color:#002244; font-size:1.1em;">&copy; 2025 Ampvio Voltsplus Power Solution Pvt Ltd. All rights reserved.</div>', unsafe_allow_html=True)


