In today’s digital world, secure communication is becoming increasingly important — not just through encryption, but also by hiding the fact that a message exists at all. This concept is known as steganography. While cryptography scrambles data to make it unreadable, steganography hides the data in plain sight, often within images, audio, or video files.

This project focuses on image-based steganography, where a secret text message is hidden inside an image without making any visible change. The method used is called Least Significant Bit (LSB) steganography, where the last bit of each color value (Red, Green, and Blue) in a pixel is modified to store bits of a message. Since the LSB change is too small for the human eye to detect, the image looks the same — but it secretly contains information.

Using Python and the Pillow (PIL) library, this project allows us to encode and decode secret messages in images. It demonstrates how simple manipulations at the pixel level can be used to securely embed and retrieve hidden messages, making it a beginner-friendly yet insightful application of both image processing and cybersecurity concepts.

