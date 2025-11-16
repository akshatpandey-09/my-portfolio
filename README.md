# My Portfolio

A modern, responsive portfolio website built with [Streamlit](https://streamlit.io/) showcasing education, experience, skills, projects, and achievements with a beautiful dark/light mode theme.

## Features

✨ **Modern Design**
- Responsive and mobile-friendly interface
- Smooth scroll animations
- Glass-morphism UI elements
- Gradient backgrounds and modern typography

🌓 **Theme Support**
- Automatic light/dark mode detection based on system preferences
- Smooth theme transitions
- Custom CSS variables for consistent color scheme

📱 **Interactive Components**
- Timeline view for education and experience
- Project showcases with descriptions
- Skill cards with visual organization
- Achievement badges and milestones

📊 **Sections Included**
- **Hero Section**: Personal introduction with profile image
- **Education**: Timeline of educational background
- **Experience**: Work experience and internships
- **Skills**: Technical and professional competencies
- **Projects**: Showcased projects with details
- **Achievements**: Certifications and recognitions
- **Contact**: Social media and contact information

## Project Structure

```
my-portfolio-main/
├── main.py              # Main Streamlit application
├── README.md           # Project documentation
├── test.py             # Test file
├── Document/           # Documentation files
├── photos/             # Image assets
└── Video/              # Video assets
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the repository**
   ```bash
   cd my-portfolio-main
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Access in browser**
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

## Configuration

### Streamlit Settings

A `~/.streamlit/config.toml` file can be created to customize Streamlit behavior:

```toml
[browser]
gatherUsageStats = false

[client]
showErrorDetails = true
```

### Customization

Edit `main.py` to customize:
- **Colors**: Modify CSS variables in the `:root` selector
- **Content**: Update section text and information
- **Images**: Replace image paths in the `photos/` directory
- **Styling**: Adjust CSS rules for your preferred appearance

## Color Scheme

### Light Mode
- Background: #ffffff
- Text: #111827
- Accent: #0066cc
- Cards: #f5f5f5

### Dark Mode
- Background: #0b0b0d
- Text: #e6eef8
- Accent: #8ab4ff
- Cards: rgba(255,255,255,0.07)

The theme automatically detects user's system preference via `prefers-color-scheme` media query.

## Components

### Timeline
- Educational institutions and milestones
- Interactive hover effects
- Responsive layout for different screen sizes

### Timeline Styling
- Light mode: Dark text with blue accent on hover
- Dark mode: Light text with light blue accent on hover
- Smooth transitions and animations

### Project Cards
- Showcase your work with descriptions
- Links to live projects or repositories
- Visual project previews

### Skill Cards
- Organized skill categories
- Visual representation of proficiency
- Easy to update and maintain

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## File Assets

### Images
Place your images in the `photos/` directory:
- Profile picture
- Project screenshots
- Achievement images

### Videos
Place videos in the `Video/` directory for embedding in your portfolio.

### Documents
Store any documentation or PDFs in the `Document/` folder.

## Technologies Used

- **Streamlit**: Web framework for creating data applications
- **HTML/CSS**: Markup and styling
- **Font Awesome**: Icon library
- **Python**: Backend logic

## Tips for Customization

1. **Update Personal Information**
   - Edit name, title, and bio in main.py

2. **Add New Sections**
   - Follow the existing section structure in the code
   - Use consistent styling with CSS classes

3. **Customize Colors**
   - Modify CSS variables in the `:root` selector
   - Update both light and dark mode variables

4. **Add Social Links**
   - Update contact section with your social profiles
   - Use Font Awesome icons for consistency

5. **Responsive Images**
   - Ensure images are optimized for web
   - Use appropriate sizing for different screen sizes

## Performance Optimization

- Lazy loading for images
- Efficient CSS with variables
- Minimal JavaScript usage
- Streamlit's built-in caching for faster loads

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run main.py --server.port 8502
```

### Images Not Loading
- Verify image paths are correct
- Ensure images are in the `photos/` directory
- Check file permissions

### Theme Not Changing
- Clear browser cache
- Ensure system dark mode preference is set correctly
- Check CSS media queries in developer tools

## Deployment

### Deploy to Streamlit Cloud
1. Push your repository to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io/)
3. Deploy from your GitHub repository
4. Share the public URL

### Deploy to Other Platforms
- Heroku
- AWS
- Google Cloud
- Azure
- PythonAnywhere

## Future Enhancements

- [ ] Blog section for articles
- [ ] Interactive skill visualization
- [ ] Project filtering by category
- [ ] Contact form integration
- [ ] Analytics tracking
- [ ] Multi-language support

## License

This project is open source and available under the MIT License.

## Contact & Support

For questions or suggestions about this portfolio template, feel free to reach out through the contact section in the application.

---

**Last Updated**: November 17, 2025

Made with ❤️ using Streamlit
