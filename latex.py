import subprocess
import os
import json

def run_latex(tex_file, output_pdf, style_file="resume.sty"):
    """Run the LaTeX command to generate the PDF with the style file."""
    # Ensure the style file is in the same directory as the tex file or provide full path to it
    command = ['C:/Program Files/Git/bin/bash.exe', './laton', tex_file, style_file]
    
    try:
        subprocess.run(command, check=True)
        print(f"PDF generated successfully: {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating PDF: {e}")

def update_tex_file(input_file, output_file, email_map):
    """Update the .tex file with new emails from the email_map."""
    with open(input_file, 'r') as file:
        tex_content = file.read()

    # Loop through the email replacements and apply them
    for old_email, new_email in email_map.items():
        tex_content = tex_content.replace(old_email, new_email)

    # Write the updated content to a new .tex file
    with open(output_file, 'w') as file:
        file.write(tex_content)

    print(f"Updated .tex file saved as: {output_file}")

def rename_pdf(original_pdf, new_name):
    """Rename the PDF to the new name."""
    new_pdf = f"{new_name}.pdf"
    os.rename(original_pdf, new_pdf)
    print(f"Renamed PDF to: {new_pdf}")
    return new_pdf

def main():
    # Load the email configurations from the JSON file
    with open('config.json', 'r') as config_file:
        email_configs = json.load(config_file)
    
    style_file = 'resume.sty'  # Assuming 'resume.sty' is in the same directory

    # Step through each email config
    for config in email_configs:
        # Get the replacement map and output name from the config
        tex_file = config['text-file']
        email_map = config['replace']
        output_name = config['output_name']

        # Step 2: Update the email in the .tex file
        updated_tex_file = 'gopala-swamy-updated.tex'
        update_tex_file(tex_file, updated_tex_file, email_map)

        # Step 3: Generate the PDF with the updated email
        updated_pdf = f"{output_name}"
        run_latex(updated_tex_file, updated_pdf, style_file)
        
        # Step 4: Rename the PDF
        rename_pdf("gopala-swamy-updated.pdf",updated_pdf )

if __name__ == "__main__":
    main()
