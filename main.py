import streamlit as st
from urllib.parse import quote, unquote
import streamlit.components.v1 as components

st.markdown("""
<style>
    :root {
        scroll-behavior: smooth;
        --bg: #ffffff;
        --text: #111827;
        --primary-color: #333333;
        --accent-color: #0066cc;
        --light-gray: #f5f5f5;
        --medium-gray: #999999;
        --dark-gray: #444444;
        --card-bg: #f5f5f5;
        --glass-bg: rgba(255,255,255,0.9);
        --section-bg: rgba(0,0,0,0.06);
        --section-text: #111827;
        --skill-text: #111827;
        --popup-bg: #ffffff;
        --popup-text: #000000;
        --header-text: #333333;
        --image-filter: grayscale(100%);
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --bg: #0b0b0d;
            --text: #e6eef8;
            --primary-color: #e6eef8;
            --accent-color: #8ab4ff;
            --card-bg: rgba(255,255,255,0.07);
            --glass-bg: rgba(255,255,255,0.05);
            --section-bg: rgba(51,51,51,0.7);
            --section-text: #ffffff;
            --skill-text: #ffffff;
            --popup-bg: #111214;
            --popup-text: #ffffff;
            --header-text: #e6eef8;
            --image-filter: grayscale(100%);
        }
    }

    html, body {
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden;
        background-color: var(--bg) !important;
        color: var(--text) !important;
    }

    /* Hide Streamlit header, footer, and main menu */
    #MainMenu, footer, header {
        display: none !important;
        visibility: hidden;
        height: 0 !important;
    }

    /* Header styling */
    .header {
        font-size: clamp(2rem, 6vw, 3.5rem) !important;
        font-weight: bold !important;
        color: var(--header-text) !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Section Header */
    .section-header {
        font-size: clamp(1.5rem, 4vw, 2rem) !important;
        color: var(--section-text) !important;
        background: var(--section-bg) !important;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 1rem !important;
        margin: 2rem 0 1rem !important;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    }

    .stApp {
        padding: 0 !important;
        margin: 0 !important;
        background: transparent !important;
    }

    /* Skill box */
    .skill-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: var(--card-bg);
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(0,0,0,0.04);
        color: var(--skill-text);
    }

    .highlight {
        color: var(--text);
        font-weight: bold;
    }

    /* Streamlit image grayscale + hover effect */
    [data-testid="stImage"] img {
        filter: var(--image-filter);
        transition: filter 0.3s ease;
        border-radius: 12px;
    }

    [data-testid="stImage"] img:hover {
        filter: none;
    }

    /* Subheader fix */
    .stSubheader, [data-testid="stSubheader"] {
        color: var(--text) !important;
        background-color: var(--card-bg) !important;
        padding: 0.5rem 1rem !important;
        border-radius: 5px;
        margin-bottom: 1rem !important;
    }

    /* Column adjustments */
    .element-container {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding: 0 !important;
    }

    .hero-image-wrapper {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem 0;
    }

    .hero-image {
        height: 320px;
        width: auto;
        object-fit: contain;
        border-radius: 12px;
        filter: var(--image-filter);
        transition: filter 0.3s ease;
    }

    .hero-image:hover {
        filter: none;
    }

    /* Responsive hero image on small screens */
    @media (max-width: 768px) {
        .hero-image {
            height: 220px;
        }
    }

    @media (max-width: 480px) {
        .hero-image {
            height: 160px;
        }
        .gallery-grid {
            grid-template-columns: 1fr;
        }
    }

    /* Popup for copy */
    .copy-popup {
        position: fixed;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        background-color: var(--popup-bg);
        color: var(--popup-text);
        padding: 10px 18px;
        border-radius: 6px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        font-size: 14px;
        font-weight: bold;
        z-index: 9999;
        display: none;
    }
</style>
""", unsafe_allow_html=True)


menu = ["Home", "Education", "Skills", "Experience", "Achievements", "Media", "Photo Gallery"]
tabs = st.tabs(menu)

