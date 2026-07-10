import re

with open('investment-approach.html', 'r') as f:
    content = f.read()

# The new items
new_sa_list = """            <div class="sa-list">
                <div class="sa-item fade-up">
                    <span class="sa-num">01</span>
                    <div class="sa-text-wrapper">
                        <h3 class="sa-text">Fundamental Research</h3>
                        <p class="sa-desc">Every investment begins with in-depth analysis of issuers, capital structures and valuation.</p>
                    </div>
                </div>

                <div class="sa-item fade-up">
                    <span class="sa-num">02</span>
                    <div class="sa-text-wrapper">
                        <h3 class="sa-text">Catalyst-Driven Investing</h3>
                        <p class="sa-desc">We focus on events that can unlock value, including refinancing, M&A, deleveraging, liability management and rating transitions.</p>
                    </div>
                </div>

                <div class="sa-item fade-up">
                    <span class="sa-num">03</span>
                    <div class="sa-text-wrapper">
                        <h3 class="sa-text">High-Conviction Portfolios</h3>
                        <p class="sa-desc">A concentrated portfolio of carefully selected investments balanced by disciplined diversification.</p>
                    </div>
                </div>

                <div class="sa-item fade-up">
                    <span class="sa-num">04</span>
                    <div class="sa-text-wrapper">
                        <h3 class="sa-text">Active Risk Management</h3>
                        <p class="sa-desc">Dynamic management of duration, credit exposure and FX through liquid derivatives to protect capital and enhance returns.</p>
                    </div>
                </div>

                <div class="sa-item fade-up">
                    <span class="sa-num">05</span>
                    <div class="sa-text-wrapper">
                        <h3 class="sa-text">Data-Driven Insights</h3>
                        <p class="sa-desc">Proprietary tools complement fundamental research to identify relative value and market dislocations.</p>
                    </div>
                </div>
            </div>"""

# Replace the old sa-list (which ends before </div>\n        </div>\n    </div>)
pattern_sa = r"            <div class=\"sa-list\">.*?            </div>\n        </div>\n    </div>"
# Wait, sa-list contains a lot of </div>. Let's use a simpler match:
# From <div class="sa-list"> down to the last </div> of sa-item 06.
pattern_sa2 = r"            <div class=\"sa-list\">.*?<span class=\"sa-num\">06</span>.*?</div>\n                </div>\n            </div>"
match = re.search(pattern_sa2, content, flags=re.DOTALL)
if match:
    content = content[:match.start()] + new_sa_list + content[match.end():]
    print("Replaced sa-list")

# Now delete the static grid:
pattern_grid = r"    <!-- Our Approach List Section -->.*?    </div>\n    </div>\n"
match_grid = re.search(pattern_grid, content, flags=re.DOTALL)
if match_grid:
    content = content[:match_grid.start()] + content[match_grid.end():]
    print("Deleted static grid")

with open('investment-approach.html', 'w') as f:
    f.write(content)
print("Done")
