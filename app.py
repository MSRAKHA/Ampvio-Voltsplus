import streamlit as st

st.set_page_config(page_title="Ampvio Voltsplus Power Solution Pvt Ltd", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {background-color: #f4f4f4;}
    .big-header {color: #0a3d62; text-align: center; font-size: 2.5em; font-weight: bold;}
    .subtitle {color: #3c6382; text-align: center; font-size: 1.2em;}
    .section-title {color: #3c6382; text-align: center; font-size: 2em; margin-top: 2em;}
    .feature-card {background: #fff; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); padding: 1.5em; text-align: center;}
    .gallery-img {border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);}
    .contact-info {text-align: center;}
    .download-btn {background: #3c6382; color: #fff; padding: 0.5em 1em; border-radius: 5px; text-decoration: none;}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="big-header">Ampvio Voltsplus Power Solution Pvt Ltd</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Powering Your Home With Innovation – Solar Panels, Electronics & More</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your trusted partner for solar panels, gadgets & home solutions</div>', unsafe_allow_html=True)

# Navigation (Streamlit doesn't support sticky nav, but we can use sidebar)
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
    st.write("")

# About Section
if section == "About Us":
    st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)
    st.write("""
    We specialize in solar energy solutions with government subsidies, top-notch electronic gadgets, and essential hardware supplies. 
    From solar panels to fans, switches, wires, and water tanks – we've got everything to power your home.
    """)

# Products Section
if section == "Products":
    st.markdown('<div class="section-title">Product Gallery</div>', unsafe_allow_html=True)
    gallery_images = [
        "abb.webp", "abbl.webp", "ABW.webp", "ATOMBERG.webp", "remote_pli_remote_1_3.webp", "ivory_3_.webp", "ivory_4_.webp",
        "https://ae-solar.com/_next/image?url=%2Fimages%2FheroSectionBackground.webp&w=3840&q=100",
        "https://ca-times.brightspotcdn.com/dims4/default/4e71677/2147483647/strip/true/crop/2048x1365+0+0/resize/1200x800!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F0a%2Fe7%2Ffe44c7d4ed2f28db1f7c00fe3adf%2Fla-fi-mo-incandescent-lightbulb-ban-20140101-001",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvIh4agP0ddkjiP3d9FyFxdkCr3ynGwNhQIA&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7pPuWYYtGijWTsdn8ylE-8fcAXfSGuF_yFQ&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD0aOhZTT3TzWcTqieMbxrwVucegaYtO4JoQ&s",
        "https://img.freepik.com/premium-photo/smart-home-concept-with-various-electronic-devices-displayed-black-background_1022970-54043.jpg",
        "https://img.freepik.com/premium-photo/flat-lay-various-modern-tech-gadgets-black-background_1022970-54917.jpg",
        "https://img.freepik.com/premium-photo/home-appliances-set-household-kitchen-technics-isolated-white-background_913665-4512.jpg",
        "https://cbx-prod.b-cdn.net/COLOURBOX59763974.jpg?width=800&height=800&quality=70",
        "https://insolationenergy.in/public/upload/blog/mobilebanner/20240305151028.jpg",
        "https://img.freepik.com/free-photo/aerial-view-private-house-with-solar-panels-roof_181624-14677.jpg?t=st=1746646198~exp=1746649798~hmac=576333925af6ffff4ec36a5b4a0a8b10416fc1bb4b722b099a2398afe1d506c6&w=2000",
        "https://img.freepik.com/premium-photo/compilation-electronic-gadgets-black-background_893571-15167.jpg"
    ]
    cols = st.columns(4)
    for i, img in enumerate(gallery_images):
        with cols[i % 4]:
            if img.startswith("http"):
                st.image(img, use_column_width=True)
            else:
                st.image(img, use_column_width=True, caption=img)

# Services Section
if section == "Services":
    st.markdown('<div class="section-title">Services</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Solar Panels**")
        st.write("High-efficiency panels with government subsidies.")
        st.markdown("**Lights & Fans**")
        st.write("LED lighting, ceiling fans, and more.")
    with col2:
        st.markdown("**Home Gadgets**")
        st.write("Fridges, electronics, and energy-efficient appliances.")
        st.markdown("**Hardware Supplies**")
        st.write("Pipes, wires, switches, tanks and accessories.")
    st.markdown("---")
    st.video("Home Slider 2.mp4")

# Order Now Section
if section == "Order Now":
    st.markdown('<div class="section-title">Order Now</div>', unsafe_allow_html=True)
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

# Testimonials Section
if section == "Testimonials":
    st.markdown('<div class="section-title">Customer Testimonials</div>', unsafe_allow_html=True)
    st.info('"Excellent service and top-quality solar panels!" – Ravi, Andhra Pradesh')
    st.info('"Fast delivery and great support. Highly recommended!" – Priya, Kurnool')
    st.info('"Ampvio helped me switch to solar power with ease. Great service and fast installation!" – Ravi Kumar, Hyderabad')
    st.info('"Affordable electronics and friendly staff. Highly recommend their services!" – Anjali Mehta, Vijayawada')
    st.info('"Best place for all electrical and solar needs. Quick delivery and genuine products." – Suresh Reddy, Warangal')

# Contact Section
if section == "Contact":
    st.markdown('<div class="section-title">Contact Us</div>', unsafe_allow_html=True)
    st.image("Business Card.png", caption="Business Card")
    st.markdown('<a href="Business Card.png" download="Ampvio_Business_Card.png" class="download-btn">Download Business Card</a>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-info">
      <p><b>Phone:</b> <a href="tel:+919849794727">+91 9849794727</a> & <a href="tel:+919441394727">+91 9441394727</a></p>
      <p><b>Email:</b> <a href="mailto:sales.ampviovoltsplus@gmail.com">sales.ampviovoltsplus@gmail.com</a></p>
      <p><b>Address:</b> Ampvio Voltsplus Power Solution Pvt. Ltd, Near Salfia Masjid, Bypass Road, Yemmiganur, Andhra Pradesh, India – 518360</p>
      <p><a href="https://wa.me/919849794727" target="_blank">WhatsApp</a></p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div style="text-align:center;">&copy; 2025 Ampvio Voltsplus Power Solution Pvt Ltd. All rights reserved.</div>', unsafe_allow_html=True)
st.image("Banner.jpeg")