with tabs[0]:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("""
<style>
.stImage > img {
    /* Your hero-image styles here */
}
</style>
            """, unsafe_allow_html=True)
        st.image("photos/profile.jpg", use_container_width=True)

    with col2:
        st.markdown('<p class="header">Akshat Pandey</p>', unsafe_allow_html=True)

        # Inject global popup HTML + JS
        st.markdown("""
<div id="copyPopup" class="copy-popup"></div>

<script>
function copyToClipboard(text, message) {
    navigator.clipboard.writeText(text).then(() => {
        const popup = document.getElementById("copyPopup");
        popup.textContent = message;
        popup.style.display = "block";
        setTimeout(() => {
            popup.style.display = "none";
        }, 2000);
    });
}
</script>
        """, unsafe_allow_html=True)

        # Now render social icons
        components.html("""
        <style>
        :root {
            --social-text: #333333;
            --social-hover: #0066cc;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --social-text: #a0a0a0;
                --social-hover: #8ab4ff;
            }
        }

        .social-container {
            display: flex;
            gap: 26px;
            margin-top: 0px;
            align-items: center;
            flex-wrap: wrap;
            position: relative;
            z-index: 0;
            margin-bottom: 0; 
            margin: 0px 0px 0px 0px; !important;
      
        }

        .social-link, .copy-icon {
            color: var(--social-text);
            text-decoration: none;
            transition: color 0.3s ease;
            font-size: 24px;
            cursor: pointer;
        }
        .social-link:hover,
        .copy-icon:hover {
            color: var(--social-hover);
        }

        /* Copy popup */
        .copy-popup {
            position: fixed;
            top: 10px;
            left: 30%;
            transform: translateX(-50%);
            background-color: #ffffff;
            color: #000000;
            padding: 10px 18px;
            border-radius: 6px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
            font-size: 14px;
            font-weight: bold;
            z-index: 9999;
            display: none;
        }

        @media (prefers-color-scheme: dark) {
            .copy-popup {
                background-color: #111214;
                color: #ffffff;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            }
        }
        </style>

        <!-- Font Awesome -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <!-- Social Icons -->
        <div class="social-container">
            <a class="social-link" href="https://instagram.com/akshat_pandey0111" target="_blank" aria-label="Instagram">
                <i class="fab fa-instagram"></i>
            </a>

            <a class="social-link" href="https://in.linkedin.com/in/akshat-pandey-4739a82a7" target="_blank" aria-label="LinkedIn">
                <i class="fab fa-linkedin"></i>
            </a>

            <i class="fas fa-phone copy-icon" onclick="copyToClipboard('+91 9925112498', 'Phone copied to clipboard')"></i>

            <i class="fas fa-envelope copy-icon" onclick="copyToClipboard('akshatp0905@gmail.com', 'Email ID copied to clipboard')"></i>
        </div>

        <!-- Copy Popup -->
        <div id="copyPopup" class="copy-popup"></div>

        <script>
        function copyToClipboard(text, message) {
            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(() => {
                    showCopyPopup(message);
                }).catch(err => {
                    console.error('Clipboard copy failed:', err);
                });
            } else {
                console.warn('Clipboard not supported');
            }
        }

        function showCopyPopup(message) {
            const popup = document.getElementById("copyPopup");
            popup.textContent = message;
            popup.style.display = "block";
            setTimeout(() => {
                popup.style.display = "none";
            }, 2000);
        }
        </script>
        """, height=40)

        # Final title bar
        st.markdown('<p style="margin-top: 0;">Anchor | Orator | Public Speaker | Debater</p>', unsafe_allow_html=True)


    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    st.write("""
     I am a passionate anchor, public speaker, and debater with a deep love for literature, mythology, and poetry. 
    With experience in anchoring major formal and informal events, I take pride in my ability to engage audiences 
    with confidence and clarity. My journey has been enriched by numerous opportunities that have helped me grow 
    into a versatile speaker and performer.
    """)


