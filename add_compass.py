import re

compass_code = """
    <!-- Compass Section -->
    <style>
        .compass-section {
            background-color: var(--accent);
            color: #ffffff;
            position: relative;
            /* Will be dynamically sized based on scroll */
        }
        .compass-sticky {
            position: sticky;
            top: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10%;
            overflow: hidden;
        }
        .compass-side {
            flex: 1;
            max-width: 400px;
            z-index: 5;
        }
        .compass-side h2 {
            font-size: 4.5rem;
            font-weight: 300;
            margin: 0 0 30px 0;
            letter-spacing: -1px;
            font-family: 'Aperto', "Georgia", serif;
            line-height: 1.1;
        }
        .compass-side p {
            font-family: 'Inter', sans-serif;
            font-size: 1.25rem;
            line-height: 1.6;
            color: rgba(255,255,255,0.7);
            font-weight: 300;
        }
        .compass-container {
            flex: 1.2;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .compass-svg {
            position: absolute;
            width: 100%;
            height: 100%;
            max-width: 700px;
            max-height: 700px;
            z-index: 1;
        }
        .tick-line {
            stroke: rgba(255,255,255,0.15);
            transition: stroke 0.3s;
        }
        .ring-bg {
            fill: none;
            stroke: rgba(255,255,255,0.08); 
            stroke-width: 1;
        }
        .ring-progress {
            fill: none;
            stroke: var(--gold);
            stroke-width: 2; 
            stroke-dasharray: 1068;
            stroke-dashoffset: 1068;
            stroke-linecap: round;
            will-change: stroke-dashoffset;
        }
        .compass-content {
            text-align: center;
            width: 60%;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .compass-step {
            background: #ffffff;
            color: #000000;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 30px;
            font-family: 'Inter', -apple-system, sans-serif;
            letter-spacing: 2px;
        }
        .compass-title {
            font-size: 2.8rem;
            font-weight: 400;
            margin: 0 0 20px 0;
            font-family: 'Aperto', "Georgia", serif;
            color: #ffffff;
            opacity: 1;
            transition: opacity 0.3s ease;
        }
        .compass-desc {
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            color: rgba(255,255,255,0.6);
            margin: 0;
            font-weight: 300;
            opacity: 1;
            transition: opacity 0.3s ease;
        }

        @media (max-width: 1024px) {
            .compass-sticky {
                flex-direction: column;
                justify-content: center;
                padding: 10% 5%;
            }
            .compass-side {
                width: 100%;
                text-align: center;
                margin-bottom: 40px;
            }
            .compass-side h2 { font-size: 2.5rem; }
            .compass-side p { display: none; }
            .compass-container {
                width: 100vw;
                height: 100vw;
            }
            .compass-content { width: 80%; }
            .compass-title { font-size: 2rem; }
            .compass-desc { font-size: 1rem; }
        }
    </style>

    <div class="compass-section" id="compass-section">
        <div class="compass-sticky">
            <div class="compass-side">
                <h2>Generating<br>Alpha</h2>
                <p>Rather than relying on broad market direction, we generate alpha through:</p>
            </div>
            
            <div class="compass-container" id="compass-wrapper">
                <svg class="compass-svg" viewBox="0 0 400 400" id="compass-svg-graphic"></svg>
                
                <div class="compass-content">
                    <div class="compass-step" id="compass-step">1 / 5</div>
                    <h3 class="compass-title" id="compass-title">Selection</h3>
                    <p class="compass-desc" id="compass-desc">Fundamental credit selection</p>
                </div>
            </div>
        </div>
        
        <!-- 5 items = 500vh height to trigger massive scrub distance mapping seamlessly -->
        <div style="height: 500vh;"></div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const compassSection = document.getElementById("compass-section");
            const svgGraphic = document.getElementById("compass-svg-graphic");
            const titleEl = document.getElementById("compass-title");
            const descEl = document.getElementById("compass-desc");
            const stepEl = document.getElementById("compass-step");
            
            if(!compassSection || !svgGraphic) return;

            const characteristics = [
                { label: "Selection", value: "Fundamental credit selection" },
                { label: "Relative Value", value: "Capital structure and relative value opportunities" },
                { label: "Catalysts", value: "Event-driven catalysts" },
                { label: "Macro", value: "Active macro overlays" },
                { label: "Construction", value: "Disciplined portfolio construction" }
            ];
            
            const cx = 200, cy = 200, rTicks = 160, rProgress = 180;
            const totalTicks = 84; 
            
            let svgHTML = `<circle cx="${cx}" cy="${cy}" r="${rProgress}" class="ring-bg"></circle>`;
            
            for(let i=0; i<totalTicks; i++) {
                const angle = (i / totalTicks) * Math.PI * 2;
                const isMajor = (i % 12 === 0);
                const innerR = isMajor ? rTicks - 16 : rTicks - 6;
                const x1 = cx + innerR * Math.cos(angle);
                const y1 = cy + innerR * Math.sin(angle);
                const x2 = cx + rTicks * Math.cos(angle);
                const y2 = cy + rTicks * Math.sin(angle);
                const strokeW = isMajor ? 2 : 1;
                svgHTML += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="tick-line" id="tick-${i}" stroke-width="${strokeW}"></line>`;
            }
            
            const circumference = 2 * Math.PI * rProgress;
            svgHTML += `<circle cx="${cx}" cy="${cy}" r="${rProgress}" class="ring-progress" id="compass-progress" style="stroke-dasharray: ${circumference}; stroke-dashoffset: ${circumference};"></circle>`; 
            
            svgGraphic.innerHTML = svgHTML;
            const progressRing = document.getElementById("compass-progress");
            
            let lastIndex = -1;
            
            window.addEventListener('scroll', () => {
                const rect = compassSection.getBoundingClientRect();
                const scrollDistance = compassSection.offsetHeight - window.innerHeight;
                
                let progress = -rect.top / Math.max(1, scrollDistance);
                progress = Math.max(0, Math.min(1, progress));
                if(progress < 0) progress = 0;
                
                const offset = circumference - (progress * circumference);
                if(progressRing) progressRing.style.strokeDashoffset = offset;
                
                const currentTick = Math.floor(progress * totalTicks);
                for(let i=0; i<totalTicks; i++) {
                    const tk = document.getElementById(`tick-${i}`);
                    if(tk) {
                        if (i <= currentTick && progress > 0.01) {
                            tk.style.stroke = "var(--gold)";
                        } else {
                            tk.style.stroke = "rgba(255,255,255,0.15)";
                        }
                    }
                }
                
                let activeIndex = Math.floor(progress * characteristics.length);
                if(activeIndex >= characteristics.length) activeIndex = characteristics.length - 1;
                if(activeIndex < 0) activeIndex = 0;
                
                if(activeIndex !== lastIndex) {
                    titleEl.style.opacity = 0;
                    descEl.style.opacity = 0;
                    
                    setTimeout(() => {
                        titleEl.innerText = characteristics[activeIndex].label;
                        descEl.innerText = characteristics[activeIndex].value;
                        stepEl.innerText = `${activeIndex + 1} / ${characteristics.length}`;
                        titleEl.style.opacity = 1;
                        descEl.style.opacity = 1;
                    }, 150);
                    lastIndex = activeIndex;
                }
            });
        });
    </script>
"""

