import re

with open('investment-approach.html', 'r') as f:
    content = f.read()

# 1. Extract the Methodology section (both CSS and HTML)
# The section starts with:
#    <!-- Interactive Scroll-Based Approach Section -->
#    <style>
#        .scroll-approach-section {
# And ends after:
#            </div>
#        </div>
#    </div>
# which is right before:
#    <!-- Applied Strategy Section -->

pattern = r"(    <!-- Interactive Scroll-Based Approach Section -->\n    <style>.*?    <div class=\"scroll-approach-section\">.*?    </div>\n)"
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    methodology_block = match.group(1)
    print("Found Methodology block")
    
    # 2. Remove it from its current position
    new_content = content.replace(methodology_block, "")
    
    # 3. Find the injection point: right after the intro text block
    # which ends with:
    #                 </p>
    #             </div>
    #         </div>
    #     </div>
    #
    #     <!-- Our Approach List Section -->
    injection_pattern = r"(                </p>\n            </div>\n        </div>\n    </div>\n)"
    match_inj = re.search(injection_pattern, new_content)
    if match_inj:
        print("Found Injection point")
        # insert the methodology_block after the injection point
        new_content = new_content[:match_inj.end()] + "\n" + methodology_block + new_content[match_inj.end():]
        
        with open('investment-approach.html', 'w') as f:
            f.write(new_content)
        print("Successfully moved the section")
    else:
        print("Could not find injection point")
else:
    print("Could not find Methodology block")

