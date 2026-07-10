import re

with open('investment-approach.html', 'r') as f:
    content = f.read()

# 1. Extract the orphaned sa-list block
# It starts at '            <div class="sa-list">' and ends at the closing div of 'scroll-approach-section'
# which is right before '    <!-- Applied Strategy Section -->'
pattern_orphan = r"(            <div class=\"sa-list\">.*?            </div>\n        </div>\n    </div>\n)"
match_orphan = re.search(pattern_orphan, content, flags=re.DOTALL)

if match_orphan:
    orphan_block = match_orphan.group(1)
    print("Found orphan block")
    
    # 2. Remove orphan block from its current spot
    new_content = content.replace(orphan_block, "")
    
    # 3. Find the incomplete sa-sticky block at the top
    # It ends with:
    #                 <div style="width: 60px; height: 1px; background: rgba(255,255,255,0.2);"></div>
    #             </div>
    pattern_sticky = r"(                <div style=\"width: 60px; height: 1px; background: rgba\(255,255,255,0\.2\);\"></div>\n            </div>\n)"
    match_sticky = re.search(pattern_sticky, new_content)
    
    if match_sticky:
        print("Found incomplete sticky block")
        # inject the orphan block right after match_sticky
        insertion_index = match_sticky.end()
        new_content = new_content[:insertion_index] + "\n" + orphan_block + "\n" + new_content[insertion_index:]
        
        with open('investment-approach.html', 'w') as f:
            f.write(new_content)
        print("Successfully fixed the layout")
    else:
        print("Could not find incomplete sticky block")
else:
    print("Could not find orphan block")