with tabs[1]:
    st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)

    components.html("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>
    .timeline-container {
      display: flex;
      justify-content: center;
      margin-top: 40px;
      overflow-x: auto;
    }

    .timeline-horizontal {
      display: flex;
      align-items: center;
      position: relative;
      gap: 80px;
      padding: 20px 0;
    }

    /* Light Mode Timeline */
    .timeline-item {
      text-align: center;
      color: #333333;
      transition: color 0.3s ease;
      position: relative;
    }

    .timeline-item:hover {
      color: var(--accent-color);
    }

    .timeline-item:hover .timeline-dot {
      background-color: var(--accent-color);
      border-color: var(--accent-color);
    }

    .timeline-icon {
      font-size: 30px;
      margin-bottom: 8px;
      color: #333333;
    }

    .timeline-dot {
      width: 14px;
      height: 14px;
      background-color: #666666;
      border: 2px solid #333333;
      border-radius: 50%;
      margin: 0 auto 8px auto;
      transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .timeline-title {
      font-weight: bold;
      font-size: 14px;
      color: #111827;
    }

    .timeline-subtitle {
      font-size: 12px;
      opacity: 0.8;
      color: #666666;
    }

    .timeline-line {
      position: absolute;
      top: 38px;
      left: 0;
      right: 0;
      height: 2px;
      background-color: #333;
    }

    /* Dark Mode Timeline */
    @media (prefers-color-scheme: dark) {
      .timeline-item {
        color: #e6eef8;
      }

      .timeline-item:hover {
        color: var(--accent-color);
      }

      .timeline-item:hover .timeline-dot {
        background-color: var(--accent-color);
        border-color: var(--accent-color);
      }

      .timeline-icon {
        color: #e6eef8;
      }

      .timeline-dot {
        background-color: #5a6d8a;
        border: 2px solid #8ab4ff;
      }

      .timeline-title {
        color: #e6eef8;
      }

      .timeline-subtitle {
        color: #a8b8d4;
      }

      .timeline-line {
        background-color: #8ab4ff;
      }
    }
    </style>

    <div class="timeline-container">
      <div class="timeline-horizontal">
        <div class="timeline-line"></div>

        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-icon"><i class="fas fa-graduation-cap"></i></div>
          <div class="timeline-title">KV Sangathan</div>
          <div class="timeline-subtitle">Alumni</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-icon"><i class="fas fa-graduation-cap"></i></div>
          <div class="timeline-title">KV No.4 ONGC</div>
          <div class="timeline-subtitle">Passed out in 2021</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-icon"><i class="fas fa-university"></i></div>
          <div class="timeline-title">GSFC University</div>
          <div class="timeline-subtitle">B.Tech Chem Engg (Current)</div>
        </div>
      </div>
    </div>
    """, height=300)


st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }

        :root {
            --section-bg: rgba(0,0,0,0.06);
            --section-text: #111827;
            --card-bg: #f5f5f5;
            --skill-text: #111827;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --section-bg: rgba(51,51,51,0.7);
                --section-text: #ffffff;
                --card-bg: rgba(255,255,255,0.07);
                --skill-text: #ffffff;
            }
        }

        .section-header {
            font-size: 36px;
            font-weight: 600;
            color: var(--section-text);
            text-align: center;
            border-bottom: 2px solid var(--section-text);
            display: inline-block;
            padding-bottom: 6px;
            margin-top: 20px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }

        .skill-box {
            background-color: var(--card-bg);
            color: var(--skill-text);
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            font-size: 16px;
            border: 1px solid rgba(0,0,0,0.04);
        }

        .skill-box:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
        }

        @media (max-width: 768px) {
            .skill-box {
                margin: 10px auto;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- Fancy Skills Grid CSS ---
st.markdown("""
<style>
    :root {
        --section-bg: rgba(0,0,0,0.06);
        --section-text: #111827;
        --card-bg: rgba(0,0,0,0.06);
        --card-border: rgba(0,0,0,0.08);
        --card-shadow: rgba(0,0,0,0.08);
        --card-text: #111827;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --section-bg: rgba(51,51,51,0.7);
            --section-text: #ffffff;
            --card-bg: rgba(255,255,255,0.08);
            --card-border: rgba(255,255,255,0.15);
            --card-shadow: rgba(0,0,0,0.3);
            --card-text: #ffffff;
        }
    }

    .section-header {
        font-size: clamp(1.5rem, 4vw, 2rem) !important;
        color: var(--section-text) !important;
        background: var(--section-bg);
        backdrop-filter: blur(8px);
        padding: 1rem !important;
        border-radius: 12px;
        margin: 2rem 0 1rem !important;
        box-shadow: 0 2px 8px var(--card-shadow);
        text-align: center;
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 1rem;
        padding: 1rem 0;
    }

    .skill-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 1.5rem;
        color: var(--card-text);
        font-size: 1.05rem;
        box-shadow: 0 8px 24px var(--card-shadow);
        transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .skill-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 32px var(--card-shadow);
        background-color: var(--card-bg);
        opacity: 0.95;
    }

