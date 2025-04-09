import qrcode
from PIL import Image

# Define the URL to encode
url = "https://lenarori.github.io/oldfrank"

# Generate the QR code - increased box_size for better printing
qr = qrcode.QRCode(version=3, box_size=16, border=0)  # Set border to 0 for no border
qr.add_data(url)
qr.make(fit=True)

# Create QR code image with custom colors
qr_img = qr.make_image(fill="black", back_color="gray").convert("RGBA")  # Changed back_color to gray

# Use a PNG image instead of SVG
logo_path = "/Users/calenwalshe/franksite/skull.png"  # Convert your SVG to PNG first

logo = Image.open(logo_path).convert("RGBA")
# Resize the logo to fit within the QR code
qr_size = qr_img.size[0]
logo_size = qr_size // 4
logo_aspect_ratio = logo.size[0] / logo.size[1]
logo = logo.resize((logo_size, int(logo_size / logo_aspect_ratio)))

# Get positioning for the logo (center)
pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

# Paste the logo onto the QR code
qr_img.paste(logo, pos, mask=logo)

# Save the decorative QR code without border
qr_img.save("decorative_qr.png", dpi=(300, 300))  # Added DPI setting for better print quality

# Show the QR code
qr_img.show()
