import os
import glob
import re

old_css_and_footer = """
    <style>
        /* Modern Green Footer */
        .alba-footer {
            background-color: #1a3622;
            color: #ffffff;
            padding: 80px 10% 40px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            position: relative;
            z-index: 20;
            border-top: 1px solid rgba(255,255,255,0.05);
            scroll-snap-align: end; 
        }
        
        .footer-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .footer-top {
            display: flex;
            justify-content: space-between;
            gap: 60px;
            margin-bottom: 80px;
        }

        .footer-brand {
            max-width: 300px;
        }

        .footer-logo {
            height: 65px;
            margin-bottom: 25px;
            object-fit: contain;
            opacity: 0.9;
        }

        .footer-mission {
            color: rgba(255, 255, 255, 0.6);
            font-size: 1.05rem;
            line-height: 1.6;
            margin: 0;
            font-weight: 300;
        }

        .footer-links-grid {
            display: flex;
            gap: 80px;
        }

        .footer-column h4 {
            color: #ffffff;
            font-size: 1.15rem;
            font-weight: 400;
            margin-bottom: 25px;
            text-transform: capitalize;
            letter-spacing: 1px;
            font-family: 'Aperto', "Georgia", "Times New Roman", serif;
        }

        .footer-column a {
            display: block;
            color: rgba(255, 255, 255, 0.6);
            text-decoration: none;
            margin-bottom: 12px;
            font-size: 0.95rem;
            transition: color 0.3s ease;
            font-weight: 300;
        }

        .footer-column a:hover {
            color: var(--gold);
        }

        .footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .copyright {
            color: rgba(255, 255, 255, 0.4);
            font-size: 0.85rem;
            margin: 0;
        }

        .legal-links {
            display: flex;
            gap: 20px;
        }

        .legal-links a {
            color: rgba(255, 255, 255, 0.4);
            text-decoration: none;
            font-size: 0.85rem;
            transition: color 0.3s ease;
        }

        .legal-links a:hover {
            color: #ffffff;
        }

        @media (max-width: 900px) {
            .footer-top { flex-direction: column; gap: 40px; margin-bottom: 40px; }
            .footer-links-grid { flex-direction: column; gap: 40px; }
            .alba-footer { padding: 60px 8% 30px; }
            .footer-bottom { flex-direction: column; gap: 20px; align-items: flex-start; }
        }
    </style>

    <footer class="alba-footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="footer-brand">
                    <img src="logos/light.png" alt="Alba Investment Partners" class="footer-logo">
                </div>
                
                <div class="footer-links-grid">
                    <div class="footer-column">
                        <h4>Firm</h4>
                        <a href="index.html">Home</a>
                        <a href="about.html">About Us</a>
                        <a href="insights.html">Insights</a>
                    </div>
                    <div class="footer-column">
                        <h4>Strategies</h4>
                        <a href="investment-approach.html">Investment Approach</a>
                        <a href="our-people.html">Our People</a>
                    </div>
                    <div class="footer-column">
                        <h4>Connect</h4>
                        <a href="contact.html">Contact</a>
                        <a href="#">LinkedIn</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p class="copyright">&copy; 2026 Alba Investment Partners. All rights reserved.</p>
                <div class="legal-links">
                    <a href="privacy-policy.html">Privacy Policy</a>
                    <a href="terms-of-use.html">Terms of Use</a>
                </div>
            </div>
        </div>
    </footer>
"""

html_files = glob.glob('**/*.html', recursive=True)
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    modified = False

    # Remove the Stay Informed section if it exists
    # It might start with <!-- Stay Informed Section --> and end with </section>
    newsletter_pattern = r"(?:<!-- Stay Informed Section -->\s*<style>.*?|\s*<style>\s*\.newsletter-section.*?)<section class=\"newsletter-section\">.*?</section>"
    # Let's use a simpler pattern since we know the class
    # Actually it's easier to just strip from <style> .newsletter-section to </section>
    # In some files it's preceded by <!-- Stay Informed Section -->
    # Let's match from <!-- Stay Informed Section --> down to </section> if present
    p1 = r"\s*<!-- Stay Informed Section -->\s*<style>.*?</section>"
    if re.search(p1, content, flags=re.DOTALL):
        content = re.sub(p1, "", content, flags=re.DOTALL)
        modified = True
    else:
        # Try matching just the style and section
        p2 = r"\s*<style>\s*\.newsletter-section.*?</section>"
        if re.search(p2, content, flags=re.DOTALL):
            content = re.sub(p2, "", content, flags=re.DOTALL)
            modified = True

    # Revert the footer
    # Replace the current <style> + <footer class="alba-footer">...</footer> block
    # Since my previous script injected <style>... Modern Elegant Footer CSS...</style> \n <footer...>
    p_footer = r"\s*<style>\s*/\* Modern Elegant Footer CSS \*/.*?</style>\s*<footer class=\"alba-footer\">.*?</footer>"
    if re.search(p_footer, content, flags=re.DOTALL):
        content = re.sub(p_footer, old_css_and_footer, content, flags=re.DOTALL)
        modified = True

    if modified:
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")