with open('investment-approach.html', 'r') as f:
    content = f.read()

# First, remove the text and ul from the Credit Opportunities block
pattern_text = r"                <p class=\"section-desc\" style=\"font-family: 'Inter', sans-serif; font-size: 1.15rem; color: var(--text-secondary); line-height: 1.7; margin: 0 0 20px 0; max-width: 800px;\">\n                    Rather than relying on broad market direction, we generate alpha through:\n                </p>\n                <ul class=\"section-desc\" style=\"font-family: 'Inter', sans-serif; font-size: 1.15rem; color: var(--text-secondary); line-height: 1.7; margin: 0 0 30px 0; padding-left: 20px;\">\n                    <li style=\"margin-bottom: 10px;\">Fundamental credit selection</li>\n                    <li style=\"margin-bottom: 10px;\">Capital structure and relative value opportunities</li>\n                    <li style=\"margin-bottom: 10px;\">Event-driven catalysts</li>\n                    <li style=\"margin-bottom: 10px;\">Active macro overlays</li>\n                    <li style=\"margin-bottom: 10px;\">Disciplined portfolio construction</li>\n                </ul>\n"
content = re.sub(pattern_text, "", content, flags=re.DOTALL)

# Inject compass right before the footer
pattern_footer = r"    <!-- Modern Green Footer -->"
match = re.search(pattern_footer, content)
if match:
    new_content = content[:match.start()] + compass_code + "\n" + content[match.start():]
    with open('investment-approach.html', 'w') as f:
        f.write(new_content)
    print("Injected compass!")
else:
    print("Could not find footer to inject compass.")