</style>
""", unsafe_allow_html=True)

# --- Skills Section Content ---
with tabs[2]:
    st.markdown('<h2 class="section-header">🧠 Skills</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="skills-grid">
        <div class="skill-card">🎤 Public Speaking & Anchoring</div>
        <div class="skill-card">💬 Communication & Debate</div>
        <div class="skill-card">📚 Literature & Mythology</div>
        <div class="skill-card">🎭 Event Management</div>
        <div class="skill-card">🌐 Bilingual Proficiency (Hindi/English)</div>
        <div class="skill-card">✍️ Content Creation & Writing</div>
        <div class="skill-card">🎥 Video Production</div>
        <div class="skill-card">🎶 Music & Poetry</div>
    </div>
    """, unsafe_allow_html=True)

# --- CSS for Experience Grid ---
st.markdown("""
<style>
    :root {
        --exp-card-bg: rgba(0,0,0,0.06);
        --exp-card-border: rgba(0,0,0,0.08);
        --exp-card-shadow: rgba(0,0,0,0.08);
        --exp-card-text: #111827;
        --exp-card-hover-bg: rgba(0,0,0,0.09);
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --exp-card-bg: rgba(255,255,255,0.08);
            --exp-card-border: rgba(255,255,255,0.15);
            --exp-card-shadow: rgba(0,0,0,0.3);
            --exp-card-text: #ffffff;
            --exp-card-hover-bg: rgba(255,255,255,0.13);
        }
    }

    .experience-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-top: 1rem;
    }

    .experience-card {
        background: var(--exp-card-bg);
        border: 1px solid var(--exp-card-border);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 16px;
        padding: 1.5rem;
        color: var(--exp-card-text);
        font-size: 1.05rem;
        box-shadow: 0 6px 16px var(--exp-card-shadow);
        transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
    }

    .experience-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 32px var(--exp-card-shadow);
        background-color: var(--exp-card-hover-bg);
    }
</style>
""", unsafe_allow_html=True)
experiences = [
    {
        "title": "🎤 Hosted 10+ events at GSFC University (both formal and informal)",
        "details": [
            "📅 Holi Celebration 2025",
            "📅 University Foundation Day 2024",
            "📅 National Youth Day 2024",
            "📅 University Foundation Day 2023",
        ]
    },
    {
        "title":    "🏛️ Anchored key national celebrations at University level:",
        "details": [
            "🎉 Republic Day 2025",
            "🎉 Independence Day 2024",
            "🎉 Republic Day 2024"
        ]
    },
    {
        "title": "🗣️ Participated in All India Nandlal Gadiya Memorial Debate Competition (National Level) at Mewar University, Chittorgarh",
        "details": [

        ]
    },
    {
        "title": "📱 Featured in social media reels for:",
        "details": [
            "📅 Independence Day 2024",
            "📅 Diwali 2024",
            "📅 National Youth Day 2024"
        ]
    }

]
with tabs[3]:
    st.markdown('<p class="section-header">💼 Experience</p>', unsafe_allow_html=True)
    st.markdown('<div class="experience-grid">', unsafe_allow_html=True)

    for exp in experiences:
        exp_html = f"""
        <div class="experience-card">
            {exp['title']}<br><br>
        """
        for detail in exp['details']:
            exp_html += f"&nbsp;&nbsp;&nbsp;&nbsp;{detail}<br>"
        exp_html += "</div>"

        st.markdown(exp_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


achievements = [
    "🏆 Winner, GSFC University Debate Competition 2023",
    "🥇 1st Place, Inter-College Anchoring Challenge",
    "🗣️ Selected Speaker, National Youth Parliament 2022",
    "📜 Certified in Advanced Public Speaking",
    "🎙️ Featured Host on GSFCU's official YouTube Channel",
    "🏅 Awarded Best Orator, Cultural Fest 2023",
    "✍️ Recognized Writer for University Magazine",
    "🎖️ Lead Organizer, Literary and Cultural Events"
]

with tabs[4]:
    st.markdown('<p class="section-header">🏅 Achievements</p>', unsafe_allow_html=True)
    st.markdown('<div class="skill-grid">', unsafe_allow_html=True)

    for item in achievements:
        st.markdown(f'<div class="skill-card">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<style>
    :root {
        --achievement-bg: rgba(0,0,0,0.06);
        --achievement-border: rgba(0,0,0,0.08);
        --achievement-shadow: rgba(0,0,0,0.08);
        --achievement-text: #111827;
        --achievement-hover-bg: rgba(0,0,0,0.09);
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --achievement-bg: rgba(255,255,255,0.08);
            --achievement-border: rgba(255,255,255,0.15);
            --achievement-shadow: rgba(0,0,0,0.3);
            --achievement-text: #ffffff;
            --achievement-hover-bg: rgba(255,255,255,0.13);
        }
    }

    .skill-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 1rem;
    }

    .skill-card {
        background-color: var(--achievement-bg);
        border: 1px solid var(--achievement-border);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 1.25rem;
        color: var(--achievement-text);
        font-weight: 500;
        box-shadow: 0 4px 12px var(--achievement-shadow);
        transition: transform 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
    }

    .skill-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 24px var(--achievement-shadow);
        background-color: var(--achievement-hover-bg);
    }
