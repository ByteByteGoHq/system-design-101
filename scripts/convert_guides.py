#!/usr/bin/env python3
"""
Convert system-design-101 guides to Jekyll blog posts for atakuzi.github.io
"""

import os
import re
from pathlib import Path
from datetime import datetime

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        return frontmatter, body
    return None, content

def parse_frontmatter(frontmatter_text):
    """Parse YAML frontmatter into a dictionary."""
    data = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            if key == 'categories' or key == 'tags':
                # Skip, will process next
                continue
            data[key] = value
        elif line.strip().startswith('- '):
            # This is a list item
            item = line.strip()[2:].strip('"\'')
            if 'tags' not in data:
                data['tags'] = []
            data['tags'].append(item)
    return data

def create_jekyll_frontmatter(original_data):
    """Create Jekyll-compatible frontmatter."""
    title = original_data.get('title', 'Untitled')
    description = original_data.get('description', '')
    created_at = original_data.get('createdAt', datetime.now().strftime('%Y-%m-%d'))
    tags = original_data.get('tags', [])

    # Build the frontmatter
    frontmatter = f"""---
layout: post
title: "{title}"
subtitle: "{description}"
date: {created_at}
tags: {tags}
---
"""
    return frontmatter

def convert_guide_to_post(guide_path, output_dir):
    """Convert a single guide file to Jekyll post format."""
    # Read the guide content
    with open(guide_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract and parse frontmatter
    frontmatter_text, body = extract_frontmatter(content)
    if not frontmatter_text:
        print(f"Warning: No frontmatter found in {guide_path}")
        return None

    original_data = parse_frontmatter(frontmatter_text)

    # Create Jekyll frontmatter
    jekyll_frontmatter = create_jekyll_frontmatter(original_data)

    # Combine frontmatter and body
    jekyll_content = jekyll_frontmatter + '\n' + body

    # Generate output filename
    created_at = original_data.get('createdAt', datetime.now().strftime('%Y-%m-%d'))
    guide_name = Path(guide_path).stem
    output_filename = f"{created_at}-{guide_name}.md"
    output_path = output_dir / output_filename

    # Write the Jekyll post
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(jekyll_content)

    return output_path

def main():
    """Main conversion function."""
    # Define paths
    guides_dir = Path('/home/user/system-design-101/data/guides')
    output_dir = Path('/home/user/atakuzi.github.io/_posts')

    # Get all guide files
    guide_files = sorted(guides_dir.glob('*.md'))

    print(f"Found {len(guide_files)} guide files to convert")

    converted = 0
    failed = 0

    for guide_file in guide_files:
        try:
            result = convert_guide_to_post(guide_file, output_dir)
            if result:
                converted += 1
                if converted % 50 == 0:
                    print(f"Converted {converted} files...")
            else:
                failed += 1
        except Exception as e:
            print(f"Error converting {guide_file}: {e}")
            failed += 1

    print(f"\n✅ Conversion complete!")
    print(f"   Successfully converted: {converted}")
    print(f"   Failed: {failed}")
    print(f"   Output directory: {output_dir}")

if __name__ == '__main__':
    main()
