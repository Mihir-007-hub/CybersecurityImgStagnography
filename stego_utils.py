from PIL import Image

def encode_text_to_image(image: Image.Image, message: str) -> Image.Image:
    binary_msg = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'
    img = image.convert('RGB')
    pixels = list(img.getdata())

    new_pixels = []
    msg_index = 0
    for pixel in pixels:
        if msg_index < len(binary_msg):
            r = pixel[0] & ~1 | int(binary_msg[msg_index])
            msg_index += 1
        else:
            r = pixel[0]

        if msg_index < len(binary_msg):
            g = pixel[1] & ~1 | int(binary_msg[msg_index])
            msg_index += 1
        else:
            g = pixel[1]

        if msg_index < len(binary_msg):
            b = pixel[2] & ~1 | int(binary_msg[msg_index])
            msg_index += 1
        else:
            b = pixel[2]

        new_pixels.append((r, g, b))

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    return new_img

def decode_text_from_image(image: Image.Image) -> str:
    pixels = list(image.getdata())
    binary_data = ''

    for pixel in pixels:
        for color in pixel[:3]:
            binary_data += str(color & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in all_bytes:
        if byte == '11111110':  # stop sequence
            break
        message += chr(int(byte, 2))
    return message