</style>
""", unsafe_allow_html=True)




with tabs[5]:
    st.markdown('<p class="section-header">Media Gallery</p>', unsafe_allow_html=True)
    st.subheader("Featured Videos")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Foundation Day", "Independence Day", "Republic Day", "Diwali Celebration", "National Youth Day", "Youth Parliament"])
    with tab1:
        st.video("https://www.youtube.com/embed/7Fzq5t4BTVs?si=ZZtFwEKXKixHevIE")

    with tab2:
        instagram_embed = """
        <div style="display: flex; justify-content: center;">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/C-mzJNDBsF3/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/C-mzJNDBsF3/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/C-mzJNDBsF3/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by GSFC University (@gsfcuniversity)</a></p></div></blockquote>
        <script async src="//www.instagram.com/embed.js"></script>
        """
        st.components.v1.html(instagram_embed, height=550, scrolling=False)
        st.video("https://www.youtube.com/embed/L1bDMYQ6mr8?si=GnFGppSzMgsGYUV4")

    with tab3:
        st.video("https://www.youtube.com/embed/YMr-EaR5-QY?si=7QIezqU24eO5eubD")

    with tab4:
        instagram_embed = """
        <div style="display: flex; justify-content: center;">
            <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DEtXaymhuDd/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);">
                <!-- Rest of your Instagram embed code -->
            </blockquote>
            <script async src="//www.instagram.com/embed.js"></script>
        </div>
        """
        st.components.v1.html(instagram_embed, height=600,scrolling=False)
    with tab5:
        instagram_embed = """
        <div style="display: flex; justify-content: center; width: 100%; max-width: 540px; margin: 0 auto;">
            <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DBtE37APqdB/?utm_source=ig_embed&amp;utm_campaign=loading"
            data-instgrm-version="14"
            style="background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15);
            margin: 1px; width: 100%; aspect-ratio: 16/9;">
                <!-- Rest of your Instagram embed code -->
            </blockquote>
            <script async src="//www.instagram.com/embed.js"></script>
        </div>
        """
        st.components.v1.html(instagram_embed, height=900, scrolling=False)
    with tab6:
        st.video('Video/video.mp4')



with tabs[6]:
    def display_event(title, indices):
        st.markdown(
            f'''
            <style>
                .event-title {{
                    font-size: 20px;
                    font-weight: 600;
                    margin-bottom: 4px;
                    color: #111827;
                }}

                @media (prefers-color-scheme: dark) {{
                    .event-title {{
                        color: #ebebeb;
                    }}
                }}

                .event-divider {{
                    margin-top: 2px;
                    margin-bottom: 10px;
                    border: 1px solid #d0d0d0;
                }}

                @media (prefers-color-scheme: dark) {{
                    .event-divider {{
                        border-color: #444;
                    }}
                }}
            </style>
            <p class="event-title">{title}</p>
            <hr class="event-divider">
          <br>
            ''',
            unsafe_allow_html=True
        )
        cols = st.columns(4)
        for idx in indices:
            with cols[(idx - indices[0]) % 4]:
                try:
                    st.image(f"photos/{idx}.jpeg", use_container_width=True)
                except:
                    st.error(f"Image {idx}.jpeg not found")
        st.markdown("<hr>", unsafe_allow_html=True)

    display_event("Independence Day & Republic Day", range(2, 8))
    display_event("Hosting University Events", range(8, 12))
    display_event("Youth Parliament", range(12, 17))
    display_event("Holi Celebration at University", range(22, 26))
    display_event("All India Nandlal Gadiya Memorial Debate Competition", range(26, 32))
